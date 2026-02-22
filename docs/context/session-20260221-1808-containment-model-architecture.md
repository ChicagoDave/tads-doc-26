# Session Summary: 2026-02-21 - containment-model-architecture

## Status: Completed

## Goals
- Create the fourth of six planned deep-dive architecture documents: the Containment Model
- Integrate the new document into navigation, the architecture index, the overview, and footers of adjacent deep-dives
- Verify zero build warnings

## Completed

### New Document: containment-model.md

Created `/Users/david/repos/tads3/docs/docs/architecture/containment-model.md`, a comprehensive 10-section deep-dive following the template established by parser-pipeline.md, action-resolution.md, and sense-perception.md. This is the 4th of 6 planned deep-dive architecture documents.

**Section breakdown:**

1. **Containment Model Overview** — ASCII diagram of five design layers (Tree, Container Types, Reachability, Capacity, Nested Rooms). Source-file-to-role mapping table covering thing.t, objects.t, extras.t, travel.t, precond.t, actor.t, and adv3.h.

2. **The Containment Tree** — location/contents as a single-parent tree; Rooms as roots (isTopLevel); the `+` syntax and `@location` template; containment query methods table (isIn, isDirectlyIn, isHeldBy, isNominallyIn, getCommonContainer); special semantics of isIn(nil).

3. **Moving Objects** — Four layers of moveInto: baseMoveInto → mainMoveInto → moveIntoForTravel → moveInto, with a comparison table of each layer's responsibilities. Notification chain: sendNotifyRemove up the old tree, sendNotifyInsert down the new tree (outside-in order), notifyMoveInto on the object. Verify-phase variant for circular containment detection. Containment paths: PathIn/PathOut/PathPeer/PathThrough enums table, getAllPathsTo, selectPathTo, traversePath.

4. **The Container Hierarchy** — Full class tree from BulkLimiter through Container/Surface/SpaceOverlay. BulkLimiter capacity properties and whatIf enforcement. BasicContainer as the enclosure boundary class (isOpen, material, transSensingIn/Out, checkMoveViaPath, checkTouchViaPath, fillMedium). Container vs Surface behavior comparison table. OpenableContainer with implicit-open and tryImplicitRemoveObstructor. LockableContainer. RestrictedContainer with canPutIn. SingleContainer with objEmpty precondition.

5. **Spatial Relationships** — SpaceOverlay with abandon-on-move behavior (abandonLocation). Comparison table of Underside, RearContainer, RearSurface. ComplexContainer with secret sub-objects (ComplexComponent), command remapping table, subLocation property for initial placement.

6. **Reachability** — ASCII algorithm diagram of the touch path: touchObj precondition gets the containment path, walks it calling checkTouchViaPath at each boundary, identifies obstructors, tries implicit removal (e.g., implicit OPEN). BasicContainer's checkTouchViaPath override as the key logic. preCondOrder 200 explanation (runs last among preconditions). Verify-phase disambiguation adjustments table. OutOfReach mixin with directional reach override table.

7. **Bulk and Weight** — getBulk (external only) vs getWeight (recursive) methods table; getEncumberingBulk (0 if worn). StretchyContainer exception. whatIf speculative testing. Actor carrying capacity table with editorial note about inventory limits ("authors love this sort of 'realism' a whole lot more than players do" — quoted from source). BagOfHolding algorithm with affinity scoring and most-recent-item protection.

8. **Nested Rooms and Staging** — NestedRoom as travelWithin (not travelTo). Concrete subclasses table (BasicChair/Chair/BasicBed/Bed/BasicPlatform/Platform/Booth/Vehicle) with postures and drop destinations. ASCII staging location algorithm diagram. HighNestedRoom. isStagingLocationKnown for puzzles. Room/NestedRoom extra scope items.

9. **Multi-Location Objects** — MultiLoc (one object, many locations), MultiInstance (separate copies), MultiFaceted (facets with pronoun tracking). Movement methods: moveIntoAdd, moveOutOf. Usage guidance for each type.

10. **Practical Intervention Points** — Six lookup tables: controlling containment, controlling capacity, controlling reachability, controlling open/close and lock/unlock, controlling nested rooms, controlling multi-location objects.

### Navigation and Cross-Reference Integration

Updated five existing files to integrate the new document:

- `docs/mkdocs.yml` — Added nav entry for Containment Model after Sense and Perception
- `docs/docs/architecture/index.md` — Added Containment Model entry with description between Sense and Perception and IF Development Guide
- `docs/docs/architecture/overview.md` — Added cross-reference to containment-model.md in The Containment Model section
- `docs/docs/architecture/sense-perception.md` — Updated footer: replaced development-guide.md placeholder link with actual containment-model.md link
- `docs/docs/architecture/action-resolution.md` — Added forward link to containment-model.md in footer

### Build Verification

Fixed one anchor mismatch: an em dash in a heading produced a double-hyphen anchor (`#preconditions--precondt`) that did not match the internal link. Corrected to `#preconditions-precondt`. Build completed with zero warnings for the new document.

## Key Decisions

### 1. Five-Layer Architecture as Organizing Principle
The containment model spans tree structure, container types, reachability, capacity, and nested rooms. Organizing the document by layer (bottom-up) rather than by source file makes dependencies between concerns explicit and easier to follow than a file-by-file walkthrough would.

### 2. Container vs Surface as the Key Design Distinction
Container inherits from BasicContainer (enclosure boundary) while Surface inherits from BulkLimiter directly (no boundary). This is the single most important class hierarchy decision in the containment system. It is called out prominently in Section 4 with a side-by-side comparison table.

### 3. Four Layers of moveInto Explicitly Documented
The baseMoveInto → mainMoveInto → moveIntoForTravel → moveInto layering is non-obvious and critical for understanding when notifications fire and where to intercept object movement for game logic. Each layer's specific responsibility is described in a comparison table.

### 4. Reachability Documented as a Containment-Path Walk
The full touchObj algorithm is laid out: get path, walk path, check at each boundary, identify obstructor, try implicit removal, loop. This makes the bridge between the containment model and the action precondition system explicit. The cross-system relationship is why reachability is covered here rather than in the action-resolution deep-dive.

### 5. Author Editorial Note Preserved
The source code warning about inventory limits is quoted directly because it communicates a key design philosophy: carrying limits exist in the system but are discouraged for good UX reasons. This is useful context for anyone customizing the BagOfHolding or actor capacity system.

## Open Items

### Short Term
- Message System deep-dive (5 of 6): parameter substitutions, msg_neu.t, message customization patterns
- Event Scheduling deep-dive (6 of 6): Schedulable, Daemon, Fuse, turn ordering

### Long Term
- Once all six deep-dives are complete, review architecture/index.md for coherence as a reading guide
- Consider a cross-cutting "how the systems interact" summary document tying all six together

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

The containment model is the most sprawling of the four deep-dives completed so far — it touches thing.t, objects.t, extras.t, travel.t, precond.t, actor.t, and adv3.h. The key insight is that containment is not just a data structure (the tree) but an active system with five distinct concerns: structure, boundaries, reachability, capacity, and actor positioning. Each concern has its own set of classes and algorithms, but they all operate on the same underlying tree.

The reachability system (touchObj → containment path → checkTouchViaPath → implicit open) is the most architecturally significant bridge between the containment model and the action system. It is what makes glass jars interesting: you can see through them (sense system) but not reach through them (reachability). This distinction drives different gameplay outcomes from the same physical object, and it is the reason reachability is covered here rather than in the action-resolution deep-dive.

Source files referenced: thing.t, objects.t, extras.t, travel.t, precond.t, actor.t, adv3.h, en_us.h.

**Architecture doc count**: 4 of 6 planned deep-dives complete (parser-pipeline, action-resolution, sense-perception, containment-model). 2 remaining (message-system, event-scheduling).

## Notes

**Session duration**: approximately 28 minutes

**Approach**: Bottom-up, layer-by-layer organization mirroring the actual dependency structure of the source classes, with practical intervention-point lookup tables at the end to serve authors who need quick answers without reading the full analysis. Pattern is consistent with the three preceding deep-dives.

---

**Progressive update**: Session completed 2026-02-21 18:08
