# The Sense and Perception System

TADS 3 models four senses — sight, sound, smell, and touch — as first-class concepts in its world model. Every sensory interaction in the game, from seeing objects in a lit room to hearing sounds through a closed door, flows through a unified architecture that traces paths through the containment tree, applies material transparency at each boundary, and propagates ambient energy (light) from sources to receivers. This document explains that architecture: the class hierarchies, the path calculation algorithm, and the places where game authors can intervene.

[Overview](#sense-system-overview) | [Materials](#materials-and-transparency-senset) | [Four Senses](#the-four-senses-senset) | [Path Calculation](#sense-path-calculation-thingt) | [Fill Media](#fill-media-and-asymmetric-containers) | [Connectors](#sense-connectors-and-occluders) | [Emanations](#sensory-emanations-objectst) | [Scope](#how-senses-drive-scope) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to other architecture docs"
    The [Architecture Overview](overview.md#the-sensory-model) introduces the sensory model at a high level — the four senses, the five built-in materials, and a quick example. The [Action Resolution](action-resolution.md#scope-who-can-see-what) document explains how scope feeds noun resolution. The library guide covers practical usage of [SenseConnector](../library/guide/senseconnector.md), [Noise and Odor](../library/guide/sensoryevent.md), and [SenseDaemon/SenseFuse](../library/guide/sensedaemon.md). This document explains the internal machinery — how sense paths are calculated, how brightness propagates, and how all the pieces fit together end-to-end.

---

## Sense System Overview

The sense system is organized in four layers. Each layer builds on the one below:

```
Layer 1: Materials & Transparency        What senses pass through (sense.t)
     │   Material class, transparency enums,
     │   transparencyAdd(), adjustBrightness()
     │
     ▼
Layer 2: Sense Path Calculation          Trace containment paths (thing.t)
     │   connectionTable()  →  universe of reachable objects
     │   cacheAmbientInfo() →  brightness at each object (sight only)
     │   cacheSensePath()   →  transparency from POV to each object
     │
     ▼
Layer 3: SenseInfo Assembly              Package results per object (thing.t)
     │   canBeSensed() gate
     │   SenseInfo(obj, trans, obstructor, ambient)
     │
     ▼
Layer 4: Consumers                       Scope, descriptions, preconditions
         Actor.scopeList()               →  parser noun resolution
         canSee / canHear / canSmell     →  action preconditions
         Room descriptions               →  what the player reads
```

The key design principle is **cache-and-query**. The expensive work — tracing paths through the containment tree — is done once per `senseInfoTable()` call. Results are cached on scratch-pad properties (`tmpTrans_`, `tmpAmbient_`, etc.) on each object. Consumers call convenience methods that just look up the cached results. The cache is keyed by `[pov, sense]` and stored in `libGlobal.senseCache`.

### Source files and responsibilities

| Source | Role |
|--------|------|
| `sense.t` | Material class, Sense class, transparency math, SenseConnector, DistanceConnector, Occluder |
| `thing.t` | SenseInfo, senseInfoTable(), connectionTable(), path calculation, brightness propagation, scratch-pads |
| `objects.t` | Container transparency overrides, FillMedium, Intangible, SensoryEmanation, Noise, Odor |
| `adv3.h` | Transparency enums (`transparent`, `distant`, `attenuated`, `obscured`, `opaque`), size enums (`large`, `medium`, `small`) |
| `actor.t` | `scopeSenses`, `scopeList()`, `sensePresenceList()` |

---

## Materials and Transparency — sense.t

### The Material class

Every container in the game has a `material` property — an instance of the `Material` class that determines what senses pass through it. The Material class uses a property-pointer dispatch pattern:

```tads3
class Material: object
    senseThru(sense) { return self.(sense.thruProp); }

    seeThru = opaque
    hearThru = opaque
    smellThru = opaque
    touchThru = opaque
;
```

When code calls `material.senseThru(sight)`, the method reads `sight.thruProp` (which is `&seeThru`) and evaluates `self.seeThru`. This indirection means adding a new sense requires no changes to the Material class — just define a new `xxxThru` property.

### The five built-in materials

| Material | seeThru | hearThru | smellThru | touchThru | Typical use |
|----------|---------|----------|-----------|-----------|-------------|
| `adventium` | opaque | opaque | opaque | opaque | Default for all objects |
| `paper` | opaque | transparent | transparent | opaque | Cardboard boxes, envelopes |
| `glass` | transparent | opaque | opaque | opaque | Windows, display cases |
| `fineMesh` | transparent | transparent | transparent | opaque | Screen doors, wire fences |
| `coarseMesh` | transparent | transparent | transparent | transparent | Chain-link fences, grates |

`adventium` is the default material for every object. This is **safe-by-default** design: an object is opaque to everything unless the author explicitly says otherwise.

### Transparency arithmetic

The five transparency levels, from most to least transparent:

| Level | Meaning | Effect on sensibility |
|-------|---------|----------------------|
| `transparent` | No degradation | All objects sensible in full detail |
| `attenuated` | Energy reduced | All objects sensible in full detail |
| `distant` | Physical distance | Small objects not sensible |
| `obscured` | Detail lost | Small objects not sensible |
| `opaque` | Fully blocked | Nothing passes |

Three functions operate on these levels:

**`transparencyAdd(a, b)`** — combines two transparency levels when a sense path crosses multiple boundaries. The critical rule: `transparent + x → x`, `opaque + x → opaque`, and **any other combination → opaque**. This means two non-transparent layers always produce opaque. A practical consequence: there can never be more than one obstructor in a non-opaque path.

**`transparencyCompare(a, b)`** — orders transparency levels. Returns 1 if `a` is more transparent, -1 if less, 0 if equal. The ordering is: `transparent > attenuated > distant == obscured > opaque`.

**`adjustBrightness(br, trans)`** — applies a transparency level to a brightness value (sight only). Transparent and distant pass brightness unchanged. Attenuated and obscured reduce levels below 3 to 0 and decrement levels 3+. Opaque yields 0.

---

## The Four Senses — sense.t

### Sense anatomy

Each `Sense` object carries four property pointers that parameterize the entire system:

| Property | `sight` | `sound` | `smell` | `touch` |
|----------|---------|---------|---------|---------|
| `thruProp` | `&seeThru` | `&hearThru` | `&smellThru` | `&touchThru` |
| `sizeProp` | `&sightSize` | `&soundSize` | `&smellSize` | `&touchSize` |
| `presenceProp` | `&sightPresence` | `&soundPresence` | `&smellPresence` | `&touchPresence` |
| `ambienceProp` | `&brightness` | nil | nil | nil |

Every algorithm in the system — path calculation, sensibility checks, scope building — operates through these property pointers. This is the core extensibility mechanism: to add a fifth sense, you define a new `Sense` object with four property pointers, add `xxxThru` to Material, and add `xxxSize`/`xxxPresence` to Thing. No algorithms change.

The source code documents this explicitly (at `sense.t:228`):

> *To add a new sense, you must define the sense object itself, modify class Material to set the default transparency level, and modify class Thing to set the default xxxSize and xxxPresence settings.*

### Sight is special: ambient energy

Sight is the only sense with a non-nil `ambienceProp`. This means sight requires an external energy source — light — to function. The other three senses detect directly emitted phenomena (sounds, smells, physical contact) and work regardless of ambient conditions.

Brightness is an integer property on Thing:

| Value | Meaning | Propagation |
|-------|---------|-------------|
| 0 | No light emitted (default) | — |
| 1 | Self-illuminating only (glowing watch dial) | Does not propagate to other objects |
| 2 | Dim light (candle) | Propagates outward through containment |
| 3 | Moderate light (torch) | Propagates outward |
| 4 | Bright light (overhead lamp) | Propagates outward |

The boundary between level 1 and level 2 is significant: level 1 objects are visible to themselves but do not illuminate their surroundings. A glowing gem in a dark room lets you see the gem, but not the room.

If `adjustBrightness(ambient, trans)` yields 0 at an object, that object cannot be seen regardless of the path transparency. A room with no light source has ambient 0, so nothing inside is visible — this is how darkness works.

### Touch is special: no distance

Touch overrides `canObjBeSensed()` to return `nil` when transparency is `distant`, regardless of the object's size. This makes physical contact impossible at range, even for large objects, while all other senses allow large objects to be sensed at distance.

Touch is also excluded from the default `scopeSenses` list (`[sight, sound, smell]`). As the source comment explains (at `actor.t:7508`): objects may be touchable in the sense that there's no physical barrier, but without another sense to locate them, the actor wouldn't know where to reach.

### Size, presence, and sensibility

**Size** determines whether an object can be sensed through degraded paths:

| Transparency | `small` | `medium` | `large` |
|-------------|---------|----------|---------|
| transparent | yes | yes | yes |
| attenuated | yes | yes | yes |
| distant | **no** | yes | yes |
| obscured | **no** | yes | yes |
| opaque | no | no | no |

All objects default to `medium` for all senses.

**Presence** determines whether an object *actively calls attention to itself* and enters scope. Presence is independent of sensibility — an object without `soundPresence` can still be heard if there's a non-opaque sound path to it; it just won't appear in the actor's scope list automatically.

| Property | Default | Meaning |
|----------|---------|---------|
| `sightPresence` | `true` | Object is visible (has a visual appearance) |
| `soundPresence` | `nil` | Object makes no sound |
| `smellPresence` | `nil` | Object emits no odor |
| `touchPresence` | `true` | Object is physically present |

The distinction matters: an object in a glass jar is visible (`sightPresence = true`, transparent path) and in scope. A silent object behind a closed door is not in scope — even though it could be heard if it made a sound.

---

## Sense Path Calculation — thing.t

This is the core of the system. The method `senseInfoTable(sense)` (at `thing.t:6818`) is the master entry point. It returns a `LookupTable` keyed by object, with `SenseInfo` values describing how each object can be sensed from the point of view.

### The algorithm

```
pov.senseInfoTable(sense)
     │
     ├── 1. connectionTable()
     │       Walk containment tree up and down from pov
     │       Follow SenseConnector links across rooms
     │       Result: LookupTable of all connected objects
     │
     ├── 2. cacheSenseInfo(objs, sense)
     │   │
     │   ├── cacheAmbientInfo(objs, sense)
     │   │     If sense has ambienceProp (sight only):
     │   │       Find all brightness sources (brightness != 0)
     │   │       Each source calls transmitAmbient()
     │   │         └── shineOnLoc() ↑  shineOnContents() ↓
     │   │             shineFromWithin() ↑  shineFromWithout() ↓
     │   │     Result: tmpAmbient_ / tmpAmbientWithin_ set on each object
     │   │
     │   ├── cacheSensePath(sense)
     │   │     Start at pov with transparent/nil/nil
     │   │       └── sensePathToLoc() ↑  sensePathToContents() ↓
     │   │           sensePathFromWithin() ↑  sensePathFromWithout() ↓
     │   │     Result: tmpTrans_ / tmpTransWithin_ set on each object
     │   │
     │   └── Notify Occluders via senseTmp.notifyList
     │         Each Occluder.finishSensePath() sets occluded objects to opaque
     │
     └── 3. Build SenseInfo table
             For each connected object:
               addToSenseInfoTable() checks canBeSensed()
               Creates SenseInfo(obj, trans, obstructor, ambient)
             Result: LookupTable keyed by object → SenseInfo
```

### Step 1: connectionTable()

`connectionTable()` (at `thing.t:5726`) is a pre-filter that finds every object connected by containment to the point of view — walking up to parent containers, down to child contents, and across `SenseConnector` links. The result is the universe of objects that *could* be sensed; the actual sensibility is determined in steps 2 and 3.

The table is cached in `libGlobal.connectionCache` because it is called frequently — the source notes that the sample game invokes it ~500 times per turn.

### Step 2: cacheAmbientInfo() — brightness propagation

For senses without `ambienceProp` (sound, smell, touch), this step just calls `clearSenseInfo()` on each object to reset the scratch-pads.

For sight, the algorithm is a greedy flood-fill:

1. Clear all scratch-pad properties on every connected object
2. Find all brightness sources (objects where `brightness != 0`)
3. Each source calls `transmitAmbient()`, which sets its own `tmpAmbient_` and, if brightness >= 2, calls `shineOnLoc()` (upward) and `shineOnContents()` (downward)
4. At each containment boundary, `adjustBrightness()` reduces the level based on `transSensingIn()`/`transSensingOut()`
5. Fill media are applied at each traversal, but consecutive traversals of the same fill material count as one

Each object tracks the highest ambient level received so far. If a new path offers a higher level, it replaces the old one and propagation continues. If not, propagation stops at that branch. This is how the system finds the best path without exhaustive search.

### Step 3: cacheSensePath() — transparency propagation

The transparency calculation has a parallel structure to brightness propagation: same four directional methods, same best-path-wins logic, but tracking transparency instead of brightness.

| Method | Direction | What it does |
|--------|-----------|-------------|
| `sensePathToLoc()` | Child → container | Calls `location.sensePathFromWithin()` |
| `sensePathToContents()` | Container → children | Applies `transSensingIn()` + fill medium, calls `sensePathFromWithout()` on each child |
| `sensePathFromWithin()` | Container receives from child | Applies fill medium + `transSensingOut()`, propagates to peers and upward |
| `sensePathFromWithout()` | Child receives from container | Stores path if better than previous, propagates downward to contents |

The path starts at `transparent` from the point of view to itself, then walks outward to containers and inward to contents. At each boundary, `transparencyAdd()` combines the current path transparency with the boundary's transparency. If the result changes, the boundary object becomes the new `obstructor`.

Because `transparencyAdd()` collapses two non-transparent levels to `opaque`, there is at most **one obstructor** per non-opaque path. This is an important invariant: the `obstructor` field in `SenseInfo` always identifies the single object responsible for any degradation.

### The SenseInfo result

After path calculation, `addToSenseInfoTable()` checks `canBeSensed()` for each connected object and packages the results:

| Field | Type | Meaning |
|-------|------|---------|
| `obj` | Thing | The object being sensed |
| `trans` | enum | Transparency from POV to object (`transparent`, `attenuated`, `distant`, `obscured`) |
| `obstructor` | Thing | The object causing a non-transparent path (nil if `transparent`) |
| `ambient` | integer | Ambient energy at the object, adjusted for path transparency |

The method checks `tmpPathIsIn_` to decide whether to use exterior data (`tmpTrans_`, `tmpAmbient_`) or interior data (`tmpTransWithin_`, `tmpAmbientWithin_`). This distinction matters because the point of view may be *inside* a container (a room) looking at objects that are also inside it.

### Scratch-pad properties

These transient properties on every Thing store intermediate results during calculation:

| Property | Meaning |
|----------|---------|
| `tmpTrans_` | Best transparency to this object's exterior |
| `tmpTransWithin_` | Best transparency to this object's interior |
| `tmpObstructor_` | Object causing degradation in the exterior path |
| `tmpObstructorWithin_` | Object causing degradation in the interior path |
| `tmpAmbient_` | Best ambient energy at this object's exterior |
| `tmpAmbientWithin_` | Best ambient energy at this object's interior |
| `tmpAmbientFill_` | Last fill medium traversed (for deduplication) |
| `tmpFillMedium_` | Cached result of `fillMedium()` |
| `tmpPathIsIn_` | `true` if best path arrives from outside; `nil` if from inside |

---

## Fill Media and Asymmetric Containers

### FillMedium

A `FillMedium` (in `objects.t`) is a Thing subclass representing a medium that permeates a container's interior — fog, smoke, murky water. It has a `material` property and a `senseThru()` method that returns the material's transparency.

The critical rule: **consecutive traversals of the same fill medium count as one**. When sense energy enters a foggy room through one wall and crosses to the other side, the fog is applied once, not twice. The `tmpAmbientFill_` / last-fill parameter in the path methods tracks this.

The `fillMedium()` method on Thing walks up the containment tree by default, so a fill medium in a room also affects open containers within it. The `Container` class overrides this: when closed, it returns `nil`, isolating its interior from the parent's medium.

### transSensingIn() vs. transSensingOut()

By default, `transSensingOut(sense)` returns `transSensingIn(sense)` — containers are symmetric. Override `transSensingOut()` to create asymmetric containers like one-way mirrors (visible from one side only).

`Container` overrides `transSensingIn()`: if open, returns `transparent`; if closed, returns `material.senseThru(sense)`. This is the mechanism that makes closing a glass jar change its sensory behavior — the jar becomes transparent to sight but opaque to the other senses.

---

## Sense Connectors and Occluders

### SenseConnector

`SenseConnector` (in `sense.t`) is a `MultiLoc` mixin that bridges sense paths between rooms. It overrides `addDirectConnections()` to add all its locations to the connection table, and overrides `sensePathFromWithout()` and `shineFromWithout()` to propagate paths and brightness between its locations, applying `transSensingThru()` at the crossing.

```tads3
class SenseConnector: MultiLoc
    connectorMaterial = adventium
    transSensingThru(sense) { return connectorMaterial.senseThru(sense); }
;
```

`connectorMaterial` defaults to `adventium` (opaque) — you must set it to a transparent material for the connector to pass any senses. A glass window between rooms would use `connectorMaterial = glass`.

SenseConnector also provides `checkTouchThrough()`, `checkMoveThrough()`, and `checkThrowThrough()` for controlling physical interactions across the connection. By default, all three block the action.

### DistanceConnector

`DistanceConnector` is a `SenseConnector + Intangible` whose `transSensingThru()` always returns `distant`. Use it for divided rooms or locations that are open to one another but physically separated — a balcony overlooking a courtyard, or the north and south ends of a large cave.

At `distant` transparency: small objects are not sensible, touch does not work at all, and large/medium objects can be perceived but without fine detail.

### Occluder

`Occluder` is a mixin for selective post-calculation blocking. The classic example: a window connecting two rooms, with a bookcase against the window in one room. The bookcase's contents should not be visible through the window, even though everything else in the room is.

Occluders register for notification during `clearSenseInfo()` by appending themselves to `senseTmp.notifyList`. After the path calculation is complete, each Occluder's `finishSensePath(objs, sense)` walks the result table and sets specific objects to `opaque`. The key method is `occludeObj(obj, sense, pov)`, which by default delegates to `obj.isOccludedBy(self, sense, pov)`.

Occlusion is **global within a room** — once an Occluder hides an object, it stays hidden even if another connector would make it visible. Occlusion always runs last and takes precedence over inclusion.

---

## Sensory Emanations — objects.t

### The emanation hierarchy

```
Intangible          no presence in any sense; filtered from 'all'
├── Vaporous        sightPresence = true (visible gas, cloud)
└── SensoryEmanation    base for ongoing sensory output
    ├── Noise           soundPresence = (isEmanating)
    │   └── SimpleNoise     ambient noise with simple descriptions
    └── Odor            smellPresence = (isEmanating)
        └── SimpleOdor      ambient odor with simple descriptions
```

Sensory emanations are `Intangible` objects placed inside or near a source object. They have no physical presence — they cannot be taken, moved, or listed in inventories. Their role is to project a sense presence through the containment tree.

Key properties:

| Property | Purpose |
|----------|---------|
| `isEmanating` | On/off switch — set to `nil` to silence a noise or suppress an odor |
| `isAmbient` | If `true`, this is background (not actively mentioned in room descriptions) |
| `descWithSource` | Description shown when the emanation's source is visible |
| `descWithoutSource` | Description shown when the source is obstructed |
| `hereWithSource` / `hereWithoutSource` | Room-description text variants |

### Display scheduling

`displaySchedule` is a list of turn intervals that mimics human "edge sensitivity" — a continuous noise is mentioned frequently at first, then less often as it fades into the background. The last entry repeats indefinitely. If the last entry is `nil`, the emanation stops being mentioned altogether. `displayCount` resets when the emanation leaves scope, so re-entering a noisy room re-triggers the initial schedule.

---

## How Senses Drive Scope

The chain from senses to the parser:

1. **`Actor.scopeList()`** (at `actor.t:8594`) iterates over `scopeSenses` (default: `[sight, sound, smell]`)
2. For each sense, calls **`sensePresenceList(sense)`**, which calls `senseInfoTable(sense)` and filters for objects where `obj.(sense.presenceProp)` is true
3. The union of all results, plus the actor itself and directly held items, forms the scope list
4. The scope list feeds the parser's noun resolution (see [Action Resolution — Scope](action-resolution.md#scope-who-can-see-what))

The key insight: **scope is multi-sensory**. An object making noise behind a closed door (`soundPresence = true`, path through door transparent for sound) is in scope and can be referred to by the parser, even if the player cannot see it. A smelly object in a closed paper box is in scope for the same reason.

This is why the sense system matters for the parser, not just for descriptions. It determines which objects the player can name, which in turn determines what commands are possible.

---

## Practical Intervention Points

### Controlling what can be sensed

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `material` | Property on container | Set a container's material to control what senses pass through its walls |
| `transSensingIn(sense)` | Override on Thing | Custom or conditional transparency (e.g., open vs. closed) |
| `transSensingOut(sense)` | Override on Thing | Asymmetric transparency (one-way mirrors) |
| `canBeSensed(sense, trans, ambient)` | Override on Thing | Custom sensibility rules (invisible objects, smell-only objects) |
| `sightSize` / `soundSize` / etc. | Properties on Thing | Control whether the object is detectable at distance or through obscuring media |
| `sightPresence` / `soundPresence` / etc. | Properties on Thing | Control whether the object actively emits in a sense and enters scope |
| `brightness` | Property on Thing | Set light emission level (0 = none, 1 = self-illuminating, 2+ = illuminates surroundings) |

### Custom sense connectors

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `SenseConnector` | Subclass with MultiLoc | Connect rooms for sense propagation with custom material |
| `connectorMaterial` | Property on SenseConnector | Set what senses pass through the connection |
| `transSensingThru(sense)` | Override on SenseConnector | Fine-grained per-sense transparency control |
| `DistanceConnector` | Place in multiple rooms | Connect rooms at a distance (small objects invisible, touch impossible) |
| `Occluder` | Mix in with SenseConnector | Selectively block specific objects from being sensed |
| `occludeObj(obj, sense, pov)` | Override on Occluder | Custom occlusion rules based on object, sense, or point of view |
| `checkTouchThrough(obj, dest)` | Override on SenseConnector | Custom messages or permission for reaching through the connection |

### Custom sensory objects

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `Noise` / `SimpleNoise` | Place inside source object | Ongoing sound that propagates through containment |
| `Odor` / `SimpleOdor` | Place inside source object | Ongoing smell that propagates through containment |
| `isEmanating` | Property on SensoryEmanation | Turn emanation on/off dynamically |
| `isAmbient` | Property on SensoryEmanation | Mark as background (not actively mentioned) |
| `displaySchedule` | Property on SensoryEmanation | Control how often the emanation is re-mentioned |
| `FillMedium` | Place inside a room or container | Permeating medium (fog, smoke) that affects all senses in the interior |
| `SenseFuse` / `SenseDaemon` | Create in code | Timed sensory events with automatic scope-checking |

### Lighting and darkness

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `brightness = 0` | Default on Thing | Object emits no light |
| `brightness = 1` | Property on Thing | Self-illuminating (visible in dark but doesn't light surroundings) |
| `brightness = 2..4` | Property on Thing | Light source that illuminates surroundings |
| `brightness = 4` | On Room | A lit room (default for most rooms; set to 0 for dark rooms) |

### Debugging sense paths

| Method | What it returns |
|--------|-----------------|
| `pov.senseInfoTable(sense)` | Full LookupTable of all sensible objects with transparency, obstructor, and ambient data |
| `pov.sensePresenceList(sense)` | List of objects with a presence in the given sense |
| `actor.canSee(obj)` | Boolean: can the actor see the object? |
| `actor.canHear(obj)` | Boolean: can the actor hear the object? |
| `actor.canSmell(obj)` | Boolean: can the actor smell the object? |
| `actor.scopeList()` | Full scope list for the actor across all scope senses |

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [Action Resolution](action-resolution.md) for how scope connects to noun resolution. For the containment model that underpins sense paths, see [Containment Model](containment-model.md).*
