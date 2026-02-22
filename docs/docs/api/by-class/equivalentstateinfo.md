# EquivalentStateInfo

*class* — defined in [thing.t](../by-file/thing.t.md) (line 227)


Equivalent group state information. This keeps track of a state and the number of items in that state when we're listing a group of equivalent items in different states.


**Superclass chain:** `object` > **EquivalentStateInfo**


## Properties


### `stateNameProp`

Defined in thing.t, line 255

the property to evaluate to get the name for listing purposes


### `stateObj`

Defined in thing.t, line 252

the ThingState object describing the state


### `stateVec`

Defined in thing.t, line 258

list of items in this same state


## Methods


### `addEquivObj(obj)`

Defined in thing.t, line 240

add an object to the list of equivalent objects in this state


### `construct(st, obj, nameProp)`

Defined in thing.t, line 228


### `getEquivCount`

Defined in thing.t, line 243

get the number of equivalent items in the same state


### `getEquivList`

Defined in thing.t, line 246

get the list of equivalent items in the same state


### `getName`

Defined in thing.t, line 249

get the name to use for listing purposes
