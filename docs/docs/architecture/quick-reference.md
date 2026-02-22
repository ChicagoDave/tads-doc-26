# Quick Reference

A dense, scannable reference for writing adv3 games. For explanations, see the [Architecture Overview](overview.md), [Development Guide](development-guide.md), and [Design Patterns](design-patterns.md).

[Game Skeleton](#game-skeleton) | [Things](#thing-hierarchy) | [Rooms](#rooms-and-travel) | [Actions](#action-handlers) | [Grammar](#grammar-and-custom-verbs) | [Properties](#key-properties) | [Macros](#global-macros) | [Templates](#object-templates) | [Strings](#string-syntax) | [Conversations](#conversations) | [Events](#timed-events) | [Debugging](#debugging)

---

## Game Skeleton

Every adv3 game needs these four objects:

```tads3
#include <adv3.h>
#include <en_us.h>

versionInfo: GameID
    IFID = 'PUT-A-UUID-HERE'
    name = 'Game Title'
    byline = 'by Author'
    version = '1'
;

gameMain: GameMainDef
    initialPlayerChar = me
    showIntro() { "Welcome!\b"; }
;

startRoom: Room 'Start Room'
    "Description of the room. "
;

+ me: Actor
;
```

Build with: `t3make -d -f mygame.t3m`

---

## Thing Hierarchy

### Portability

| Class | Behavior | Use for |
|-------|----------|---------|
| `Thing` | Can be taken and carried | Keys, coins, letters, food |
| `Fixture` | Cannot be taken; responds to other verbs | Fireplace, shelf, window |
| `Decoration` | Cannot be taken; blocks most verbs with "not important" | Wallpaper, carvings, sky |
| `Distant` | Visible but too far to interact with | Mountains, distant ships |
| `Immovable` | Cannot be taken; other verbs work normally | Boulders, heavy statues |
| `Heavy` | Immovable; says it's too heavy | Piano, anvil |

### Containers and Surfaces

| Class | Behavior |
|-------|----------|
| `Container` | Things go inside; LOOK IN shows contents |
| `Surface` | Things rest on top; PUT ON works |
| `OpenableContainer` | Container with open/close; closed hides contents |
| `LockableContainer` | OpenableContainer with lock/unlock |
| `KeyedContainer` | LockableContainer requiring a specific key |
| `RestrictedContainer` | Container that only accepts certain items |
| `ComplexContainer` | Both container and surface (from `extras.t`) |

### Interaction Types

| Class | Behavior |
|-------|----------|
| `Readable` | Adds `readDesc` for READ command |
| `Food` | Can be eaten (EAT command) |
| `Wearable` | Can be worn (WEAR/DOFF commands) |
| `Switch` | Can be turned on/off |
| `Lever` | Can be pushed/pulled |
| `Button` | Can be pushed |
| `Dial` | Can be set to a value |
| `Settable` | Can be set to a value (base class for Dial) |
| `Consultable` | Can be looked up in (LOOK UP X IN Y) |

### Light Sources

| Class | Behavior |
|-------|----------|
| `LightSource` | Emits light always |
| `Flashlight` | LightSource with on/off switching |
| `Candle` | Light source that can be lit/extinguished, burns down |
| `FueledLightSource` | Light source with limited fuel |
| `Matchstick` | Single-use light source |

### Nested Rooms

| Class | Behavior |
|-------|----------|
| `Chair` | Can be sat on |
| `Platform` | Can be stood on |
| `Bed` | Can be lain on |
| `Vehicle` | Mobile nested room |
| `Booth` | Enclosed nested room |

### Mix-ins (put before base class)

| Mix-in | Adds |
|--------|------|
| `Openable` | Open/close without containment |
| `Lockable` | Lock/unlock |
| `LockableWithKey` | Key-based locking; set `keyList` |
| `Hidden` | Not visible until revealed via `discover()` |
| `MultiLoc` | Present in multiple rooms; set `locationList` |
| `Collectible` | Can be grouped in listings |

Example: `+ chest: LockableWithKey, OpenableContainer 'chest' 'chest'`

See: [Things hub](../library/things/index.md) | [Thing introduction](../library/guide/thing-introduction.md)

---

## Rooms and Travel

### Room Types

| Class | Behavior |
|-------|----------|
| `Room` | Standard lit room |
| `DarkRoom` | No light; needs light source to see |
| `OutdoorRoom` | Sky instead of ceiling, ground instead of floor |
| `FloorlessRoom` | Dropped items fall to room below |

### Direction Properties

Set on rooms: `north`, `south`, `east`, `west`, `northeast`, `northwest`, `southeast`, `southwest`, `up`, `down`, `in`, `out`.

```tads3
kitchen: Room 'Kitchen'
    "A warm kitchen. "
    north = livingRoom
    east = kitchenDoor
;
```

### Travel Connectors

| Class | Behavior |
|-------|----------|
| `Door` | Physical passage; links two sides with `otherSide` |
| `ThroughPassage` | One-way passage object |
| `StairwayUp`/`StairwayDown` | Staircase connecting rooms |
| `FakeConnector` | Displays refusal message instead of travel |
| `DeadEndConnector` | Brief visit, then auto-return |
| `OneWayRoomConnector` | Connects rooms without a visible object |

### Door Pattern

```tads3
+ kitchenDoor: LockableWithKey, Door 'oak door' 'door'
    otherSide = hallDoor
    keyList = [brassKey]
    isLocked = true
;
```

### Regions

```tads3
forestRegion: Region;

clearing: Room 'Clearing'
    "Trees everywhere. "
    regions = [forestRegion]
;
```

Test with: `me.isIn(forestRegion)`

See: [Rooms hub](../library/rooms-and-travel/index.md) | [Room overview](../library/guide/roomoverview.md)

---

## Action Handlers

### The Four Phases

```tads3
dobjFor(Verb)
{
    verify()  { /* can this object do this? (ranking) */ }
    check()   { /* should it happen now? (blocking) */ }
    action()  { /* do it */ }
    report()  { /* default success message */ }
}
```

- **verify** — ranks objects for disambiguation; never changes state
- **check** — enforces preconditions; call `failCheck(msg)` to block
- **action** — performs the effect; call `inherited()` for default behavior
- **report** — optional; the library provides default reports for most actions

### Verify Macros

| Macro | Meaning |
|-------|---------|
| `illogical(msg)` | This action makes no sense for this object |
| `illogicalAlready(msg)` | Already in the desired state (door already open) |
| `illogicalNow(msg)` | Not logical right now, but might be later |
| `illogicalSelf(msg)` | Can't do this to yourself |
| `logicalRank(n, key)` | Set ranking (lower = less likely); default is 100 |
| `dangerous` | Warn the player; parser prefers safer alternatives |
| `inaccessible(msg)` | Object is not accessible |
| `nonObvious` | Don't use as a default for disambiguation |

### Report Functions (in action phase)

| Function | Use |
|----------|-----|
| `defaultReport(msg)` | Terse confirmation; suppressed by other reports |
| `mainReport(msg)` | Primary result message |
| `reportAfter(msg)` | Additional message after the main report |
| `reportFailure(msg)` | Report failure; marks action unsuccessful |

### Redirecting Actions

```tads3
dobjFor(Read) asDobjFor(Examine)     // treat READ as EXAMINE
dobjFor(Enter) remapTo(TravelVia, self) // redirect to travel
```

### Preconditions

```tads3
dobjFor(Eat) { preCond = [objHeld] }  // must be held first
```

Common preconditions: `objHeld`, `objVisible`, `objAudible`, `objOpen`, `touchObj`, `actorInStagingLocation`

### Common Actions

| Action | Direct Object | Indirect Object |
|--------|--------------|----------------|
| `Take` | thing to take | — |
| `Drop` | thing to drop | — |
| `Examine` | thing to look at | — |
| `Read` | thing to read | — |
| `Open` | thing to open | — |
| `Close` | thing to close | — |
| `Lock` | thing to lock | — |
| `Unlock` | thing to unlock | — |
| `LockWith` | thing to lock | key |
| `UnlockWith` | thing to unlock | key |
| `PutIn` | thing to put | container |
| `PutOn` | thing to put | surface |
| `TakeFrom` | thing to take | container |
| `GiveTo` | thing to give | recipient |
| `ShowTo` | thing to show | recipient |
| `ThrowAt` | thing to throw | target |
| `AttackWith` | target | weapon |
| `TurnOn` | thing | — |
| `TurnOff` | thing | — |
| `Eat` | food | — |
| `Wear` | clothing | — |
| `Doff` | clothing | — |
| `LookIn` | container | — |
| `Search` | thing | — |
| `Push` | thing | — |
| `Pull` | thing | — |
| `SitOn` | surface | — |
| `StandOn` | surface | — |
| `LieOn` | surface | — |

See: [Design Patterns: dobjFor/iobjFor](design-patterns.md#the-dobjforiobjfor-property-set-system) | [Action Results](../library/actions/action-results.md) | [Creating New Verbs](../library/actions/creating-verbs.md)

---

## Grammar and Custom Verbs

### Defining New Actions

| Macro | Slots | Example |
|-------|-------|---------|
| `DefineIAction(Name)` | none | SLEEP, JUMP |
| `DefineTAction(Name)` | dobj | REPAIR X |
| `DefineTIAction(Name)` | dobj + iobj | SCRAPE X WITH Y |
| `DefineLiteralAction(Name)` | literal text | SAY HELLO |
| `DefineTopicAction(Name)` | topic | THINK ABOUT X |
| `DefineLiteralTAction(Name, Role)` | literal + obj | WRITE X ON Y |
| `DefineTopicTAction(Name, Role)` | topic + obj | ASK X ABOUT Y |

### VerbRule Syntax

```tads3
VerbRule(Repair)
    ('repair' | 'fix') singleDobj
    : RepairAction
    verbPhrase = 'repair/repairing (what)'
;
```

### Slot Keywords

| Keyword | Meaning |
|---------|---------|
| `singleDobj` | Single direct object |
| `dobjList` | Multiple direct objects (TAKE A AND B) |
| `singleIobj` | Single indirect object |
| `singleLiteral` | Literal text (SAY "HELLO") |
| `singleTopic` | Topic reference (ASK ABOUT X) |

In two-object verbs, at most one slot can be a list keyword.

### verbPhrase Format

| Action Type | Pattern |
|-------------|---------|
| Intransitive | `'sleep/sleeping'` |
| One object | `'repair/repairing (what)'` |
| Two objects | `'scrape/scraping (what) (with what)'` |
| Person target | `'talk/talking (to whom)'` |

### Complete Example

```tads3
DefineTAction(Repair);

VerbRule(Repair)
    ('repair' | 'fix') singleDobj
    : RepairAction
    verbPhrase = 'repair/repairing (what)'
;
```

Then handle it on objects:

```tads3
modify Thing
    dobjFor(Repair) {
        verify() { illogical('{That dobj/he} can\'t be repaired. '); }
    }
;
```

### Modifying Existing Grammar

```tads3
modify grammar predicate(Quit): 'quit' | 'q' : QuitAction;   // extend
replace grammar predicate(Quit): 'quit' | 'q' : QuitAction;  // replace
```

See: [Creating New Verbs](../library/actions/creating-verbs.md) | [GrammarProd](../intrinsics/classes/gramprod.md)

---

## Key Properties

### Thing Properties

| Property | Type | Purpose |
|----------|------|---------|
| `vocabWords` | sstring | Parser vocabulary (first template slot) |
| `name` | sstring | Display name (second template slot) |
| `desc` | dstring/method | EXAMINE description |
| `specialDesc` | dstring/method | Standalone paragraph in room listing |
| `initSpecialDesc` | dstring/method | `specialDesc` until first taken |
| `initDesc` | dstring/method | `desc` until first moved |
| `readDesc` | dstring/method | READ description (Readable) |
| `location` | object | Where this object is |
| `bulk` | int | How much space it takes up (default 1) |
| `weight` | int | How heavy it is (default 1) |
| `bulkCapacity` | int | How much it can hold (containers) |
| `isListed` | bool | Show in room contents listing? |
| `isKnown` | bool | Player has encountered this object? |
| `isProperName` | bool | Use name without articles? |
| `isHim`/`isHer` | bool | Pronoun gender |
| `isPlural` | bool | Plural noun? |

### Room Properties

| Property | Type | Purpose |
|----------|------|---------|
| `roomName` | sstring | Status-line name (template slot) |
| `desc` | dstring/method | LOOK description |
| `darkName` | sstring | Name when dark |
| `darkDesc` | dstring/method | Description when dark |
| `brightness` | int | Light level (0=dark, default 3) |
| `regions` | list | Regions this room belongs to |
| `north`, `south`, etc. | obj/method | Travel destinations |
| `roomBeforeAction()` | method | Called before every action in this room |
| `roomAfterAction()` | method | Called after every action in this room |
| `travelerArriving()` | method | Called when someone enters |
| `travelerLeaving()` | method | Called when someone leaves |

### Actor Properties

| Property | Type | Purpose |
|----------|------|---------|
| `isHim`/`isHer` | bool | Gender |
| `isProperName` | bool | Use name without articles |
| `curState` | ActorState | Current state object |
| `pcReferralPerson` | enum | 1st/2nd/3rd person narration |
| `globalParamName` | sstring | Name for message substitutions |
| `contentsListed` | bool | List inventory in room desc? |

See: [Overview: Key Properties](overview.md) | [Tour Guide](../library/guide/thing-introduction.md)

---

## Object Templates

Templates let you write object definitions in a compact shorthand. The template defines which positional values map to which properties.

### Thing Template

```tads3
+ key: Thing 'small brass key' 'brass key'
    "A small, tarnished brass key. "
;
```

Slots: `'vocabWords'` `'name'` then `"desc"`.

### Room Template

```tads3
startRoom: Room 'Room Name'
    "Room description. "
;
```

Slot: `'roomName'` then `"desc"`.

### TopicEntry Template

```tads3
++ AskTopic @brassKey
    "The guard says, <q>It opens the box.</q> "
;
```

Slot: `@matchObj` then `"topicResponse"`.

### Passage Template

```tads3
+ hallDoor: Door ->otherRoom 'door' 'door'
    "A heavy oak door. "
;
```

Slot: `->masterObject` then `'vocabWords'` `'name'` then `"desc"`.

!!! tip "Template Syntax"
    Single-quoted strings are properties set at compile time (`name`, `vocabWords`). Double-quoted strings are methods (the compiler turns them into `desc() { "..."; }`). The `@` prefix means "match this object," and `->` means "point to this object."

---

## String Syntax

### Single vs Double Quotes

- **Single-quoted** `'hello'` — a string value (an object of class String); used for properties, comparisons, concatenation
- **Double-quoted** `"hello"` — sends text to the output stream; used for descriptions and messages

### Escape Sequences

| Sequence | Output |
|----------|--------|
| `\n` | Line break |
| `\b` | Blank line (paragraph break) |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\'` | Literal single quote |
| `\"` | Literal double quote |
| `<.p>` | Paragraph break (same as `\b`) |
| `<.br>` | Line break (same as `\n`) |

### Embedded Expressions

In double-quoted strings, `<<expression>>` evaluates and prints the expression:

```tads3
"The dial reads <<dialSetting>>. "
"You have <<coins.length()>> coins. "
"<<one of>>alpha<<or>>beta<<or>>gamma<<shuffled>>"
```

### Conditional Text

```tads3
"The door is <<if isOpen>>open<<else>>closed<<end>>. "
"You see <<if count == 1>>one item<<else>><<count>> items<<end>>. "
```

### Library Message Tags

| Tag | Purpose |
|-----|---------|
| `<q>...</q>` | Quoted speech (auto-selects single/double quotes) |
| `<.p>` | Paragraph break |
| `<.br>` | Line break |
| `<.reveal key>` | Mark a fact as revealed (for conversation tracking) |
| `<.inform key>` | Mark a fact as informed (NPC knowledge) |
| `<.convnode name>` | Enter a conversation node |
| `<.topics>` | Show available conversation topics |

See: [String Literals](../language/strlit.md) | [Output Formatting](development-guide.md#output-formatting)

---

## Conversations

### TopicEntry Types

| Class | Responds to | Player command |
|-------|------------|----------------|
| `AskTopic` | ASK ABOUT | `>ask guard about key` |
| `TellTopic` | TELL ABOUT | `>tell guard about ghost` |
| `AskTellTopic` | ASK or TELL | Either command |
| `GiveTopic` | GIVE TO | `>give key to guard` |
| `ShowTopic` | SHOW TO | `>show map to guard` |
| `AskForTopic` | ASK FOR | `>ask guard for key` |
| `YesTopic` | YES | `>yes` |
| `NoTopic` | NO | `>no` |
| `CommandTopic` | orders | `>guard, go north` |
| `InitiateTopic` | NPC-initiated | via `initiateTopic()` |
| `SpecialTopic` | custom vocab | `>offer truce` |

### Default Topics

Each type has a Default variant: `DefaultAskTopic`, `DefaultTellTopic`, `DefaultAskTellTopic`, `DefaultGiveTopic`, `DefaultShowTopic`, `DefaultAnyTopic`.

### Actor State Pattern

```tads3
+ guard: Person 'guard' 'guard'
    isHim = true
;

++ guardReady: ConversationReadyState
    isInitState = true
    specialDesc = "A guard stands here. "
;

+++ guardTalking: InConversationState
    specialDesc = "The guard is talking to you. "
;

++++ AskTopic @brassKey
    "<q>It opens the cellar box,</q> he says. "
;

++++ DefaultAskTopic
    "He shrugs. "
;
```

### Agenda Items

| Class | Behavior |
|-------|----------|
| `AgendaItem` | Fires when `isReady` is true |
| `ConvAgendaItem` | Fires during an active conversation |
| `DelayedAgendaItem` | Fires after a specified turn count |

```tads3
++ guardWarning: ConvAgendaItem
    isReady = (guard.curState == guardTalking)
    invokeItem()
    {
        "<q>By the way, watch out for the cellar,</q> the guard says. ";
        isDone = true;
    }
;
```

Add to agenda: `guard.addToAgenda(guardWarning)`

See: [Conversations hub](../library/actors/index.md) | [Programming Conversations](../library/actors/programming-conversations.md)

---

## Timed Events

### Creating Events

```tads3
new Fuse(obj, &method, turns)       // fires once after N turns
new Daemon(obj, &method, interval)   // fires every N turns
new SenseFuse(obj, &method, turns, source) // fires if player can sense source
new PromptDaemon(obj, &method)       // fires every turn at command prompt
```

### Cleanup Pattern

```tads3
myObj: Thing 'thing' 'thing'
    myFuse = nil
    activate()
    {
        myFuse = new Fuse(self, &fire, 5);
    }
    fire()
    {
        "It fires! ";
        myFuse = nil;
    }
    cancelEvent()
    {
        if (myFuse) { myFuse.removeEvent(); myFuse = nil; }
    }
;
```

!!! tip "Always clean up"
    Store the event in a property. Call `removeEvent()` and nil the property when done or when cancelling early. An orphaned Daemon will fire forever.

See: [Fuse](../library/guide/fuse.md) | [Daemon](../library/guide/daemon.md) | [Design Patterns: Daemons](design-patterns.md#daemon-and-fuse-patterns)

---

## Global Macros

### Action Context

| Macro | Returns | Available in |
|-------|---------|--------------|
| `gPlayerChar` | Player character Actor | Anywhere |
| `gActor` | Actor performing current action | Action handlers |
| `gAction` | Current Action object | Action handlers |
| `gDobj` | Direct object (Thing) | `dobjFor` handlers |
| `gIobj` | Indirect object (Thing) | `iobjFor` handlers |
| `gTopic` | ResolvedTopic object | TopicAction handlers |
| `gTopicText` | Topic text (lowercase string) | TopicAction handlers |
| `gLiteral` | Literal text string | LiteralAction handlers |
| `gTranscript` | CommandTranscript object | Anywhere |

### Testing Actions

| Macro | Returns |
|-------|---------|
| `gActionIs(Action)` | `true` if current action matches the type |
| `gActionIn([A, B, ...])` | `true` if current action is any in the list |

### Knowledge Tracking

| Macro | Effect |
|-------|--------|
| `gSetKnown(obj)` | Mark object as known to PC |
| `gReveal(key)` | Mark a string key as revealed |
| `gRevealed(key)` | `true` if key has been revealed |

### Message Parameters

```tads3
gMessageParams(obj, actor);  // register for {obj} {actor} substitutions
```

See: [Design Patterns](design-patterns.md) | [Messages and Substitutions](../library/messages-substitutions.md)

---

## Debugging

### Debug Commands (debug builds only)

| Command | Effect |
|---------|--------|
| `>PURLOIN obj` | Teleport object to player inventory |
| `>GONEAR obj` | Teleport player to object's location |
| `>EVAL expr` | Evaluate TADS 3 expression at runtime |
| `>DEBUG` | Enter interactive debugger |
| `>SCRIPT` | Start recording commands to file |
| `>SCRIPT OFF` | Stop recording |
| `>REPLAY` | Replay a recorded script |

### Build Commands

```
t3make -d -f mygame.t3m      # debug build
t3make -f mygame.t3m          # release build
```

### Common Compiler Errors

| Error | Likely Cause |
|-------|-------------|
| `unknown symbol 'X'` | Typo in class/property name, or missing `#include` |
| `semicolon expected` | Missing `;` at end of object definition |
| `property value required` | Missing `=` in property definition |
| `undefined symbol 'inherited'` | Using `inherited()` in a base object, not a `modify` or subclass |
| `object definition expected` | Extra `}` or mismatched braces |

### Conditional Compilation

```tads3
#ifdef __DEBUG
    // only included in debug builds
#endif
```

See: [Compilation and Testing](development-guide.md#compilation-and-testing) | [Build Configurations](../tools/build-configurations.md)

---

## Modify and Replace

### modify — change an existing class

```tads3
modify Thing
    dobjFor(Smell)
    {
        action() { "You smell nothing unusual. "; }
    }
;
```

### replace — completely replace a class definition

```tads3
replace grammar predicate(Quit): 'quit' | 'q' : QuitAction
;
```

### When to use which

- **modify** — extending or overriding methods on a library class; the original class is still the base
- **replace** — completely redefining something; the original definition is erased
- **Subclassing** — when you want both the original and a specialized version

See: [Design Patterns: modify vs. Subclassing](design-patterns.md#modify-vs-subclassing)

---

## Scoring

```tads3
// Simple scoring
addToScore(10, 'finding the key');

// Achievement objects
foundKey: Achievement { points = 10  desc = "finding the brass key" }
foundKey.awardPointsOnce();  // safe to call multiple times

// Ending the game
finishGameMsg(ftVictory, [finishOptionUndo, finishOptionRestart]);
// Types: ftVictory, ftDeath, ftFailure, ftGameOver
```

Set `gameMain.maxScore` for simple scoring. With Achievement objects, `maxScore` is computed automatically.

---

*For conceptual understanding, see the [Architecture Overview](overview.md). For building a game from scratch, see the [IF Development Guide](development-guide.md). For library idioms, see [Design Patterns](design-patterns.md).*
