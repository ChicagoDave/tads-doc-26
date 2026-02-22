# The Containment Model

The physical world in TADS 3 is a tree. Every object has a `location` pointing to its parent, every parent has a `contents` list of its children, and rooms sit at the roots with no parent of their own. This tree is the foundation of everything else in adv3 — scope, sense paths, reachability, action preconditions, and room descriptions all walk the containment tree to answer their questions. This document explains the tree's structure, the algorithms that operate on it, and the places where game authors can intervene.

[Overview](#containment-model-overview) | [The Tree](#the-containment-tree) | [Moving Objects](#moving-objects) | [Container Hierarchy](#the-container-hierarchy) | [Spatial Relationships](#spatial-relationships) | [Reachability](#reachability) | [Bulk and Weight](#bulk-and-weight) | [Nested Rooms](#nested-rooms-and-staging) | [Multi-Location](#multi-location-objects) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to other architecture docs"
    The [Architecture Overview](overview.md#the-containment-model) introduces containment at a high level — the `+` syntax, rooms as roots, and scope as a consequence. The [Sense and Perception](sense-perception.md) document explains how sense paths trace through the containment tree and how materials gate what passes through container boundaries. The [Action Resolution](action-resolution.md#preconditions-precondt) document explains how preconditions like `touchObj` and `objHeld` enforce reachability during command execution. The library guide covers practical usage of [Containers](../library/guide/containers-introduction.md), [Nested Rooms](../library/guide/nestedroomoverview.md), and [Bulk and Weight](../library/guide/bulkandweight.md). This document explains the internal machinery — how the tree is maintained, how objects move through it, and how every containment query is resolved.

---

## Containment Model Overview

The containment model is organized in five layers:

```
Layer 1: The Tree                       Structure (thing.t)
     │   location / contents, isIn(), Rooms as roots,
     │   the + syntax, baseMoveInto()
     │
     ▼
Layer 2: Container Types                Boundaries (objects.t, extras.t)
     │   BulkLimiter, Container, Surface, SpaceOverlay
     │   open/close, material, transSensingIn/Out
     │
     ▼
Layer 3: Reachability                   Touch paths (thing.t, precond.t)
     │   containment paths, checkTouchViaPath(),
     │   obstructors, implicit opening
     │
     ▼
Layer 4: Capacity                       Limits (objects.t, actor.t)
     │   bulk, weight, bulkCapacity, maxSingleBulk,
     │   BagOfHolding, whatIf()
     │
     ▼
Layer 5: Nested Rooms & Staging         Actor positions (travel.t)
         BasicLocation, NestedRoom, staging locations,
         drop destinations, postures
```

### Source files and responsibilities

| Source | Role |
|--------|------|
| `thing.t` | Thing class, `location`/`contents`, `isIn()`, `moveInto()`, containment paths, reachability, bulk/weight properties, scope helpers |
| `objects.t` | BulkLimiter, BasicContainer, Container, Surface, Openable, Lockable, RestrictedContainer, SingleContainer, Component, Wearable, MultiLoc, MultiInstance |
| `extras.t` | ComplexContainer, SpaceOverlay, Underside, RearContainer, StretchyContainer, BagOfHolding |
| `travel.t` | BasicLocation, Room, NestedRoom, BasicChair, BasicPlatform, Booth, Vehicle, staging locations |
| `precond.t` | `touchObj`, `objHeld`, `objOpen`, `actorDirectlyInRoom`, `roomToHoldObj` |
| `actor.t` | Actor as container, carrying capacity, `tryMakingRoomToHold()`, inventory, `scopeList()` |
| `adv3.h` | Path enums (`PathIn`, `PathOut`, `PathPeer`, `PathThrough`, `PathFrom`, `PathTo`) |

---

## The Containment Tree

### location and contents

Every Thing has two containment properties:

- **`location`** — a single object reference pointing to the parent container, or `nil` if the object is not in the game world. This is a **private property** — game code should never read or write it directly. Use `isIn()`, `isDirectlyIn()`, and `moveInto()` instead.

- **`contents`** — a list of all objects directly inside this one. Maintained automatically by `baseMoveInto()`.

The tree is **single-parent**: every object has exactly one `location` (or `nil`). There is no way for a standard object to exist in two places at once. (Multi-location objects use a separate mechanism — see [Multi-Location Objects](#multi-location-objects).)

### Rooms as roots

Rooms are the roots of the containment tree. A Room has `isTopLevel = true` and `location = nil`, but it is considered part of the game world. An object with `location = nil` and `isTopLevel = nil` is considered *outside* the game world entirely — removed from play.

```
Room (isTopLevel = true, location = nil)      ← root
  ├── table: Surface
  │     ├── vase: Container
  │     │     └── rose: Thing
  │     └── book: Thing
  ├── chair: BasicChair                       ← nested room
  │     └── player: Actor
  └── lamp: Thing
```

### The + syntax

The `+` prefix in source code is compiler-level syntactic sugar for setting `location`:

```tads3
cave: Room 'Dark Cave' "The walls glisten. " ;
+ torch: Thing 'torch' 'torch' "A battered torch. " ;
+ chest: OpenableContainer 'chest' 'chest' "A sturdy chest. " ;
++ goldCoin: Thing 'gold coin' 'gold coin' "A gold coin. " ;
```

The compiler sets `torch.location = cave`, `chest.location = cave`, and `goldCoin.location = chest`. During pre-initialization, `initializeLocation()` calls `location.addToContents(self)` on every Thing, building the `contents` lists from the `location` pointers.

The `@location` template syntax is the explicit equivalent:

```tads3
goldCoin: Thing 'gold coin' 'gold coin' @chest "A gold coin. " ;
```

### Containment queries

| Method | Returns | Use |
|--------|---------|-----|
| `isDirectlyIn(obj)` | `location == obj` | Direct parent test |
| `isIn(obj)` | Walks up tree recursively | Transitive containment |
| `isOrIsIn(obj)` | `self == obj \|\| isIn(obj)` | Identity or containment |
| `isHeldBy(actor)` | `isDirectlyIn(actor)` | In actor's direct inventory |
| `isNominallyIn(obj)` | `isIn(obj)` or nominal location | Includes RoomPart locations |
| `getCommonContainer(obj)` | Nearest shared ancestor | For path computation |

The `isIn(nil)` call has special semantics: it returns `true` if the object is outside the game world (`location == nil` and `!isTopLevel`), and `nil` for rooms (which are in the world despite having `nil` location).

---

## Moving Objects

The containment system provides four layers of object movement, each adding behavior on top of the one below:

### The four layers

```
moveInto(newContainer)                    Full move: path + notifications + transfer
  │
  ├── moveIntoNotifyPath(newContainer)    Sense-path notifications via containment path
  │
  └── mainMoveInto(newContainer)          Notifications + transfer
        │
        ├── sendNotifyRemove(...)         Walk up OLD container tree: notifyRemove
        ├── sendNotifyInsert(...)         Walk up NEW container tree: notifyInsert
        ├── notifyMoveInto(newContainer)  Notify the object itself
        │
        └── baseMoveInto(newContainer)    Raw transfer: no notifications
              ├── location.removeFromContents(self)
              ├── location = newContainer
              └── newContainer.addToContents(self)
```

| Method | Notifications | Sense path | Use case |
|--------|:---:|:---:|-----------|
| `baseMoveInto()` | | | Internal moves, speculative tests |
| `mainMoveInto()` | yes | | Most gameplay moves |
| `moveIntoForTravel()` | yes | | Actor travel (connectors handle path) |
| `moveInto()` | yes | yes | Standard object manipulation (Take, Drop, PutIn) |

### Notification chain

When `mainMoveInto()` runs, it sends notifications up both container trees:

1. **`sendNotifyRemove(obj, newLoc)`** — walks up the old container tree. At each ancestor, calls `notifyRemove(obj)`. Stops at the common ancestor of the old and new locations (no need to notify containers the object isn't actually leaving).

2. **`sendNotifyInsert(obj, newCont)`** — walks up the new container tree from the *outside in* (parents notified before children). Calls `notifyInsert(obj, newCont)` at each level. This ordering lets outer containers veto an insertion before the inner container commits to it.

3. **`notifyMoveInto(newContainer)`** — notifies the moving object itself.

There is also a verify-phase variant: `verifyMoveTo(newLoc)` sends `verifyRemove` and `verifyInsert` notifications, allowing containers to veto a move during disambiguation. The `verifyInsert` method on Thing checks for circular containment (putting a box inside itself).

### Containment paths

The system can compute all possible containment paths between any two objects in the tree. A path is a list of alternating objects and operations:

```
[actor, PathOut, room, PathIn, table, PathIn, vase, PathTo, rose]
```

The path operations:

| Enum | Meaning |
|------|---------|
| `PathFrom` | Starting point of the path |
| `PathIn` | Traverse into a container's contents |
| `PathOut` | Traverse out to a container's parent |
| `PathPeer` | Traverse between siblings in the same container |
| `PathThrough` | Traverse through a SenseConnector between unrelated locations |
| `PathTo` | Ending point of the path |

`getAllPathsTo(obj)` finds every path via recursive DFS through the containment tree. `selectPathTo(obj, traverseProp)` picks the best path by testing each with a traverse function and returning the shortest one that passes. If no path passes, it returns the shortest failing path — useful for error messages that identify the specific obstructor.

`traversePath(path, func)` walks a path and calls `func(element, operation)` at each step. This is the core mechanism for both sense-path calculation and touch-reachability testing.

---

## The Container Hierarchy

### Class tree

```
Thing
  └── BulkLimiter                         Capacity limits (bulk, weight)
        ├── BasicContainer                Enclosure + sense boundaries
        │     └── Container               Full PUT IN / LOOK IN support
        │           ├── OpenableContainer  = Openable + Container
        │           │     ├── LockableContainer  = Lockable + OpenableContainer
        │           │     └── KeyedContainer     = LockableWithKey + OpenableContainer
        │           ├── RestrictedContainer  Only specific objects accepted
        │           ├── SingleContainer      One item at a time (via objEmpty)
        │           └── StretchyContainer    External bulk changes with contents
        ├── Surface                       PUT ON (no enclosure boundary)
        │     └── RestrictedSurface
        └── SpaceOverlay                  Adjacent-space base (under, behind)
              ├── Underside               PUT UNDER / LOOK UNDER
              └── RearContainer           PUT BEHIND / LOOK BEHIND
                    └── RearSurface       Contents stay attached on move
```

### BulkLimiter — the capacity base

`BulkLimiter` is the common ancestor of everything that limits its contents. It defines two capacity properties:

| Property | Default | Meaning |
|----------|---------|---------|
| `bulkCapacity` | 10000 | Maximum total bulk of all contents combined |
| `maxSingleBulk` | 10 | Maximum bulk of any single item |

When an object is about to be inserted, `notifyInsert()` uses `whatIf()` to speculatively test the insertion, calling `checkBulkInserted()` to verify the item fits. Two checks run: single-item size (`objBulk > maxSingleBulk`) and cumulative capacity (`getBulkWithin() > bulkCapacity`).

### BasicContainer — the enclosure boundary

`BasicContainer` adds the **enclosure boundary** — the distinction between inside and outside that affects both senses and reachability:

- **`isOpen`** — whether the container is currently open. Defaults to `true` (fixed).
- **`material`** — an instance of `Material` that determines what senses pass through when closed. Defaults to `adventium` (opaque to all).
- **`transSensingIn(sense)`** — if open, returns `transparent`; if closed, returns `material.senseThru(sense)`. This is how a closed glass jar blocks touch but not sight.
- **`transSensingOut(sense)`** — defaults to `transSensingIn(sense)` (symmetric). Override for asymmetric containers like one-way mirrors.
- **`checkMoveViaPath(obj, dest, op)`** — blocks object movement through a closed container.
- **`checkTouchViaPath(obj, dest, op)`** — blocks touch/reach through a closed container.
- **`fillMedium()`** — if open, inherits the parent's fill medium (fog disperses in); if closed, returns `nil` (isolated).

### Container vs. Surface

The critical design distinction: **Container inherits from BasicContainer** and has an enclosure boundary. **Surface inherits directly from BulkLimiter** and has no enclosure boundary at all.

| Behavior | Container | Surface |
|----------|-----------|---------|
| Enclosure | Yes — inside/outside distinction | No — contents are "on top" |
| Open/closed | Yes (via BasicContainer) | N/A (always accessible) |
| Sense boundary | Yes — material gates senses when closed | No — contents always visible/reachable |
| Player action | PUT IN | PUT ON |
| Fill medium | Isolated when closed | Inherits from parent |

### Openable and Lockable

`OpenableContainer` combines the `Openable` mixin with `Container`. The `Openable` mixin (which inherits from `BasicOpenable`) provides:

- `initiallyOpen` — starting state (default: `nil`, i.e., closed)
- `makeOpen(stat)` — changes state, with support for linked objects (both sides of a door)
- Open/Close action handlers with smart content listing — when you open a container, newly visible contents are listed
- `tryImplicitRemoveObstructor()` — when a closed container blocks a touch path, the reachability system calls this to attempt an implicit OPEN

`LockableContainer` adds `Lockable`, which provides:

- `initiallyLocked` — starting state (default: `true`)
- `makeLocked(stat)` — changes state
- Lock/Unlock action handlers
- `objClosed` precondition on Lock — you must close something before locking it

### Restricted and Single containers

`RestrictedContainer` uses the `RestrictedHolder` mixin to limit which objects can be placed inside:

```tads3
safe: RestrictedContainer 'safe' 'safe'
    validContents = [diamond, passport, cash]
    cannotPutInMsg(obj) { return 'Only valuables go in the safe. '; }
;
```

Override `canPutIn(obj)` for class-based or attribute-based tests instead of a fixed list.

`SingleContainer` enforces a one-item limit by adding the `objEmpty` precondition to PutIn. The precondition attempts to implicitly remove the current contents before inserting the new item.

---

## Spatial Relationships

### SpaceOverlay — under and behind

`SpaceOverlay` models spaces adjacent to an object — underneath it, behind it. The key behavior: when the overlay's parent object moves, contents are **abandoned** (left behind at the old location) rather than traveling with the object.

```tads3
+ bookcase: Heavy 'bookcase' 'bookcase' "A tall oak bookcase. " ;
++ RearContainer, Component { contentsReachable = nil }
+++ secretNote: Thing 'note' 'note' "A folded note. " ;
```

When the bookcase is pushed to a new room, the note stays behind and is revealed to the player. The `abandonLocation` property controls where abandoned contents end up (defaults to the parent object's container — typically the room floor).

| Class | Verb | Contents on move | abandonLocation |
|-------|------|-----------------|-----------------|
| `Underside` | PUT UNDER / LOOK UNDER | Left behind | Parent's container |
| `RearContainer` | PUT BEHIND / LOOK BEHIND | Left behind | Parent's container |
| `RearSurface` | PUT BEHIND / LOOK BEHIND | **Stay attached** | `nil` |

### ComplexContainer — multiple spatial relationships

A single game object often has multiple containment facets — a desk has drawers (container), a top surface, and space underneath. `ComplexContainer` solves this by using secret sub-objects:

```tads3
+ desk: ComplexContainer 'desk' 'desk'
    subContainer: ComplexComponent, OpenableContainer { }
    subSurface: ComplexComponent, Surface { bulkCapacity = 5 }
    subUnderside: ComplexComponent, Underside { }
;
```

All player-facing commands are remapped to the appropriate sub-object:

| Command | Routed to |
|---------|-----------|
| PUT IN / OPEN / CLOSE / LOCK | `subContainer` |
| PUT ON | `subSurface` |
| PUT UNDER / LOOK UNDER | `subUnderside` |
| PUT BEHIND / LOOK BEHIND | `subRear` |

The sub-objects use the `ComplexComponent` mixin, which:

- Sets location to the lexical parent automatically
- Uses the parent's name in messages ("The desk contains..." not "The sub-container contains...")
- Hides from ALL/EVERYTHING commands
- Reports its identity as the parent object

Initial placement uses the `subLocation` property pointer:

```tads3
++ pen: Thing 'pen' 'pen' subLocation = &subSurface ;
++ key: Thing 'key' 'key' subLocation = &subContainer ;
```

---

## Reachability

Reachability answers the question: "Can the actor physically touch this object?" It is the gate for most physical actions — Take, Open, Push, PutIn all require touch access.

### The touch path algorithm

When the `touchObj` precondition fires (at `precond.t:419`), it runs:

```
1. sourceObj.canTouch(obj)?
   │
   ├── yes → done
   │
   └── no → find and remove obstructors
         │
         ├── Get containment path: sourceObj.getTouchPathTo(obj)
         │
         ├── Walk path: for each element, call checkTouchViaPath(src, dest, op)
         │     │
         │     ├── success → continue to next element
         │     └── failure → this element is the obstructor
         │
         ├── Try implicit action: obstructor.tryImplicitRemoveObstructor(touch, obj)
         │     │
         │     ├── success (e.g., implicit OPEN) → loop back to step 1
         │     └── failure → report obstruction and exit
         │
         └── Track past obstructors to prevent infinite loops
```

### checkTouchViaPath — the boundary gate

Each object along the containment path gets a `checkTouchViaPath(source, dest, operation)` call. The base Thing implementation delegates to `checkMoveViaPath()`, which returns success by default — most objects don't obstruct touch.

`BasicContainer` overrides this with the key logic:

- **`PathOut` to self** — always allowed. An actor inside a container can always touch the container's interior.
- **`PathIn` or `PathOut`** — if the container is closed, touch is blocked. If open but the object can't fit through the opening (`canObjReachThruOpening`), touch is still blocked.

This is what makes a closed glass jar interesting: `transSensingIn(sight)` returns `transparent` (you can see through glass), but `checkTouchViaPath` returns failure (you can't reach through a closed container). The object is in scope — you can refer to it — but the `touchObj` precondition blocks physical manipulation.

### Implicit obstruction removal

When `checkTouchViaPath` fails, the obstructor gets a chance to fix the problem. `Openable` containers override `tryImplicitRemoveObstructor()` to attempt an implicit OPEN. If the open succeeds, the touch path is re-evaluated. This cascading loop is how TADS 3 generates messages like "(first opening the chest)" before a TAKE command.

The loop tracks previously encountered obstructors to prevent infinite cycles — if the same obstructor appears twice, the system gives up.

### The touchObj precondition

`touchObj` has `preCondOrder = 200`, deliberately running **after** most other preconditions. This is because touch reachability is fragile — other preconditions that move the actor (like `actorDirectlyInRoom`) or change containment might undo the implicit action that made the object touchable. Running last minimizes this problem.

During the verify phase, `touchObj` adjusts disambiguation rankings:

| Condition | Effect |
|-----------|--------|
| Object visible but at `distant` transparency | Marked inaccessible (too far to reach) |
| Object visible but not reachable | Likelihood reduced to 80 (might be fixable) |
| Object audible but not visible | "You can hear it but can't see it" |
| Too dark to see | Reports darkness |

### OutOfReach — custom reachability

The `OutOfReach` mixin provides fine-grained control over which directions reach works:

```tads3
highShelf: OutOfReach, Surface, Fixture 'high shelf' 'shelf'
    canObjReachContents(obj) { return obj.isIn(ladder); }
    cannotReachFromOutsideMsg(dest)
        { return 'The shelf is too high to reach. '; }
;
```

| Override | Controls |
|----------|----------|
| `canObjReachSelf(obj)` | Can `obj` touch this object? |
| `canObjReachContents(obj)` | Can `obj` touch things inside this object? |
| `canReachSelfFromInside(obj)` | Can `obj` inside this touch this object? |
| `canReachFromInside(obj, dest)` | Can `obj` inside this reach `dest` outside? |

---

## Bulk and Weight

### The capacity system

Every Thing has intrinsic `bulk` (default 1) and `weight` (default 1). The key distinction: **bulk is external only** by default (a box takes up the same space whether full or empty), while **weight is always recursive** (a full box weighs more than an empty one).

| Method | What it returns |
|--------|-----------------|
| `getBulk()` | Intrinsic `bulk` (does not include contents) |
| `getWeight()` | Intrinsic `weight` + sum of all contents' weights (recursive) |
| `getBulkWithin()` | Sum of `getBulk()` for all direct contents |
| `getEncumberingBulk(actor)` | How much bulk this uses in an actor's hands (0 if worn) |
| `getEncumberingWeight(actor)` | How much weight this adds to an actor's load |

`StretchyContainer` is the exception to the bulk rule — it overrides `getBulk()` to include contents, modeling objects like cloth bags that expand when filled.

### Speculative testing with whatIf

Capacity checks must run *before* the actual move, but they need to know what the state *would be* after the move. The `whatIf(func, [changes])` method solves this:

```tads3
whatIf({: checkBulkInserted(obj)}, &moveInto, self)
```

This temporarily applies property changes using `baseMoveInto` (no side effects), calls the test function, then restores the original state. If the test throws an exception (capacity exceeded), the state is still restored before the exception propagates.

### Actor carrying capacity

Actors are containers too. Their defaults are deliberately generous:

| Property | Default | Meaning |
|----------|---------|---------|
| `bulkCapacity` | 10000 | Effectively unlimited |
| `maxSingleBulk` | 10 | Individual item size limit |
| `weightCapacity` | 10000 | Effectively unlimited |

The source code at `actor.t:6314` contains a notable editorial: *"Many authors worry that it's unrealistic if the player character can carry too much... Be advised that authors love this sort of 'realism' a whole lot more than players do."*

### BagOfHolding

When an actor's hands are too full, `tryMakingRoomToHold()` attempts to implicitly move items into `BagOfHolding` containers. The algorithm:

1. Check if the new object alone is too heavy or bulky — if so, fail immediately
2. Gather all held items with their bag affinities (how strongly each bag "wants" each item)
3. Protect the two most recently picked up items from being shuffled (to prevent annoying behavior)
4. Sort remaining items by affinity and move them into bags until enough room is freed

Each `BagOfHolding` returns an affinity score (0–200) for each object: 0 means "cannot hold," 50 means "reluctant," 100 is the default, and 200 means special affinity (a sword sheath for swords).

---

## Nested Rooms and Staging

### NestedRoom — locations within locations

A `NestedRoom` is any object that isn't a Room but can contain an actor: chairs, beds, platforms, vehicles. The key design principle: moving between a room and a nested room within it is **not travel**. It does not trigger `travelTo()` — instead it uses `travelWithin()`, which skips arrival/departure messages and connector processing.

```
Room
  └── NestedRoom (chair, bed, platform, booth)
        └── Actor (sitting, lying, standing)
```

| Class | Posture | Drop destination | Key behavior |
|-------|---------|-----------------|--------------|
| `BasicChair` | sitting | Enclosing room | Dropped items fall to the floor |
| `Chair` | sitting | Enclosing room | BasicChair + Surface |
| `BasicBed` | lying | Enclosing room | Can sit, lie, or stand |
| `Bed` | lying | Enclosing room | BasicBed + Surface |
| `BasicPlatform` | standing | **Self** | Dropped items stay on the platform |
| `Platform` | standing | **Self** | BasicPlatform + Surface |
| `Booth` | standing | **Self** | BasicPlatform + Container (enclosed) |
| `Vehicle` | varies | varies | NestedRoom + Traveler; moves with the actor |

The `getDropDestination()` distinction matters: dropping an item from a chair puts it on the floor (the chair's enclosing room), but dropping an item on a platform leaves it on the platform. This models the physical difference — things fall off chairs but stay on elevated surfaces.

### Staging locations

The staging location system prevents puzzle-breaking shortcuts. Before an actor can enter a nested room, the system checks that the actor is in a valid **staging location** — typically the room that directly contains the nested room.

```
Actor wants to SIT ON chair
     │
     ├── checkActorReadyToEnterNestedRoom()
     │     │
     │     ├── Already directly in chair? → done
     │     │
     │     ├── In staging location? → done
     │     │
     │     └── Not in staging location?
     │           ├── Find best staging location (chooseStagingLocation)
     │           ├── Validate (checkStagingLocation)
     │           └── Move actor there (checkMovingActorInto, may be implicit)
     │
     └── tryMovingIntoNested() → implicit SIT ON
```

`stagingLocations` defaults to `[location]` — the nested room's direct container. For a chair on a stage, the actor must be standing on the stage before sitting in the chair. This prevents an actor in the audience from sitting directly in a chair on stage without first climbing up.

`HighNestedRoom` sets `stagingLocations = []` (empty), meaning no one can reach it by default. The game must dynamically manage the list — placing a ladder under a high shelf, for example, could add the room to its staging locations.

`isStagingLocationKnown(loc)` defaults to `true`. Set it to `nil` to prevent automatic implied travel, forcing the player to explicitly figure out how to reach the staging location.

### Room scope and extra scope items

Rooms and nested rooms add items to scope beyond the standard sensory scan:

- **Room** adds its floor to scope when the actor is directly inside — you can always refer to "the floor" even in the dark, because you're physically standing on it.
- **NestedRoom** adds itself to scope when the actor is directly inside — you know you're sitting in a chair even if you can't see it.
- Both call `getExtraScopeItems(actor)`, which game code can override to add puzzle-relevant objects.

---

## Multi-Location Objects

The standard containment tree is single-parent, but some objects logically exist in multiple places. TADS 3 provides three classes for this, each with different semantics.

### MultiLoc — one object, many locations

A `MultiLoc` exists **entirely and simultaneously** in all its locations. There is one object instance, but it appears in the `contents` list of every container in its `locationList`.

```tads3
window: SenseConnector, MultiLoc, Fixture 'window' 'window'
    locationList = [bedroom, garden]
    connectorMaterial = glass
;
```

Good for: overlapping locations (a statue at the center of a square), sense connections (a window between rooms), distant objects (the moon visible from multiple outdoor rooms).

Key behavior:

- `isIn(obj)` checks both direct and transitive containment through any location
- `baseMoveInto(newContainer)` removes from all locations and moves to a single one
- `moveIntoAdd(newContainer)` adds a new location without removing old ones
- `moveOutOf(container)` removes from one location
- A MultiLoc does **not** connect its locations for sense purposes by default. Combine with `SenseConnector` to bridge senses across locations.

### MultiInstance — separate copies

`MultiInstance` creates **independent copies** of a template object in each location. Each copy has its own sense information, state, and identity.

```tads3
trees: MultiInstance
    locationList = [forest1, forest2, forest3]
    instanceObject: Fixture { 'trees' 'trees'
        "Many tall trees grow here. "
        isPlural = true
    }
;
```

Each location gets its own "trees" object. The instances are marked `isEquivalent = true`, so the parser treats them as interchangeable.

Good for: repeated decorations (trees, rocks, streetlamps), where each location needs its own independent copy.

### MultiFaceted — facets of one object

`MultiFaceted` extends `MultiInstance` but tracks instances as **facets** of a single conceptual object. Pronoun references carry across facets — if you EXAMINE RIVER in one room, "it" refers to the river facet in the next room.

```tads3
river: MultiFaceted
    locationList = [clearing, bridge, waterfall]
    instanceObject: Fixture { 'river/water' 'river'
        "The river flows swiftly past. "
    }
;
```

Good for: objects that span multiple locations — rivers, long walls, ropes, roads.

---

## Practical Intervention Points

### Controlling containment

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `location` | Property on Thing (set via `+` or `@`) | Initial placement in containment tree |
| `moveInto(dest)` | Call on Thing | Move an object with full notifications and sense-path updates |
| `baseMoveInto(dest)` | Call on Thing | Move silently (no notifications — use for setup, not gameplay) |
| `notifyInsert(obj, newCont)` | Override on container | React to objects being placed inside (bulk checks, puzzle triggers) |
| `notifyRemove(obj)` | Override on container | React to objects being removed |
| `verifyInsert(obj, newCont)` | Override on container | Veto insertion during verify phase (circular containment) |
| `isIn(obj)` / `isDirectlyIn(obj)` | Call on Thing | Test containment relationships |

### Controlling capacity

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `bulk` / `weight` | Properties on Thing | Set intrinsic size and weight (default: 1 each) |
| `bulkCapacity` | Property on BulkLimiter | Maximum total bulk of all contents |
| `maxSingleBulk` | Property on BulkLimiter | Maximum bulk of any single item |
| `weightCapacity` | Property on Actor | Maximum carrying weight |
| `getBulk()` | Override on Thing | Dynamic bulk (StretchyContainer uses this) |
| `getWeight()` | Override on Thing | Dynamic weight |
| `getEncumberingBulk(actor)` | Override on Thing | Worn items return 0; struggling animals return more |
| `BagOfHolding` | Mix in with Container | Auto-stash items when actor's hands are full |
| `affinityFor(obj)` | Override on BagOfHolding | Control which items a bag prefers to hold |
| `checkBulkInserted(obj)` | Override on BulkLimiter | Custom capacity rules |

### Controlling reachability

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `checkTouchViaPath(src, dest, op)` | Override on Thing | Custom touch obstruction at a containment boundary |
| `checkMoveViaPath(src, dest, op)` | Override on Thing | Custom movement obstruction (taking objects in/out) |
| `canFitObjThruOpening(obj)` | Override on BasicContainer | Narrow-mouthed containers |
| `canObjReachThruOpening(obj)` | Override on BasicContainer | Whether a hand fits through |
| `tryImplicitRemoveObstructor()` | Override on Thing | Custom implicit action to clear a touch obstruction |
| `OutOfReach` | Mix in with any Thing | Directional reach control (high shelves, deep pits) |
| `canObjReachSelf(obj)` | Override on OutOfReach | Who can touch this object |
| `canObjReachContents(obj)` | Override on OutOfReach | Who can reach inside this object |
| `touchObj` | Precondition on actions | Enforce touch reachability (preCondOrder 200) |

### Controlling open/close and lock/unlock

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `isOpen` | Property on BasicContainer | Current open/closed state |
| `makeOpen(stat)` | Call on Openable | Change state (supports linked objects) |
| `initiallyOpen` | Property on Openable | Starting state (default: closed) |
| `isLocked` / `makeLocked(stat)` | On Lockable | Lock/unlock state and control |
| `initiallyLocked` | Property on Lockable | Starting state (default: locked) |
| `lockStatusObvious` | Property on Lockable | Whether lock state is visible to the player |
| `material` | Property on BasicContainer | What senses pass through when closed |
| `transSensingIn(sense)` | Override on BasicContainer | Custom per-sense transparency (open/closed aware) |
| `transSensingOut(sense)` | Override on BasicContainer | Asymmetric transparency (one-way mirrors) |

### Controlling nested rooms

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `stagingLocations` | Property on NestedRoom | Valid intermediate locations for entry |
| `exitDestination` | Property on NestedRoom | Where actor goes on GET OUT |
| `getDropDestination(obj, path)` | Override on location | Where dropped objects land |
| `isStagingLocationKnown(loc)` | Override on NestedRoom | Prevent automatic implied travel (puzzles) |
| `defaultPosture` | Property on NestedRoom | Posture on entry (sitting, lying, standing) |
| `tryMovingIntoNested()` | Override on NestedRoom subclass | Custom entry action (SIT ON, LIE ON, BOARD) |
| `tryRemovingFromNested()` | Override on NestedRoom subclass | Custom exit action |
| `HighNestedRoom` | Class | Nested room with no staging locations (unreachable by default) |

### Controlling multi-location objects

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `locationList` | Property on BaseMultiLoc | Initial set of locations |
| `initialLocationClass` | Property on BaseMultiLoc | Restrict auto-detection to a class |
| `isInitiallyIn(obj)` | Override on BaseMultiLoc | Dynamic initial location selection |
| `moveIntoAdd(loc)` | Call on MultiLoc | Add a new location at runtime |
| `moveOutOf(loc)` | Call on MultiLoc | Remove a location at runtime |
| `instanceObject` | Property on MultiInstance | Template for creating per-location copies |

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [Sense and Perception](sense-perception.md) for how sense paths trace through the containment tree. For how scope connects to noun resolution, see [Action Resolution](action-resolution.md). For how actions produce player-visible text, see the [Message System](message-system.md).*
