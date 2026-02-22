# Session: Containment Model Accuracy Review
**Date:** 2026-02-21
**Task:** Verify all technical claims in containment-model.md against TADS 3 adv3 source code and fix inaccuracies

## Changes Made

### ERROR (1 fix)
1. **Fabricated property `contentsReachable`** in SpaceOverlay code example (was `{ contentsReachable = nil }`, fixed to `{ }`). This property does not exist anywhere in the TADS 3 library.

### INACCURACIES (3 fixes)
1. **`objClosed` precondition on Lock misattributed to `Lockable`** — actually defined in `Openable` (objects.t line 3696). Restructured the Lockable bullet list and added a clarifying note.
2. **`tryImplicitRemoveObstructor()` attributed to `Openable`** — actually defined on `BasicOpenable` (objects.t line 3450). Added "(inherited from `BasicOpenable`)" to the bullet point.
3. **`touchObj` line reference `precond.t:419`** — line 419 is the `TouchObjCondition` class, not the `touchObj` singleton (which is at line 690). Expanded the reference to mention both.

### MINOR (4 fixes)
1. **Verify-phase table for `touchObj` incomplete** — omitted smell presence ("You can smell it but can't see it") and generic not-visible ("Marked inaccessible") cases. Added both rows.
2. **Path example included `PathTo` as if stored in path data structure** — `PathFrom` and `PathTo` are synthesized by `traversePath()`, not stored in the path list. Fixed the example to use actual stored operations (`PathOut`, `PathPeer`, `PathIn`) and added a clarifying note. Also fixed the example to match the diagram (actor is in the chair, not directly in the room).
3. **`Vehicle` posture listed as "varies"** — default is `standing` (inherited from `NestedRoom`). Changed to "standing (default)" with note about typical multi-inheritance usage.
4. **`PathFrom`/`PathTo` table entries** — added "(synthesized during traversal)" to both entries to match the new clarification note.

## Files Modified
- `/Users/david/repos/tads3/docs/docs/architecture/containment-model.md`

## Source Files Consulted
- `thing.t` — location/contents, isIn/isDirectlyIn/isHeldBy, moveInto chain, containment paths, whatIf, getEncumberingBulk/Weight
- `objects.t` — BulkLimiter, BasicContainer, Container, Surface, Openable, BasicOpenable, Lockable, RestrictedHolder, RestrictedContainer, SingleContainer, OpenableContainer, LockableContainer, KeyedContainer, OutOfReach, MultiLoc, MultiInstance, MultiFaceted
- `extras.t` — ComplexContainer, ComplexComponent, SpaceOverlay, Underside, RearContainer, RearSurface, StretchyContainer, BagOfHolding
- `travel.t` — NestedRoom, BasicChair, Chair, BasicBed, Bed, BasicPlatform, Platform, Booth, Vehicle, HighNestedRoom, staging locations
- `precond.t` — TouchObjCondition, touchObj, objClosed, preCondOrder
- `actor.t` — weightCapacity, tryMakingRoomToHold, carrying capacity editorial
- `adv3.h` — PathFrom/In/Out/Peer/Through/To enums
