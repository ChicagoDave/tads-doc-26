# CanTouchInfo

*class* — defined in [thing.t](../by-file/thing.t.md) (line 94)


Can-Touch information. This object keeps track of whether or not a given object is able to reach out and touch another object.


**Superclass chain:** `object` > **CanTouchInfo**


## Properties


### `// canTouch`

Defined in thing.t, line 107

if we have calculated whether or not the source can touch the target, we'll set the property canTouch to nil or true accordingly; if this property is left undefined, this information has never been calculated


### `touchPath`

Defined in thing.t, line 99

the full reach-and-touch path from the source to the target


## Methods


### `construct(path)`

Defined in thing.t, line 96

construct, given the touch path
