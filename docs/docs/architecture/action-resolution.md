# Action Resolution

Once the parser has selected a winning parse tree, the game must transform it into a concrete change in the world. This is action resolution — the pipeline that takes an Action with unresolved noun phrases and produces a fully executed command applied to specific game objects. The pipeline spans four source files (`action.t`, `verify.t`, `precond.t`, `resolver.t`) and one header (`adv3.h`), and its architecture determines how every verb interaction in the game behaves.

[Overview](#action-resolution-overview) | [Action Hierarchy](#the-action-class-hierarchy--actiont) | [Scope](#scope--who-can-see-what) | [Execution Cycle](#the-execution-cycle--doactiononce) | [Verification](#verification--verifyt) | [Preconditions](#preconditions--precondt) | [Remapping](#remapping) | [Topics](#topic-resolution-and-resolvedtopic) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to other architecture docs"
    The [Parser Pipeline](parser-pipeline.md) explains everything that happens *before* this stage — grammar matching, command ranking, and noun resolution. The [Design Patterns](design-patterns.md) document explains the `dobjFor`/`iobjFor` macro system that game authors use to write handlers. The library reference pages on [Verify and Check](../library/actions/verify-check.md), [Preconditions](../library/actions/preconditions.md), and [Creating Verbs](../library/actions/creating-verbs.md) provide practical how-to guides. This document explains the architecture underneath all of them — why the classes are shaped the way they are, how the execution cycle is orchestrated, and where the extension points live.

---

## Action Resolution Overview

After the parser selects a winning parse tree and `executeAction()` begins, the command passes through a sequence of phases before the world state changes:

```
Winning Parse Tree  (Action + noun phrase productions)
     │
     ▼
Global Remapping              action → possibly different action
     │
     ▼
Noun Resolution               noun phrases → ResolveInfo lists
     │
     ▼
Object Iteration Start        for each resolved object...
     │
     ▼
Remapping Check               object may redirect the action
     │
     ▼
Verify (pass 1)               is the action logical for this object?
     │
     ▼
Preconditions (pass 1)        enforce prerequisites, run implicit actions
     │
     ▼
Verify (pass 2, if needed)    re-verify after implicit actions
     │
     ▼
Preconditions (pass 2)        re-check, no new implicit actions allowed
     │
     ▼
Check                         runtime go/no-go (hidden state)
     │
     ▼
Before Notifications          beforeAction on actor and scope objects
     │
     ▼
Action                        world state changes happen here
     │
     ▼
After Notifications           afterAction on actor and scope objects
```

The phases are orchestrated by these source files:

| Phase | Source | Key entry point |
|-------|--------|-----------------|
| Global remapping | `exec.t` | `GlobalRemapping.getRemapping()` |
| Noun resolution | `resolver.t`, `action.t` | `action.resolveNouns()` via `Resolver` |
| Object iteration | `action.t` | `TAction.doActionMain()`, `TIAction.doActionMain()` |
| Remapping check | `action.t` | `action.checkRemapping()` |
| Verify | `action.t`, `verify.t` | `action.verifyAction()` → `callVerifyProp()` |
| Preconditions | `action.t`, `precond.t` | `action.checkPreConditions()` |
| Check | `action.t` | `action.checkAction()` |
| Action execution | `action.t` | `action.execAction()` |
| Notifications | `action.t` | `action.runBeforeNotifiers()`, `action.afterAction()` |

The single most important design principle: **verb behavior is defined on the objects involved in the command, not on the action class itself.** When the player types TAKE THE KEY, the key defines what "take" means for a key, via its `dobjFor(Take)` handler block. The action class orchestrates the pipeline; the objects supply the logic.

---

## The Action Class Hierarchy — action.t

Every action in adv3 inherits from `Action`, which inherits from `BasicProd` (the grammar production base class). This means every action is both an executable command and a grammar rule — a design choice explained in the [Parser Pipeline](parser-pipeline.md#the-production-hierarchy).

```
Action: BasicProd
├── IAction                          no objects (JUMP, SLEEP, INVENTORY)
│
├── TAction: Action, Resolver        one object (TAKE X, OPEN X)
│   │
│   └── TIAction                     two objects (PUT X IN Y, UNLOCK X WITH Y)
│
├── LiteralActionBase (mixin)
│   ├── LiteralAction: IAction       literal text (TYPE HELLO)
│   └── LiteralTAction: TAction      literal + object (TYPE HELLO ON KEYBOARD)
│
├── TopicActionBase (mixin)
│   ├── TopicAction: IAction          topic (THINK ABOUT WAR)
│   └── TopicTAction: TAction         topic + object (ASK BOB ABOUT WAR)
│
└── ConvIAction: IAction              conversational (HELLO, YES, NO)
```

| Action type | Object slots | How nouns are resolved | Example |
|-------------|-------------|----------------------|---------|
| `IAction` | None | `resolveNouns()` notes 0 slots | JUMP |
| `TAction` | Direct object | Action serves as its own dobj Resolver | TAKE BALL |
| `TIAction` | Direct + indirect | Separate `IobjResolver` for iobj | PUT BALL IN BOX |
| `LiteralAction` | Literal text | Text captured verbatim, no resolution | SAY HELLO |
| `LiteralTAction` | Object + literal | Object resolved, text captured | WRITE NOTE ON PAPER |
| `TopicAction` | Topic | `TopicResolver` with global scope | THINK ABOUT TREASURE |
| `TopicTAction` | Object + topic | Object resolved physically, topic globally | ASK BOB ABOUT TREASURE |
| `ConvIAction` | None | No resolution; marks action as conversational | HELLO |

### TAction is its own Resolver

The most architecturally significant choice in the hierarchy: `TAction` inherits from both `Action` and `Resolver`. A TAction *is* its own direct-object resolver — it does not delegate to a separate resolver object. The source comment explains why:

> For simplicity, this object is its own object resolver — we really don't need a separate resolver object because we have only one object list for this verb. The advantage of implementing the Resolver behavior in this object, rather than using a separate object, is that it's less trouble to override object resolution rules — simply override the resolver methods in the subclass where you define the grammar rule for the action.

This means that when you want to change how a specific action resolves its direct object — for example, making LISTEN use audible scope instead of visual scope — you override the resolver methods directly on the action class, not on a separate object.

`TIAction` uses the action itself for its direct object and creates a separate `IobjResolver` for the indirect object, because the two roles often need different scope and filtering rules.

---

## Scope — Who Can See What

Before noun phrases can be resolved to objects, the system must determine which objects are *in scope* — available for the player to refer to. Scope is the bridge between the physical world model and the parser.

### How scope is built

The default scope is the actor's sensory environment. When `Resolver.cacheScopeList()` runs, it asks the actor for every object the actor can perceive through any sense:

1. The actor calls its sensory scope method, which traverses the containment tree
2. Objects reachable through sight, hearing, smell, or touch enter the scope list
3. The scope list is cached for the duration of the resolution pass

### Physical scope vs. global scope

Most actions use physical scope — you can only TAKE what you can perceive. But topic-related actions use global scope, because conversation topics are not physical objects. `TopicResolver` overrides `isGlobalScope` to return `true`, and its `matchName()` matches against the entire game dictionary rather than just objects in the actor's immediate environment.

### Overriding scope on actions

Any action can expand or restrict scope by overriding `objInScope(obj)`:

```tads3
// Allow LISTEN to match objects the actor can hear but not see
modify ListenToAction
    objInScope(obj) { return gActor.canHear(obj); }
;
```

The scope system connects to the sense and perception model (material transparency, the four senses). For the full architecture of sense path calculation, brightness propagation, and how senses feed scope, see [Sense and Perception](sense-perception.md).

---

## The Execution Cycle — doActionOnce()

The heart of action resolution is `doActionOnce()` (at `action.t:1326`), which runs the full execution sequence for one set of objects. Understanding its structure is the key to understanding how every command in the game executes.

### The ten-step sequence

For each combination of resolved objects, `doActionOnce()` runs:

1. **`checkRemapping()`** — Ask each resolved object if it wants to redirect the action. If an object returns remap info, the action is replaced entirely (via `exit`) and the new action starts fresh.

2. **Implicit action check** — If this is an implicit action (triggered by a precondition), verify that the action is safe to perform implicitly. If verification returns `allowAction = true` but `allowImplicit = nil`, abort silently.

3. **`verifyAction()` (pass 1)** — Call the `verify()` handler on each involved object. If any result has `allowAction = nil`, display the failure message and terminate the command.

4. **`checkPreConditions(pass 1)`** — Run all preconditions. Each precondition may trigger an implicit action (e.g., automatically taking an object). If any implicit action fires, the loop continues to pass 2.

5. **`verifyAction()` (pass 2)** — Re-verify after implicit actions may have changed game state. An object that was logical before might now be illogical (or vice versa).

6. **`checkPreConditions(pass 2)`** — Re-check preconditions, but with `allowImplicit = nil` — no new implicit actions are permitted on the second pass. This prevents infinite loops from conflicting preconditions.

7. **`checkAction()`** — Run the `check()` handler on each involved object. Unlike verify, check failures do not influence disambiguation — they represent conditions the player cannot see.

8. **`runBeforeNotifiers()`** — Fire `beforeAction` notifications on the actor, the actor's location, and every object in scope. Any notifier can cancel the action with `exit`.

9. **`execAction()`** — Run the `action()` handler on the involved objects. This is where world state changes happen — moving objects, changing properties, printing descriptions.

10. **`afterAction()`** — Fire after-action notifications. These cannot cancel the action (it has already happened) but can react to the change.

### The two-pass design

The verify-precondition loop runs up to two iterations. The reason: a precondition might trigger an implicit action (like taking an object), which changes the world state. That change might invalidate a verification that passed on the first iteration, or it might make a different precondition fail. The second pass catches these cascading effects.

Critically, the second pass does *not* allow new implicit actions. If it did, two conflicting preconditions could loop forever — one pass opens the door, the other closes it, and so on. The two-pass limit is a deliberate safety bound.

### Object iteration

The execution cycle runs once per object combination:

- **`IAction`** — No objects. `doActionMain()` calls `doActionOnce()` exactly once.

- **`TAction`** — Iterates over `dobjList_`. For each direct object, sets `dobjCur_` and calls `doActionOnce()`. If the player says TAKE ALL, this iterates over every object that ALL resolves to.

- **`TIAction`** — Iterates over whichever list has multiple objects (dobj or iobj). For each iteration, sets both `dobjCur_` and `iobjCur_`, then calls `doActionOnce()`. The non-iterated object stays fixed.

### Current-object globals

During execution, several global variables track the current state:

| Global | Meaning |
|--------|---------|
| `gActor` | The actor performing the action |
| `gIssuingActor` | The actor who issued the command (may differ for NPC commands) |
| `gAction` | The current action object |
| `gDobj` | The current direct object (shorthand for `gAction.getDobj()`) |
| `gIobj` | The current indirect object (shorthand for `gAction.getIobj()`) |
| `gVerifyResults` | The current `VerifyResultList` (only during verify phase) |

These are set by `withParserGlobals()` and are safe across nested actions — each nested call saves and restores the previous values.

---

## Verification — verify.t

Verification answers the question: "Is this action logical for this object, from the player's perspective?" It serves two purposes — disambiguation (helping the parser choose the right object) and validation (preventing obviously nonsensical actions).

### The VerifyResult hierarchy

```
VerifyResult                           base class
├── LogicalVerifyResult                resultRank = 100  (logical, allowed)
├── DangerousVerifyResult              resultRank = 90   (allowed, not implicitly)
├── NonObviousVerifyResult             resultRank = 30*  (allowed, not implicitly)
├── IllogicalNowVerifyResult           resultRank = 40   (not allowed, state-dependent)
│   └── IllogicalAlreadyVerifyResult   resultRank = 40   (already in desired state)
├── IllogicalVerifyResult              resultRank = 30   (not allowed, always illogical)
│   └── IllogicalSelfVerifyResult      resultRank = 30   (object used on itself)
└── InaccessibleVerifyResult           resultRank = 10   (not allowed, sense barrier)

* NonObviousVerifyResult uses IllogicalVerifyResult.resultRank (30)
```

| Result class | Rank | allowAction | allowImplicit | When to use |
|-------------|------|-------------|---------------|-------------|
| `LogicalVerifyResult` | 100 | yes | yes | Action makes sense (default) |
| `DangerousVerifyResult` | 90 | yes | no | Logical but obviously risky |
| `NonObviousVerifyResult` | 30 | yes | no | Logical but not obvious to player |
| `IllogicalNowVerifyResult` | 40 | no | no | Illogical due to current state |
| `IllogicalAlreadyVerifyResult` | 40 | no | no | Target state already achieved |
| `IllogicalVerifyResult` | 30 | no | no | Always illogical for this object |
| `IllogicalSelfVerifyResult` | 30 | no | no | Object used on itself (PUT BOX IN BOX) |
| `InaccessibleVerifyResult` | 10 | no | no | Cannot perceive object via required sense |

### The key design insight

The source comment at the top of `verify.t` captures the most important rule:

> It is important to understand that the purpose of verification results is to guess what's in the player's mind, not to reflect the full internal state of the game.

A locked door should verify as *logical* for OPEN, because the player can see it is closed and knows doors can be opened. The lock is hidden state — it belongs in `check()`, not `verify()`. This principle is what makes disambiguation work correctly: the parser uses verify results to pick the object the player most likely means, and that choice must be based on what the player can observe.

### The likelihood mechanism

`LogicalVerifyResult` has a `likelihood` property (default 100) that provides fine-grained preference among logical objects. If two red balls both verify as logical for TAKE, but one is already being carried indirectly, the carried one can return a lower likelihood to make the parser prefer the other. This is a softer signal than `illogicalNow` — both objects are valid, but one is preferred.

Preconditions use a secondary ranking mechanism: `listOrder = 150` (vs. the default 100) ensures that precondition-derived likelihood adjustments lose to action-specific ones when both are present.

### How verify drives disambiguation

Verification is called in two contexts:

1. **During command ranking** — The parser calls verify *tentatively* on each candidate object to count problems. The results feed into `CommandRanking` criteria like `rankByNonMatch` and `rankByAmbiguity` (see [Command Ranking](parser-pipeline.md#command-ranking)).

2. **During execution** — The action calls verify for real, and objects that fail verification are reported as errors.

This dual use is why verify must be side-effect-free — it runs speculatively during ranking and must not change game state.

---

## Preconditions — precond.t

Preconditions enforce requirements that must be met before an action can execute, and they can automatically satisfy those requirements via implicit actions.

### The PreCondition interface

Every precondition implements two methods:

| Method | Purpose |
|--------|---------|
| `verifyPreCondition(obj)` | Called during the verify phase to adjust likelihood. An object that doesn't meet the condition gets a lower likelihood, making the parser prefer objects that already satisfy the requirement. |
| `checkPreCondition(obj, allowImplicit)` | Called during the precondition phase. If the condition is not met and `allowImplicit` is true, attempt an implicit action to satisfy it. If the condition still isn't met, report failure and terminate. |

### Built-in preconditions

| Precondition | What it checks | Implicit action |
|-------------|---------------|-----------------|
| `objVisible` | Object is visible to actor | None (verify only) |
| `objAudible` | Object is audible to actor | None (verify only) |
| `objSmellable` | Object is within smell range | None (verify only) |
| `touchObj` | Actor can physically touch object | Open containers in the way |
| `objHeld` | Actor is holding the object | `Take` the object |
| `objNotWorn` | Actor is not wearing the object | `Doff` the object |
| `objOpen` | Object is open | `Open` the object |
| `objClosed` | Object is closed | `Close` the object |
| `objUnlocked` | Object is unlocked | `Unlock` the object |
| `objBurning` | Object is lit | `Burn` the object |
| `objEmpty` | Object contains nothing | `TakeFrom` each child |
| `actorStanding` | Actor is standing | `Stand` |
| `actorTravelReady` | Actor is ready to travel | Delegate to location |
| `actorDirectlyInRoom` | Actor is directly in room | Move actor to room |
| `canTalkToObj` | Actor can communicate with object | None |
| `roomToHoldObj` | Actor has room in inventory | Delegate to actor |

### The implicit action loop

When a precondition's `checkPreCondition()` fires an implicit action, the entire verify-precondition sequence re-runs (pass 2). This catches cascading effects — for example, if the `objHeld` precondition implicitly takes an object, the `touchObj` precondition needs to re-verify that the object is still reachable in its new location.

The pattern used by most preconditions follows a consistent structure:

1. Check if the condition is already met → return `nil` (no implicit action needed)
2. If `allowImplicit`, try the implicit action → if it worked, return `true`
3. If it didn't work or `allowImplicit` is false → report failure and `exit`

### Precondition ordering

Preconditions have a `preCondOrder` property (default 100) that controls execution order. The `touchObj` family uses order 200 (runs later) because touch reachability is fragile — other preconditions that move the actor or change containment might undo its effects. Running it last minimizes this problem.

For a full tutorial on writing custom preconditions, see [Custom Preconditions](../library/actions/preconditions.md).

---

## Remapping

Remapping redirects a command to a different action or a different target object. TADS 3 provides two remapping levels that operate at different points in the pipeline.

### GlobalRemapping — action level

`GlobalRemapping` runs in `executeAction()` *before* nouns are fully resolved. It intercepts at the action level and can transform one action into a completely different one:

```tads3
globalRemapGiveMe: GlobalRemapping
    getRemapping(action, issuingActor, targetActor)
    {
        // Turn GIVE ME X (where "me" is the issuing actor) into ASK FOR X
        if (action.ofKind(GiveToAction) && action.getIobj() == issuingActor)
            return [targetActor, AskForAction, action.getDobj()];
        return nil;
    }
;
```

Because GlobalRemapping runs before resolution, it can change the entire structure of the command — even switching from a two-object action to a single-object action.

### remapTo — object level

`remapTo()` operates on individual objects and runs during `checkRemapping()`, after nouns are resolved but before verify. An object's remap property redirects the action:

```tads3
desk: Heavy, Surface 'desk' 'desk'
    dobjFor(Open) { remap = remapTo(Open, drawer) }
;
```

When the player types OPEN DESK, the desk redirects the action to OPEN DRAWER. The remapping fires `remapVerify()` to verify the action on the new target, and if the original object has an overriding verify (defined more specifically than the remap), that runs too.

### asDobjFor / asIobjFor — handler reuse

Unlike `remapTo`, which redirects the *action* to a different object, `asDobjFor`/`asIobjFor` reuses another action's *handlers* on the same object:

```tads3
+ heavyBox: Container 'heavy box' 'heavy box'
    dobjFor(Search) asDobjFor(LookIn)
;
```

This means "when someone searches this box, use the LookIn handlers." No new action is created — the same object simply borrows another action's verify/check/action methods.

### Comparison

| Mechanism | When it runs | What it changes | Use case |
|-----------|-------------|----------------|----------|
| `GlobalRemapping` | Before noun resolution | Entire action, any objects | Transform one verb into another globally |
| `remapTo()` | After resolution, before verify | Target object and/or action | Redirect on a per-object basis |
| `asDobjFor()`/`asIobjFor()` | During verify/check/action | Only the handler methods called | Reuse handlers without changing the action |

---

## Topic Resolution and ResolvedTopic

Topic actions (`TopicAction`, `TopicTAction`) resolve their topic argument differently from physical objects. The player might ASK BOB ABOUT THE TREASURE even when no "treasure" object is in the room — topics are matched against knowledge, not physical presence.

### How topic resolution differs

1. **Global scope** — `TopicResolver` uses global scope, so every object in the game with matching vocabulary is a candidate.
2. **Three-tier classification** — Matches are sorted into three lists, not filtered to a single winner.
3. **No disambiguation** — The game never asks "Which treasure do you mean?" for topics. Instead, the three lists give the action handler enough information to decide what to do.

### The ResolvedTopic structure

When a topic noun phrase resolves, it produces a `ResolvedTopic` object:

| Property | Contents |
|----------|----------|
| `inScopeList` | Objects matching the topic that are in the actor's physical scope |
| `likelyList` | Objects not in scope but that the actor considers likely topics (via `isLikelyTopic`) |
| `otherList` | All remaining objects matching the topic vocabulary |
| `topicProd` | The grammar production that matched the topic phrase |
| `resInfoTab` | Lookup table from game object to its `ResolveInfo` (for vocabulary match details) |

The `getBestMatch()` method picks the strongest match: in-scope objects first, then likely topics, then others. Game authors can override this method to implement custom topic-matching strategies.

---

## Practical Intervention Points

The action resolution pipeline provides hooks at every stage. Here is a consolidated reference of the places where game authors can intervene, organized by what you want to accomplish.

### Controlling which objects get chosen

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `verify()` | `dobjFor(X) { verify() { ... } }` | The primary disambiguation tool — make the parser prefer or reject this object |
| `vocabLikelihood` | Property on Thing | Bias disambiguation without adding verify logic |
| `filterResolveList()` | Override on Thing | Remove, substitute, or add objects during resolution |
| `matchName()` | Override on Thing | Customize which words match an object |
| `isEquivalent` | Property on Thing | Collapse interchangeable objects (five gold coins → one) |

### Adding or customizing preconditions

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `preCond` list | `dobjFor(X) { preCond = [objHeld, touchObj] }` | Specify which preconditions apply to an action on this object |
| Custom `PreCondition` | Subclass `PreCondition`, define `checkPreCondition` and `verifyPreCondition` | Create new preconditions with custom implicit actions |
| `ObjectPreCondition` | `new ObjectPreCondition(specificObj, existingCond)` | Apply an existing precondition to a specific object, not the action's default target |

### Redirecting actions

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `GlobalRemapping` | Subclass, override `getRemapping()` | Transform one action into another globally (GIVE ME X → ASK FOR X) |
| `remapTo()` | In `dobjFor`/`iobjFor` remap block | Redirect to a different object on a per-object basis (OPEN DESK → OPEN DRAWER) |
| `asDobjFor()`/`asIobjFor()` | In `dobjFor`/`iobjFor` blocks | Reuse another action's handlers on the same object (SEARCH → LOOK IN) |
| `replaceAction()` | In check/action handlers | Replace the current action mid-execution |

### Customizing scope

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `objInScope(obj)` | Override on Action | Expand or restrict what objects the parser can match for this action |
| `cacheScopeList()` | Override on Resolver/Action | Completely replace the scope-building logic |
| `isGlobalScope` | Property on Resolver | Switch to global (non-physical) scope for the action |

### Intercepting before and after execution

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `actorAction()` | Override on Actor | Intercept any action the actor is about to perform |
| `beforeAction()` | Override on Thing | React to (or cancel) actions before they execute; called on every in-scope object |
| `roomBeforeAction()` | Override on Room | Room-level interception of actions |
| `afterAction()` | Override on Thing | React to actions after they execute; called on every in-scope object |
| `roomAfterAction()` | Override on Room | Room-level reaction to completed actions |
| `callAfterActionMain(obj)` | Call during action | Register an object for a one-time post-action callback |

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [The Parser Pipeline](parser-pipeline.md) for how text becomes a parsed action before this stage. For how scope connects to the sensory model, see [Sense and Perception](sense-perception.md). For the containment tree, reachability, and capacity system that underpin preconditions, see [Containment Model](containment-model.md). For how action handlers produce player-visible text through parameter substitution and the report system, see the [Message System](message-system.md). For the `dobjFor`/`iobjFor` pattern used to write handlers, see [Design Patterns](design-patterns.md).*
