# disambigOrdinalList(tail)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7547)


A disambig ordinal list consists of two or more ordinal words separated by noun phrase conjunctions. Note that there is a minimum of two entries in the list.


**Superclass chain:** [DisambigOrdProd](disambigordprod.md) > [DisambigProd](disambigprod.md) > [BasicProd](basicprod.md) > `object` > **disambigOrdinalList(tail)**


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)` *(overridden)*

Defined in en_us.t, line 7549


## Inherited Methods


*From [DisambigOrdProd](disambigordprod.md):* [`selectByOrdinal`](disambigordprod.md#selectByOrdinal)


*From [DisambigProd](disambigprod.md):* [`removeAmbigFlags`](disambigprod.md#removeAmbigFlags)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
