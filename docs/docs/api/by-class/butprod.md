# ButProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1667)


Basic "but" rule, which selects a list of plurals minus a list of specifically excepted objects. This can be used to construct more specific production classes for things like "everything but the book" and "all books except the red ones".


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ButProdSubclasses:** [EverythingButProd](everythingbutprod.md), [terminalNounPhrase(allBut)](terminalnounphrase%28allbut%29.md), [IndefiniteNounButProd](indefinitenounbutprod.md), [terminalNounPhrase(anyBut)](terminalnounphrase%28anybut%29.md), [ListButProd](listbutprod.md), [terminalNounPhrase(pluralExcept)](terminalnounphrase%28pluralexcept%29.md)


## Properties


### `addedFlags`

Defined in parser.t, line 1776

by default, add no extra flags to our resolved object list


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `filterFinalList(lst)`

Defined in parser.t, line 1773

filter the final list - by default we just return the same list


### `flagAllExcepted(resolver, results)`

Defined in parser.t, line 1770

flag an error - everything has been excluded by the 'but' list


### `getMainList(resolver, results)`

Defined in parser.t, line 1767

get my main list, which is the list of items to include


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1668


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
