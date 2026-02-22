# EverythingButProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1786)


Base class for "all but" rules, which select everything available except for objects in a specified list of exceptions; for example, in English, "take everything but the book".


**Superclass chain:** [ButProd](butprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **EverythingButProdSubclasses:** [terminalNounPhrase(allBut)](terminalnounphrase%28allbut%29.md)


## Properties


### `addedFlags` *(overridden)*

Defined in parser.t, line 1813

set the "always announce" flag for each item - the player didn't name the selected items specifically, so always show what we chose


### `filterForCollectives` *(overridden)*

Defined in parser.t, line 1816

match Collective objects instead of their individuals


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `flagAllExcepted(resolver, results)` *(overridden)*

Defined in parser.t, line 1803

flag an error - our main list has been completely excluded


### `getMainList(resolver, results)` *(overridden)*

Defined in parser.t, line 1788

our main list is given by the "all" list


## Inherited Methods


*From [ButProd](butprod.md):* [`filterFinalList`](butprod.md#filterFinalList), [`resolveNouns`](butprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
