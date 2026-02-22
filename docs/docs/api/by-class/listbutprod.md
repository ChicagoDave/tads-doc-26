# ListButProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1828)


Base class for "list but" rules, which select everything in an explicitly provided list minus a set of exceptions; for example, in English, "take all of the books except the red ones".


**Superclass chain:** [ButProd](butprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ListButProdSubclasses:** [terminalNounPhrase(pluralExcept)](terminalnounphrase%28pluralexcept%29.md)


## Properties


### `addedFlags` *(overridden)*

Defined in parser.t, line 1845

set the "unclear disambig" flag in our results, so we provide an indication of which object we chose


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `flagAllExcepted(resolver, results)` *(overridden)*

Defined in parser.t, line 1836

flag an error - everything has been excluded


### `getMainList(resolver, results)` *(overridden)*

Defined in parser.t, line 1830

our main list is given by the 'np_' subproduction


## Inherited Methods


*From [ButProd](butprod.md):* [`filterFinalList`](butprod.md#filterFinalList), [`resolveNouns`](butprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
