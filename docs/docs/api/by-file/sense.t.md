# sense.t


## Classes

- [DistanceConnector](../by-class/distanceconnector.md)
- [DropTypeShortThrow](../by-class/droptypeshortthrow.md)
- [Material](../by-class/material.md)
- [Occluder](../by-class/occluder.md)
- [Sense](../by-class/sense.md)
- [SenseConnector](../by-class/senseconnector.md)


## Global Objects

- [adventium](../by-class/adventium.md)
- [coarseMesh](../by-class/coarsemesh.md)
- [fineMesh](../by-class/finemesh.md)
- [glass](../by-class/glass.md)
- [paper](../by-class/paper.md)
- [sight](../by-class/sight.md)
- [smell](../by-class/smell.md)
- [sound](../by-class/sound.md)
- [touch](../by-class/touch.md)
- adjustBrightness
- transparencyAdd
- transparencyCompare


## Functions


### `adjustBrightness(br, trans)`

Defined in sense.t, line 383

Given a brightness level and a transparency level, compute the brightness as modified by the transparency level.


### `transparencyAdd(a, b)`

Defined in sense.t, line 299

"Add" two transparency levels, yielding a new transparency level. This function can be used to determine the result of passing a sense through multiple layers of material.


### `transparencyCompare(a, b)`

Defined in sense.t, line 328

Compare two transparency levels to determine which one is more transparent. Returns 0 if the two levels are equally transparent, 1 if the first one is more transparent, and -1 if the second one is more transparent. The comparison follows this rule:
