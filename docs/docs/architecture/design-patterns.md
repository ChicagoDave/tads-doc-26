# adv3 Design Patterns

The adv3 library was designed for extension. The patterns described here are not accidental — they recur throughout the library source and in well-written TADS 3 games. Understanding them lets you write code that works *with* the library rather than against it.

We assume you have read the [Architecture Overview](overview.md) and the [IF Development Guide](development-guide.md). This document goes deeper — into the mechanics of how adv3 is built and the idioms you will use when extending it.

[dobjFor/iobjFor](#the-dobjforiobjfor-property-set-system) | [Mix-ins](#mix-in-composition) | [State Objects](#the-state-object-pattern) | [modify vs. Subclass](#modify-vs-subclassing) | [+ Syntax](#source-organization-with-the-syntax) | [Scenery](#scenery-management) | [Daemons & Fuses](#daemon-and-fuse-patterns) | [Agenda NPCs](#agenda-driven-npc-patterns) | [Reports](#report-accumulation)

---

## The dobjFor/iobjFor Property Set System

This is the single most important pattern in adv3. Every verb interaction is defined by placing handler blocks on the *objects involved*, not on the action class. When the player types TAKE THE KEY, the key defines what "take" means for a key.

### What it looks like

```tads3
+ brassBox: OpenableContainer 'brass box' 'brass box'
    "A heavy brass box. "

    dobjFor(Open)
    {
        verify()
        {
            if (isOpen)
                illogicalAlready('The box is already open. ');
        }
        check()
        {
            if (isSealed)
                failCheck('The box appears to be hermetically sealed. ');
        }
        action()
        {
            makeOpen(true);
            defaultReport('You open the box. ');
        }
    }
;
```

This reads naturally: "when the brass box is the direct object of an Open action, here is how to verify, check, and execute it." But there is nothing magical about this syntax. It is built entirely on standard TADS 3 language features.

### How the macros work

The `dobjFor` macro is defined in `adv3.h`:

```tads3
#define objFor(which, action) \
    propertyset '*' ## #@which ## #@action

#define dobjFor(action) objFor(Dobj, action)
#define iobjFor(action) objFor(Iobj, action)
```

The `propertyset` keyword is a TADS 3 language feature that creates a namespace of related properties sharing a common prefix. When you write:

```tads3
dobjFor(Open) { verify() { ... } action() { ... } }
```

The preprocessor expands this to:

```tads3
propertyset '*DobjOpen' { verify() { ... } action() { ... } }
```

Which the compiler turns into individual properties named `verifyDobjOpen`, `actionDobjOpen`, `preCondDobjOpen`, `checkDobjOpen`, and `remapDobjOpen`. These are ordinary TADS 3 properties — the action system looks them up by name during command execution. There is no special dispatch mechanism; it is just string concatenation and property lookup.

This matters because it means you can override any individual phase. You can override `verify()` without touching `action()`, or add a `preCond` list without changing anything else.

### The four phases

Each handler block can define up to five sub-properties:

- **`preCond`** — a list of `PreCondition` objects that must be satisfied. Returns a list. Example: `preCond = [objHeld]` requires the actor to be holding the object.
- **`verify()`** — tests whether the action makes sense for this object. Calls `illogical()`, `illogicalAlready()`, `dangerous()`, `logicalRank()`, etc. Used for disambiguation — the parser picks the object with the best verify result.
- **`remap()`** — redirects the action to a different action or object. Returns a list like `[PutInAction, DirectObject, deskDrawer]`.
- **`check()`** — tests runtime conditions that should not affect disambiguation. Calls `failCheck()` to abort.
- **`action()`** — performs the actual world-state change.

These run in order: preCond → verify → remap → check → action. For the full pipeline, see [The Command Execution Cycle](../library/advanced/command-execution-cycle.md).

### Aliasing with asDobjFor

To make one action behave exactly like another, use `asDobjFor`:

```tads3
dobjFor(Search) asDobjFor(LookIn)
```

This copies all five sub-properties from the LookIn handler. It is a compile-time alias, not a runtime redirect — the compiler generates property definitions that simply delegate to the target action's properties.

**Important:** `asDobjFor` should not change the object's role. `dobjFor(X)` should map to `asDobjFor(Y)`, not `asIobjFor(Y)`, because handler code often assumes it is operating on the direct object.

### Redirecting with remapTo

When you need to redirect an action to a different object or change roles, use `remapTo`:

```tads3
/* Redirect PUT IN desk → PUT IN desk drawer */
iobjFor(PutIn) remapTo(PutIn, DirectObject, deskDrawer)
```

Unlike `asDobjFor`, `remapTo` is a runtime redirect — it rewrites the action before noun resolution completes, allowing the new action to run its own full verify/check/action cycle on the target object.

Use `maybeRemapTo` for conditional redirects:

```tads3
iobjFor(PutIn) maybeRemapTo(deskDrawer != nil, PutIn, DirectObject, deskDrawer)
```

### When to use which

- **`asDobjFor`** — one action should behave identically to another on the same object. Fast (compile-time). Cannot change roles.
- **`remapTo`** — one action should be rewritten as a different action, possibly involving different objects. Runtime redirect. Can change roles.
- **Override individual phases** — when you need some behavior from the parent class and different behavior for one phase. Use `inherited()` in the phase you want to keep.

## Mix-in Composition

TADS 3's multiple inheritance resolution order (C3-style linearization) makes mix-in composition safe and predictable. The library uses this extensively — nearly every "interesting" class in adv3 is composed from multiple superclasses.

### The pattern

Combine orthogonal capabilities by listing them as superclasses:

```tads3
/* From the library: */
class OpenableContainer: Openable, Container;
class LockableContainer: Lockable, OpenableContainer;
class KeyedContainer: LockableWithKey, OpenableContainer;
class Door: Openable, BasicDoor;
class Chair: BasicChair, Surface;
class Flashlight: LightSource, Switch;
```

Each mix-in adds one capability — `Openable` adds open/close, `Lockable` adds lock/unlock, `Surface` adds "put on" — and the combined class has all of them.

### Class ordering rules

The order of superclasses matters because it determines the method resolution order (MRO). TADS 3 uses a C3 linearization algorithm, which means:

1. The leftmost superclass takes priority.
2. `inherited()` follows the MRO chain.

**Rule of thumb:** put the most specific or behaviorally dominant class first. `LockableWithKey, OpenableContainer` means LockableWithKey's methods take priority if there are conflicts. Since LockableWithKey provides the locking behavior you care about, it goes first.

For the detailed algorithm and worked examples, see [Multiple Inheritance](../library/advanced/multiple-inheritance.md).

### In your own code

You can compose library mix-ins freely:

```tads3
/* A container that is both lockable and readable */
+ spellbook: LockableWithKey, OpenableContainer, Readable
    'ancient spellbook' 'spellbook'
    "A leather-bound spellbook with a brass clasp. "
    keyList = [brassKey]
    readDesc = "The pages are covered in arcane symbols. "
;
```

You can also define your own mix-in classes:

```tads3
class Fragile: object
    dobjFor(ThrowAt)
    {
        action()
        {
            "<<theName>> shatters into pieces! ";
            moveInto(nil);
        }
    }
    dobjFor(Drop)
    {
        action()
        {
            inherited();
            "<<theName>> shatters on impact! ";
            moveInto(nil);
        }
    }
;

/* Now use it: */
+ vase: Fragile, Thing 'delicate vase' 'vase'
    "A delicate porcelain vase. "
;
```

## The State Object Pattern

Rather than embedding state-dependent behavior directly in a Thing, adv3 often delegates it to a separate **state object**. This keeps state logic clean and composable.

### ThingState: the general form

`ThingState` (defined in `thing.t`) is the base class for state objects. A ThingState provides:

- `listName(lst)` — how the object appears in listings when in this state (e.g., "(lit)" or "(open)")
- `inventoryName(lst)` — how the object appears in inventory listings
- `matchName(obj, origTokens, adjustedTokens, states)` — how the object's name matching changes based on state (e.g., "lit torch" only matches when the state is "lit")
- `listingOrder` — relative order when sorting by state

A Thing points to its current ThingState via its `thingState` property. The library already defines ThingState objects for common states — lit/unlit, open/closed — but you can define your own.

### ActorState: the visible instance

The most prominent use of the state object pattern is `ActorState`. Every NPC has a `curState` property pointing to its current ActorState, which controls:

- `specialDesc()` — how the actor appears in room listings
- `stateDesc` — text appended to the actor's EXAMINE description
- `obeyCommand()` — whether the actor obeys player commands in this state
- `handleConversation()` — how conversation is dispatched
- `takeTurn()` — what the actor does on their turn

Switching states is as simple as calling `setCurState(newState)`. The state object pattern eliminates the need for if-then-else chains that test multiple boolean flags. See [Creating Dynamic Characters](../library/actors/dynamic-characters.md) for the full treatment.

### When to use state objects vs. flags

**Use a state object** when multiple properties change together. If an object's description, its listing name, its vocabulary matching, and its behavior all change as a unit, that unit of change is a state.

**Use a boolean flag** when only one thing changes. An `isOpen` flag on a container is fine because "open" and "closed" only affect a few well-defined behaviors that the library already handles.

**The test:** if you find yourself writing `if (myFlag)` in three or more different methods on the same object, you probably want a state object instead.

## modify vs. Subclassing

TADS 3 provides two ways to extend existing behavior: subclassing (creating a new class) and `modify` (patching an existing class in place). They serve different purposes.

### Subclassing

Creates a new named class that you can instantiate multiple times:

```tads3
class MagicItem: Thing
    dobjFor(RubMagicLamp)
    {
        action()
        {
            "The <<theName>> glows briefly. ";
        }
    }
;

+ ring: MagicItem 'magic ring' 'ring' "A plain silver ring. ";
+ amulet: MagicItem 'magic amulet' 'amulet' "A jade amulet. ";
```

Use subclassing when you want a reusable type. "I have several objects that all share this behavior" is the signal.

### modify

Patches an existing class or object in place. All existing instances are affected:

```tads3
modify Thing
    isFragile = nil
    dobjFor(ThrowAt)
    {
        check()
        {
            if (isFragile)
                "You'd better not throw <<theName>> — it might break. ";
            else
                inherited();
        }
    }
;
```

After this modification, *every* Thing in the game gains an `isFragile` property. No new class is created; the existing Thing class is patched.

Use `modify` when you want to change how the entire library behaves. "All containers should do X" or "The TAKE action should check Y" are `modify` situations.

### The `replace` keyword

Where `modify` adds to a class (preserving `inherited()`), `replace` completely replaces a method:

```tads3
modify Room
    replace roomBeforeAction()
    {
        /* Completely replace the library's roomBeforeAction */
        /* inherited() is NOT available here */
    }
;
```

Use `replace` sparingly. It prevents the original method (and any earlier modifications) from running.

### Risks of modify

If two library extensions both `modify` the same class and the same property, the last one compiled wins. The first extension's `modify` is still in the `inherited()` chain, but the order depends on compilation order in the `.t3m` file. This is manageable in practice — just be aware that `modify` order matters when multiple extensions interact.

## Source Organization with the + Syntax

The `+` prefix sets an object's `location` to the most recently defined object at the previous nesting level. This lets your source code mirror the physical containment of your game world:

```tads3
/* One + = inside the room */
cave: Room 'Dark Cave'  "A damp cave. ";
+ torch: Thing 'wooden torch' 'torch'  "A battered torch. ";
+ chest: OpenableContainer 'wooden chest' 'chest'  "A sturdy chest. ";

/* Two ++ = inside the chest */
++ goldCoin: Thing 'gold coin' 'gold coin'  "A gleaming coin. ";
++ silverRing: Thing 'silver ring' 'ring'  "A tarnished ring. ";
```

### The file-per-region pattern

For larger games, organize one file per geographical region. Each file begins with the region's rooms, then uses `+` to place objects:

```tads3
/* forest.t */
#include <adv3.h>
#include <en_us.h>

clearing: Room 'Forest Clearing'
    "Sunlight filters through the trees. Paths lead north and east. "
    north = deepWoods
    east = streamBank
;

+ oldLog: Surface, Fixture 'fallen log/tree' 'log'
    "A moss-covered log lies across the clearing. "
;

++ mushroom: Food 'red mushroom' 'mushroom'
    "A bright red mushroom growing on the log. "
;

deepWoods: DarkRoom 'Deep Woods'
    "The canopy is so thick that almost no light penetrates. "
    south = clearing
;
```

### When not to use +

`MultiLoc` objects exist in multiple locations simultaneously and must set their `locationList` property directly:

```tads3
sky: MultiLoc, Distant 'blue sky' 'sky'
    "The sky stretches overhead. "
    locationList = [clearing, streamBank, hilltop]
;
```

Objects created dynamically at runtime (with `new`) must set their `location` explicitly via `moveInto()`.

## Scenery Management

Most rooms mention objects in their descriptions that the player will try to interact with but that are not full game objects. adv3 provides a three-tier model for handling these.

### Fixture

A Fixture is a permanent, reachable object. The player can EXAMINE it and interact with it normally, but cannot TAKE or MOVE it:

```tads3
+ fireplace: Fixture 'stone fireplace/hearth' 'fireplace'
    "A large stone fireplace with a cold, empty grate. "
;
```

TAKE FIREPLACE produces "The fireplace is not something you can take." Other commands (EXAMINE, LOOK IN, SEARCH) work normally. Use Fixture for structural features that players might reasonably try to interact with.

### Decoration

A Decoration is a Fixture that additionally blocks most interactions. Only EXAMINE works; everything else produces a generic "That's not important" message:

```tads3
+ paintings: Decoration 'oil paintings/art' 'paintings'
    "Several oil paintings hang on the walls, depicting pastoral scenes. "
;
```

Use Decoration for flavor text that you mention in the room description but that does not participate in gameplay.

### Distant

A Distant object is visible but too far away to touch. All direct-interaction commands produce "It's too far away":

```tads3
+ mountain: Distant 'snow-capped mountain/peak' 'mountain'
    "A snow-capped peak rises to the north. "
;
```

Use Distant for objects the player can see from this room but that exist in another location or are purely scenic.

### Unthing

An `Unthing` is a special Decoration that exists solely to intercept a specific noun phrase and produce a tailored "not here" message:

```tads3
+ noWindow: Unthing 'window' 'window'
    notHereMsg = 'There are no windows in this underground chamber. '
;
```

Without the Unthing, the player typing LOOK AT WINDOW would get a generic "You don't see any window here." With it, they get a response that acknowledges the word and explains the absence. This is a polish technique for anticipated player commands.

### Choosing the right tier

| Class | EXAMINE | Other verbs | When to use |
|-------|---------|-------------|-------------|
| Fixture | Full description | Normal responses | Structural features, interactable scenery |
| Decoration | Full description | "Not important" | Mentioned in room desc, no gameplay role |
| Distant | Full description | "Too far away" | Visible from afar |
| Unthing | Custom "not here" | Custom "not here" | Anticipated noun with custom denial |

## Daemon and Fuse Patterns

Fuses and Daemons handle timed events. The [Development Guide](development-guide.md#timed-events) covers the basics; here we focus on the patterns for using them robustly.

### The store-and-cleanup pattern

Always store the event in a property and nil it when done:

```tads3
bombFuse = nil

activate()
{
    bombFuse = new Fuse(self, &explode, 5);
}

explode()
{
    bombFuse = nil;
    /* ... do the explosion ... */
}

deactivate()
{
    if (bombFuse != nil)
    {
        bombFuse.removeEvent();
        bombFuse = nil;
    }
}
```

This ensures you can always cancel the event cleanly, and you always know whether an event is pending.

### The guard pattern

Prevent duplicate events by checking before creating:

```tads3
startTicking()
{
    if (tickDaemon == nil)
        tickDaemon = new Daemon(self, &tick, 1);
}
```

Without the guard, calling `startTicking()` twice would create two daemons, both calling `tick()` every turn.

### SenseFuse and SenseDaemon

These variants only display their message when the player can sense a specified source object. A `SenseFuse` takes an additional argument specifying the source:

```tads3
/* The clock only chimes audibly if the player can hear it */
new SenseFuse(clock, &chime, 3, clock, sound);
```

The fourth argument is the source object to test, and the fifth is the sense to check. If the player cannot hear the clock when it fires, the message is silently suppressed. Use these for ambient effects — ticking clocks, dripping water, distant thunder — that should only be narrated when perceivable.

### PromptDaemon

A `PromptDaemon` fires just before the command prompt is displayed, every turn. It is useful for status updates or ambient descriptions that should appear after all action processing is complete:

```tads3
new PromptDaemon(self, &showWeather);
```

Unlike a regular Daemon, a PromptDaemon does not use a turn interval — it fires every prompt.

For worked examples with full game context, see the Tour Guide pages on [Fuse](../library/guide/fuse.md) and [Daemon](../library/guide/daemon.md).

## Agenda-Driven NPC Patterns

`AgendaItem` is adv3's mechanism for giving NPCs proactive behavior — things they want to say or do when conditions are right, rather than simply reacting to the player's commands.

### How agendas work

An `AgendaItem` has three key properties:

- **`isReady`** — a condition that must be true for the item to fire (default: `true`)
- **`isDone`** — set to true when the item has completed its work
- **`invokeItem()`** — the method that executes when the item fires

On each NPC turn, the actor checks its agenda list, removes any items marked `isDone`, and executes the lowest-`agendaOrder` item whose `isReady` is true.

```tads3
+ guard: Person 'guard' 'guard'
    "A stern-looking guard. "
    isHim = true
;

++ guardWarning: AgendaItem
    isReady = (guard.canSee(gPlayerChar)
               && gPlayerChar.isIn(throneRoom))
    invokeItem()
    {
        "The guard clears his throat. <q>You shouldn't be here,</q>
        he says pointedly. ";
        isDone = true;
    }
;
```

The guard says his line the first time the player enters the throne room while the guard can see them. Because `isDone` is set to true, it fires only once.

### Adding items to the agenda

Items do not automatically start on the agenda. You must add them explicitly:

```tads3
guard.addToAgenda(guardWarning);
```

You can add items from anywhere — during action processing, from another AgendaItem, from a topic response. To add an item during game initialization, set `initiallyActive = true` on the AgendaItem.

### ConvAgendaItem

A `ConvAgendaItem` is an AgendaItem that only fires when the actor has not already conversed this turn and can talk to its target (the PC by default). This prevents the NPC from interrupting their own conversation:

```tads3
++ guardGreeting: ConvAgendaItem
    invokeItem()
    {
        "The guard waves you over. <q>Hey, come here a moment,</q>
        he calls. ";
        isDone = true;
    }
;
```

### DelayedAgendaItem

A `DelayedAgendaItem` becomes ready after a specified number of game clock turns. Use `setDelay()` for convenience:

```tads3
guard.addToAgenda(guardReminder.setDelay(10));
```

This adds the item to the agenda and sets it to fire 10 turns from now.

### Agendas vs. Daemons

Both Daemons and AgendaItems can make NPCs do things on their turn, but they work differently:

- A **Daemon** fires unconditionally on schedule, whether or not the NPC is taking a turn. It is a global timer.
- An **AgendaItem** fires only during the NPC's own turn, only when `isReady` is true, and only once (unless you reset `isDone`). It is part of the NPC's decision-making.

Use Daemons for world events (weather, background sounds). Use AgendaItems for NPC behavior that should feel like the NPC is making a choice.

## Report Accumulation

When the player types TAKE ALL, adv3 executes the Take action separately for each object. Without special handling, the output would be a repetitive series of "Taken." messages. The report accumulation system solves this.

### How it works

During action execution, output is not displayed immediately. Instead, it is collected as `CommandReport` objects in the `CommandTranscript` (accessible via `gTranscript`). After all objects have been processed, the transcript is rendered, consolidating reports where possible.

The key report types:

- **`defaultReport(msg)`** — a terse confirmation like "Taken." or "Dropped." If multiple objects produce the same default report, only one is shown.
- **`mainReport(msg)`** — a specific result message. Replaces any default report for this object. Each object's main report is shown individually.
- **`reportAfter(msg)`** — appended after the main report. Used for side effects.
- **`reportBefore(msg)`** — prepended before the main report.

### When you need to care

For most games, the default report system just works. You need to think about it only when:

1. **Writing a custom action** that handles multiple direct objects and should consolidate results.
2. **Overriding an action handler** where you want your message to suppress the library's default "Taken." or similar.
3. **Adding side-effect messages** to existing actions (use `reportAfter` rather than raw output).

The rule of thumb: in an `action()` method, use `defaultReport()` or `mainReport()` rather than bare double-quoted strings. This ensures your messages participate in the transcript system and render correctly for multi-object commands.

For the full details, see [Action Results](../library/actions/action-results.md) and [Manipulating the Transcript](../library/advanced/transcript.md).

---

*Back to the [Architecture Overview](overview.md) for the big picture, or the [IF Development Guide](development-guide.md) for a practical introduction.*
