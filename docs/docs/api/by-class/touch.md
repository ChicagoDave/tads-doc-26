# touch

*object* — defined in [sense.t](../by-file/sense.t.md) (line 271)


**Superclass chain:** [Sense](sense.md) > `object` > **touch**


## Properties


### `presenceProp` *(overridden)*

Defined in sense.t, line 274


### `sizeProp` *(overridden)*

Defined in sense.t, line 273


### `thruProp` *(overridden)*

Defined in sense.t, line 272


## Inherited Properties


*From [Sense](sense.md):* [`ambienceProp`](sense.md#ambienceProp)


## Methods


### `canObjBeSensed(obj, trans, ambient)` *(overridden)*

Defined in sense.t, line 281

Override canObjBeSensed for touch. Unlike other senses, touch requires physical contact with an object, so it cannot operate at a distance, regardless of the size of an object.
