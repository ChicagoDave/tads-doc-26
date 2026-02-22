# SightTouchInfo

*class* — defined in [thing.t](../by-file/thing.t.md) (line 1016)


A small data structure class recording SenseInfo objects for sight and touch. We use this to pick the best facet from a list of facets.


**Superclass chain:** `object` > **SightTouchInfo**


## Properties


### `obj_`

Defined in thing.t, line 1030

the object we're associated with


### `touchInfo`

Defined in thing.t, line 1034


### `visInfo`

Defined in thing.t, line 1033

our SenseInfo objects for sight and touch


## Methods


### `construct(actor, obj)`

Defined in thing.t, line 1017


### `selectBetter(a, b)`

Defined in thing.t, line 1042

Class method: select the "better" of two SightTouchInfo's. Returns the one with the more transparent visual status, or, visual transparencies being equal, the one with the more transparent touch status.
