# DisambigOrdProd

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 7423)


Base class for ordinal disambiguation items


**Superclass chain:** [DisambigProd](disambigprod.md) > [BasicProd](basicprod.md) > `object` > **DisambigOrdProdSubclasses:** [disambigListItem(ordinal)](disambiglistitem%28ordinal%29.md), [disambigOrdinalList(head)](disambigordinallist%28head%29.md), [disambigOrdinalList(tail)](disambigordinallist%28tail%29.md)


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)`

Defined in en_us.t, line 7424


### `selectByOrdinal(ordTok, resolver, results)`

Defined in en_us.t, line 7433

select the result by the ordinal


## Inherited Methods


*From [DisambigProd](disambigprod.md):* [`removeAmbigFlags`](disambigprod.md#removeAmbigFlags)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
