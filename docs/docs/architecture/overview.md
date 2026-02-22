# TADS 3 Architecture Overview

TADS 3 is not a monolithic system. It is built in layers, and understanding those layers is the key to understanding everything else. This document is a map of the whole — the architecture from the virtual machine up through the library to your game. We will not go deep on any single topic here. Instead, we will show you how the pieces connect, and point you to the detailed documentation for each piece.

[The Layered Stack](#the-layered-stack) | [The Build Pipeline](#the-build-pipeline) | [The adv3 Module Map](#the-adv3-module-map) | [The Three Pillars](#the-three-pillars-things-actions-actors) | [Class Hierarchies](#class-hierarchy-maps) | [Containment](#the-containment-model) | [Senses](#the-sensory-model) | [Pre-Initialization](#pre-initialization) | [The Turn Cycle](#the-turn-cycle)

---

## The Layered Stack

Four layers sit on top of each other, each building on the one below.

```
┌──────────────────────────────────────┐
│          Your Game (.t files)        │
├──────────────────────────────────────┤
│   adv3 Library (adv3.tl — 35 modules)│
├──────────────────────────────────────┤
│   System Library (tads.h, t3.h, etc.)│
├──────────────────────────────────────┤
│       T3 Virtual Machine             │
└──────────────────────────────────────┘
```

**The T3 Virtual Machine** is a bytecode interpreter. It provides the runtime for the TADS 3 language — garbage collection, object creation, property dispatch, save/restore, and a set of [intrinsic function sets](../intrinsics/index.md) for I/O, regular expressions, file access, and more. The VM is documented in the [VM Specification](../vm-spec/index.md).

**The system library** is a thin set of headers — `tads.h`, `t3.h`, `tok.h`, `vector.h`, `dict.h`, and others — that expose the VM's intrinsic classes and functions to TADS 3 source code. When you write `#include <tads.h>`, you get access to `toString()`, `toInteger()`, regular expression functions, and the basic object model. The system library knows nothing about interactive fiction.

**The adv3 library** is where IF happens. It provides the parser, the world model, the action system, the actor and conversation framework, the output pipeline, and everything else a text adventure needs. The adv3 library is not part of the language — it is a TADS 3 program, written in the same language you use for your game. When you write `#include <adv3.h>`, you pull in the library's header, which defines the macros, properties, and dictionary objects that form the adv3 API. The actual library source is linked as a pre-compiled unit via `adv3.tl`.

**Your game** is the top layer. It `#include`s the adv3 header, defines rooms, objects, actors, and actions, and links against the adv3 library. You can override, extend, or replace anything in adv3 — the library is designed for it.

The language module sits alongside adv3 as a partner. The English-specific module (`en_us.tl`) provides grammar rules, verb definitions, message text, and natural language generation. A different language module could replace `en_us` entirely without changing adv3 itself. This is why your game always includes both headers:

```tads3
#include <adv3.h>
#include <en_us.h>
```

## The Build Pipeline

A TADS 3 game starts as `.t` source files and ends as a `.t3` image file that an interpreter can run.

```
  .t source files
       │
       ▼
  t3make (compiler + linker)
       │  reads .t3m project file
       │  compiles sources
       │  links adv3.tl + en_us.tl
       │  runs pre-initialization
       │  writes .t3 image
       ▼
  .t3 image file
       │
       ▼
  Interpreter (FrobTADS, QTads, etc.)
```

The `.t3m` project file tells `t3make` what to compile and how. A minimal one looks like this:

```
-D LANGUAGE=en_us
-Fy obj
-Fo obj
-o mygame.t3
-lib system
-lib adv3/adv3
-source mygame
```

The `-lib` lines link the system library and adv3. The `-source` line lists your game source (without the `.t` extension). You can have as many `-source` lines as you need. See [Compiling and Linking](../tools/build.md) for the full set of compiler options.

**Pre-initialization** is a distinctive feature of the build process. After compiling and linking, `t3make` runs all `PreinitObject.execute()` methods, then snapshots the resulting object state into the `.t3` image. This means expensive setup work — building index tables, registering objects in class lists, resolving cross-references — happens once at compile time rather than every time the game starts. We will return to this in [Pre-Initialization](#pre-initialization) below.

[TADS Workbench](../tools/workbench/overview.md) provides a graphical IDE that wraps `t3make` with a project editor, source editor, and integrated debugger. Under the hood it runs the same compiler.

## The adv3 Module Map

The adv3 library is organized into 35 source modules, each responsible for a distinct area of functionality. When you need to understand or override something, knowing which file to look in is half the battle.

### Core engine

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `exec.t` | 1,852 | The command execution pipeline — from raw input tokens to a completed action |
| `action.t` | 6,670 | The Action class hierarchy and the verify/check/action execution phases |
| `actions.t` | 3,202 | Built-in action definitions (Take, Drop, Look, Examine, and dozens more) |
| `parser.t` | 7,133 | The command parser, grammar matching, and CommandRanking |
| `resolver.t` | 1,085 | Noun phrase resolution — mapping words to game objects |
| `disambig.t` | 609 | Disambiguation — asking "which one do you mean?" and interpreting the answer |
| `verify.t` | 703 | The VerifyResult hierarchy that drives object selection |
| `precond.t` | 1,176 | PreCondition objects (objHeld, objVisible, objOpened, etc.) |

### World model

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `thing.t` | 10,307 | VocabObject, Thing, and everything about physical objects in the game world |
| `objects.t` | 6,063 | The container hierarchy, mix-in classes (Openable, Lockable), Fixture, Decoration |
| `travel.t` | 7,022 | Rooms, directions, TravelConnectors, doors, passages, NestedRooms |
| `sense.t` | 866 | The sensory model — Material, Sense, transparency levels |
| `extras.t` | 3,789 | ComplexContainer, SensoryEmanation, Collective, MultiLoc, and more |

### Actors and conversation

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `actor.t` | 10,583 | Actor, ActorState, TopicDatabase, ConvNode, AgendaItem, conversation management |

### Game loop and events

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `events.t` | 1,294 | The scheduler (`runScheduler`), Fuse, Daemon, SenseFuse, PromptDaemon |
| `misc.t` | 2,489 | GameMainDef, global state, utility functions |
| `score.t` | 520 | Achievement-based scoring |

### Output and display

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `output.t` | 2,017 | The output stream stack and OutputManager |
| `report.t` | 1,955 | The deferred CommandTranscript and CommandReport system |
| `lister.t` | 2,241 | List formatting for room contents, inventory, and container listings |
| `status.t` | 568 | The status line |
| `banner.t` | 1,225 | Banner windows for split-screen layouts |
| `input.t` | 1,099 | The input manager |

### Support systems

| Module | Lines | Responsibility |
|--------|------:|----------------|
| `hintsys.t` | 669 | The adaptive hint system |
| `footnote.t` | — | Footnote management |
| `settings.t` | 605 | Persistent game settings and preferences |
| `modid.t` | 638 | Module identification and GameInfo metadata |
| `pov.t` | — | Point-of-view tracking |
| `tips.t` | — | Context-sensitive gameplay tips |
| `menusys.t` | 495 | Menu system framework |
| `menucon.t` | 1,136 | Console-mode menu implementation |
| `exits.t` | — | Exit lister (shows available exits) |
| `numbers.t` | — | Number word parsing |
| `console.t` | — | Console I/O adapter |

### Language module (English)

| Module | Responsibility |
|--------|----------------|
| `en_us/en_us.t` | Grammar rules, VerbRule definitions, English-specific language logic |
| `en_us/en_us.h` | English macros and vocabulary properties |
| `en_us/msg_neu.t` | All library messages in English (neutral voice) |
| `en_us/instruct.t` | Built-in instructions text shown at game start |

## The Three Pillars: Things, Actions, Actors

Three subsystems form the heart of adv3. Every command the player types involves all three.

**Things** are the physical world. Every object in the game — from a brass key to a dark forest — is an instance of `Thing` or one of its descendants. Things carry vocabulary words for the parser, descriptions for the player, containment relationships, sensory properties, and most importantly, *action handlers*. When the player types TAKE THE KEY, it is the key object that defines what "take" means for a key, through its `dobjFor(Take)` handler.

**Actions** are the verbs. An Action object represents a command: Take, Drop, Look, Open, PutIn, AskAbout. The action system drives the command execution cycle — parsing the player's input, resolving noun phrases to Things, then running the verify/check/action pipeline on those Things. Actions know *how* to execute a command in general; Things know *what happens* when a specific command is applied to them.

**Actors** are the people. The player character and every NPC are Actor objects — which are also Things, so they exist in the physical world and can be seen, talked to, and interacted with. Actors execute Actions on behalf of themselves or in response to commands from others. Each Actor has its own state machine (`ActorState`), conversation database (`TopicDatabase`), and agenda (`AgendaItem` list).

The interlock works like this: the player types a command. The parser finds an Action. The Action resolves noun phrases to Things. The Action calls the relevant `dobjFor`/`iobjFor` handlers on those Things. The Actor that issued the command receives `beforeAction`/`afterAction` notifications, as does every other Actor and Thing in scope. The result is reported through the output pipeline.

For the complete pipeline specification, see [The Command Execution Cycle](../library/advanced/command-execution-cycle.md).

## Class Hierarchy Maps

These trees show the major classes in each pillar. They are not exhaustive — adv3 defines many more specialized classes — but they cover the classes you will encounter most often.

### Things

The world model class hierarchy, drawn from `thing.t`, `objects.t`, and `extras.t`:

```
VocabObject
└── Thing
    ├── NonPortable
    │   ├── Fixture
    │   │   ├── Component
    │   │   ├── CustomFixture
    │   │   ├── SecretFixture
    │   │   ├── Decoration
    │   │   │   └── Unthing
    │   │   └── Distant
    │   └── Immovable
    │       ├── CustomImmovable
    │       └── Heavy
    ├── BulkLimiter
    │   ├── BasicContainer
    │   │   └── Container
    │   │       ├── OpenableContainer  (= Openable + Container)
    │   │       │   ├── LockableContainer  (= Lockable + OpenableContainer)
    │   │       │   └── KeyedContainer  (= LockableWithKey + OpenableContainer)
    │   │       ├── RestrictedContainer
    │   │       └── SingleContainer
    │   └── Surface
    ├── Readable
    ├── Consultable
    ├── Food
    ├── Wearable
    ├── LightSource
    │   └── Flashlight  (= LightSource + Switch)
    ├── OnOffControl
    │   └── Switch
    ├── Settable
    │   └── Dial
    │       ├── NumberedDial
    │       └── LabeledDial
    ├── Button
    ├── Lever
    │   └── SpringLever
    ├── Intangible
    │   └── Vaporous
    │       └── SensoryEmanation
    │           ├── Noise / SimpleNoise
    │           └── Odor / SimpleOdor
    └── Hidden

Mix-in classes (combine with any Thing subclass):
    Openable ← BasicOpenable ← Linkable
    Lockable ← Linkable
    LockableWithKey ← Lockable
    IndirectLockable ← Lockable

Multi-location classes:
    BaseMultiLoc
    ├── MultiLoc
    └── MultiInstance
        └── MultiFaceted
```

### Actions

The action class hierarchy, from `action.t`:

```
Action (extends BasicProd)
├── IAction                 no objects: LOOK, INVENTORY, QUIT
├── TAction                 one object: TAKE box, EXAMINE sword
│   └── TIAction            two objects: PUT box IN chest, GIVE coin TO guard
├── LiteralAction           literal string: SAY "hello"  (= LiteralActionBase + IAction)
├── LiteralTAction          object + literal: TYPE "code" ON keypad  (= LiteralActionBase + TAction)
├── TopicAction             topic phrase: THINK ABOUT war  (= TopicActionBase + IAction)
└── TopicTAction            object + topic: ASK guard ABOUT war  (= TopicActionBase + TAction)
```

Specific actions like `TakeAction`, `DropAction`, `ExamineAction` are defined using macros such as `DefineTAction(Take)`, which expands to `class TakeAction: TAction` with the appropriate property bindings. These are defined in `actions.t` and `en_us/en_us.t`.

### Rooms and travel

The location and travel hierarchy, from `travel.t`:

```
BasicLocation (extends Thing)
├── Room (= Fixture + BasicLocation + RoomAutoConnector)
│   ├── DarkRoom
│   ├── OutdoorRoom
│   ├── ShipboardRoom  (= Shipboard + Room)
│   └── FloorlessRoom  (= Floorless + Room)
└── NestedRoom
    ├── BasicChair
    │   ├── Chair  (= BasicChair + Surface)
    │   ├── BasicBed
    │   │   ├── Bed  (= BasicBed + Surface)
    │   │   └── BasicPlatform
    │   │       ├── Platform  (= BasicPlatform + Surface)
    │   │       └── Booth  (= BasicPlatform + Container)
    └── HighNestedRoom
    └── Vehicle  (= NestedRoom + Traveler)

TravelConnector (extends Thing)
├── RoomConnector
│   ├── OneWayRoomConnector
│   └── RoomAutoConnector
├── Passage  (= Linkable + Fixture + TravelConnector)
│   ├── ThroughPassage
│   │   ├── PathPassage
│   │   ├── ExitOnlyPassage
│   │   └── BasicDoor  (= BasicOpenable + ThroughPassage)
│   │       ├── Door  (= Openable + BasicDoor)
│   │       │   └── AutoClosingDoor
│   │       ├── SecretDoor
│   │       │   └── HiddenDoor
│   └── Stairway
│       ├── StairwayUp
│       └── StairwayDown
├── AskConnector
│   └── DefaultAskConnector
└── TravelMessage  (= TravelWithMessage + TravelConnector)
    ├── NoTravelMessage
    │   └── FakeConnector
    └── DeadEndConnector

Direction
├── CompassDirection    north, south, east, west, ne, nw, se, sw
├── VerticalDirection   up, down
├── ShipboardDirection  port, starboard, fore, aft
└── RelativeDirection   in, out
```

## The Containment Model

The physical world in adv3 is a tree of containment. Every Thing has a `location` property pointing to its container, and every container has a `contents` list of the Things it holds. Rooms are the roots of these trees — they have no location of their own.

In source code, the `+` prefix is syntactic sugar for setting `location` to the most recently defined object at the previous nesting level:

```tads3
cave: Room 'Dark Cave'
    "The walls glisten with moisture. "
;

+ torch: Flashlight 'old torch' 'torch'
    "A battered wooden torch, still burning. "
    isLit = true
;

+ chest: OpenableContainer 'wooden chest' 'chest'
    "A sturdy wooden chest with iron bands. "
;

++ goldCoin: Thing 'gold coin' 'gold coin'
    "A gleaming gold coin. "
;
```

Here `torch` and `chest` are in `cave` (one `+` = one level deep). `goldCoin` is in `chest` (two `++` = two levels). The nesting mirrors the physical containment.

The containment tree determines **scope** — which objects the parser considers when resolving noun phrases. By default, an object is in scope if the player character can sense it through the containment tree. The `isIn(obj)` method walks up the containment tree to test whether one object is (directly or indirectly) inside another. This is the foundation of most spatial reasoning in adv3.

For the full architecture of the containment tree — container types, reachability, bulk and weight, nested rooms, and multi-location objects — see [Containment Model](containment-model.md). For the full scope mechanism, including sensory scope, topic scope, and how to extend scope, see [Redefining Scope](../library/advanced/scope.md).

## The Sensory Model

Most IF systems treat visibility as a simple boolean — you can either see an object or you cannot. adv3 takes a different approach. It models four senses — sight, sound, smell, and touch — and defines how each sense propagates through materials.

Every container has a `material` property, which is an instance of the `Material` class. A Material defines four transparency levels, one per sense:

```tads3
/* The default material: opaque to everything */
adventium: Material
    seeThru = opaque
    hearThru = opaque
    smellThru = opaque
    touchThru = opaque
;

/* Glass: you can see through it, but not hear, smell, or touch */
glass: Material
    seeThru = transparent
    hearThru = opaque
    smellThru = opaque
    touchThru = opaque
;

/* Paper: blocks sight and touch, but sound and smell pass through */
paper: Material
    seeThru = opaque
    hearThru = transparent
    smellThru = transparent
    touchThru = opaque
;
```

When the parser needs to determine whether the player can perceive an object, it traces a path through the containment tree from the player character to the target object, asking each intervening container's material how the relevant sense passes through it. The result is a `SenseInfo` object carrying a transparency level: `transparent`, `obscured`, `distant`, or `opaque`.

This matters for game design in several ways:

- A closed glass jar lets you see the key inside but not take it (touch is opaque).
- Sounds from behind a closed door can be heard but their source cannot be seen.
- A player in a dark room can still hear and smell objects, even though they cannot see them.
- The `SensoryEmanation` classes (`Noise`, `Odor`) use this model to create ambient sounds and smells that propagate through the containment tree based on material transparency.

The five built-in materials are `adventium` (opaque to all), `paper`, `glass`, `fineMesh` (transparent to sight, sound, and smell), and `coarseMesh` (transparent to all senses). You can define your own materials for custom behavior.

For the full architecture of sense path calculation, brightness propagation, and how senses feed into scope, see [Sense and Perception](sense-perception.md).

## Pre-Initialization

TADS 3 has a distinctive compile-time execution feature. After compiling and linking all source modules, `t3make` runs the program in a special pre-initialization phase. During this phase, every `PreinitObject` gets its `execute()` method called. The resulting object state is then frozen into the `.t3` image file.

This means that expensive setup work happens once at build time, not at game startup:

- Direction objects register themselves in the global `allDirections` list
- The action system builds lookup tables mapping object roles to property names
- Objects compute and cache initial sense paths and containment relationships
- Any `ModuleExecObject` subclass can perform arbitrary initialization

The practical consequence is that `PreinitObject` is the right place for any setup that needs to scan all objects of a certain class, build indexes, or establish cross-references. These operations run once, and their results are baked into the image.

`InitObject` is the complementary class for setup that must happen at runtime — after a game is loaded from a save file, for example, or when the state depends on the particular session. `InitObject.execute()` runs every time the game starts, whether from scratch or from a restored save.

```tads3
/* Runs once at compile time; results are saved in the .t3 image */
mySetup: PreinitObject
    execute()
    {
        /* Build a lookup table of all Readable objects */
        forEachInstance(Readable, {obj: readableIndex[obj.name] = obj});
    }
    readableIndex = static new LookupTable()
;

/* Runs every time the game starts */
myRuntimeSetup: InitObject
    execute()
    {
        /* Display a session-specific greeting */
        "Welcome back!\b";
    }
;
```

## The Turn Cycle

Here is the high-level flow of a single turn. Each step is a complex subsystem in its own right — this is the map, not the territory.

1. **Read input** — The scheduler calls the player character's `executeTurn()`, which reads a line of text from the player.
2. **Pre-parse** — `StringPreParser` objects get a chance to transform the raw input string before parsing.
3. **Parse** — The parser tokenizes the input and matches it against grammar rules, producing a list of `CommandRanking` candidates. The best interpretation is selected.
4. **Resolve nouns** — For `TAction` and `TIAction`, noun phrases are resolved to game objects through vocabulary matching, scope filtering, and the verify pass.
5. **Global remapping** — `GlobalRemapping` objects can redirect the entire command before execution proceeds.
6. **Verify** — Each candidate object's `verify()` handler is called. `VerifyResult` objects rank how logical the action is for that object. This drives disambiguation — the parser picks the object with the best verify result.
7. **Pre-conditions** — `PreCondition` objects run between verify and check. They may trigger implicit actions (e.g., automatically taking an object before examining it).
8. **Check** — Each object's `check()` handler runs. Unlike verify, check failures do not affect disambiguation — they represent conditions the player would only discover by trying.
9. **Action** — Each object's `action()` handler runs. This is where world state changes happen.
10. **Report** — The `CommandTranscript` collects deferred reports from all phases and displays them.
11. **After-action** — `afterAction` notifications fire on the actor and every object in scope.
12. **Fuses and daemons** — The scheduler runs any pending `Fuse` or `Daemon` events whose time has come.
13. **Next actor** — The scheduler moves to the next `Schedulable` (typically an NPC) at the current game clock time, then advances the clock.

For the complete, step-by-step specification of this cycle, see [The Command Execution Cycle](../library/advanced/command-execution-cycle.md). For the architecture of steps 1–5 (the parser pipeline), see [The Parser Pipeline](parser-pipeline.md). For the architecture of steps 6–9 (action resolution), see [Action Resolution](action-resolution.md). For the critical verify-vs-check distinction, see [Verify and Check](../library/actions/verify-check.md).

---

*Next: [IF Development Guide](development-guide.md) for a practical roadmap of building a TADS 3 game, or [Design Patterns](design-patterns.md) for the recurring code patterns in adv3.*
