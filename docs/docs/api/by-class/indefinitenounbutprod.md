# IndefiniteNounButProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2557)


Noun phrase with an indefinite article and an exclusion ("any of the books except the red one")


**Superclass chain:** [ButProd](butprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **IndefiniteNounButProdSubclasses:** [terminalNounPhrase(anyBut)](terminalnounphrase%28anybut%29.md)


## Properties


### `addedFlags` *(overridden)*

Defined in parser.t, line 2604

set the "unclear disambig" flag in our results, so we provide an indication of which object we chose


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `filterFinalList(lst)` *(overridden)*

Defined in parser.t, line 2594

filter the final list


### `flagAllExcepted(resolver, results)` *(overridden)*

Defined in parser.t, line 2588

flag an error - everything has been excluded


### `getMainList(resolver, results)` *(overridden)*

Defined in parser.t, line 2569

get our main list


### `resolveMainPhrase(resolver, results)`

Defined in parser.t, line 2559

resolve our main phrase


## Inherited Methods


*From [ButProd](butprod.md):* [`resolveNouns`](butprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
