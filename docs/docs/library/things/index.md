# Things

Everything the player can see, touch, take, or interact with in an adv3 game is a `Thing` or one of its many descendants. The Thing class hierarchy is the foundation of the physical world model.

Things vary along three axes: **portability** (can it be picked up?), **containment** (does it hold other objects?), and **state** (can it be opened, locked, switched?). Most library classes combine these axes through mix-in composition — an `OpenableContainer` is an `Openable` mixed with a `Container`, a `KeyedContainer` adds `LockableWithKey` to that, and so on.

For the full class hierarchy diagram, see the [Architecture Overview](../../architecture/overview.md#things). For a practical introduction to using Things in your game, see the [IF Development Guide](../../architecture/development-guide.md#the-thing-hierarchy).

---

## The Basics

Every Thing needs vocabulary words (for the parser), a name (for display), and a description (for EXAMINE). The library provides template syntax that makes this compact.

- [Thing - Introduction](../guide/thing-introduction.md) — what a Thing is, the role it plays in the world model
- [Thing - The Basics](../guide/thing-thebasics.md) — essential properties every Thing should define
- [vocabWords](../guide/vocabwords.md) — the vocabulary format: adjectives, nouns, and how the parser matches them
- [disambigName](../guide/disambigname.md) — controlling disambiguation prompts
- [globalParamName](../guide/globalparamname.md) — registering objects for use in message substitutions
- [setSuperclassList](../guide/setsuperclasslist.md) — dynamically changing an object's class at runtime

## Descriptions and Listings

How objects appear in room descriptions, inventory lists, and EXAMINE output.

- [specialDesc](../guide/specialdesc.md) — standalone paragraphs in room descriptions
- [initDesc & initSpecialDesc](../guide/initdesc+initspecialdesc.md) — descriptions that change after the object is first moved
- [described](../guide/described.md) — controlling whether an object appears in listings at all
- [Bulk and Weight](../guide/bulkandweight.md) — the size system for containers

## Non-Portable Objects

Objects that cannot be picked up. Use these for scenery, structural features, and distant objects.

- [Introduction to Non-Portables](../guide/nonportableintroduction.md) — when and why to use non-portable objects
- [Fixture](../guide/fixture.md) — permanently attached; blocks TAKE but allows most other interactions
- [CustomFixture](../guide/customfixture.md) — a Fixture with customizable refusal messages
- [Component](../guide/component.md) — a Fixture that is part of another object
- [Decoration](../guide/decoration.md) — scenery that blocks most interactions with "not important"
- [Unthing](../guide/unthing.md) — intercepts a noun phrase to explain an object's absence
- [Distant](../guide/distant.md) — visible but too far away to interact with
- [Immovable](../guide/immovable.md) — cannot be taken but otherwise interactable
- [CustomImmovable](../guide/customimmovable.md) — an Immovable with customizable messages
- [Heavy](../guide/heavy.md) — an Immovable that explains it is too heavy to lift

## Containers and Surfaces

Objects that hold other objects, either inside or on top.

- [Introduction to Containers](../guide/containers-introduction.md) — how containment works in adv3
- [BulkLimiter](../guide/bulklimiter.md) — the base class for anything with capacity limits
- [BasicContainer](../guide/basiccontainer.md) — a container without open/close behavior
- [Container](../guide/container.md) — the standard container; things go inside
- [OpenableContainer](../guide/openablecontainer.md) — a container that can be opened and closed
- [RestrictedContainer](../guide/restrictedcontainer.md) — limits what can be put inside
- [SingleContainer](../guide/singlecontainer.md) — holds only one object at a time
- [Surface](../guide/surface.md) — things rest on top
- [Underside](../guide/underside.md) — things go underneath
- [RearContainer](../guide/rearcontainer.md) — things go behind
- [RearSurface](../guide/rearsurface.md) — things rest on the back surface
- [ComplexContainer](../guide/complexcontainer.md) — an object that is both a container and a surface
- [ContainerDoor](../guide/containerdoor.md) — a door that belongs to a container
- [SpaceOverlay](../guide/spaceoverlay.md) — combining containment types
- [StretchyContainer](../guide/stretchycontainer.md) — container with flexible bulk capacity
- [Dispenser](../guide/dispenser.md) — dispenses objects when taken from
- [BagOfAffinity](../guide/bagofaffinity.md) — automatically stores items of a certain type
- [notifyInsert & notifyRemove](../guide/notifyinsert+notifyremove.md) — hooks for containment changes

## Locks and Keys

Lockable objects and the key system.

- [Introduction to Locks & Keys](../guide/locks+keys-introduction.md) — the locking model
- [Lockable](../guide/lockable.md) — adds lock/unlock without requiring a key
- [LockableWithKey](../guide/lockablewithkey.md) — requires a specific key to unlock
- [LockableContainer](../guide/lockablecontainer.md) — a lockable openable container
- [KeyedContainer](../guide/keyedcontainer.md) — a keyed lockable container
- [IndirectLockable](../guide/indirectlockable.md) — locked/unlocked by an indirect mechanism
- [Openable](../guide/openable.md) — open/close behavior as a standalone mix-in
- [BasicOpenable](../guide/basicopenable.md) — minimal open/close without the full Openable interface
- [KeyRing](../guide/keyring.md) — a key ring that tries keys automatically

## Light and Fire

Light sources and fire-related objects.

- [Introduction to Light & Fire](../guide/lightandfire-introduction.md) — how the lighting model works
- [Brightness](../guide/brightness.md) — the brightness scale (0-4)
- [LightSource](../guide/lightsource.md) — any object that emits light
- [Flashlight](../guide/flashlight.md) — a switchable light source
- [Candle](../guide/candle.md) — a light source that burns down
- [OilLamp](../guide/oillamp.md) — a refillable light source
- [Matchstick & Matchbook](../guide/matchstick+matchbook.md) — single-use fire sources
- [Dynamite](../guide/dynamite.md) — a fused explosive (example of Fuse + LightSource)

## Other Thing Subclasses

- [Readable](../guide/readable.md) — objects with readable text
- [Food](../guide/food.md) — edible objects
- [Wearable](../guide/wearable.md) — objects that can be worn
- [Hidden](../guide/hiding+fiding-introduction.md) — objects that start hidden until discovered
- [MultiLoc](../guide/multiloc.md) — objects that exist in multiple locations simultaneously

## Nested Rooms

Objects that an actor can be "in" or "on" — chairs, beds, platforms, vehicles.

- [NestedRoom Overview](../guide/nestedroomoverview.md) — the class hierarchy and how nested rooms work
- [NestedRoom](../guide/nestedroom.md) — the base class
- [Chair](../guide/chair.md) — sitting furniture
- [Bed](../guide/bed.md) — lying furniture
- [Platform](../guide/platform.md) — standing surface
- [Booth](../guide/booth.md) — an enclosed nested room (container + platform)
- [HighNestedRoom](../guide/highnestedroom.md) — a nested room that makes objects below out of reach
- [Vehicle](../guide/vehicle.md) — a mobile nested room

## Templates

Shorthand syntax for defining Things and their properties.

- [Templates](../guide/templates.md) — the template syntax for Thing and its subclasses
