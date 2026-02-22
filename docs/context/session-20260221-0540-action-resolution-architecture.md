# Session Summary: 2026-02-21 - action-resolution-architecture

## Status: Completed

## Goals
- Create the second deep-dive architecture document: Action Resolution
- Document how parsed actions become world-state changes in TADS 3
- Integrate the new document into the mkdocs site navigation and cross-reference network

## Completed

### Action Resolution Deep-Dive (`docs/docs/architecture/action-resolution.md`)

Created a comprehensive 9-section deep-dive document covering the full action resolution pipeline, following the template established by `parser-pipeline.md`.

**Document Sections:**

1. **Action Resolution Overview** — ASCII pipeline diagram from winning parse tree through after-action notifications. Stage-to-source-file mapping table (action.t, verify.t, precond.t, resolver.t, adv3.h). Key design principle: handlers live on objects, not on actions.

2. **The Action Class Hierarchy (action.t)** — ASCII class tree: Action → IAction, TAction → TIAction, plus LiteralAction, TopicAction, ConvIAction and their mixins. Table mapping each action type to its object slots and resolution behavior. Documents the non-obvious insight that TAction inherits from both Action and Resolver — it IS its own dobj resolver.

3. **Scope — Who Can See What** — How scope is built from the actor's sensory environment. Physical scope vs. global scope (topics). How actions override scope via `objInScope()`. Forward reference to the future Sense/Perception deep-dive.

4. **The Execution Cycle (doActionOnce())** — The full 10-step execution sequence: checkRemapping → implicit check → verify (pass 1) → preconditions (pass 1) → verify (pass 2) → preconditions (pass 2, no implicit) → check → beforeAction → action → afterAction. Explains the two-pass design as infinite-loop prevention. Object iteration patterns for IAction, TAction, and TIAction. Current-object globals table (gActor, gAction, gDobj, gIobj, etc.).

5. **Verification (verify.t)** — VerifyResult class hierarchy (ASCII tree) with all 8 result classes. Table with resultRank, allowAction, allowImplicit, and when-to-use for each. Quotes the key source comment verbatim: "the purpose of verification results is to guess what's in the player's mind, not to reflect the full internal state of the game." Covers the LogicalVerifyResult likelihood mechanism and the dual use of verify for disambiguation and validation.

6. **Preconditions (precond.t)** — PreCondition interface (`verifyPreCondition` + `checkPreCondition`). Table of all 16 built-in preconditions with what they check and what implicit action they trigger. The implicit action loop pattern. Precondition ordering via `preCondOrder`.

7. **Remapping** — Three levels: GlobalRemapping (action-level, before resolution), `remapTo` (object-level, after resolution), `asDobjFor`/`asIobjFor` (handler reuse). Code examples for each. Comparison table showing when each runs, what it changes, and use cases.

8. **Topic Resolution and ResolvedTopic** — How topic actions differ (global scope, three-tier classification, no disambiguation). ResolvedTopic structure table (inScopeList, likelyList, otherList, topicProd, resInfoTab).

9. **Practical Intervention Points** — 5 lookup tables organized by authoring goal: controlling which objects get chosen, adding/customizing preconditions, redirecting actions, customizing scope, intercepting before/after execution.

### Navigation and Cross-Reference Integration

- **`docs/docs/architecture/index.md`** — Added Action Resolution entry between Parser Pipeline and IF Development Guide with 2-sentence description
- **`docs/mkdocs.yml`** — Added nav entry `Action Resolution: architecture/action-resolution.md` after Parser Pipeline
- **`docs/docs/architecture/overview.md`** — Added cross-reference "For the architecture of steps 6–9 (action resolution), see Action Resolution" alongside the existing parser-pipeline link (at line 433)
- **`docs/docs/architecture/parser-pipeline.md`** — Updated footer to include forward link to action-resolution.md

### Build Verification

Zero new warnings. All pre-existing warnings unchanged. Build completed in approximately 38 seconds.

## Key Decisions

### 1. TAction-as-Resolver Documented as Primary Architectural Insight
TAction's dual inheritance (Action + Resolver) is non-obvious from the class name. This has major practical implications: when authors override dobj resolution behavior, they are overriding methods on TAction itself, not on a separate resolver object. Calling this out explicitly prevents confusion for authors who expect a separate resolver class.

### 2. Two-Pass Verify/Precondition Loop Explained as Safety Bound
The 10-step execution cycle runs verify and preconditions twice. The document explains this as an infinite-loop prevention mechanism: the second precondition pass disallows further implicit actions. This is critical for understanding why some implicit action chains stop unexpectedly.

### 3. Three-Level Remapping Compared in a Single Table
GlobalRemapping, `remapTo`, and `asDobjFor`/`asIobjFor` serve different purposes at different pipeline stages and are often confused. Documenting all three together with a unified comparison table (when it runs, what it changes, use cases) makes the distinction concrete.

### 4. Verbatim Source Quote for Verify Philosophy
The comment in verify.t — "the purpose of verification results is to guess what's in the player's mind, not to reflect the full internal state of the game" — is the single most important design principle in the action system. Quoting it directly rather than paraphrasing preserves its authority and gives authors the right mental model for when to use which result class.

### 5. Practical Intervention Tables Consolidated at End
Following the parser-pipeline.md template, all "how do I do X" lookup content is grouped into a single final section rather than scattered through the reference sections. This makes the document useful both as a top-to-bottom read and as a reference.

## Open Items

### Short Term
- No outstanding items from this session

### Long Term (Remaining Deep-Dive Architecture Documents)
The architecture section now has 6 documents. Four more deep-dives are planned per the project plan:

1. **Sense and Perception System** — Material transparency, the four senses, sight/sound/smell/touch propagation through containment hierarchies
2. **Containment Model** — Thing hierarchy, scope, reachability, bulk and weight
3. **Message System** — Parameter substitutions, msg_neu.t, message customization patterns
4. **Event Scheduling** — Schedulable, Daemon, Fuse, turn ordering, the realTime scheduler

## Files Modified

**New document** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/action-resolution.md` — Full deep-dive document, ~9 major sections

**Updated navigation and cross-references** (4 files):
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — Added Action Resolution entry
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — Added cross-reference link at line 433
- `/Users/david/repos/tads3/docs/docs/architecture/parser-pipeline.md` — Updated footer with forward link
- `/Users/david/repos/tads3/docs/mkdocs.yml` — Added nav entry

## Architectural Notes

The action-resolution document follows the template established by parser-pipeline.md:
1. Overview diagram + stage-to-file mapping table
2. Per-stage sections: concept explanation, key class/method reference table, process walkthrough
3. Practical intervention points consolidated at the end as lookup tables

This template is working well and should be maintained for the remaining four deep-dive documents.

**Architecture section document count: 6** (was 5 before this session):
- `overview.md`
- `parser-pipeline.md`
- `action-resolution.md` (new this session)
- `design-patterns.md`
- `development-guide.md`
- `quick-reference.md`

**Source files referenced in the document:**
- `action.t` — Action class hierarchy and doActionOnce() execution cycle
- `verify.t` — VerifyResult class hierarchy and result rank constants
- `precond.t` — PreCondition interface and all 16 built-in preconditions
- `resolver.t` — Resolver base class (inherited by TAction)
- `adv3.h` — Global macros (gActor, gAction, gDobj, gIobj, etc.)

## Notes

**Session duration**: ~15-20 minutes

**Approach**: Source-driven documentation — read the actual TADS 3 library source files (action.t, verify.t, precond.t, resolver.t) to extract accurate class hierarchies, method signatures, and design comments, then organized into the established deep-dive template with authoring-focused intervention tables.

---

**Progressive update**: Session completed 2026-02-21 05:40
