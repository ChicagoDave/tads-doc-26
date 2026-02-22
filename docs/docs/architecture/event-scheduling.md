# Event Scheduling

TADS 3 games are driven by a scheduling loop that decides *who acts next*. Every actor — player and NPC alike — is a `Schedulable` object with a clock time. Fuses and daemons are events managed by a separate `Schedulable`, the `eventManager`, which runs after all actors have had their turn. A parallel real-time system handles wall-clock events independently. This document explains the scheduling loop, the event class hierarchy, the actor scheduling model, and the places where game authors can intervene.

[Overview](#event-scheduling-overview) | [The Scheduling Loop](#the-scheduling-loop) | [Actors as Schedulables](#actors-as-schedulables) | [Turn-Based Events](#turn-based-events) | [Sense-Aware Events](#sense-aware-events) | [Prompt Daemons](#prompt-daemons) | [Real-Time Events](#real-time-events) | [Customization](#author-customization-patterns) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to other architecture docs"
    The [Architecture Overview](overview.md) lists `events.t` in its module map and sketches the turn cycle at a high level. The [Action Resolution](action-resolution.md) document explains what happens *during* an actor's turn — the verify/check/action pipeline. The [Sense and Perception](sense-perception.md) document explains the sensory model that `SenseFuse` and `SenseDaemon` depend on. The library guide covers practical usage: [Fuse](../library/guide/fuse.md), [Daemon](../library/guide/daemon.md), [SenseFuse](../library/guide/sensefuse.md), [SenseDaemon](../library/guide/sensedaemon.md), [PromptDaemon](../library/guide/promptdaemon.md). The [Design Patterns](design-patterns.md#daemon-and-fuse-patterns) document covers robustness idioms for event management. This document explains the internal machinery — the scheduling algorithm, class hierarchies, and design decisions.

---

## Event Scheduling Overview

The event system is organized in three layers:

```
Layer 1: The Scheduling Loop                Who acts next (events.t)
     │   runScheduler(), Schedulable,
     │   gameClockTime, allSchedulables,
     │   priority ordering, turn dispatch
     │
     ├── Actors (actor.t)                   Characters taking turns
     │   PC (100/300), NPCs (200/400),
     │   executeTurn(), addBusyTime()
     │
     ├── Turn-Based Events (events.t)       Fuses and daemons
     │   eventManager (scheduleOrder 1000),
     │   Fuse, Daemon, SenseFuse,
     │   SenseDaemon, PromptDaemon
     │
     └── Real-Time Events (events.t)        Wall-clock events
         realTimeManager, RealTimeFuse,
         RealTimeDaemon, elapsed ms
```

### Source files and responsibilities

| Source | Role |
|--------|------|
| `events.t` | `runScheduler()`, `Schedulable` base class, `eventManager`, `realTimeManager`, all event classes (`Fuse`, `Daemon`, `SenseFuse`, `SenseDaemon`, `PromptDaemon`, `OneTimePromptDaemon`, `RealTimeFuse`, `RealTimeDaemon`, and their sense-aware variants) |
| `actor.t` | `Actor` as a `Schedulable` — scheduling priority, `executeTurn()`, `addBusyTime()`, `idleTurn()`, `readyForTurn()` |
| `misc.t` | `runGame()` — the entry point that calls `runScheduler()` after showing the initial room description |
| `input.t` | `readMainCommand()` — calls `eventManager.executePrompt()` to fire prompt daemons before each command prompt |
| `adv3.h` | `EventAction` pseudo-action class, event-related macros |

---

## The Scheduling Loop

The heart of the system is `runScheduler()` (events.t:26), an infinite loop that runs until the game ends. Each iteration selects the schedulable objects with the earliest `nextRunTime`, sorts them by priority, and executes them.

### Algorithm

```
┌─────────────────────────────────────────────────────────────┐
│ runScheduler()                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Scan Schedulable.allSchedulables                        │
│     Find minimum getNextRunTime() → minTime                 │
│     Collect all schedulables at minTime → vec               │
│                                                             │
│  2. If minTime is nil → no schedulables → terminate         │
│                                                             │
│  3. Advance turn counter:                                   │
│     libGlobal.totalTurns += (minTime - gameClockTime)       │
│     Schedulable.gameClockTime = minTime                     │
│                                                             │
│  4. Calculate and sort by scheduleOrder (ascending):        │
│     vec.forEach({x: x.calcScheduleOrder()})                 │
│     vec.sort(SortAsc, scheduleOrder)                        │
│                                                             │
│  5. For each schedulable in sorted order:                   │
│     While getNextRunTime() == minTime:                      │
│       result = executeTurn()                                │
│       If result is nil → break all, restart from step 1     │
│                                                             │
│  6. Catch QuittingException, EndOfFileException → exit      │
│     Catch RuntimeError → display error, continue            │
│     Catch TerminateCommandException → ignore, continue      │
│                                                             │
│  7. Loop back to step 1                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key design decisions

**Game clock time is abstract.** `Schedulable.gameClockTime` is a simple integer counter, not wall-clock time. It starts at zero and increments by the amount of time consumed by actions. When no action occurs between two clock ticks, the scheduler jumps directly to the next meaningful time — there is no idle spinning.

**The `executeTurn()` return value controls rescheduling.** If `executeTurn()` returns `true`, the scheduler continues to the next schedulable. If it returns `nil`, the scheduler breaks out of the entire sorted list and recalculates priorities from scratch. This is how the system handles priority changes mid-turn — for example, when an NPC's action changes whether another actor is ready to act.

**Exception safety.** If a schedulable throws an exception without advancing its `nextRunTime`, the scheduler forces a one-unit advance to prevent starvation. Events that throw exceptions are removed from the event list entirely. The outer loop catches `TerminateCommandException`, `ExitSignal`, and `ExitActionSignal` as no-ops, allowing code inside events to use these flow-control exceptions without crashing the scheduler.

---

## Actors as Schedulables

`Actor` inherits from `Schedulable` (along with `Thing`, `Traveler`, and `ActorTopicDatabase`). Every actor is a first-class participant in the scheduling loop.

### Priority tiers

When multiple schedulables share the same `nextRunTime`, their relative order is determined by `calcScheduleOrder()` (actor.t:9031):

| Schedule Order | Condition | Meaning |
|:-:|---|---|
| **100** | Player character, ready | PC has a pending command or will prompt for one |
| **200** | NPC, ready | NPC has a pending command in its queue |
| **300** | Player character, idle | PC is waiting for another actor |
| **400** | NPC, idle | NPC has no pending commands |
| **1000** | `eventManager` | Turn-based fuses and daemons (always last) |

This ordering ensures that actors with work to do go first. The PC always precedes NPCs at the same priority level. Fuses and daemons always run after all actors.

### Readiness

`readyForTurn()` (actor.t:9049) determines whether an actor is "ready" or "idle":

1. If the actor is waiting for another actor (`checkWaitingForActor()`), it is not ready.
2. The PC is always ready (it can prompt the player for a command).
3. An NPC is ready only if its `pendingCommand` queue contains a real command (not just placeholders).

### Time consumption

Actions consume game time by calling `addBusyTime(action, units)` (actor.t:9154). This advances the actor's `nextRunTime` by the specified units, preventing the actor from acting again until that time arrives. A standard action consumes one unit. Multi-turn actions consume more.

### Actor turn execution

`executeTurn()` (actor.t:9268) wraps the actor's turn in two contexts:

1. An `EventAction` action environment — so that event-related code has a valid action context.
2. A sensory context — NPC actions are filtered through `callWithSenseContext(self, sight, ...)` so their output is only displayed if the PC can see the NPC. The PC's own actions bypass this filter.

The actual work happens in `executeActorTurn()` (actor.t:9297), which processes pending commands or falls through to `idleTurn()`.

### Idle turns

When an NPC has no pending commands, `idleTurn()` (actor.t:9168):

1. Checks for pending conversations to initiate (if `lastConvTime` is earlier than the current clock).
2. Calls `curState.takeTurn()` — the current `ActorState` can perform scripted behavior here.
3. If `nextRunTime` was not already advanced (by a nested command, for example), increments it by 1.

---

## Turn-Based Events

Turn-based events are objects managed by the `eventManager` singleton. They fire at specific game clock times.

### Class hierarchy

```
BasicEvent                          Base: obj_, prop_, callMethod()
│
├── Event                           Adds nextRunTime, eventOrder, registration
│   │
│   ├── Fuse                        One-shot: fires once, then self-removes
│   │   └── SenseFuse               Adds source_/sense_ for sensory filtering
│   │
│   ├── Daemon                      Recurring: fires every N turns
│   │   └── SenseDaemon             Adds source_/sense_ for sensory filtering
│   │
│   ├── PromptDaemon                Fires before each command prompt
│   │   └── OneTimePromptDaemon     Fires once before the next prompt, then self-removes
│   │
│   └── (custom Event subclasses)
│
└── RealTimeEvent                   (see Real-Time Events below)
```

### The eventManager singleton

`eventManager` (events.t:425) is both a `BasicEventManager` and a `Schedulable`. Its `scheduleOrder` is 1000, ensuring it runs after all actors. Its key methods:

| Method | What it does |
|--------|-------------|
| `addEvent(event)` | Appends an event to the internal `events_` vector |
| `removeEvent(event)` | Removes a specific event from the vector |
| `removeMatchingEvents(obj, prop)` | Removes all events matching the given object/property pair |
| `removeCurrentEvent()` | Removes the event currently being executed (safe to call from within `executeEvent()`) |
| `getNextRunTime()` | Scans all events and returns the earliest `nextRunTime` |
| `executeTurn()` | Finds all events due at the current game clock time, calls `executeList()` |
| `executePrompt()` | Finds all events with `isPromptDaemon == true`, calls `executeList()` |

### Event execution

`executeList()` (events.t:499) processes a list of events:

1. Sorts by `eventOrder` (ascending — lowest fires first, default is 100).
2. For each event:
    - Saves and sets `curEvent_` (so `removeCurrentEvent()` works).
    - Calls `gPlayerChar.noteConditionsBefore()` to snapshot the PC's state.
    - Disables the sense cache (`libGlobal.disableSenseCache()`).
    - Calls `event.executeEvent()`.
    - Calls `gPlayerChar.noteConditionsAfter()` to detect and report changes (e.g., light going out).
3. If an event throws an exception, it is removed from the event list to prevent infinite loops.

### Fuse

A `Fuse` (events.t:682) fires once at a specified future turn and then removes itself.

```tads3
// Fire myObj.&explode in 5 turns
new Fuse(myObj, &explode, 5);
```

- **Constructor**: `Fuse(obj, prop, turns)` — schedules at `gameClockTime + turns`. A value of 0 fires on the current turn.
- **executeEvent()**: Calls `callMethod()`, then `eventManager.removeEvent(self)`.

### Daemon

A `Daemon` (events.t:744) fires repeatedly at a fixed interval.

```tads3
// Call myObj.&tick every turn
new Daemon(myObj, &tick, 1);

// Call myObj.&chime every 12 turns
new Daemon(myObj, &chime, 12);
```

- **Constructor**: `Daemon(obj, prop, interval)` — first execution at `gameClockTime + interval - 1`. An interval of 1 means "fire this turn, then every turn." The minimum interval is clamped to 1.
- **executeEvent()**: Calls `callMethod()`, then advances `nextRunTime += interval_`.

### The callMethod() mechanism

All events invoke their target through `callMethod()` (events.t:605), which wraps the call in two contexts:

1. **Action environment**: `withActionEnv(EventAction, gPlayerChar, ...)` — provides a valid action context so the event handler can use macros like `gActor`, `gPlayerChar`, and report macros.
2. **Sensory context**: `callWithSenseContext(source_, sense_, ...)` — if `source_` and `sense_` are set (as in `SenseFuse`/`SenseDaemon`), output is only displayed when the PC can sense the source object. If both are nil (the default), output is always displayed.

### Event ordering

When multiple events fire at the same game clock time, they execute in ascending `eventOrder` (default 100). You can control relative ordering by overriding this property:

```tads3
myEarlyFuse: Fuse
    eventOrder = 50   // fires before default events
    construct(obj, prop, turns) { inherited(obj, prop, turns); }
;
```

### Delaying and removing events

| Operation | Code |
|-----------|------|
| Delay a scheduled event | `myFuse.delayEvent(3)` — adds 3 turns to `nextRunTime` |
| Remove by reference | `myFuse.removeEvent()` or `eventManager.removeEvent(myFuse)` |
| Remove by object/property | `eventManager.removeMatchingEvents(myObj, &explode)` |
| Remove current event (from within handler) | `eventManager.removeCurrentEvent()` |

---

## Sense-Aware Events

`SenseFuse` and `SenseDaemon` are variants that specify a sensory context — a source object and a sense. Their output is only displayed if the PC can sense the source object in the given sense.

### SenseFuse

```tads3
// The alarm goes off in 10 turns; only audible if the PC can hear the clock
new SenseFuse(clock, &alarmGoesOff, 10, clock, sound);
```

**Constructor**: `SenseFuse(obj, prop, turns, source, sense)` — inherits `Fuse` behavior but sets `source_` and `sense_` on the `BasicEvent`. When `callMethod()` executes, it wraps the call in `callWithSenseContext(clock, sound, ...)`, so any output is suppressed if the PC cannot hear the clock.

### SenseDaemon

```tads3
// The clock ticks every turn; only visible if the PC can see the clock
new SenseDaemon(clock, &showTicking, 1, clock, sight);
```

**Constructor**: `SenseDaemon(obj, prop, interval, source, sense)` — inherits `Daemon` behavior with the same sensory filtering.

### How sensory filtering works

The filtering is handled by `callWithSenseContext()`, which is part of the [Sense and Perception](sense-perception.md) system. When a sense context is active:

1. The system calculates the sense path from the PC to the source object in the specified sense.
2. If the path has sufficient transparency (the PC can sense the source), output is displayed normally.
3. If the PC cannot sense the source, all output generated during the event is silently discarded.

This means the event's *code* always runs — side effects like state changes happen regardless. Only the *output* is suppressed. This is a deliberate design choice: the game world evolves consistently whether or not the PC witnesses it.

---

## Prompt Daemons

`PromptDaemon` (events.t:813) and `OneTimePromptDaemon` (events.t:853) are special events that fire just before the command prompt is displayed, outside the game clock.

### How they work

Prompt daemons are not scheduled by game clock time — they have no `nextRunTime`. Instead, `readMainCommand()` (input.t:797) calls `eventManager.executePrompt()` before every command prompt. This method finds all events with `isPromptDaemon == true` and executes them.

```tads3
// Show weather before every command prompt
new PromptDaemon(self, &showWeather);
```

### OneTimePromptDaemon

`OneTimePromptDaemon` fires once and then removes itself. This is useful for deferred initialization that needs an action context:

```tads3
// In gameMain.newGame() or an InitObject:
new OneTimePromptDaemon(narrator, &openingMonologue);
```

The callback will run just before the first command prompt, in a valid `EventAction` context where conversation and action macros work. This solves the common problem of wanting to initiate a conversation at game start — `newGame()` runs before the action environment exists, but a `OneTimePromptDaemon` defers until the environment is ready.

### Prompt daemons vs. regular daemons

| | PromptDaemon | Daemon (interval 1) |
|---|---|---|
| **When it fires** | Before every command prompt | After all actors, on the game clock |
| **Tied to game clock?** | No | Yes |
| **Fires during multi-turn actions?** | Yes (once per prompt) | May not fire until the action completes |
| **Typical use** | Status updates, ambient text | World simulation, timed puzzles |

---

## Real-Time Events

The real-time system handles events based on wall-clock elapsed time in milliseconds, independent of the turn-based game clock.

### The realTimeManager

`realTimeManager` (events.t:870) is a `BasicEventManager` and an `InitObject`. It tracks elapsed time from the start of the game session:

- **`getElapsedTime()`** — returns `getTime(GetTimeTicks) - startingTime`, the number of milliseconds since the game started.
- **`setElapsedTime(t)`** — freezes the clock at a specific point (useful for pausing real-time during menus or conversation).
- **`executeEvents()`** — runs all events whose `eventTime` has passed, then returns the time of the next event.
- **`getNextEventTime()`** — returns the earliest `eventTime` of any pending real-time event.

### Save and restore

Real-time events must survive save/restore. The system handles this through:

1. `PreSaveObject` calls `realTimeManager.saveElapsedTime()` before saving — this stores the elapsed time.
2. `PostRestoreObject` calls `realTimeManager.restoreElapsedTime()` after restoring — this projects the saved elapsed time backwards from the current wall clock to compute a virtual start time. The effect is seamless: after restoring, `getElapsedTime()` returns the saved value and continues counting from there.

### Class hierarchy

```
BasicEvent
│
└── RealTimeEvent                      Base: eventTime, registration with realTimeManager
    │
    ├── RealTimeFuse                   One-shot after N milliseconds
    │   └── RealTimeSenseFuse          Adds source_/sense_ for sensory filtering
    │
    └── RealTimeDaemon                 Recurring every N milliseconds
        └── RealTimeSenseDaemon        Adds source_/sense_ for sensory filtering
```

### RealTimeFuse

```tads3
// Trigger an event in 30 seconds (30,000 ms)
new RealTimeFuse(bomb, &explode, 30000);
```

- **Constructor**: `RealTimeFuse(obj, prop, delta)` — schedules at `getElapsedTime() + delta`.
- **executeEvent()**: Calls `callMethod()`, then removes itself from `realTimeManager`.

### RealTimeDaemon

```tads3
// Play a background sound every 5 seconds
new RealTimeDaemon(ambient, &playSound, 5000);
```

- **Constructor**: `RealTimeDaemon(obj, prop, interval)` — first execution at `getElapsedTime() + interval`.
- **executeEvent()**: Calls `callMethod()`, then reschedules. The rescheduling uses drift prevention: `eventTime += interval_`. If this would put the next event in the past (because the daemon ran late), it falls back to `getElapsedTime() + interval_` to avoid firing repeatedly in a burst.

### When real-time events execute

Real-time events do **not** run inside `runScheduler()`. They run during command input — `readMainCommand()` passes the next event time to the input system, which can interrupt command-line editing to execute events. On platforms that don't support input interruption, real-time events fire between commands.

### Sense-aware real-time events

`RealTimeSenseFuse` and `RealTimeSenseDaemon` mirror their turn-based counterparts, adding `source_` and `sense_` parameters:

```tads3
// A ticking clock, audible in real time every 60 seconds
new RealTimeSenseDaemon(clock, &tick, 60000, clock, sound);
```

---

## Author Customization Patterns

### Creating and tracking events

Always store event references in properties so you can cancel them later:

```tads3
bombFuse = nil

lightFuse()
{
    bombFuse = new Fuse(self, &explode, 5);
}

explode()
{
    bombFuse = nil;
    // ... explosion logic ...
}

defuse()
{
    if (bombFuse != nil)
    {
        bombFuse.removeEvent();
        bombFuse = nil;
    }
}
```

### Guarding against duplicate events

Prevent double-creation by checking before instantiating:

```tads3
startTicking()
{
    if (tickDaemon == nil)
        tickDaemon = new Daemon(self, &tick, 1);
}
```

Without the guard, calling `startTicking()` twice creates two daemons, both firing every turn.

### Delayed NPC actions with fuses

Use a fuse to make an NPC do something after a delay:

```tads3
// The guard investigates a noise 3 turns later
new SenseFuse(guard, &investigate, 3, guard, sight);
```

The player will only see the guard's investigation if the guard is visible.

### Controlling event order

When multiple events fire on the same turn, override `eventOrder` to control sequencing:

```tads3
// Ensure the warning fires before the explosion
warningFuse = new Fuse(self, &showWarning, 5);
warningFuse.eventOrder = 50;

explosionFuse = new Fuse(self, &explode, 5);
explosionFuse.eventOrder = 150;
```

### Using OneTimePromptDaemon for game-start events

```tads3
// In an InitObject or gameMain.newGame():
new OneTimePromptDaemon(storyteller, &openingScene);
```

This defers the opening scene until a valid action context exists, allowing conversation initiation and other action-dependent code to work.

### Real-time countdown

```tads3
// 60-second real-time puzzle timer
puzzleTimer = new RealTimeFuse(self, &timeUp, 60000);

timeUp()
{
    puzzleTimer = nil;
    "Time's up! The door slams shut. ";
}
```

For more robustness patterns (nil-guarding, cleanup, daemon-vs-agenda trade-offs), see [Design Patterns: Daemon and Fuse Patterns](design-patterns.md#daemon-and-fuse-patterns).

---

## Practical Intervention Points

### Creating and removing events

| Goal | Code |
|------|------|
| One-shot event in N turns | `new Fuse(obj, &prop, N)` |
| Recurring event every N turns | `new Daemon(obj, &prop, N)` |
| One-shot with sensory filter | `new SenseFuse(obj, &prop, N, source, sense)` |
| Recurring with sensory filter | `new SenseDaemon(obj, &prop, N, source, sense)` |
| Fire before every command prompt | `new PromptDaemon(obj, &prop)` |
| Fire once before next prompt | `new OneTimePromptDaemon(obj, &prop)` |
| Real-time one-shot (ms) | `new RealTimeFuse(obj, &prop, ms)` |
| Real-time recurring (ms) | `new RealTimeDaemon(obj, &prop, ms)` |
| Remove by reference | `event.removeEvent()` |
| Remove by object/property | `eventManager.removeMatchingEvents(obj, &prop)` |
| Remove current event from handler | `eventManager.removeCurrentEvent()` |
| Delay a turn-based event | `event.delayEvent(turns)` |

### Scheduling priority

| Hook | How to use it |
|------|---------------|
| Actor schedule order | Override `calcScheduleOrder()` on an Actor subclass |
| Event execution order | Set `eventOrder` on individual Fuse/Daemon instances (default 100, lower fires first) |
| Custom schedulable | Subclass `Schedulable`, override `getNextRunTime()`, `executeTurn()`, `calcScheduleOrder()` |
| Prevent actor from acting | Return `nil` from `readyForTurn()` on an Actor subclass |
| Multi-turn actions | Call `actor.addBusyTime(action, units)` to delay the actor's next turn |

### Real-time integration

| Hook | How to use it |
|------|---------------|
| Freeze real-time clock | `realTimeManager.setElapsedTime(realTimeManager.getElapsedTime())` — freezes at current point |
| Query elapsed time | `realTimeManager.getElapsedTime()` — milliseconds since game start |
| Next real-time event | `realTimeManager.getNextEventTime()` — absolute elapsed time of next event |

### NPC behavior hooks

| Hook | What it does |
|------|-------------|
| `ActorState.takeTurn()` | Called on the NPC's current state during `idleTurn()` — scripted NPC behavior goes here |
| `AgendaItem` | Goal-driven NPC actions that fire when conditions are met (see [Design Patterns](design-patterns.md#agenda-driven-npc-patterns)) |
| `pendingConv` | Conversations the NPC wants to initiate — checked during `idleTurn()` before `takeTurn()` |

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [The Message System](message-system.md) for how event output is parameterized and displayed. For the action pipeline that runs during each actor's turn, see [Action Resolution](action-resolution.md). For the sensory model that SenseFuse and SenseDaemon depend on, see [Sense and Perception](sense-perception.md).*
