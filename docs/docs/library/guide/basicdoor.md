# BasicDoor

BasicDoor: [BasicOpenable](basicopenable.md), [ThroughPassage](throughpassage.md)

A BasicDoor encapsulates the behaviour common to both [Door](door.md) and [SecretDoor](secretdoor.md) and their descendents, and is thus intended as an abstract class containing the common behaviour of door-like objects, rather than as a class that a game author would use directly in a game. If you wanted to a special kind of door that didn't fit either Door or SecretDoor (and their descendents) you might want to derive it from this class.

The framework provided by BasicDoor does the following:

- Provides a getFacets routine which makes both sides of a BasicDoor facets of each other (assuming one of the doors points to the other as its other side).

- Overrided makeOpen to keep both sides of a BasicDoor in sync with each other when one side is opened or closed.

- Provides routines for noting and describing a remote opening of the door (to cope with the situation where a door is opened or closed from the other side from that on which the player character is on).

- Provides handling for executing TravelVia the BasicDoor

- Boost the likelihood that this door is the object of commands like LOCK or CLOSE if this is the last door-like object the PC has traversed.
