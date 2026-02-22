# locationDistinguisher

*object* — defined in [disambig.t](../by-file/disambig.t.md) (line 218)


Location Distinguisher. This distinguisher identifies objects purely by their immediate locations.


**Superclass chain:** [Distinguisher](distinguisher.md) > `object` > **locationDistinguisher**


## Methods


### `aName(obj)`

Defined in en_us.t, line 3556


### `canDistinguish(a, b)` *(overridden)*

Defined in disambig.t, line 219


### `countName(obj, cnt)`

Defined in en_us.t, line 3558


### `matchName(obj, origTokens, adjustedTokens, matchList, fullMatchList)` *(overridden)*

Defined in disambig.t, line 235

otherwise, use the inherited handling


### `name(obj)`

Defined in en_us.t, line 3555


### `notePrompt(lst)` *(overridden)*

Defined in en_us.t, line 3561

note that we're prompting based on this distinguisher


### `objInScope(obj, matchList, fullMatchList)` *(overridden)*

Defined in disambig.t, line 225

we tell the objects apart by their immediate locations


### `theName(obj)`

Defined in en_us.t, line 3557
