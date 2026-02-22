# ownershipDistinguisher

*object* — defined in [disambig.t](../by-file/disambig.t.md) (line 129)


Ownership Distinguisher. This distinguisher can tell two objects apart if they have different owners. "Unowned" objects are identified by their immediate containers instead of their owners.


**Superclass chain:** [Distinguisher](distinguisher.md) > `object` > **ownershipDistinguisher**


## Methods


### `aName(obj)`

Defined in en_us.t, line 3534


### `canDistinguish(a, b)` *(overridden)*

Defined in disambig.t, line 130


### `countName(obj, cnt)`

Defined in en_us.t, line 3536


### `matchName(obj, origTokens, adjustedTokens, matchList, fullMatchList)` *(overridden)*

Defined in disambig.t, line 180

otherwise, use the inherited handling


### `name(obj)`

Defined in en_us.t, line 3533


### `notePrompt(lst)` *(overridden)*

Defined in en_us.t, line 3539

note that we're prompting based on this distinguisher


### `objInScope(obj, matchList, fullMatchList)` *(overridden)*

Defined in disambig.t, line 160

One or both objects are owned, so we can tell them apart if and only if they have different owners.


### `theName(obj)`

Defined in en_us.t, line 3535
