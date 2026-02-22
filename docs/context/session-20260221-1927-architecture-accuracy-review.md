# Session Summary: 2026-02-21 - architecture-accuracy-review

## Status: Interrupted (Fixes Partially Applied)

## Goals
- Assess all 6 architecture deep-dive documents for technical accuracy against actual TADS 3 source code
- Fix all errors, inaccuracies, and minor issues found
- Commit and push corrected documents

## Completed

### Event Scheduling Deep-Dive Assessment and Fixes
Verified every claim in `docs/docs/architecture/event-scheduling.md` against source files in
`tads-sources/tads3/lib/adv3/` (events.t, actor.t, misc.t, input.t, adv3.h).

Five issues found and fixed:

1. **ERROR**: Removed incorrect `adv3.h` row from source file table; moved `EventAction`
   attribution to `events.t` where it is actually defined.

2. **INACCURACY**: Rewrote RealTimeDaemon drift prevention description. Added `!!! note` callout
   about the reversed comparison operator in the source (events.t:1270) — the condition uses `<=`
   where `>=` would be the more intuitive expression.

3. **MINOR**: Separated exception handling into two levels: `runScheduler` anti-starvation guard
   versus `executeList` event removal on exception.

4. **MINOR**: Completed the algorithm step 6 exception list by adding `RestartSignal`,
   `ExitSignal`, `ExitActionSignal`, and the catch-all `Exception`.

5. **MINOR**: Fixed `executeTurn()` return value prose to accurately describe the while-loop
   behavior.

Committed as `ee0ea1d` and pushed to main.

### Assessment of All 5 Remaining Deep-Dives
Five parallel assessment agents verified each remaining document against TADS 3 source code.

| Document | Errors | Inaccuracies | Minor | Verified Correct |
|---|:---:|:---:|:---:|:---:|
| parser-pipeline.md | 3 | 7 | 6 | 40+ |
| action-resolution.md | 3 | 5 | 4 | 35+ |
| sense-perception.md | 1 | 4 | 4 | 38 |
| containment-model.md | 1 | 3 | 4 | 55+ |
| message-system.md | 1 | 4 | 7 | 35+ |
| **Totals** | **9** | **23** | **25** | **200+** |

Key errors found across documents:

- **parser-pipeline.md**: Distinguisher instances shown as subclasses; InteractiveResolver
  hierarchy wrong; `getDefaultObject()` signature wrong; `objInScope()` shown on Action rather
  than Resolver.
- **action-resolution.md**: `GlobalRemapping.getRemapping()` parameter order wrong; return format
  wrong; default Check vs Before ordering wrong.
- **sense-perception.md**: `adventium` claimed as default material for every object (only
  BasicContainer uses it as default).
- **containment-model.md**: Fabricated property `contentsReachable` in code example.
- **message-system.md**: `resolveMessageText()` described as standalone function (it is a method
  of MessageResult).

### Partial Fixes Applied to parser-pipeline.md
Seven of approximately thirteen fixes were applied before the session was interrupted:

1. Fixed action filtering source attribution (parser.t, not exec.t)
2. Fixed GlobalRemapping entry point (findGlobalRemapping, not getRemapping)
3. Fixed `executeCommand()` to mention both commandPhrase alternatives
4. Fixed ExitSignal description (toned down "abort the entire turn")
5. Fixed AbortImplicitSignal attribution (implicit action system, not verify handlers)
6. Fixed FirstCommandProd hierarchy (child of CommandProd, not sibling)
7. Fixed Action class hierarchy (showed IAction/TAction with Resolver, LiteralActionBase/TopicActionBase mixins)

## Key Decisions

### 1. Source-Grounded Accuracy Standard
Every claim in the architecture documents was verified against actual TADS 3 library source code
in `tads-sources/tads3/lib/adv3/`. Where the document described behavior that could not be
confirmed in source, it was flagged as an error regardless of how plausible the description
seemed. This is the appropriate standard for reference documentation.

### 2. Parallel Assessment Approach
The five remaining documents were assessed simultaneously using parallel subagents, each given
one document and the relevant source files. This produced consistent, structured findings in the
format: ERROR / INACCURACY / MINOR / VERIFIED CORRECT, making the subsequent fix pass
straightforward.

### 3. Errors vs Inaccuracies vs Minor
- **ERROR**: Factually wrong, could cause a programmer to write incorrect code.
- **INACCURACY**: Misleading or imprecise, but doesn't directly produce wrong code.
- **MINOR**: Prose imprecision, incomplete enumeration, or style issue.

## Open Items

### Immediate (next session)
- Complete remaining parser-pipeline.md fixes (6 items):
  - Distinguisher: change "subclasses" to "singleton instances" throughout
  - InteractiveResolver: show it under ProxyResolver in the hierarchy, not as a peer
  - `getDefaultObject()` signature: correct parameter list
  - `objInScope()`: move from Action to Resolver in the method tables
  - TAction: show it inherits Resolver in the class hierarchy diagram
  - Any additional minor prose items from the assessment report

- Apply all fixes to action-resolution.md (3 errors, 5 inaccuracies, 4 minor)
- Apply all fixes to sense-perception.md (1 error, 4 inaccuracies, 4 minor)
- Apply all fixes to containment-model.md (1 error, 3 inaccuracies, 4 minor)
- Apply all fixes to message-system.md (1 error, 4 inaccuracies, 7 minor)

### After All Fixes
- Run `mkdocs build` to verify no broken links or formatting errors
- Commit all 5 fixed documents together with a single descriptive commit message
- Push to main

### Long Term
- Consider a systematic lint pass: grep for fabricated method names and verify each one exists in
  source before each future commit.

## Files Modified

**Architecture deep-dives** (1 committed, 1 partially modified):
- `docs/docs/architecture/event-scheduling.md` — 5 fixes applied, committed as ee0ea1d, pushed
- `docs/docs/architecture/parser-pipeline.md` — 7 of ~13 fixes applied, NOT yet committed

**Architecture deep-dives pending fixes** (not yet touched):
- `docs/docs/architecture/action-resolution.md`
- `docs/docs/architecture/sense-perception.md`
- `docs/docs/architecture/containment-model.md`
- `docs/docs/architecture/message-system.md`

## Architectural Notes

The assessment revealed a consistent pattern: the original AI-generated deep-dives were accurate
in broad strokes (class names, method names, general flow) but had systemic issues in two areas:

1. **Class hierarchy details**: Subclass vs. singleton instance distinctions were frequently
   wrong. TADS 3 uses the singleton object pattern heavily (e.g., Distinguisher subclasses are
   actually singleton instances of those classes). The documents consistently described these as
   subclass relationships.

2. **Method signatures**: Parameter order and types were often slightly wrong, particularly for
   methods with three or more parameters. These errors are the most dangerous for users trying to
   override or call these methods.

The high verified-correct count (200+) confirms the documents are valuable and worth fixing
rather than rewriting. The corrections are targeted and surgical.

## Notes

**Session duration**: ~3 hours

**Approach**: Assessment-first, then fixes. Each document was fully assessed before any edits
were made. This produced a complete picture of work remaining and allowed efficient parallel
assessment.

**Commit**: ee0ea1d (event-scheduling.md fixes only; parser-pipeline.md changes are unstaged)

---

**Progressive update**: Session interrupted 2026-02-21 19:27
