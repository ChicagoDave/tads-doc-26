# Session: Message System Accuracy Fixes

**Date:** 2026-02-21
**Task:** Verify every technical claim in `docs/docs/architecture/message-system.md` against TADS 3 adv3 library source, fix all issues.

## Source Files Checked

- `tads-sources/tads3/lib/adv3/en_us/msg_neu.t` (message definitions)
- `tads-sources/tads3/lib/adv3/output.t` (MessageBuilder class)
- `tads-sources/tads3/lib/adv3/en_us/en_us.t` (langMessageBuilder, MessageHelper, paramList_)
- `tads-sources/tads3/lib/adv3/exec.t` (MessageResult, resolveMessageText)
- `tads-sources/tads3/lib/adv3/report.t` (CommandReport hierarchy)
- `tads-sources/tads3/lib/adv3/action.t` (getMessageParam, setMessageParam, synthMessageParam)
- `tads-sources/tads3/lib/adv3/adv3.h` (macros: report macros, gMessageParams, dobjMsg/iobjMsg, tSel, withPresent/withPast)
- `tads-sources/tads3/lib/adv3/actor.t` (getActionMessageObj)

## Fixes Applied

### ERROR (1 fix)

1. **`resolveMessageText()` is a method of `MessageResult`, not a standalone function.** Fixed in 7 locations:
   - Layer 3 overview diagram
   - Source files table (exec.t entry)
   - Message lifecycle trace (step 3)
   - Dispatch section opening paragraph
   - Override resolution algorithm header
   - Role-selective overrides paragraph
   - Method-based messages explanation

### INACCURACIES (4 fixes)

1. **Spatial preposition output was wrong.** `{on}`, `{into}`, `{outof}` etc. do NOT produce just the preposition ("on", "into"). They produce the full prepositional phrase via `actorInName` ("on the chair", "into the box"). Fixed example output column and explanation paragraph.

2. **`langMessageBuilder` called a "subclass" of `MessageBuilder`.** It is actually an object (instance), not a class. Changed to "object (an instance of `MessageBuilder` defined in en_us.t)".

3. **`okayTakeMsg` oversimplified.** Document said playerActionMessages' `okayTakeMsg` is simply `'Taken. '`. In reality it is `shortTMsg('Taken. ', '{You/he} {take[s]|took} {the dobj/him}. ')`, which conditionally selects between short and long forms based on disambiguation context. Fixed description.

4. **`tSel`, `withPresent`, `withPast` called "Functions".** All three are macros defined in `en_us.h`, not functions. Fixed in both the tense tools table and the intervention points table (3 locations total).

### MINOR (7 fixes)

1. **Missing `npcMessages` from class hierarchy.** Added `npcMessages` as a child of `playerMessages` (npcMessages: playerMessages, line 2150 of msg_neu.t).

2. **Missing `{was}`/`{were}` parameters and verb base forms.** Added `{was}`/`{were}` -> `&verbWas` row to verb table. Updated specialized verbs line to include base forms (`{go}`, `{come}`, `{leave}`, `{see}`, `{say}`).

3. **"roughly 600" message properties overstated.** Actual count in msg_neu.t is ~429. Changed to "several hundred" / "hundreds of" in 3 locations.

4. **Missing `QuestionCommandReport`** from report class hierarchy. Added as child of `MainCommandReport`.

5. **`shortTMsg` argument order reversed.** Doc said `shortTMsg(msg, shortMsg)` but actual signature is `shortTMsg(short, long)`. Fixed.

6. **Verb `isNominative` description misleading.** Changed from "track the same subject" to "set `lastSubject_` to the current target object" for precision.

7. **`theName` description imprecise.** Changed from "returns its name with article" to "returns its name with the definite article", and added clarification that Actor adapts to person/number.

### Additional minor fixes

- **`PreinitObject` described as "compile time"**: Changed to "pre-initialization" (correct TADS 3 terminology).
- **Pirate example inherited from `playerActionMessages`**: Changed to `npcActionMessages` since the pirate is an NPC and should inherit NPC-specific message overrides.
- **Reflexive punctuation reset**: Added detail that punctuation must be followed by non-alphanumeric (matches actual regex `[.;:!?]<^alphanum>`).
- **`action.t` role description**: Lowercase "action" changed to "Action" (class name).

## Total Changes: 1 error, 4 inaccuracies, 7 minor issues = 12 fixes applied
