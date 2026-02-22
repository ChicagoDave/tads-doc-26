# ShuffledIntegerList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1546)


A Shuffled Integer List is a special kind of Shuffled List that returns integers in a given range. Like an ordinary Shuffled List, we'll return integers in the given range in random order, but we'll only return each integer once during a given round; when we exhaust the supply, we'll reshuffle the set of integers and start over.


**Superclass chain:** [ShuffledList](shuffledlist.md) > `object` > **ShuffledIntegerList**


## Properties


### `rangeMax`

Defined in misc.t, line 1552


### `rangeMin`

Defined in misc.t, line 1551

The minimum and maximum values for our range. Instances should define these to the range desired.


### `valueList` *(overridden)*

Defined in misc.t, line 1555

initialize the value list on demand


## Inherited Properties


*From [ShuffledList](shuffledlist.md):* [`suppressRepeats`](shuffledlist.md#suppressRepeats), [`valuesAvail`](shuffledlist.md#valuesAvail), [`valuesVec`](shuffledlist.md#valuesVec)


## Methods


### `construct(rmin, rmax)` *(overridden)*

Defined in misc.t, line 1558

construct with the given range


### `getNextValue` *(overridden)*

Defined in misc.t, line 1565

get the next value


## Inherited Methods


*From [ShuffledList](shuffledlist.md):* [`reshuffle`](shuffledlist.md#reshuffle)
