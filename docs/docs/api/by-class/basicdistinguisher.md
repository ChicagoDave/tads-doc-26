# basicDistinguisher

*object* — defined in [disambig.t](../by-file/disambig.t.md) (line 101)


"Basic" Distinguisher. This distinguisher can tell two objects apart if one or the other object is not marked as isEquivalent, OR if the two objects don't have an identical superclass list. This distinguisher thus can tell apart objects unless they're "basic equivalents," marked with isEquivalent and having the same equivalence keys.


**Superclass chain:** [Distinguisher](distinguisher.md) > `object` > **basicDistinguisher**


## Methods


### `aName(obj)`

Defined in en_us.t, line 3523


### `canDistinguish(a, b)` *(overridden)*

Defined in disambig.t, line 102


### `countName(obj, cnt)`

Defined in en_us.t, line 3525


### `name(obj)`

Defined in en_us.t, line 3522


### `theName(obj)`

Defined in en_us.t, line 3524


## Inherited Methods


*From [Distinguisher](distinguisher.md):* [`matchName`](distinguisher.md#matchName), [`notePrompt`](distinguisher.md#notePrompt), [`objInScope`](distinguisher.md#objInScope)
