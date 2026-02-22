# nullDistinguisher

*object* — defined in [disambig.t](../by-file/disambig.t.md) (line 90)


A "null" distinguisher. This can tell two objects apart if they have different names (so it's inherently language-specific).


**Superclass chain:** [Distinguisher](distinguisher.md) > `object` > **nullDistinguisher**


## Methods


### `aName(obj)`

Defined in en_us.t, line 3510


### `canDistinguish(a, b)` *(overridden)*

Defined in en_us.t, line 3507

we can tell objects apart if they have different base names


### `countName(obj, cnt)`

Defined in en_us.t, line 3512


### `name(obj)`

Defined in en_us.t, line 3509


### `theName(obj)`

Defined in en_us.t, line 3511


## Inherited Methods


*From [Distinguisher](distinguisher.md):* [`matchName`](distinguisher.md#matchName), [`notePrompt`](distinguisher.md#notePrompt), [`objInScope`](distinguisher.md#objInScope)
