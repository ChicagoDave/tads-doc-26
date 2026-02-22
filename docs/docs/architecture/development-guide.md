# IF Development Guide

The [tutorial](../getting-started/tutorial/generalintroduction.md) shows you how to build a specific game. This guide shows you the structure of *any* adv3 game. Think of it as the blueprint you keep next to you while writing — a conceptual roadmap of the building blocks and how they fit together.

We assume you have read the [Architecture Overview](overview.md). We will not repeat the high-level picture here, but we will reference it often.

[The Minimal Game](#the-minimal-game-skeleton) | [Rooms and Travel](#rooms-directions-and-travel) | [Things](#the-thing-hierarchy) | [Actors](#actor-creation-and-conversations) | [Output](#output-formatting) | [Timed Events](#timed-events) | [Scoring](#score-and-achievements) | [Compiling](#compilation-and-testing) | [Source Organization](#source-organization)

---

## The Minimal Game Skeleton

Every adv3 game needs at least four objects. Here is a complete, compilable game:

```tads3
#include <adv3.h>
#include <en_us.h>

versionInfo: GameID
    IFID = 'B8563851-6257-77C4-C150-B7E755D1170F'
    name = 'My First Game'
    byline = 'by A. Author'
    version = '1'
    desc = 'A minimal TADS 3 game. '
;

gameMain: GameMainDef
    initialPlayerChar = me
    showIntro()
    {
        "Welcome to your adventure!\b";
    }
;

startRoom: Room 'Start Room'
    "You are in a featureless white room. There is a door to the north. "
;

+ me: Actor
;
```

**`versionInfo`** is a `GameID` object that holds the game's bibliographic identity — its name, author, version, and IFID (a unique identifier for the IF Archive). The IFID should be a UUID; you can generate one with any UUID tool.

**`gameMain`** is the control object. It must be an instance of `GameMainDef`, and it must define `initialPlayerChar` — the Actor who serves as the player character. The `showIntro()` method runs once when the game starts (but not when restoring a save). Other useful properties include `showGoodbye()` (runs on QUIT), `maxScore` (for the status-line score display), and `verbose` (whether the game starts in verbose mode).

**The Room** is the starting location. The single-quoted string `'Start Room'` is the room's name, shown on the status line and when entering the room. The double-quoted string is the room's description, shown on LOOK and when the player first enters.

**`+ me: Actor`** is the player character. The `+` places it inside `startRoom`. You do not need to give the player character any vocabulary or description — the library provides defaults for whichever Actor is serving as the PC.

## Rooms, Directions, and Travel

### Basic rooms

A Room is the fundamental unit of geography. Each Room is a self-contained location with a name and description:

```tads3
kitchen: Room 'Kitchen'
    "A warm kitchen with copper pots hanging from the ceiling.
    A doorway leads north to the living room. "
;
```

### Connecting rooms

The simplest way to connect two rooms is with direction properties. Each Room inherits properties for every compass direction, plus `up`, `down`, `in`, and `out`:

```tads3
kitchen: Room 'Kitchen'
    "A warm kitchen. A doorway leads north. "
    north = livingRoom
;

livingRoom: Room 'Living Room'
    "A cozy living room. The kitchen is to the south. "
    south = kitchen
;
```

When the player types GO NORTH in the kitchen, adv3 checks `kitchen.north`, finds `livingRoom`, and moves the player there. Note that connections are one-directional — if you want the player to go back, you must set `livingRoom.south = kitchen` as well. (If you want automatic two-way connections, use `RoomAutoConnector` or set both properties.)

### Room variants

**`DarkRoom`** starts with no light. The player needs a light source to see anything:

```tads3
cellar: DarkRoom 'Cellar'
    "A damp, musty cellar. Stairs lead up. "
    up = kitchen
;
```

**`OutdoorRoom`** behaves like a room but defaults to having sky instead of a ceiling and ground instead of a floor, which affects how the library describes room parts.

**`FloorlessRoom`** has no floor — objects dropped here fall to the room below.

### Doors

A Door is both a physical object and a travel connector. Because the player can approach a door from either side, doors come in pairs — one object per side, linked by `otherSide`:

```tads3
kitchen: Room 'Kitchen'
    "A kitchen. A heavy oak door leads east. "
    east = kitchenDoor
;

+ kitchenDoor: Door 'heavy oak door' 'oak door'
    otherSide = hallDoor
;

hallway: Room 'Hallway'
    "A long hallway. An oak door leads west. "
    west = hallDoor
;

+ hallDoor: Door 'heavy oak door' 'oak door'
    otherSide = kitchenDoor
;
```

The Door class provides the `isOpen`/`isClosed` state, an implicit OPEN action when the player tries to walk through a closed door, and synchronization between both sides (opening one side opens the other). To make a door lockable, use `LockableWithKey` as a mix-in:

```tads3
+ kitchenDoor: LockableWithKey, Door 'heavy oak door' 'oak door'
    otherSide = hallDoor
    isLocked = true
    keyList = [brassKey]
;
```

### Other connectors

**`TravelConnector`** is the base class for anything that connects rooms. When you set `north = someObject`, that object can be a Room (direct connection), a Door (physical passage), or any TravelConnector subclass.

**`FakeConnector`** displays a message instead of allowing travel — useful for explaining why a direction is blocked:

```tads3
kitchen: Room 'Kitchen'
    "A kitchen. The window faces south. "
    south: FakeConnector { "The window is too small to climb through. " }
;
```

**`DeadEndConnector`** lets the player travel to a location, see a brief description, and then automatically return. Useful for closets, alcoves, and other locations that do not deserve their own Room.

**`StairwayUp`** and **`StairwayDown`** are physical passage objects that also serve as connectors for the `up` and `down` directions.

### Regions

A `Region` groups rooms for shared behavior. You can use regions to define background sounds or smells that pervade an area, to trigger events when the player enters or leaves a zone, or to test whether the player is "in the forest" without checking every individual room:

```tads3
forestRegion: Region
;

clearing: Room 'Forest Clearing'
    "Sunlight filters through the trees. "
    regions = [forestRegion]
;

deepWoods: Room 'Deep Woods'
    "The trees press close. "
    regions = [forestRegion]
;
```

## The Thing Hierarchy

Everything the player can see, touch, take, or talk about is a Thing or one of its descendants. Things vary along three axes.

### Portability

By default, a `Thing` can be picked up and carried:

```tads3
+ brassKey: Thing 'small brass key' 'brass key'
    "A small, tarnished brass key. "
;
```

The single-quoted string is the **vocabulary** — the words the parser will recognize. The second single-quoted string is the **name** — the display name used in room listings and messages. (In practice, templates allow shorthand — see the [Tour Guide on vocabWords](../library/guide/vocabwords.md) for the full syntax.)

The double-quoted string is the **description**, displayed when the player types EXAMINE KEY.

For objects that should not be picked up:

- **`Fixture`** — permanently attached to its location. TAKE produces "That's not something you can take." Use for structural features: a fireplace, a window, a shelf.
- **`Decoration`** — like a Fixture, but also blocks most other interactions with "That's not important." Use for flavor-text scenery: carvings on a wall, patterns on a rug.
- **`Distant`** — visible but too far away to interact with. Use for objects the player can see across a distance: a mountain, a distant ship.
- **`Immovable`** — cannot be picked up but responds normally to other verbs. `Heavy` is an Immovable that explains it is too heavy to lift.

```tads3
+ fireplace: Fixture 'stone fireplace' 'fireplace'
    "A large stone fireplace dominates the north wall. "
;

+ paintings: Decoration 'oil paintings' 'paintings'
    "Several oil paintings hang on the walls. "
;

+ mountain: Distant 'distant mountain' 'mountain'
    "A snow-capped peak rises to the north. "
;
```

### Containment

Objects can hold other objects. The library provides several container types:

**`Container`** — things go inside it. LOOK IN shows contents; PUT X IN Y works.

**`Surface`** — things rest on top. PUT X ON Y works.

**`OpenableContainer`** — a Container that can be opened and closed. When closed, contents are hidden.

**`LockableContainer`** — an OpenableContainer that can be locked. Combine with `LockableWithKey` if a key is required.

```tads3
+ desk: Surface 'wooden desk' 'desk'
    "A sturdy oak desk. "
;

++ paperweight: Thing 'glass paperweight' 'paperweight'
    "A heavy glass paperweight with a butterfly inside. "
;

+ cabinet: LockableContainer 'metal cabinet' 'cabinet'
    "A small metal cabinet with a latch. "
    isLocked = nil
;
```

**`ComplexContainer`** (from `extras.t`) handles objects that are both a container and a surface — like a desk with a drawer and a top surface. See the [Tour Guide on ComplexContainer](../library/guide/complexcontainer.md) for details.

### State mix-ins

State mix-ins can be combined with any Thing subclass:

- **`Openable`** — adds open/close behavior without containment
- **`Lockable`** — adds lock/unlock behavior
- **`LockableWithKey`** — adds key-based locking

These are designed for mix-in composition:

```tads3
/* A box you can open, close, and lock with a key */
+ brassBox: LockableWithKey, OpenableContainer 'brass box' 'brass box'
    "A heavy brass box with a padlock. "
    isOpen = nil
    isLocked = true
    keyList = [brassKey]
;
```

The order matters: put mix-ins before the base class. `LockableWithKey, OpenableContainer` gives you a lockable openable container. See [Multiple Inheritance](../library/advanced/multiple-inheritance.md) for why class order matters.

### Description properties

Every Thing has several description properties that control how it appears in different contexts:

- **`desc`** — the EXAMINE description (double-quoted string or method)
- **`specialDesc`** — if defined, this replaces the object's entry in the room's contents list with a standalone paragraph
- **`initSpecialDesc`** — like `specialDesc`, but only used until the object is first picked up; after that, the object falls back to the normal contents list
- **`initDesc`** — an alternative EXAMINE description used until the object has been moved; after that, `desc` is used instead

```tads3
+ letter: Readable 'sealed letter' 'letter'
    "A letter sealed with red wax. "
    initSpecialDesc = "A sealed letter lies on the table. "
    readDesc = "Dear adventurer, beware the cellar..."
;
```

### Other useful Thing subclasses

**`Readable`** — adds a `readDesc` property for the READ command. **`Food`** — can be eaten. **`Wearable`** — can be worn. **`LightSource`** — emits light; the `Flashlight` subclass adds on/off switching. **`Button`** and **`Lever`** provide push/pull interactions.

For the complete class reference, see the [Things](../library/things/index.md) hub page and the [Tour Guide](../library/guide/thing-introduction.md).

## Actor Creation and Conversations

### A minimal NPC

An NPC is an Actor placed in a room, with at least one ActorState:

```tads3
+ guard: Person 'burly guard' 'guard'
    "A burly guard stands at attention. "
    isHim = true
;

++ guardStanding: ConversationReadyState
    isInitState = true
    specialDesc = "A burly guard stands at attention by the door. "
;

+++ guardTalking: InConversationState
    specialDesc = "The guard is talking to you. "
;
```

The `ConversationReadyState` is the NPC's default state — what they do when not in conversation. When the player initiates conversation (ASK, TELL, etc.), the NPC transitions to the `InConversationState`. The `isInitState = true` flag marks the starting state.

### Topics

Topics define what the NPC says in response to conversation commands. They nest inside an ActorState (or directly inside the Actor for state-independent topics):

```tads3
+++ AskTopic @brassKey
    "<q>What do you know about the brass key?</q> you ask.
    <.p><q>It opens the box in the cellar,</q> he replies. "
;

+++ DefaultAskTopic
    "<q>I don't know anything about that,</q> the guard says. "
;
```

`AskTopic @brassKey` responds when the player types ASK GUARD ABOUT KEY. The `@brassKey` matches the game object. `DefaultAskTopic` catches any ASK that does not match a specific topic.

The topic classes cover all conversation verbs: `AskTopic`, `TellTopic`, `AskTellTopic`, `GiveTopic`, `ShowTopic`, `YesTopic`, `NoTopic`, and their Default variants.

### Beyond basic topics

The conversation system has three levels of complexity. Basic topics (above) handle simple ASK/TELL exchanges. For branching conversations, **`ConvNode`** objects create conversation threads where the NPC asks a question and the player's response determines the next node. For NPC-initiated speech, **`AgendaItem`** objects queue behaviors that fire when conditions are met.

These are substantial systems. See [Choosing a Conversation System](../library/actors/conversation-systems.md) for a survey of approaches, [Programming Conversations](../library/actors/programming-conversations.md) for the full implementation guide, and [Creating Dynamic Characters](../library/actors/dynamic-characters.md) for the ActorState architecture.

## Output Formatting

### Basic output

In TADS 3, any double-quoted string inside a method body sends text to the player:

```tads3
showIntro()
{
    "Welcome to the adventure!\b";
}
```

The `\b` sequence produces a blank line (paragraph break). Other formatting sequences:

- `\n` — line break (no blank line)
- `\t` — tab
- `<.p>` — paragraph break (equivalent to `\b`)
- `<.br>` — line break (equivalent to `\n`)

### Embedded expressions

Use `<<expression>>` to embed computed values in output strings:

```tads3
desc()
{
    "The dial reads <<dialSetting>>. ";
    if (isOpen)
        "The lid is open. ";
}
```

### The say function

For programmatic output, use `say()`:

```tads3
say('The treasure is worth ' + toString(points) + ' points. ');
```

In practice, double-quoted strings with `<<>>` are almost always clearer than `say()`.

### Action reports

When writing action handlers, use the report functions rather than raw output:

- **`defaultReport(msg)`** — the standard terse confirmation (e.g., "Taken."). Suppressed if a more specific report is generated.
- **`mainReport(msg)`** — the primary result message. Replaces any default report.
- **`reportAfter(msg)`** — a message appended after the main report. Useful for side effects ("A loud click echoes through the room.").
- **`reportFailure(msg)`** — reports a failure. Marks the action as unsuccessful.

```tads3
dobjFor(Take)
{
    action()
    {
        inherited();
        if (isMagic)
            reportAfter('The object tingles in your hand. ');
    }
}
```

These report functions feed into the deferred `CommandTranscript` system, which batches reports intelligently — consolidating identical reports for multi-object commands, ordering implicit-action reports before main reports, and suppressing redundant defaults. See [Manipulating the Transcript](../library/advanced/transcript.md) for details.

## Timed Events

### Fuses

A `Fuse` fires once after a specified number of turns:

```tads3
bomb: Thing 'ticking bomb' 'bomb'
    "A bomb with a digital countdown display. "
    fuse = nil

    activate()
    {
        fuse = new Fuse(self, &explode, 5);
        "The countdown begins: five turns. ";
    }

    explode()
    {
        "BOOM! The bomb explodes! ";
        fuse = nil;
        finishGameMsg(ftDeath, [finishOptionUndo]);
    }
;
```

The three arguments to `new Fuse()` are: the object to call, the method to call, and the number of turns to wait.

### Daemons

A `Daemon` fires repeatedly at a regular interval:

```tads3
weatherDaemon: object
    daemon = nil
    counter = 0
    messages = ['The wind picks up. ',
                'Clouds gather overhead. ',
                'Rain begins to fall. ']

    start()
    {
        daemon = new Daemon(self, &tick, 3);
    }

    tick()
    {
        if (counter < messages.length())
        {
            say(messages[++counter]);
        }
        else
        {
            daemon.removeEvent();
            daemon = nil;
        }
    }
;
```

This daemon fires every 3 turns, cycling through weather messages, then stops itself.

### Cleanup

Always store the event object in a property and nil it out when done. To stop an event early, call `eventObj.removeEvent()`. A `SenseFuse` and `SenseDaemon` are variants that only fire their message when the player can sense a specified source object — useful for sounds, smells, and visual effects.

For worked examples, see the Tour Guide pages on [Fuse](../library/guide/fuse.md) and [Daemon](../library/guide/daemon.md).

## Score and Achievements

TADS 3 offers two scoring styles. You can use either or both.

### Simple scoring

Call `addToScore()` directly and set `gameMain.maxScore` by hand:

```tads3
gameMain: GameMainDef
    initialPlayerChar = me
    maxScore = 100
;

// Somewhere in your game logic:
addToScore(10, 'finding the brass key');
```

### Achievement objects

Define `Achievement` objects with point values. The library automatically computes `maxScore`:

```tads3
foundKeyAchievement: Achievement
    points = 10
    desc = "finding the brass key"
;

// When the player finds the key:
foundKeyAchievement.awardPointsOnce();
```

`awardPointsOnce()` ensures the achievement is only scored once, even if the triggering code runs multiple times. The FULL SCORE command lists all achievements and their point values.

### Ending the game

Use `finishGameMsg()` to end the game with a standard message:

```tads3
finishGameMsg(ftVictory, [finishOptionUndo, finishOptionRestart]);
```

The first argument is the finish type (`ftVictory`, `ftDeath`, `ftFailure`, `ftGameOver`). The second is a list of options offered to the player.

## Compilation and Testing

### Building your game

The basic compile command is:

```
t3make -d -f mygame.t3m
```

The `-d` flag enables debug mode, which includes the interactive debugger, the DEBUG command, and all `#ifdef __DEBUG` conditional code. For release builds, omit `-d`.

### Testing tools

adv3 includes several built-in commands that only work in debug builds:

- **`>PURLOIN object`** — teleports an object into the player's inventory, bypassing all normal game logic. Invaluable for testing puzzles without solving prerequisites.
- **`>GONEAR object`** — teleports the player to the location of a named object.
- **`>DEBUG`** — enters the interactive debugger (if running under a debugger-aware interpreter).
- **`>EVAL expression`** — evaluates a TADS 3 expression at runtime and displays the result.

### Automated testing with scripts

The `>SCRIPT` command begins recording the player's input to a file. `>SCRIPT OFF` stops recording. `>REPLAY` plays back a recorded script. This lets you create regression tests — record a sequence of commands that exercises a puzzle, then replay it after making changes to verify nothing broke.

You can also use conditional compilation to include test-only code:

```tads3
#ifdef __DEBUG
modify me
    afterAction()
    {
        inherited();
        // Debug: show scope info after every action
        "<<libGlobal.totalTurns>> turns. ";
    }
;
#endif
```

### The development loop

The typical workflow is: edit source → compile with `t3make -d` → play the game in an interpreter → find an issue → edit source → recompile. If you are using [TADS Workbench](../tools/workbench/overview.md), you can compile and launch the game from the IDE with integrated source-level debugging.

## Source Organization

A small game can live in a single `.t` file. As it grows past a few hundred lines, splitting becomes worthwhile.

### Suggested layout

```
mygame/
  mygame.t3m        Project file
  main.t             gameMain, versionInfo, startup logic
  map.t              Rooms and connections
  objects.t          Things, containers, puzzles
  npcs.t             Actors, ActorStates, topics
  events.t           Fuses, Daemons, timed logic
```

Each `.t` file must `#include <adv3.h>` and `#include <en_us.h>` at the top. The `.t3m` file lists them:

```
-D LANGUAGE=en_us
-Fy obj -Fo obj
-o mygame.t3
-lib system
-lib adv3/adv3
-source main
-source map
-source objects
-source npcs
-source events
```

### Organization principles

**Group by geography** for rooms and their contents. A file named `forest.t` might contain all the forest rooms and the objects in them. The `+`/`++` nesting syntax naturally clusters objects with their containing rooms.

**Group by system** for cross-cutting concerns. All NPCs in one file, all timed events in another. This makes it easy to find "all the actors" or "all the daemons" when debugging.

**Use `modify` for patches.** If you need to change a library class's behavior, you can `modify` it from any source file. This lets you keep library overrides in a dedicated file (say, `libmods.t`) rather than scattering them through your game code.

For the compiler's perspective on multi-file games, see [Separate Compilation](../tools/separate-compilation.md).

---

*Next: [Design Patterns](design-patterns.md) for the recurring code patterns that experienced adv3 authors rely on, or back to the [Architecture Overview](overview.md) for the big picture.*
