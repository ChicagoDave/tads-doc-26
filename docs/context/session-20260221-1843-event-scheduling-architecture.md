# Session Summary: 2026-02-21 - Event Scheduling Architecture

## Status: Completed

## Goals
- Create the 6th and final planned deep-dive architecture document: Event Scheduling
- Integrate the new document into all existing navigation and cross-reference structures
- Complete the full set of six planned architecture deep-dives

## Completed

### New Document: event-scheduling.md
Created `/Users/david/repos/tads3/docs/docs/architecture/event-scheduling.md`, a comprehensive 9-section deep-dive following the template established by the five preceding deep-dives (parser-pipeline, action-resolution, sense-perception, containment-model, message-system).

**Section breakdown:**

1. **Event Scheduling Overview** — ASCII 3-layer diagram (Scheduling Loop -> Turn-Based Events -> Real-Time Events). Source-file-to-role mapping table covering events.t, actor.t, misc.t, input.t, adv3.h.

2. **The Scheduling Loop** — Complete walkthrough of `runScheduler()` (events.t:26). ASCII algorithm flowchart. Game clock time, `allSchedulables`, `getNextRunTime()`, `calcScheduleOrder()`, `executeTurn()`. Design decisions: abstract clock, return-value rescheduling, exception safety.

3. **Actors as Schedulables** — Actor inherits Schedulable. Priority tier table (PC ready=100, NPC ready=200, PC idle=300, NPC idle=400, eventManager=1000). `readyForTurn()`, `addBusyTime()`, `executeTurn()` wrapping in EventAction and sensory context. `idleTurn()` for NPCs.

4. **Turn-Based Events** — Class hierarchy (BasicEvent -> Event -> Fuse/Daemon/PromptDaemon with Sense variants). `eventManager` singleton. `executeList()` algorithm with `eventOrder` sorting and sense cache invalidation. Fuse (one-shot) and Daemon (recurring) constructors and execution. `callMethod()` dual-context wrapping. Event ordering and delay/removal operations.

5. **Sense-Aware Events** — SenseFuse and SenseDaemon. How `callWithSenseContext()` suppresses output but not side effects. Connection to the Sense and Perception deep-dive.

6. **Prompt Daemons** — PromptDaemon and OneTimePromptDaemon. Fired by `readMainCommand()` in input.t, not by game clock. Comparison table vs regular daemons. OneTimePromptDaemon for game-start conversation initiation.

7. **Real-Time Events** — `realTimeManager` singleton, wall-clock milliseconds. RealTimeFuse, RealTimeDaemon, RealTimeSenseFuse, RealTimeSenseDaemon. Save/restore handling via PreSaveObject/PostRestoreObject. Drift prevention in RealTimeDaemon. When real-time events execute (during input, not in runScheduler).

8. **Author Customization Patterns** — Six cookbook-style patterns: creating/tracking events, duplicate guards, delayed NPC actions, event ordering, OneTimePromptDaemon for game start, real-time countdown. Reference to design-patterns.md for robustness patterns.

9. **Practical Intervention Points** — Four lookup tables: creating/removing events, scheduling priority, real-time integration, NPC behavior hooks.

### Navigation and Cross-Reference Integration

Updated five existing files to integrate the new document:

- `docs/mkdocs.yml` — Added nav entry for Event Scheduling after Message System, before Design Patterns
- `docs/docs/architecture/index.md` — Added Event Scheduling entry with description between Message System and IF Development Guide
- `docs/docs/architecture/overview.md` — Added cross-reference after the "Game loop and events" module table; updated turn cycle section to link steps 12-13 to the new deep-dive
- `docs/docs/architecture/message-system.md` — Updated footer: replaced development-guide.md link with event-scheduling.md link
- `docs/docs/architecture/design-patterns.md` — Added forward cross-reference to event-scheduling deep-dive in the "Daemon and Fuse Patterns" section

### Build Verification

mkdocs build completed with zero warnings or errors.

## Key Decisions

### 1. Top-Down Scheduling-Loop-First Structure
Starts with the `runScheduler()` algorithm before explaining what it schedules. This mirrors how the system actually works: the loop selects who runs, then the selected entity does its thing. The reader understands the frame before filling in the pieces.

### 2. Actors and Events Unified Under Schedulable
Both are presented as equals under the scheduling loop, reflecting the architecture where Actor and eventManager are both Schedulable objects with priority ordering. No special-casing of actors in the narrative matches no special-casing in the code.

### 3. Sense-Aware Events in Their Own Section
Rather than burying SenseFuse/SenseDaemon details inside the turn-based events section, they get a dedicated section. The key insight — code runs regardless, only output is filtered — deserves emphasis so authors do not accidentally rely on suppression to prevent side effects.

### 4. Prompt Daemons Separated from Turn-Based Events
Prompt daemons operate on a fundamentally different trigger (command prompt, not game clock), so they get their own section with a comparison table. Mixing them with Fuse/Daemon would obscure a critical behavioral difference.

### 5. Real-Time Events as a Separate Parallel System
Emphasized that real-time events execute during input, not in `runScheduler()`, and covered save/restore handling which is unique to real-time. The separation makes clear that the two systems do not interfere with each other's timing guarantees.

## Open Items

### Short Term
- All 6 of 6 planned deep-dives are now complete
- Review `docs/docs/architecture/index.md` for coherence as a reading guide (all entries now present)

### Long Term
- Consider a cross-cutting "how the systems interact" summary document tying all six deep-dives together
- Audit footer links across all six deep-dives for consistency (each should chain to the next)

## Files Modified

**New** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/event-scheduling.md` — Full 9-section deep-dive on the TADS 3 event scheduling system

**Updated** (5 files):
- `/Users/david/repos/tads3/docs/mkdocs.yml` — Added Event Scheduling nav entry
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — Added entry in deep-dive listing
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — Added cross-references after module table and in turn cycle section
- `/Users/david/repos/tads3/docs/docs/architecture/message-system.md` — Updated footer link from development-guide.md to event-scheduling.md
- `/Users/david/repos/tads3/docs/docs/architecture/design-patterns.md` — Added forward link to event-scheduling.md

## Architectural Notes

The event scheduling system has an elegant three-level architecture worth preserving for future reference:

**Level 1 — Schedulable loop** (`runScheduler()` in events.t): A priority-based cooperative scheduler. Finds the earliest `nextRunTime`, sorts ties by `scheduleOrder`, and dispatches. No preemption, no threads — pure cooperative multitasking.

**Level 2 — Turn-based events** (`eventManager` Schedulable, priority 1000): Sits inside the loop as a single Schedulable with the lowest priority. Manages its own internal queue of Fuse/Daemon objects sorted by `eventOrder`. This two-level scheduling — the main loop selects eventManager, eventManager selects individual events — keeps the main loop simple while supporting fine-grained event ordering within a turn.

**Level 3 — Real-time events** (`realTimeManager`): Operates entirely outside the main loop, firing during input waits. This separation means real-time events never interfere with turn sequencing, and turn-based events never delay real-time processing.

The Actor-as-Schedulable design is the key architectural insight: actors are not special-cased in the game loop. They are Schedulable objects that happen to read commands and perform actions. The same loop handles player turns, NPC turns, and fuse/daemon execution with no special control flow — just priority ordering.

Source files referenced throughout: `events.t`, `actor.t`, `misc.t`, `input.t`, `adv3.h`.

## Notes

**Session duration**: ~1 hour (estimated)

**Approach**: Document written top-down following the established template from the five preceding deep-dives. Sections organized to match the execution order of the system (scheduling loop first, then the schedulable types, then the parallel real-time system). Cookbook patterns and lookup tables added at the end following the same pattern as containment-model.md and message-system.md.

**Architecture doc count**: 6 of 6 planned deep-dives complete. The full set is:
1. Parser Pipeline (`parser-pipeline.md`)
2. Action Resolution (`action-resolution.md`)
3. Sense and Perception (`sense-perception.md`)
4. Containment Model (`containment-model.md`)
5. Message System (`message-system.md`)
6. Event Scheduling (`event-scheduling.md`)

---

**Progressive update**: Session completed 2026-02-21 18:43
