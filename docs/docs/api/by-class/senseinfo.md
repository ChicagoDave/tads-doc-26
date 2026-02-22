# SenseInfo

*class* — defined in [thing.t](../by-file/thing.t.md) (line 31)


Sense Information entry. Thing.senseInfoTable() returns a list of these objects to provide full sensory detail on the objects within range of a sense.


**Superclass chain:** `object` > **SenseInfo**


## Properties


### `ambient`

Defined in thing.t, line 60

the ambient sense energy level at this object


### `obj`

Defined in thing.t, line 51

the object being sensed


### `obstructor`

Defined in thing.t, line 57

the obstructor that introduces a non-transparent value of trans


### `trans`

Defined in thing.t, line 54

the transparency from the point of view to this object


## Methods


### `compareTransTo(other)`

Defined in thing.t, line 68

compare this SenseInfo object's transparency to the other one; returns a number greater than zero if 'self' is more transparent, zero if they're equally transparent, or a negative number if 'self' is less transparent


### `construct(obj, trans, obstructor, ambient)`

Defined in thing.t, line 32


### `selectMoreTrans(a, b)`

Defined in thing.t, line 76

Return the more transparent of two SenseInfo objects. Either argument can be nil, in which case we'll return the non-nil one; if both are nil, we'll return nil. If they're equal, we'll return the first one.
