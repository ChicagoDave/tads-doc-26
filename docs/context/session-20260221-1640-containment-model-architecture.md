# Session Summary: 2026-02-21 - containment-model-architecture

## Status: Completed

## Goals
- Create the fourth of six planned deep-dive architecture documents: the Containment Model
- Integrate the new document into navigation, the architecture index, the overview, and the footers of adjacent deep-dives
- Verify zero build warnings

## Completed

### New Document: containment-model.md
Created `/Users/david/repos/tads3/docs/docs/architecture/containment-model.md`, a comprehensive 10-section deep-dive following the template established by parser-pipeline.md, action-resolution.md, and sense-perception.md.

**Section breakdown:**

1. **Containment Model Overview** — ASCII diagram of five design layers (Tree, Container Types, Reachability, Capacity, Nested Rooms). Source-file-to-role mapping table covering thing.t, objects.t, extras.t, travel.t, precond.t, actor.t.

2. **The Containment Tree** — location/contents as a single-parent tree; Rooms as roots (isTopLevel); the `+` syntax and `@location` template; containment query methods (isIn, isDirectlyIn, isHeldBy, isNominallyIn, getCommonContainer); special semantics of isIn(nil).

3. **Moving Objects** — Four layers of moveInto: baseMoveInto → mainMoveInto → moveIntoForTravel → moveInto. Notification chain: sendNotifyRemove up old tree, sendNotifyInsert down new tree (outside-in order), notifyMoveInto on the object. Verify-phase variant for circular containment. Containment paths: PathIn/PathOut/PathPeer/PathThrough enums, getAllPathsTo, selectPathTo, traversePath.

4. **The Container Hierarchy** — Class tree from BulkLimiter through Container/Surface/SpaceOverlay. BulkLimiter capacity enforcement with whatIf. BasicContainer enclosure boundary (isOpen, material, transSensingIn/Out, checkMoveViaPath, checkTouchViaPath, fillMedium). Container vs Surface design distinction. OpenableContainer with implicit-open support. LockableContainer. RestrictedContainer with canPutIn. SingleContainer with objEmpty precondition.

5. **Spatial Relationships** — SpaceOverlay with abandon-on-move behavior. Underside, RearContainer, RearSurface. ComplexContainer with secret sub-objects (ComplexComponent), command remapping to sub-containers, subLocation property for initial placement.

6. **Reachability** — Touch path algorithm: touchObj precondition gets containment path, walks it calling checkTouchViaPath at each boundary, identifies obstructors, tries implicit removal (e.g., implicit OPEN). preCondOrder 200 (runs last). Verify-phase disambiguation adjustments. OutOfReach mixin for directional reach control.

7. **Bulk and Weight** — getBulk (external only) vs getWeight (recursive), getBulkWithin, getEncumberingBulk (0 if worn). StretchyContainer exception. whatIf speculative testing. Actor carrying capacity with editorial note about inventory limits. BagOfHolding algorithm with affinity scoring and most-recent-item protection.

8. **Nested Rooms and Staging** — NestedRoom as travelWithin (not travelTo). Concrete subclasses table (BasicChair/Chair/BasicBed/Bed/BasicPlatform/Platform/Booth/Vehicle) with postures and drop destinations. Staging location algorithm. HighNestedRoom. isStagingLocationKnown for puzzles. Room/NestedRoom extra scope items.

9. **Multi-Location Objects** — MultiLoc (one object, many locations), MultiInstance (separate copies), MultiFaceted (facets with pronoun tracking). Movement methods: moveIntoAdd, moveOutOf.

10. **Practical Intervention Points** — Six lookup tables covering: controlling containment, controlling capacity, controlling reachability, controlling open/close and lock/unlock, controlling nested rooms, controlling multi-location objects.

### Navigation and Cross-Reference Integration
Updated five existing files to integrate the new document:

- `docs/mkdocs.yml` — Added nav entry after Sense and Perception
- `docs/docs/architecture/index.md` — Added Containment Model entry between Sense and Perception and IF Development Guide
- `docs/docs/architecture/overview.md` — Added cross-reference to containment-model.md in The Containment Model section
- `docs/docs/architecture/sense-perception.md` — Updated footer: replaced development-guide.md placeholder link with actual containment-model.md link
- `docs/docs/architecture/action-resolution.md` — Added forward link to containment-model.md in footer

### Build Verification
Fixed one anchor mismatch (em dash in heading → single hyphen for mkdocs anchor format: `#preconditions--precondt` corrected to `#preconditions-precondt`). Build completed with zero warnings for the new document.

## Key Decisions

### 1. Five-Layer Architecture as Organizing Principle
The containment model spans tree structure, container types, reachability, capacity, and nested rooms. Organizing by layer (bottom-up) rather than by source file makes the dependencies between concerns explicit and easier to follow.

### 2. Container vs Surface as the Key Design Distinction
Container inherits from BasicContainer (enclosure boundary) while Surface inherits from BulkLimiter directly (no boundary). This is the single most important class hierarchy decision in the containment system, and it is called out prominently in Section 4.

### 3. Four Layers of moveInto Explicitly Documented
The baseMoveInto → mainMoveInto → moveIntoForTravel → moveInto layering is non-obvious and critical for understanding when notifications fire and where to intercept movement for game logic. Each layer's specific responsibility is described.

### 4. Reachability as a Containment-Path Walk
The full touchObj algorithm is documented: get path, walk path, check at each boundary, identify obstructor, try implicit removal, loop. This makes explicit the bridge between the containment model and the action precondition system.

### 5. Author Editorial Note Preserved
The source code warning about inventory limits ("authors love this sort of 'realism' a whole lot more than players do") is quoted directly because it communicates a key design philosophy that informs how the BagOfHolding and carrying-capacity systems should be used.

## Open Items

### Short Term
- Message System deep-dive (5 of 6): parameter substitutions, msg_neu.t, message customization patterns
- Event Scheduling deep-dive (6 of 6): Schedulable, Daemon, Fuse, turn ordering

### Long Term
- Once all six deep-dives are complete, review architecture/index.md for coherence as a reading guide
- Consider a cross-cutting "how the systems interact" summary document

## Files Modified

**New** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/containment-model.md` — Full 10-section deep-dive on the containment model

**Updated** (5 files):
- `/Users/david/repos/tads3/docs/mkdocs.yml` — Added nav entry for Containment Model
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — Added Containment Model entry to deep-dive listing
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — Added cross-reference in The Containment Model section
- `/Users/david/repos/tads3/docs/docs/architecture/sense-perception.md` — Updated footer link from placeholder to containment-model.md
- `/Users/david/repos/tads3/docs/docs/architecture/action-resolution.md` — Added forward link to containment-model.md in footer

## Architectural Notes

The containment model is the most sprawling of the deep-dives so far — it touches thing.t, objects.t, extras.t, travel.t, precond.t, and actor.t. The key insight is that containment is not just a data structure (the tree) but an active system with five distinct concerns: structure, boundaries, reachability, capacity, and actor positioning. Each concern has its own set of classes and algorithms, but they all operate on the same underlying tree.

The reachability system (touchObj → containment path → checkTouchViaPath → implicit open) is the most architecturally significant bridge between the containment model and the action system. It is what makes glass jars interesting: you can see through them (sense system) but not reach through them (reachability), and the distinction drives different gameplay outcomes. This cross-system relationship is the reason reachability is documented here rather than in the action-resolution deep-dive.

**Architecture doc count**: 8 documents total (index, overview, parser-pipeline, action-resolution, sense-perception, containment-model, IF development guide, design patterns, quick reference). 4 of the 6 planned deep-dives are complete.

## Notes

**Session duration**: ~28 minutes (1612 to 1640)

**Approach**: Bottom-up layer-by-layer organization mirroring the actual dependency structure of the source classes, with practical intervention-point lookup tables at the end to serve authors who need quick answers without reading the full analysis.

---

**Progressive update**: Session completed 2026-02-21 16:40
