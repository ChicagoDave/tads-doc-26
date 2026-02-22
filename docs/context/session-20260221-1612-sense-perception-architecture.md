# Session Summary: 2026-02-21 - sense-perception-architecture

## Status: Completed

## Goals
- Write the third deep-dive architecture document: Sense and Perception System
- Integrate it into navigation and cross-reference it from existing documents
- Verify clean build with no new warnings

## Completed

### New document: sense-perception.md
Created `/Users/david/repos/tads3/docs/docs/architecture/sense-perception.md`, a comprehensive
9-section deep-dive following the template established by parser-pipeline.md and
action-resolution.md.

**Sections:**

1. **Sense System Overview** — ASCII diagram of four design layers (Materials → Path Calculation
   → SenseInfo Assembly → Consumers). Source-file-to-role mapping table. Cache-and-query
   architecture as the primary design principle.

2. **Materials and Transparency (sense.t)** — Material class property-pointer dispatch pattern.
   Five built-in materials table (adventium, paper, glass, fineMesh, coarseMesh). Transparency
   arithmetic: five levels, transparencyAdd() collapse rule, transparencyCompare() ordering,
   adjustBrightness().

3. **The Four Senses (sense.t)** — Property-pointer anatomy table
   (thruProp/sizeProp/presenceProp/ambienceProp × 4 senses). Sight special: ambient energy
   (brightness levels 0-4, level 1 self-illumination boundary). Touch special: no distance
   sensing, excluded from scopeSenses. Size × transparency sensibility matrix. Presence vs
   sensibility distinction.

4. **Sense Path Calculation (thing.t)** — Core section. ASCII diagram of the three-step
   senseInfoTable() algorithm: connectionTable() → cacheAmbientInfo() → cacheSensePath() →
   build SenseInfo table. Four directional methods table. Scratch-pad properties table. Key
   insights: cache-and-query, best-path-wins, at most one obstructor per non-opaque path.

5. **Fill Media and Asymmetric Containers** — FillMedium class, consecutive-traversal rule.
   transSensingIn() vs transSensingOut() for asymmetric containers. Container open/closed
   behavior.

6. **Sense Connectors and Occluders** — SenseConnector (MultiLoc bridge between rooms),
   DistanceConnector (distant transparency), Occluder (selective post-calculation blocking,
   global within a room).

7. **Sensory Emanations (objects.t)** — Class tree: Intangible → SensoryEmanation → Noise/Odor
   with Simple variants. Key properties. Display scheduling for edge sensitivity.

8. **How Senses Drive Scope** — Chain from Actor.scopeList() → scopeSenses →
   sensePresenceList() → senseInfoTable(). Key insight: scope is multi-sensory, not just visual.

9. **Practical Intervention Points** — Five lookup tables: controlling what can be sensed,
   custom sense connectors, custom sensory objects, lighting and darkness, debugging sense paths.

### Navigation and cross-reference integration
Updated four files to integrate the new document:

- `docs/docs/architecture/index.md` — Added Sense and Perception entry between Action
  Resolution and IF Development Guide
- `docs/mkdocs.yml` — Added nav entry after Action Resolution
- `docs/docs/architecture/overview.md` — Added cross-reference to sense-perception.md in The
  Sensory Model section
- `docs/docs/architecture/action-resolution.md` — Updated forward reference at line 147 from
  "future document" placeholder to actual link; updated footer to include forward link to
  sense-perception.md

### Build verification
Zero new warnings introduced. All pre-existing warnings unchanged. Build completed in ~38
seconds.

## Key Decisions

### 1. Cache-and-query as primary architectural insight
The sense system's performance strategy — expensive path tracing done once, results cached on
scratch-pad properties, consumers just look up results — is documented first and returned to
throughout the document. Understanding this pattern is the prerequisite for everything else.

### 2. transparencyAdd() collapse rule highlighted
Two non-transparent levels always produce opaque, meaning at most one obstructor can appear in
any non-opaque sense path. This has major practical implications: a stack of containers can
only ever block sense once. Called out explicitly as a key insight in Section 4.

### 3. Brightness level 1 boundary explicitly documented
The self-illumination threshold (level 1 = object is visible but does not illuminate its
surroundings) is non-obvious. It determines whether an object in a dark room can be seen vs
whether it lights up the room. Critical for lighting design.

### 4. Property-pointer indirection as extensibility mechanism
Documented that the four-sense architecture uses property pointers so that adding a new sense
requires no algorithm changes — only new property pointers. This is the key extensibility
story.

### 5. Fixed nav bar anchor format for em dash stripping
Discovered that mkdocs strips em dashes (—) to single hyphens in generated HTML anchors, not
double hyphens. All section nav bar anchors were written with the correct single-hyphen format,
avoiding the pre-existing anchor-mismatch warning pattern seen in other deep-dive documents.

## Open Items

### Short Term
- Containment Model deep-dive (4 of 6): Thing hierarchy, scope, reachability, bulk and weight
- Message System deep-dive (5 of 6): Parameter substitutions, msg_neu.t, message customization
- Event Scheduling deep-dive (6 of 6): Schedulable, Daemon, Fuse, turn ordering

### Long Term
- Once all six deep-dives are complete, review the architecture/index.md for coherence as a
  reading guide
- Consider a cross-cutting "how the systems interact" summary document

## Files Modified

**New** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/sense-perception.md` — Full 9-section
  deep-dive on the sense and perception system

**Updated** (4 files):
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — Added Sense and Perception
  entry
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — Added cross-reference in
  Sensory Model section
- `/Users/david/repos/tads3/docs/docs/architecture/action-resolution.md` — Replaced forward
  reference placeholder with actual link; added footer forward link
- `/Users/david/repos/tads3/docs/mkdocs.yml` — Added nav entry for sense-perception.md

## Architectural Notes

The sense system is architecturally the most self-contained of the deep-dives so far. It has a
clean layered structure (Material → path calculation → SenseInfo assembly → consumers) that
maps almost directly onto the source files (sense.t, thing.t, objects.t, actor.t). The main
non-obvious aspect is the caching strategy: senseInfoTable() is expensive and called frequently
during turn processing, so results are written to scratch-pad properties on each object and
read back by all consumers in that same turn. This means the table is stale across turns, which
is intentional and correct.

The touch sense being excluded from scopeSenses (and thus from scope determination) is a
design choice worth remembering: you can reach into a container you cannot see or hear into,
but touch does not determine whether an object is in scope for action targeting purposes.

Source files referenced during research:
- `sense.t` — Material, Sense, transparency math, SenseConnector, Occluder, DistanceConnector
- `thing.t` — SenseInfo, senseInfoTable(), path calculation, brightness propagation, scratch-pads
- `objects.t` — Container.transSensingIn(), FillMedium, Intangible, SensoryEmanation, Noise, Odor
- `adv3.h` — Transparency and size enums
- `actor.t` — scopeSenses, scopeList(), sensePresenceList()

## Notes

**Session duration**: ~1.5 hours

**Approach**: Same methodology as parser-pipeline.md and action-resolution.md — read source
files directly, identify the core algorithm and its data structures, build up sections from
primitives to composites, write practical intervention points as the final section.

**Architecture doc count**: 7 documents total in the architecture section (index, overview,
parser-pipeline, action-resolution, sense-perception, IF development guide, and the placeholder
entries). 3 of the 6 planned deep-dives are complete.

---

**Progressive update**: Session completed 2026-02-21 16:12
