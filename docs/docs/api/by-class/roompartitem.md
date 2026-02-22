# RoomPartItem

*class* — defined in [travel.t](../by-file/travel.t.md) (line 5532)


A "room part item" is an object that's specially described as being part of, or attached to, a RoomPart (a wall, ceiling, floor, or the like). This is a mix-in class that can be combined with any ordinary object class (but usually with something non-portable, such as a Fixture or Immovable). The effect of adding RoomPartItem to an object's superclasses is that a command like EXAMINE EAST WALL (or whichever room part the object is associated with) will display the object's specialDesc, but a simple LOOK will not. This class is sometimes useful for things like doors, windows, ceiling fans, and other things attached to the room.


**Superclass chain:** `object` > **RoomPartItem**


## Methods


### `useSpecialDescInContents(cont)`

Defined in travel.t, line 5566


### `useSpecialDescInRoom(room)`

Defined in travel.t, line 5565

don't use the special description in room descriptions, or in examining any other container


### `useSpecialDescInRoomPart(part)`

Defined in travel.t, line 5537

show our special description when examining our associated room part, as long as we actually define a special description
