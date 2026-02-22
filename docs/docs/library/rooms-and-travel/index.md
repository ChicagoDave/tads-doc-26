# Rooms & Travel

Rooms are the fundamental units of geography in an adv3 game. Every location the player can visit is a `Room` or one of its subclasses. Travel between rooms happens through direction properties, `TravelConnector` objects, doors, passages, and other connector types.

For the full class hierarchy diagram, see the [Architecture Overview](../../architecture/overview.md#rooms-and-travel). For a practical introduction to building rooms and connections, see the [IF Development Guide](../../architecture/development-guide.md#rooms-directions-and-travel).

---

## Rooms

A Room is a location with a name, description, and direction properties. It can contain objects and actors.

- [Room](../guide/room.md) — the base room class; properties, descriptions, and basic usage
- [Room Template](../guide/roomtemplate.md) — shorthand syntax for defining rooms
- [OutdoorRoom](../guide/outdoorroom.md) — a room with sky and ground instead of ceiling and floor
- [DarkRoom](../guide/darkroom.md) — a room with no ambient light; requires a light source to see
- [ShipboardRoom](../guide/shipboardroom.md) — a room on a ship; adds port/starboard/fore/aft directions
- [FloorlessRoom](../guide/floorlessroom.md) — a room with no floor; dropped objects fall below
- [Floorless](../guide/floorless.md) — the mix-in class for floorless behavior
- [RoomParts](../guide/roomparts.md) — walls, floor, ceiling — the structural elements of a room
- [inRoomName](../guide/inroomname.md) — customizing "in the living room" text for nested descriptions

## Room Connections

The simplest connection is a direction property (`north = otherRoom`). For more complex connections — messages, conditions, one-way travel — use a connector class.

- [TravelConnector](../guide/travelconnector.md) — the base class for all connectors; properties and interface
- [RoomConnector](../guide/roomconnector.md) — a two-way connection between rooms
- [OneWayRoomConnector](../guide/onewayroomconnector.md) — a one-way connection
- [OneWayRoomConnector Template](../guide/onewayroomconnectortemplate.md) — shorthand syntax
- [RoomAutoConnector](../guide/roomautoconnector.md) — automatic two-way connection (Room itself is one)
- [AsExit](../guide/asexit.md) — making one direction equivalent to another

## Travel Messages

Connectors that display messages when traversed, or that explain why travel fails.

- [TravelWithMessage](../guide/travelwithmessage.md) — a mix-in that adds a message to travel
- [TravelMessage](../guide/travelmessage.md) — a connector that displays a message on traversal
- [TravelMessage Template](../guide/travelmessagetemplate.md) — shorthand syntax
- [NoTravelMessage](../guide/notravelmessage.md) — a connector that blocks travel with a message
- [NoTravelMessage Template](../guide/notravelmessagetemplate.md) — shorthand syntax
- [FakeConnector](../guide/fakeconnector.md) — blocks travel with a contextual explanation
- [DeadEndConnector](../guide/deadendconnector.md) — allows travel but immediately returns the player
- [cannotGoThatWay](../guide/cannotgothatway.md) — the default "you can't go that way" message
- [cannotGoThatWayInDark](../guide/cannotgothatwayindark.md) — the dark variant

## Passages and Doors

Physical objects that serve as connectors — things the player can see and interact with.

- [ThroughPassage](../guide/throughpassage.md) — a passage the player walks through
- [PathPassage](../guide/pathpassage.md) — a path leading to another location
- [ExitOnlyPassage](../guide/exitonlypassage.md) — a passage that can only be used from one side
- [Door](../guide/door.md) — an openable two-sided passage
- [BasicDoor](../guide/basicdoor.md) — the base door class without open/close behavior
- [SecretDoor](../guide/secretdoor.md) — a door that is hidden until discovered
- [HiddenDoor](../guide/hiddendoor.md) — a variant of SecretDoor
- [AutoClosingDoor](../guide/autoclosingdoor.md) — a door that closes itself after the player passes through

## Stairs

Vertical passages connecting rooms.

- [StairwayUp](../guide/stairwayup.md) — stairs leading up
- [StairwayDown](../guide/stairwaydown.md) — stairs leading down

## Portals and Enterable Objects

Objects that the player can enter or exit, connecting to another location.

- [Enterable](../guide/enterable.md) — a Fixture that the player can enter, connecting to a room
- [Enterable Template](../guide/enterabletemplate.md) — shorthand syntax
- [EntryPortal](../guide/entryportal.md) — an entry-side portal object
- [ExitPortal](../guide/exitportal.md) — an exit-side portal object

## Travel Restrictions

Mechanisms for controlling when and whether travel is allowed.

- [TravelBarrier](../guide/travelbarrier.md) — an object that can block travel through a connector
- [AskConnector](../guide/askconnector.md) — asks which way the player wants to go when a direction is ambiguous
- [PushTravelBarrier](../guide/pushtravelbarrier.md) — a barrier specific to pushing objects between rooms

## Push Travel

Moving large objects between rooms by pushing them.

- [TravelPushable](../guide/travelpushable.md) — an object that can be pushed between rooms

## Travel Events and Notifications

What happens when actors travel — messages, notifications, and customization points.

- [roomXxxxAction](../guide/roomxxxxaction.md) — room methods called before/after travel actions
- [TravelerArriving](../guide/travelerarriving.md) — customizing arrival messages
- [roomDarkTravel](../guide/roomdarktravel.md) — travel behavior in dark rooms

## Nested Rooms

Objects within a room that actors can occupy — see the [Things](../things/index.md#nested-rooms) section for the full listing of Chair, Bed, Platform, Booth, Vehicle, and other NestedRoom classes.

## NPC Travel

For NPC travel (making actors move between rooms on their own), see [NPC Travel](../actors/npc-travel.md), and the Tour Guide pages on [AccompanyingInTravelState](../guide/accompanyingintravelstate.md) and [GuidedInTravelState](../guide/guidedintravelstate.md).
