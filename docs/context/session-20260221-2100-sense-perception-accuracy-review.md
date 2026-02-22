# Session: Sense & Perception Architecture Accuracy Review

**Date:** 2026-02-21
**Task:** Verify every technical claim in `sense-perception.md` against adv3 source code and fix all issues

## Source Files Checked
- `sense.t` — Material, Sense, transparency functions, SenseConnector, Occluder, DistanceConnector
- `thing.t` — SenseInfo, senseInfoTable(), connectionTable(), cacheSenseInfo(), path methods, scratch-pads, canBeSensed(), transSensingIn/Out, fillMedium
- `objects.t` — BasicContainer (material, transSensingIn, fillMedium), FillMedium, Intangible, SensoryEmanation, Noise, Odor
- `actor.t` — scopeSenses, scopeList(), scope comment about touch
- `travel.t` — Room brightness default
- `adv3.h` — transparency enums, size enums

## Fixes Applied (10 total)

### ERRORS (2)

1. **`adventium` claimed as default material for every object** — Thing does not define `material` at all. Only `BasicContainer` (objects.t:4660) sets `material = adventium`. Fixed in 3 places: materials table, explanatory paragraph, and section intro.

2. **Room brightness claimed as 4** — Room actually defaults to `brightness = 3` (travel.t:4362). Fixed in intervention points table.

### INACCURACIES (4)

3. **~500 times per turn attributed to connectionTable()** — The ~500 figure (thing.t:5789) refers to the recursive helper `addDirectConnections()`, not `connectionTable()` itself. `connectionTable()` is cached and called far fewer times. Fixed to clarify the distinction.

4. **Container credited for transSensingIn/fillMedium overrides** — These are actually defined on `BasicContainer` (objects.t:4786, 4806), not `Container`. `Container` inherits them. Fixed in two places.

5. **DistanceConnector described as blocking fine detail for all non-small objects** — At `distant` transparency, large objects CAN still be perceived in full detail (via `canDetailsBeSensed` in thing.t:4546). Only medium objects lose detail. Fixed the DistanceConnector description.

6. **`sensePresenceList()` attributed to actor.t** — This method is defined on Thing (thing.t:6916), not Actor. Actor.scopeList() calls it but doesn't define it. Fixed the source files table.

### MINOR (4)

7. **Source files table said "Container transparency overrides"** — Changed to "BasicContainer material/transparency overrides" for precision.

8. **FillMedium description incomplete** — Said it "returns the material's transparency" without noting the nil-material fallback. Fixed to mention it returns `transparent` if no material is set.

9. **Step numbering inconsistent between diagram and prose** — Diagram shows cacheSensePath as part of step 2 (under cacheSenseInfo), but prose labeled it "Step 3". Fixed to "Step 2a" and "Step 2b".

10. **"Property on container" in intervention table** — Changed to "Property on BasicContainer" with clarification "when closed".

## Claims Verified as Correct
- Material class property-pointer dispatch pattern
- Five material definitions (all transparency values match source)
- transparencyAdd() semantics including "any other combination -> opaque"
- transparencyCompare() ordering: transparent > attenuated > distant == obscured > opaque
- adjustBrightness() behavior for all transparency levels
- Sense property pointer table (thruProp, sizeProp, presenceProp, ambienceProp)
- Brightness levels 0-4 semantics and propagation threshold at 2
- Touch canObjBeSensed() override for distant
- scopeSenses = [sight, sound, smell] and touch exclusion rationale
- Size/presence defaults on Thing (medium for sizes, true for sight/touch presence, nil for sound/smell)
- senseInfoTable cache keyed by [pov, sense] in libGlobal.senseCache
- connectionTable cached in libGlobal.connectionCache
- Path calculation algorithm structure (connectionTable -> cacheSenseInfo -> build table)
- Four directional path methods and their behaviors
- tmpPathIsIn_ semantics
- SenseInfo constructor adjusts ambient by transparency
- SenseConnector code structure (connectorMaterial defaults to adventium)
- Occluder notification mechanism and finishSensePath behavior
- Emanation hierarchy (Intangible -> Vaporous/SensoryEmanation -> Noise/Odor)
- displaySchedule and displayCount reset behavior
- scopeList() algorithm at actor.t:8594
