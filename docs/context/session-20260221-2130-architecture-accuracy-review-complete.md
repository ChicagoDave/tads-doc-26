# Session Summary: 2026-02-21 - architecture-accuracy-review-complete

## Status: Completed

## Goals
- Complete the accuracy fix pass interrupted in the previous session (session-20260221-1927)
- Apply all verified fixes to the five remaining architecture deep-dive documents
- Verify build and commit to main

This session is a direct continuation of `session-20260221-1927-architecture-accuracy-review.md`,
which completed assessment of all six deep-dives and applied partial fixes to parser-pipeline.md
before being interrupted. The assessment findings from that session drove all work done here.

## Completed

### parser-pipeline.md — 4 Remaining Fixes Applied

Four fixes deferred from the prior session were applied:

1. **ERROR fixed**: Distinguisher singleton instances — changed "subclasses" to "singleton
   instances" throughout. The actual pattern is that `DefaultDistinguisher`,
   `NameDistinguisher`, etc. are singleton objects, not subclass definitions.

2. **ERROR fixed**: InteractiveResolver hierarchy — moved it under `ProxyResolver` in the class
   hierarchy diagram rather than showing it as a peer of ProxyResolver.

3. **ERROR fixed**: `getDefaultObject()` signature — corrected to 1 parameter, not 2. The prior
   text showed an extra parameter that does not exist in the source.

4. **ERROR fixed**: `objInScope()` attribution — moved from the Action method table to the
   Resolver method table, where it is actually defined (resolver.t).

Combined with the 7 fixes from the prior session, parser-pipeline.md received a total of 11 fixes
covering 3 errors and 7 inaccuracies (plus 1 minor from the prior session).

### action-resolution.md — Full Assessment and Fix Pass

3 errors, 5 inaccuracies, and 4 minor issues fixed:

**Errors**:
1. `GlobalRemapping.getRemapping()` — fixed parameter order in the signature table.
2. `GlobalRemapping.getRemapping()` return format — corrected the described return value format.
3. Before/Check ordering — corrected the description of default action sequencing (Before runs
   before Check, not after).

**Inaccuracies**:
1. `actorAction` missing — added it to the action processing phase table where it belongs.
2. `TopicResolver` scope — corrected the description of what objects are in scope for topic
   resolution.
3. `ResolvedTopic` three-tier attribution — corrected which tier each piece of logic belongs to.
4. `withParserGlobals` scope — fixed the description of what globals it manages.
5. One additional inaccuracy in the noun phrase resolution flow description.

**Minor**: 4 prose precision fixes.

### sense-perception.md — Full Assessment and Fix Pass

2 errors, 4 inaccuracies, and 4 minor issues fixed:

**Errors**:
1. `adventium` scope — corrected that `adventium` is only the default material for
   `BasicContainer`, not for every `Thing` in the library. The document had stated it was the
   universal default, which is wrong.
2. `Room` brightness — corrected to `brightness = 3`, not `4`. Rooms are lit but not a light
   source; brightness 4 is reserved for actual light sources.

**Inaccuracies**:
1. ~500x attribution — corrected which class or method is responsible for the ~500x brightness
   attenuation described in the light model.
2. `BasicContainer` vs `Container` — two separate places where the wrong class was named when
   describing default material assignment.
3. Two additional inaccuracies in the sense path and transparency chain descriptions.

**Minor**: 4 prose precision fixes.

### containment-model.md — Full Assessment and Fix Pass

1 error, 3 inaccuracies, and 4 minor issues fixed:

**Errors**:
1. Fabricated `contentsReachable` property — removed this property from a code example entirely.
   The property does not exist in the adv3 library source; it was hallucinated in the original
   document.

**Inaccuracies**:
1. `objClosed` class attribution — corrected which class defines this property.
2. `tryImplicitRemoveObstructor` class attribution — corrected which class defines this method.
3. `touchObj` line reference — corrected the source file and line reference used in prose.

**Minor**: 4 prose precision fixes.

### message-system.md — Full Assessment and Fix Pass

1 error, 4 inaccuracies, and 7+ minor issues fixed:

**Errors**:
1. `resolveMessageText()` as a standalone function — corrected to describe it as a method of
   `MessageResult`, not a free function.

**Inaccuracies**:
1. `langMessageBuilder` instance — corrected description from "subclass" to "singleton instance".
   The library instantiates one `MessageBuilder` object; it does not subclass it.
2. `tSel`, `withPresent`, `withPast` — corrected from "functions" to "macros" throughout.
   These are preprocessor macros defined in `adv3.h`, not runtime functions.
3. `okayTakeMsg` — corrected to `shortTMsg` format annotation, not the format claimed.
4. Spatial preposition outputs — corrected the described output strings for several containment
   prepositions.

**Minor**: 7+ prose precision and terminology fixes.

### Build Verification and Commit

`mkdocs build` run after all fixes; no broken links or formatting errors. All five corrected
documents committed together as `c6442dc` with message "Fix source-verified accuracy issues
across all five architecture deep-dives". Pushed to main.

## Key Decisions

### 1. Parallel Fix Execution for Documents 2-5
The four documents (action-resolution, sense-perception, containment-model, message-system) were
assessed and fixed in parallel using background subagents. Each agent was given the document, the
relevant source files, and the structured assessment findings from the prior session. This
compressed what might have been 4+ sequential passes into a single round.

### 2. Single Commit for All Five Fixes
Rather than committing each document separately, all five corrected files were staged and
committed together. This keeps the fix pass as a single atomic unit in the git history, making it
easier to identify and review as a set.

### 3. Verification Against Source as Ground Truth
All fixes were verified against actual source code in `tads-sources/tads3/lib/adv3/` before
being applied. No fix was made on the basis of general knowledge alone. Where source was
ambiguous, the document was updated to reflect that ambiguity rather than asserting a specific
value.

## Open Items

### Short Term
- Consider a systematic grep pass across all architecture documents to catch any remaining
  fabricated property or method names not caught by the assessment agents.
- The Phase 6 architecture documentation is now complete and verified. No further deep-dive
  documents are planned.

### Long Term
- Establish a source-verification lint step (grep for method/property names against source)
  before future AI-generated documentation is committed.
- The singleton-vs-subclass confusion that appeared in multiple documents is a systematic LLM
  failure mode for TADS 3. Future documents should have an explicit checklist item for this
  pattern.

## Files Modified

**Architecture deep-dives — all fixes applied and committed** (5 files):
- `docs/docs/architecture/parser-pipeline.md` — 4 remaining fixes from prior session applied
- `docs/docs/architecture/action-resolution.md` — 3 errors, 5 inaccuracies, 4 minor fixed
- `docs/docs/architecture/sense-perception.md` — 2 errors, 4 inaccuracies, 4 minor fixed
- `docs/docs/architecture/containment-model.md` — 1 error, 3 inaccuracies, 4 minor fixed
- `docs/docs/architecture/message-system.md` — 1 error, 4 inaccuracies, 7+ minor fixed

## Architectural Notes

Across the full accuracy review (both sessions), the pattern of errors was consistent:

**Singleton vs. subclass**: TADS 3 uses the singleton object pattern heavily. Many classes
(Distinguisher variants, MessageBuilder, Resolver variants) are instantiated once and used as
singleton objects. AI-generated documentation systematically described these as subclass
relationships rather than instance relationships. This affects every document in the set.

**Fabricated properties**: One fully fabricated property (`contentsReachable`) was found. This is
the most dangerous error type because it looks plausible in a code example and would cause a
programmer to write broken code. The source-verification standard caught it.

**Method signatures**: Parameter order and type descriptions were a frequent minor error source,
particularly for multi-parameter methods. These are consequential for users who need to override
or call these methods.

**Macro vs. function**: Preprocessor macros defined in `adv3.h` (e.g., `tSel`, `withPresent`,
`withPast`, `shortTMsg`) were repeatedly described as functions. These are distinct in TADS 3
because they expand at compile time and cannot be called indirectly.

**High overall accuracy**: Despite these issues, 200+ verified-correct claims were found across
the six documents. The documents are structurally sound and accurate in broad strokes; the errors
are targeted and surgical, not pervasive.

## Notes

**Session duration**: ~2 hours

**Approach**: Continuation of prior session. Assessment findings were already complete; this
session was exclusively a fix pass using those findings as a work queue.

**Commits**:
- `ee0ea1d` — event-scheduling.md fixes (prior session)
- `c6442dc` — all five remaining document fixes (this session)

**Phase 6 status**: All six architecture deep-dive documents are now written, reviewed, and
source-verified. Phase 6 is complete.

---

**Progressive update**: Session completed 2026-02-21 21:30
