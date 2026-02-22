# numberPhrase(digits)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7656)


A quantifier is simply a number, entered with numerals or spelled out.


**Superclass chain:** [NumberProd](numberprod.md) > [BasicProd](basicprod.md) > `object` > **numberPhrase(digits)**


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getStrVal` *(overridden)*

Defined in en_us.t, line 7664

get the string version of the numeric value - since the token was an integer to start with, return the actual integer value


### `getval` *(overridden)*

Defined in en_us.t, line 7658

get the numeric value


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
