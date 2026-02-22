# Session Summary: 2026-02-21 - Parser Pipeline Architecture Document

## Status: Completed

## Goals
- Create the first deep-dive architecture document: The Parser Pipeline
- Update the architecture section index, site nav, and overview cross-references
- Establish the pattern for the remaining 5 planned deep-dive documents

---

## Completed

### Parser Pipeline Deep-Dive (`docs/docs/architecture/parser-pipeline.md`, 432 lines)

A comprehensive architecture document covering the TADS 3 parser pipeline across four source files. All sections verified to build with zero warnings.

**Document Structure:**

**Pipeline Overview**
- ASCII data flow diagram showing the full pipeline sequence
- Stage-to-source-file mapping table (6 stages, 4 files: exec.t, parser.t, resolver.t, disambig.t)

**Entry Points (exec.t)**
- `executeCommand()` vs `executeAction()` separation with design rationale
- Control flow signals table — 7 signals (TerminateCommandException, ExitActionSignal, ExitSignal, AbortActionSignal, RetryCommandException, RemapActionSignal, ReplacementCommandStringException) with trigger context and effect

**Grammar Matching (parser.t)**
- `BasicProd` class hierarchy tree showing the full production class inheritance
- Key insight documented: Actions ARE grammar productions (Actions inherit from `BasicProd`)
- VerbRules and the `badness` mechanism for ranking ambiguous parses
- How `resolveNouns()` is called on the winning production

**Command Ranking**
- `CommandRanking` extends `ResolveResults` pattern — tentative resolution used purely for scoring
- Two-pass comparison system (primary criteria, then tiebreakers)
- Full 22-criterion ranking priority table with criterion name, what it favors, and the reason

**Noun Resolution (resolver.t)**
- Resolver strategy pattern — different resolver classes for different grammatical roles
- Resolver class hierarchy (5 classes: BasicResolver, ActorResolver, DefaultResolver, TentativeResolver, DisambigResolver)
- Key methods table (6 methods: matchObject, filterAmbiguous, uniquelyIdentifies, getAll, getReflexive, getPossessive)
- 6-step resolution process walkthrough with method calls at each step
- `ResolveInfo` data structure fields documented
- Pronoun resolution lifecycle (first pass stores referents, second pass restores them)

**Disambiguation (disambig.t)**
- Distinguisher hierarchy — 5 distinguishers (BasicDistinguisher, NameDistinguisher, StateDistinguisher, LocationDistinguisher, PossessiveDistinguisher)
- 3 key methods per distinguisher (canDistinguish, isDistinguishable, getDistinguishingDesc)
- Iterative disambiguation loop with the "ask only once per round" rule
- Exception types (CancelCommandLineException, RetrySingleObjectException)

**Practical Intervention Points**
- 4 tables organized by pipeline stage:
  1. Before parsing — hooks for preprocessing raw input
  2. Grammar matching — VerbRule modification and badness manipulation
  3. Noun resolution — Resolver override points
  4. Action selection — doBeforeAction/doAfterAction and action remapping
- Each table row includes: hook/mechanism, override point, and use case example

### Architecture Index Update (`docs/docs/architecture/index.md`)

Added Parser Pipeline entry between Overview and Design Patterns with a 2-sentence description summarizing the four-source-file scope and the practical intervention table.

### Site Nav Update (`docs/mkdocs.yml`)

Added nav entry:
```yaml
- Parser Pipeline: architecture/parser-pipeline.md
```

### Overview Cross-Reference (`docs/docs/architecture/overview.md`)

Added cross-reference link to `parser-pipeline.md` in the turn cycle section, guiding readers from the high-level overview into the deep-dive.

### Build Verification

Zero new warnings. All cross-links between architecture documents verified functional.

---

## Key Decisions

### 1. Actions Inherit from BasicProd — Documented as a Key Insight
The fact that TADS 3 actions are themselves grammar productions (not separate objects that grammar maps to) is a non-obvious architectural choice with significant implications for how grammar is extended. This is called out explicitly in its own subsection rather than buried in prose.

### 2. 22-Criterion Ranking Table as Primary Reference Artifact
The CommandRanking criteria are scattered across the source in a long comparison method. Extracting all 22 into a single prioritized table is the primary value of that section — it gives authors a single place to understand why one parse wins over another.

### 3. Practical Intervention Points as a Separate Top-Level Section
Rather than scattering "how to override this" notes throughout the explanatory sections, all intervention points are consolidated at the end in stage-organized tables. This matches the quick-reference pattern established elsewhere in the docs: explanation first, then practical lookup table.

### 4. Resolver Strategy Pattern Highlighted
The strategy pattern (different Resolver subclasses for dobj, iobj, actor roles) is documented explicitly because it is the primary extension point authors need when writing unusual verb behavior. Naming the pattern helps authors recognize what they are looking at when reading source.

---

## Open Items

### Short Term
- No outstanding items from this session — document is complete and building cleanly

### Long Term (Remaining Deep-Dive Architecture Documents)
The architecture section now has 5 documents. Five more deep-dives are planned per the original architecture plan:

1. **Action Resolution** — noun phrases to objects, scope checking, verify/check/action method chain
2. **Sense and Perception System** — Material transparency, the four senses, sight/sound/smell/touch propagation
3. **Containment Model** — Thing hierarchy, scope, reachability, bulk and weight
4. **Message System** — parameter substitutions, msg_neu.t, message customization patterns
5. **Event Scheduling** — Schedulable, Daemon, Fuse, turn ordering, the realTime scheduler

---

## Files Modified

**Architecture documentation** (4 files):
- `/Users/david/repos/tads3/docs/docs/architecture/parser-pipeline.md` — new 432-line deep-dive document
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — added Parser Pipeline entry with description
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — added cross-reference link in turn cycle section
- `/Users/david/repos/tads3/docs/mkdocs.yml` — added Parser Pipeline nav entry

---

## Architectural Notes

The parser-pipeline document establishes the template for future deep-dive documents:
1. Overview diagram + stage-to-file mapping table
2. Per-stage sections: concept explanation, key class/method reference table, process walkthrough
3. Practical intervention points consolidated at the end as lookup tables

This structure separates "understanding what exists" (sections 1-2) from "knowing how to change it" (section 3), matching how TADS 3 authors actually use reference documentation.

The TADS 3 parser's four-file structure (exec.t, parser.t, resolver.t, disambig.t) maps cleanly onto the conceptual pipeline stages, which makes the architecture document naturally follow the source organization. Future deep-dives (e.g., Sense/Perception across sense.t and thing.t) may need more explicit mapping tables to bridge the conceptual and source-file views.

---

## Notes

**Session duration**: ~30 minutes

**Approach**: Source-reading of exec.t, parser.t, resolver.t, and disambig.t to extract architecture, followed by structured documentation. Build verification after each file change.

**Architecture section document count**: 5 (was 4)
- `overview.md`
- `parser-pipeline.md` (new)
- `design-patterns.md`
- `development-guide.md`
- `quick-reference.md`

---

**Progressive update**: Session completed 2026-02-21 05:25
