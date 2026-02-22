# directionName(port)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 3125)


The English-specific shipboard direction modifications. Certain of the ship directions have no natural descriptions for arrival and/or departure; for example, there's no good way to say "arriving from fore." Others don't fit any regular pattern: "he goes aft" rather than "he departs to aft." As a result, these are a bit irregular compared to the compass directions and so are individually defined below.


**Superclass chain:** [DirectionProd](directionprod.md) > [BasicProd](basicprod.md) > `object` > **directionName(port)**


## Inherited Properties


*From [DirectionProd](directionprod.md):* [`dir`](directionprod.md#dir)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `sayArriving(trav)`

Defined in en_us.t, line 3126


### `sayDeparting(trav)`

Defined in en_us.t, line 3128


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
