# The Message System

Every response a TADS 3 game produces — from "Taken." to "You can't put the sword in the teacup." — flows through a three-layer message system. A **definition layer** provides roughly 600 library messages as parameterized strings. A **substitution layer** expands `{...}` parameters into the correct pronouns, verb forms, and object names for the current actor and narrative tense. A **dispatch layer** determines which message to use by checking the objects involved in the command before falling back to a default. This document explains all three layers and the places where game authors can intervene.

[Overview](#message-system-overview) | [Lifecycle](#the-message-lifecycle) | [Message Objects](#message-definition-objects) | [Substitution Engine](#the-parameter-substitution-engine) | [English Layer](#the-english-language-layer) | [Dispatch](#message-dispatch-and-override-resolution) | [Reports](#the-report-and-transcript-system) | [Customization](#author-customization-patterns) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to other architecture docs"
    The [Architecture Overview](overview.md) lists `output.t`, `report.t`, and `msg_neu.t` in its module map. The [Action Resolution](action-resolution.md#the-execution-cycle-doactiononce) document explains the verify/check/action pipeline that *produces* messages — this document explains what happens to those messages after they're generated. The library guide covers practical usage: [Where Messages Come From](../library/messages.md), [Parameter Substitutions](../library/messages-substitutions.md), [Past Tense](../library/advanced/past-tense.md), and [Banishing Messages](../library/advanced/banishing-messages.md). This document explains the internal machinery — the class hierarchies, algorithms, and design decisions that make the message system work.

---

## Message System Overview

The message system is organized in three layers:

```
Layer 1: Message Definition                What to say (msg_neu.t, en_us.t)
     │   MessageHelper, libMessages,
     │   playerActionMessages, npcActionMessages
     │   ~600 message properties as parameterized strings
     │
     ▼
Layer 2: Parameter Substitution            How to say it (output.t, en_us.t)
     │   MessageBuilder, langMessageBuilder,
     │   {You/he} {can't} take {the dobj/him},
     │   pronouns, verbs, articles, tense
     │
     ▼
Layer 3: Dispatch and Reporting            When and whether to show it (exec.t, report.t)
         resolveMessageText(), CommandTranscript,
         defaultReport, mainReport, reportFailure,
         deferred display, suppression rules
```

### Source files and responsibilities

| Source | Role |
|--------|------|
| `en_us/msg_neu.t` | `libMessages`, `playerActionMessages`, `npcActionMessages` — all library message strings in English (neutral voice) |
| `output.t` | `MessageBuilder` base class — the generic `{...}` parameter substitution engine, output stream management |
| `en_us/en_us.t` | `MessageHelper` base class, `langMessageBuilder` — English-specific parameter table, pronoun/verb/tense logic |
| `report.t` | `CommandReport` class hierarchy, `CommandTranscript` — deferred report collection and display |
| `exec.t` | `resolveMessageText()` — the override resolution algorithm that checks objects before falling back to the default message object |
| `action.t` | `getMessageParam()`, `setMessageParam()`, `synthMessageParam()` — parameter binding on the current action |
| `adv3.h` | Report macros (`defaultReport`, `mainReport`, `reportFailure`, etc.), `gMessageParams`, `dobjMsg`/`iobjMsg` |

---

## The Message Lifecycle

Before diving into each layer, here is a complete trace of what happens when a message is produced. Suppose the player types **TAKE THE KEY**, and the key has no custom message override.

```
1. Action handler calls:    defaultReport(&okayTakeMsg)

2. Report macro expands to: gTranscript.addReport(
                                new DefaultCommandReport(&okayTakeMsg, ...))

3. DefaultCommandReport constructor calls resolveMessageText():
   a. sources = [key]  (the direct object)
   b. key.propDefined(&okayTakeMsg)?  → no (not overridden)
   c. Fall back to gActor.getActionMessageObj()
      → returns playerActionMessages (player is acting)
   d. playerActionMessages.okayTakeMsg → 'Taken. '

4. The string 'Taken. ' has no {parameters} → stored as-is in the report

5. After the full action cycle completes, the CommandTranscript
   assembles all reports and displays them to the player:
   → "Taken."
```

Now suppose an NPC named Bob is performing the action instead. Step 3c returns `npcActionMessages`, and step 3d evaluates `npcActionMessages.okayTakeMsg`, which returns `'{You/he} {take[s]|took} {the dobj/him}. '`. This string *does* contain parameters, so the substitution engine processes it:

```
5. langMessageBuilder.generateMessage('{You/he} {take[s]|took} {the dobj/him}. ')
   a. Tense preprocessing: present tense selected
      → '{You/he} take{s} {the dobj/him}. '
   b. {You/he}       → actor is Bob → 'Bob'          (theName on Bob)
   c. {s}            → Bob is singular → 's'          (verbEndingS)
   d. {the dobj/him} → dobj is key → 'the brass key'  (theNameObj on key)
   → "Bob takes the brass key."
```

---

## Message Definition Objects

### Class hierarchy

```
MessageHelper                          Base class (en_us.t)
 ├── libMessages                       Parser and general library messages
 │     └── playerMessages              Parser messages for the player character
 └── playerActionMessages              Action responses for the player character
       └── npcActionMessages           Action responses overridden for NPCs
```

**MessageHelper** (en_us.t) is the base class for all message collections. It provides helper methods like `shortTMsg()` and `shortTIMsg()` for selecting short or long message forms depending on whether disambiguation is needed.

**libMessages** (msg_neu.t) contains messages for the parser and general library situations — disambiguation prompts, error messages, OOPS responses, score notifications, and other non-action messages. Its design philosophy is the "neutral narrator": the parser refers to itself in the third person ("this story") or avoids self-reference entirely, minimizing the computer's visible presence as mediator.

**playerActionMessages** (msg_neu.t) contains roughly 600 message properties covering every standard action response: verification failures (`cannotDoThatMsg`, `mustBeHoldingMsg`), action success (`okayTakeMsg`, `okayDropMsg`, `okayOpenMsg`), reach and scope errors (`cannotReachObjectMsg`, `cannotSeeMsg`), sensory reports, clothing, locking, containment capacity, and more.

**npcActionMessages** (msg_neu.t) inherits from `playerActionMessages` and overrides messages that need different phrasing for NPCs. The player's `okayTakeMsg` is simply `'Taken. '` — terse and direct. The NPC version is `'{You/he} {take[s]|took} {the dobj/him}. '` — a full sentence with the actor's name and the object.

### How messages are defined

Messages are either **string properties** or **method properties**:

```tads3
/* String property — a fixed parameterized string */
cannotDoThatMsg = '{You/he} {can\'t} do that. '

/* Method property — computes the string dynamically */
mustBeHoldingMsg(obj)
{
    gMessageParams(obj);
    return '{You/he} {must} be holding {the obj/him} to do that. ';
}
```

Method properties use `gMessageParams()` to register additional objects as named parameters before returning the message string. This lets `{the obj/him}` in the string resolve to whatever object was passed as the `obj` argument.

### Actor selection

When the library needs an action message, it calls `gActor.getActionMessageObj()`. This method returns `playerActionMessages` when the current actor is the player character, and `npcActionMessages` otherwise. Authors can override `getActionMessageObj()` on an Actor subclass to provide a completely custom message set.

---

## The Parameter Substitution Engine

### MessageBuilder (output.t)

`MessageBuilder` is the generic substitution engine. It is both an `OutputFilter` (installed in the output stream) and a `PreinitObject` (builds its lookup tables at compile time). Its core method is `generateMessage()`, which processes a message string and expands every `{...}` parameter into text.

### The paramList_ structure

The English-specific `langMessageBuilder` (en_us.t) extends `MessageBuilder` with a `paramList_` that defines every recognized parameter. Each entry is a five-element list:

```
[paramName, &property, impliedTarget, &reflexiveProperty, isNominative]
```

| Element | Purpose |
|---------|---------|
| `paramName` | The text that appears inside `{...}` — e.g., `'you/he'`, `'the/him'`, `'s/d'` |
| `&property` | The property to invoke on the target object — e.g., `&theName`, `&verbEndingSD` |
| `impliedTarget` | Default target if none specified in the tag — e.g., `'actor'` for `{You/he}` |
| `&reflexiveProperty` | Property for reflexive form — e.g., `&itReflexive` for `{you/him}` |
| `isNominative` | `true` if this is a nominative (subject) usage, used for reflexive tracking |

At pre-initialization, `paramList_` is compiled into `paramTable_`, a `LookupTable` for fast name-to-info lookup.

### The generateMessage() algorithm

```
┌─ For each character in the string ─────────────────────────────┐
│                                                                 │
│  Find next '{'                                                  │
│  ├── None found → append rest of string, done                   │
│  └── Found                                                      │
│       ├── '{{' stuttered brace → append literal '{', continue   │
│       └── Extract content to closing '}'                        │
│            │                                                    │
│            ├── Note capitalization ({the} vs {The} vs {THE})    │
│            ├── Lowercase the parameter string                   │
│            ├── Call langRewriteParam() for language rewrites     │
│            │                                                    │
│            ├── Parse format:                                    │
│            │   'id obj/id2'  → paramName = id+id2, paramObj     │
│            │   'id obj'      → paramName = id, paramObj         │
│            │   'id1/id2'     → paramName = id1/id2              │
│            │   'id'          → paramName = id                   │
│            │                                                    │
│            ├── Look up paramName in paramTable_                 │
│            │   ├── Not found? Try reversed slash order          │
│            │   └── Still not found? Try as string parameter     │
│            │       via gAction.getMessageParam(paramName)       │
│            │                                                    │
│            ├── Resolve target object:                           │
│            │   1. Explicit in tag: gAction.getMessageParam(obj) │
│            │   2. Implied from paramList_[3]: e.g., 'actor'     │
│            │   3. Global nameTable_ lookup                      │
│            │   4. Same as previous parameter (lastTargetObj_)   │
│            │                                                    │
│            ├── Get property: getTargetProp() checks reflexive   │
│            ├── Invoke: targetObj.(prop)                         │
│            ├── Apply capitalization                              │
│            └── Append result, continue                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Target object resolution

When a parameter includes an object name — like `dobj` in `{the dobj/him}` — the engine resolves it through a chain of lookups:

1. **Action parameters**: `gAction.getMessageParam('dobj')` — the Action class maps `'dobj'` to the direct object, `'iobj'` to the indirect object, `'actor'` to the current actor, and `'pc'` to the player character. Custom parameters set via `setMessageParam()` are also found here.

2. **Global name table**: `nameTable_` on the MessageBuilder, populated at pre-init.

3. **Previous target**: if no object name is specified, the engine reuses `lastTargetObj_` from the previous parameter expansion. This is how consecutive parameters like `{the dobj/him} {is}` both refer to the same object — the `{is}` has no explicit target and inherits from `{the dobj/him}`.

### Capitalization

The engine checks the first two characters of the parameter text:

| Pattern | Example | Effect |
|---------|---------|--------|
| Both lowercase | `{the dobj}` | No change — "the brass key" |
| First uppercase | `{The dobj}` | Capitalize first letter — "The brass key" |
| Both uppercase | `{THE dobj}` | All caps — "THE BRASS KEY" |

---

## The English Language Layer

The `langMessageBuilder` subclass adds English-specific processing: pronouns and articles, verb conjugation, reflexive pronoun tracking, and tense switching.

### Pronouns and articles

| Category | Parameters | Property | Example output |
|----------|-----------|----------|----------------|
| Actor nominative | `{You/he}`, `{You/she}` | `&theName` | "You" or "Bob" |
| Actor objective | `{You/him}`, `{You/her}` | `&theNameObj` | "you" or "Bob" (+ reflexive) |
| Actor possessive adj | `{Your/his}`, `{Your/her}` | `&theNamePossAdj` | "your" or "Bob's" |
| Actor possessive noun | `{Yours/his}`, `{Yours/hers}` | `&theNamePossNoun` | "yours" or "Bob's" |
| Actor reflexive | `{Yourself/himself}` | `&itReflexive` | "yourself" or "himself" |
| Definite nominative | `{The/he}`, `{The/she}` | `&theName` | "the brass key" or "he" |
| Definite objective | `{The/him}`, `{The/her}` | `&theNameObj` | "the brass key" (+ reflexive) |
| Indefinite | `{A/he}`, `{An/she}` | `&aName` | "a brass key" or "he" |
| Pronoun nominative | `{It/he}`, `{It/she}` | `&itNom` | "it" or "he" |
| Pronoun objective | `{It/him}`, `{It/her}` | `&itObj` | "it" or "him" (+ reflexive) |
| Demonstrative | `{That/he}`, `{That/him}` | `&thatNom`/`&thatObj` | "that" or "he"/"him" |
| Contraction | `{It's/he's}`, `{You're/he's}` | `&itIsContraction` | "it's" or "he's" |
| Possessive pronoun | `{Its/her}`, `{Its/hers}` | `&itPossAdj`/`&itPossNoun` | "its" or "her"/"hers" |

The slash notation encodes two alternatives: the first form is used when the target is the player character (second person), the second when the target is a third-person NPC. The actual text comes from invoking the `&property` on the target object — `theName` on a Thing returns its name with article, while `theName` on the player character returns "you."

### Verb conjugation

| Parameter | Property | Present (singular) | Present (plural) | Past |
|-----------|----------|-------------------|-------------------|------|
| `{s}` | `&verbEndingS` | "s" | "" | — |
| `{s/d}` | `&verbEndingSD` | "s" | "" | "d" |
| `{s/ed}` | `&verbEndingSEd` | "s" | "" | "ed" |
| `{s/?ed}` | `&verbEndingSMessageBuilder_` | "s" | "" | custom ending |
| `{es}` / `{es/ed}` | `&verbEndingEs` | "es" | "" | "ed" |
| `{ies}` / `{ies/ied}` | `&verbEndingIes` | "ies" | "y" | "ied" |
| `{is}` / `{are}` | `&verbToBe` | "is" | "are" | "was"/"were" |
| `{has}` / `{have}` | `&verbToHave` | "has" | "have" | "had" |
| `{does}` / `{do}` | `&verbToDo` | "does" | "do" | "did" |
| `{can}` | `&verbCan` | "can" | "can" | "could" |
| `{cannot}` / `{can't}` | `&verbCannot`/`&verbCant` | "cannot"/"can't" | — | "could not"/"couldn't" |
| `{must}` | `&verbMust` | "must" | "must" | "had to" |
| `{will}` / `{won't}` | `&verbWill`/`&verbWont` | "will"/"won't" | — | "would"/"wouldn't" |

Specialized verbs: `{goes}`, `{comes}`, `{leaves}`, `{sees}`, `{says}` — each maps to a dedicated property that handles irregular conjugation.

Verb parameters have `isNominative = true`, which means they track the same subject as the preceding pronoun parameter. This is how `{You/he} {take[s]|took}` knows whether to use "takes" (singular NPC) or "take" (plural or player).

### Spatial prepositions

| Parameter | Property | Example output |
|-----------|----------|----------------|
| `{on}` / `{in}` | `&actorInName` | "on" or "in" (context-dependent) |
| `{onto}` / `{into}` | `&actorIntoName` | "onto" or "into" |
| `{outof}` / `{offof}` | `&actorOutOfName` | "out of" or "off of" |

These resolve based on the target object's posture semantics — a chair produces "on," a box produces "in."

### Reflexive pronoun tracking

The English message builder maintains two state variables:

- **`lastSubject_`** — the most recent object used in a nominative parameter
- **`lastSubjectName_`** — the parameter name that set it

When a later parameter targets the *same object* but with a different parameter name, and that parameter has a reflexive property (element [4] in paramList_), the reflexive form is used instead:

```
"{You/he} {can't} open {you/him}."
     ↑ sets lastSubject_ = actor       ↑ same target as subject → reflexive
→ "You can't open yourself."    (not "You can't open you.")
```

Reflexive state resets on sentence-ending punctuation (`.`, `!`, `?`, `;`, `:`), detected by the `processResult()` method. This prevents reflexive bleeding across sentences.

### Tense switching

TADS 3 supports both present and past tense narration, controlled by `gameMain.usePastTense`.

The `{present|past}` syntax allows a single message string to work in either tense. The `langMessageBuilder.processOrig()` method preprocesses the string *before* normal parameter substitution:

```
Source:    "{You/he} {take[s]|took} {the dobj/him}."
                     ^^^^^^^^^^^
                     tense switch

Present tense selected:
  → "{You/he} take{s} {the dobj/him}."     (square brackets → braces)

Past tense selected:
  → "{You/he} took {the dobj/him}."         (no further substitution needed)
```

The key insight: square brackets `[s]` inside the present-tense branch are converted to braces `{s}`, making them regular substitution parameters. This enables two-level processing — tense selection first, then verb agreement.

Additional tense tools:

| Tool | Usage |
|------|-------|
| `tSel(present, past)` | Function that returns the appropriate form for the current tense |
| `{parameter!}` | The `!` suffix forces present-tense evaluation regardless of narrative tense |
| `withPresent(func)` | Execute a function with present tense temporarily active |
| `withPast(func)` | Execute a function with past tense temporarily active |

### The invisible {subj} marker

Most English sentences follow subject-verb-object order, so the message builder naturally sees the subject first and can track it for reflexive pronouns. For sentences with unusual word order, the `{subj}` parameter marks the subject explicitly. It produces no visible output — it only sets `lastSubject_` for reflexive tracking:

```tads3
"From {the dobj/him}, {subj actor} {you/he} hear{s/d} a faint hum. "
```

---

## Message Dispatch and Override Resolution

When a report macro like `defaultReport(&okayTakeMsg)` fires, it creates a `CommandReport` object. The report's constructor calls `resolveMessageText()`, which determines where to get the actual message string.

### The override resolution algorithm

```
resolveMessageText(sources, &msgProp, params)
│
├── sources = [dobj, iobj, ...]  (objects involved in the action)
│   Reorder so the calling object is first (via stack trace inspection)
│
├── For each source object:
│   ├── Does it define &msgProp?
│   │   ├── TypeSString  → use this string directly, done
│   │   ├── TypeProp     → redirect to that property on the default msg object
│   │   ├── TypeCode     → call the method
│   │   │   ├── Returns string → use it, done
│   │   │   ├── Returns property → redirect to that property
│   │   │   └── Returns nil → skip this object, continue searching
│   │   ├── TypeNil      → skip this object, continue searching
│   │   └── Other        → use this object as the message source
│   └── Not defined → continue to next source
│
└── No override found:
    msgObj = gActor.getActionMessageObj()
    → playerActionMessages or npcActionMessages
    msg = msgObj.(&msgProp)(params...)
    → expanded through langMessageBuilder.generateMessage()
```

The stack trace inspection in step 1 is important: for a `TIAction` like PUT KEY IN BOX, both the key (dobj) and the box (iobj) are potential override sources. The algorithm prioritizes whichever object's handler actually generated the report — if the box's `iobjFor(PutIn)` handler called `reportFailure(&notAContainerMsg)`, the box is checked first.

### Role-selective overrides

Sometimes an object should only override a message when it plays a specific role. The `dobjMsg()` and `iobjMsg()` macros handle this:

```tads3
/* Only override when this object is the indirect object */
notAContainerMsg = iobjMsg('The vase\'s opening is too small. ')

/* Only override when this object is the direct object */
cannotTakeMsg = dobjMsg('The sword is embedded in the stone. ')
```

These macros evaluate to the message string when the object is in the specified role, and `nil` otherwise. Since `resolveMessageText()` skips `nil` results from code properties, the override is silently ignored when the object is in the wrong role.

### Custom named parameters

Authors can register additional objects as named parameters for use in message strings:

```tads3
/* Register a single parameter */
gAction.setMessageParam('container', redBox);

/* Register via the convenience macro (name = variable name) */
gMessageParams(container, key);
// equivalent to: gAction.setMessageParams('container', container, 'key', key)

/* Generate a synthetic unique name for an object */
local nm = gSynthMessageParam(someObj);
// returns 'synth1', 'synth2', etc., with the object registered under that name
```

These parameters are then available in message strings as `{the container/him}`, `{the key/him}`, etc.

---

## The Report and Transcript System

Messages are not displayed immediately. They are collected in a `CommandTranscript` and shown after the full action cycle completes. This deferred display enables suppression rules and multi-object grouping.

### CommandReport class hierarchy

```
CommandReport                              Base class
 ├── GroupSeparatorMessage                 Between action groups
 ├── InternalSeparatorMessage              Between implied/main action
 ├── MarkerReport                          Silent markers
 │    ├── EndOfDescReport                  End of description block
 │    └── FailCommandMarker                Silent failure flag
 ├── CommandReportMessage                  Reports with text (= CommandReport + MessageResult)
 │    ├── DefaultCommandReport             Suppressible confirmation ("Taken.")
 │    ├── DefaultDescCommandReport         Suppressible description ("Nothing special.")
 │    ├── ExtraCommandReport               Incidental (doesn't suppress defaults)
 │    ├── CosmeticSpacingCommandReport     Paragraph breaks (doesn't suppress defaults)
 │    └── FullCommandReport                Always-shown reports
 │         ├── BeforeCommandReport         Before main report (seqNum = 1)
 │         ├── MainCommandReport           Main narrative report (seqNum = 2)
 │         ├── FailCommandReport           Failure report (seqNum = 2, isFailure = true)
 │         └── AfterCommandReport          After main report (seqNum = 3)
 └── CommandAnnouncement                   Object announcements ("(the red book)")
      ├── AmbigObjectAnnouncement
      ├── DefaultObjectAnnouncement
      ├── MultiObjectAnnouncement
      ├── RemappedActionAnnouncement
      └── ImplicitActionAnnouncement
```

### Report macros

| Macro | Report class | Behavior |
|-------|-------------|----------|
| `defaultReport(msg)` | `DefaultCommandReport` | Shown unless a full report exists for the same action, or the action is implicit |
| `defaultDescReport(msg)` | `DefaultDescCommandReport` | Shown unless any other report exists for the same action (but *not* suppressed just because the action is implicit) |
| `mainReport(msg)` | `MainCommandReport` | Always shown; suppresses default reports |
| `reportBefore(msg)` | `BeforeCommandReport` | Shown before main report; suppresses default reports |
| `reportAfter(msg)` | `AfterCommandReport` | Shown after main report; suppresses default reports |
| `reportFailure(msg)` | `FailCommandReport` | Marks command as failed; suppresses default reports; itself suppressed for implicit NPC commands |
| `extraReport(msg)` | `ExtraCommandReport` | Always shown; does *not* suppress default reports |
| `cosmeticSpacingReport(msg)` | `CosmeticSpacingCommandReport` | Paragraph break; does *not* suppress default reports |

### Suppression rules

The two key suppression rules:

1. **Default reports are suppressed by full reports.** If any `FullCommandReport` (main, before, after, or failure) exists for the same action, all `DefaultCommandReport` messages for that action are hidden. This is how the library handles the common pattern: the default "Taken." is shown for simple takes, but if the action handler writes a custom `mainReport()`, the default is suppressed.

2. **Default reports are suppressed for implicit actions.** When a command triggers an implicit action (like implicitly taking an object before examining it), the terse "Taken." confirmation is suppressed — the player didn't ask to take it, so the confirmation adds noise. `DefaultDescCommandReport` is the exception: it is *not* suppressed for implicit actions, only when other reports exist.

### Deferred display

Reports are added to `gTranscript` during command execution but displayed only after the full action cycle completes. This allows the transcript to:

- Sort reports by sequence number (before → main → after)
- Group reports by action for multi-object commands
- Apply suppression rules with complete knowledge of all reports
- Insert group separators between different actions
- Support `summarizeAction()` for multi-object report grouping ("You take the key, the coin, and the book.")

---

## Author Customization Patterns

### Per-object message override

The simplest customization: define the message property directly on the object.

```tads3
+ sword: Thing 'rusty sword' 'rusty sword'
    /* Override the default "Taken." with a custom string */
    okayTakeMsg = 'You pry the rusty sword from the wall. '

    /* String properties can use parameter substitution */
    cannotDropMsg = '{You/he} {won\'t} let go of {the dobj/him}. '
;
```

### Class-level override

Override a message for all objects of a class:

```tads3
modify Heavy
    cannotTakeMsg = '{That dobj/he} {is} far too heavy. '
;
```

### Custom message parameters

Register additional objects so message strings can reference them:

```tads3
dobjFor(Take)
{
    check()
    {
        if (location.ofKind(LockedContainer))
        {
            gMessageParams(location);
            reportFailure('{You/he} {can\'t} reach into
                {the location/him}. ');
        }
    }
}
```

### Actor-specific message objects

Give an NPC a unique voice by providing a custom message object:

```tads3
pirate: Actor 'pirate' 'pirate' @quarterdeck
    getActionMessageObj() { return pirateMessages; }
;

pirateMessages: playerActionMessages
    okayTakeMsg = '{You/he} grab{s/d} {the dobj/him}. Arr! '
    cannotDoThatMsg = '{You/he} {won\'t} be doin\' that. '
;
```

### Method-based messages with conditions

Use a method to vary the message based on game state:

```tads3
+ door: Door 'heavy door' 'heavy door'
    cannotOpenMsg()
    {
        if (isLocked)
        {
            gMessageParams(self);
            return '{The dobj/he} {is} locked tight. ';
        }
        return nil;  /* nil = fall through to default */
    }
;
```

Returning `nil` from a method override tells `resolveMessageText()` to skip this object and continue searching — useful for conditional overrides.

### Past tense narration

Switch the entire game to past tense:

```tads3
gameMain: GameMainDef
    usePastTense = true
;
```

All parameterized messages automatically adapt: `{You/he} {take[s]|took}` produces "took" instead of "take/takes."

---

## Practical Intervention Points

### Defining and overriding messages

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `okayTakeMsg`, `cannotOpenMsg`, etc. | String or method property on Thing | Per-object message override |
| `dobjMsg(str)` | Macro returning string or nil | Override only when object is dobj |
| `iobjMsg(str)` | Macro returning string or nil | Override only when object is iobj |
| `modify playerActionMessages` | Change the default message object | Global message change for all players |
| `modify npcActionMessages` | Change the NPC message object | Global message change for all NPCs |
| `getActionMessageObj()` | Override on Actor | Per-actor custom message set |
| `nil` return from method override | Conditional skip | Fall through to default when override doesn't apply |

### Parameter substitution

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `setMessageParam(name, obj)` | Call on `gAction` | Register a custom named parameter |
| `gMessageParams(var...)` | Macro (names from variable names) | Convenient multi-parameter registration |
| `gSynthMessageParam(obj)` | Macro returning synthetic name | Generate a unique parameter name for an object |
| `buildParam(type, name)` | Function | Build `{type name}` string from variables |
| `buildSynthParam(type, obj)` | Function | Build parameter string with synthetic name |

### Report control

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `defaultReport(msg)` | Macro | Suppressible confirmation message |
| `mainReport(msg)` | Macro | Primary narrative report (suppresses defaults) |
| `reportFailure(msg)` | Macro | Failure message (marks action as failed) |
| `reportBefore(msg)` / `reportAfter(msg)` | Macros | Ordered around main report |
| `extraReport(msg)` | Macro | Incidental message (doesn't suppress defaults) |
| `defaultDescReport(msg)` | Macro | "Nothing special" descriptions |
| `cosmeticSpacingReport(msg)` | Macro | Paragraph break without suppressing defaults |

### Tense and person

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `gameMain.usePastTense` | Property | Switch entire game to past tense |
| `{present\|past}` syntax | In message strings | Tense-dependent text within a single message |
| `tSel(present, past)` | Function | Choose between forms in code |
| `withPresent(func)` / `withPast(func)` | Functions | Temporarily override tense in a callback |
| `{parameter!}` (exclamation suffix) | In message strings | Force present-tense evaluation |
| `{subj obj}` | In message strings | Explicit subject marker for reflexive tracking |

### Custom message objects

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `playerActionMessages` | Singleton object | Default messages for player actions |
| `npcActionMessages` | Singleton object | Default messages for NPC actions |
| `libMessages` | Singleton object | Parser and general library messages |
| `MessageHelper` | Base class | Inherit for custom message collections |
| `shortTMsg(msg, shortMsg)` | Method on MessageHelper | Select short/long form based on disambiguation context |

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [Action Resolution](action-resolution.md) for the verify/check/action pipeline that produces messages. For the containment tree that determines what objects are in scope, see [Containment Model](containment-model.md). For the scheduling loop, fuses, daemons, and real-time events, see [Event Scheduling](event-scheduling.md).*
