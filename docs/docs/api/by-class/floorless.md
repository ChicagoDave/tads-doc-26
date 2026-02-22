# Floorless

*class* — defined in [travel.t](../by-file/travel.t.md) (line 4799)


Make a room "floorless." This is a mix-in class that you can include in a superclass list ahead of Room or any of its subclasses to create a room where support is provided by some means other than standing on a surface, or where there's simply no support. Examples: hanging on a rope over a chasm; climbing a ladder; in free-fall after jumping out of a plane; levitating in mid-air.


**Superclass chain:** `object` > **FloorlessSubclasses:** [FloorlessRoom](floorlessroom.md)


## Properties


### `bottomRoom`

Defined in travel.t, line 4818

The room below, if any - this is where objects dropped here will actually end up. By default, this is nil, which means that objects dropped here simply disappear from the game. If there's a "bottom of chasm" location where dropped objects should land, provide it here.


### `roomParts`

Defined in travel.t, line 4809

Omit the default floor/ground objects from the room parts list. Room classes generally have static room parts lists, so calculate this once per instance and store the results.


## Methods


### `receiveDrop(obj, desc)`

Defined in travel.t, line 4821

receive a dropped object
