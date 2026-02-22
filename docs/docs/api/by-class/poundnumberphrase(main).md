# poundNumberPhrase(main)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7677)


A number phrase preceded by a pound sign. We distinguish this kind of number phrase from plain numbers, since this kind has a somewhat more limited set of valid contexts.


**Superclass chain:** [NumberProd](numberprod.md) > [BasicProd](basicprod.md) > `object` > **poundNumberPhrase(main)**


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getStrVal` *(overridden)*

Defined in en_us.t, line 7689

get the string value - we have a number token following the '#', so simply return the part after the '#'


### `getval` *(overridden)*

Defined in en_us.t, line 7683

get the numeric value - a tokPoundInt token has a pound sign followed by digits, so the numeric value is the value of the substring following the '#' sign


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
