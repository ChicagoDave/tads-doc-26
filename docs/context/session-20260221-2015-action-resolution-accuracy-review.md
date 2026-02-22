# Session: Action Resolution Architecture Doc Accuracy Review

**Date:** 2026-02-21
**Task:** Verify every technical claim in `action-resolution.md` against adv3 source code and fix all errors, inaccuracies, and minor issues.
**File modified:** `docs/docs/architecture/action-resolution.md`

## Changes Made

### ERRORS Fixed (3)

1. **`GlobalRemapping.getRemapping()` parameter order** (line 340)
   - Was: `getRemapping(action, issuingActor, targetActor)`
   - Fixed: `getRemapping(issuingActor, targetActor, action)`
   - Source: `exec.t:642`, `actions.t:2184`

2. **`GlobalRemapping.getRemapping()` return format** (lines 339-357)
   - Was: Simplified pseudo-code returning `[targetActor, AskForAction, action.getDobj()]` (3 elements, using class name and raw object)
   - Fixed: Realistic code returning `[issuingActor, newAction]` (2-element list with target actor and full Action instance, matching `exec.t:635` comment and `actions.t:2241` actual return)
   - Also renamed the object from `globalRemapGiveMe` to `giveMeToAskFor` to match `actions.t:2177`

3. **Check vs Before ordering** (flow chart + execution sequence steps 7-9)
   - Was: Check (step 7) before Before Notifications (step 8) -- the doc had the default ordering backwards
   - Fixed: Before Notifications (step 7) before Check (step 9), with note that `gameMain.beforeRunsBeforeCheck` (default `true` in `misc.t:518`) controls the ordering
   - Source: `action.t:1454` checks `beforeRunsBeforeCheck` and runs `runBeforeNotifiers()` before the try block that contains `actorAction()`/`checkAction()`

### INACCURACIES Fixed (5)

4. **`actorAction()` missing from execution sequence** (step 8)
   - Was: Omitted entirely from the numbered execution steps
   - Fixed: Added as step 8 between Before Notifications and Check. `gActor.actorAction()` always runs before `checkAction()` regardless of `beforeRunsBeforeCheck` setting.
   - Source: `action.t:1466`

5. **`inScopeList` description in ResolvedTopic** (line 412)
   - Was: "Objects matching the topic that are in the actor's physical scope"
   - Fixed: "Objects matching the topic that are in 'conversational scope' -- physically in scope *or* known to the actor (via `ConvTopicResolver.objInConvScope`)"
   - Source: `action.t:6569-6601` shows `ConvTopicResolver.resolveTopic()` uses `objInConvScope()` which returns true for physical scope OR `actor_.knowsTopic(obj)`

6. **Three-tier classification attribution** (line 403)
   - Was: Stated flatly that topic resolution sorts into three lists
   - Fixed: Clarified that only `ConvTopicResolver` performs the three-way split; the base `TopicResolver.resolveTopic()` puts everything in a single undifferentiated list
   - Source: `action.t:6478-6481` (base) vs `action.t:6560-6587` (ConvTopicResolver)

7. **TopicResolver scope mechanism description** (line 141)
   - Was: "`TopicResolver` overrides `isGlobalScope` to return `true`, and its `matchName()` matches against the entire game dictionary"
   - Fixed: "`TopicResolver` overrides `isGlobalScope` to return `true` and `objInScope()` to return `true` for every object, so the normal `matchName()` on Thing runs against every object in the game"
   - Source: `action.t:6399` (`objInScope` returns true), `action.t:6405` (`isGlobalScope = true`). `matchName()` is defined on `Thing`, not on `TopicResolver`.

8. **`withParserGlobals` scope description** (line 220)
   - Was: "These are set by `withParserGlobals()` and are safe across nested actions"
   - Fixed: Clarified that `withParserGlobals()` directly saves/restores `gActor`, `gIssuingActor`, and `gAction`; `gDobj`/`gIobj` are macros deriving from `gAction`; and `gVerifyResults` is a separate global not managed by `withParserGlobals()`
   - Source: `action.t:89-118` (withParserGlobals), `adv3.h:118-119` (gDobj/gIobj macros), `adv3.h:180` (gVerifyResults)

### MINOR Issues Fixed (4)

9. **Source file count in intro** (line 3)
   - Was: "four source files (`action.t`, `verify.t`, `precond.t`, `resolver.t`)"
   - Fixed: "five source files (`exec.t`, `action.t`, `verify.t`, `precond.t`, `resolver.t`)"
   - `exec.t` contains `GlobalRemapping` and `executeAction()`, both central to the pipeline

10. **Flow chart visual formatting** (lines 16-60)
    - Was: Asterisk note placed between "Action" and "After Notifications", breaking the arrow chain
    - Fixed: Note placed at bottom of diagram after the full arrow chain completes; also added "Actor Notification" box for `actorAction()`

11. **Phase table missing entries** (lines 69-75)
    - Was: Single "Notifications" row for both before and after
    - Fixed: Separate rows for "Before notifications" (with `misc.t` reference and `beforeRunsBeforeCheck` note) and "After notifications"

12. **Section header "The ten-step sequence"** (line 162)
    - Was: "The ten-step sequence" (now has 11 steps after adding actorAction)
    - Fixed: "The execution sequence"

## Files Checked (source code)
- `exec.t` -- GlobalRemapping, executeAction, executeCommand
- `action.t` -- Action hierarchy, doActionOnce, TAction, TIAction, IAction, TopicResolver, ConvTopicResolver, ResolvedTopic, verification flow, precondition checking, before/after notifications
- `verify.t` -- VerifyResult hierarchy, resultRanks, allowAction, allowImplicit, LogicalVerifyResult.likelihood/listOrder
- `precond.t` -- PreCondition class, preCondOrder, all built-in preconditions (objVisible through roomToHoldObj), ObjectPreCondition
- `resolver.t` -- Resolver base class, cacheScopeList, objInScope, isGlobalScope, IobjResolver
- `misc.t` -- gameMain.beforeRunsBeforeCheck
- `thing.t` -- vocabLikelihood, filterResolveList, isEquivalent, beforeAction, afterAction, matchName
- `actor.t` -- actorAction, isLikelyTopic
- `travel.t` -- BasicLocation.roomBeforeAction
- `adv3.h` -- gDobj, gIobj, gVerifyResults macros, replaceAction macro
- `actions.t` -- giveMeToAskFor GlobalRemapping instance
