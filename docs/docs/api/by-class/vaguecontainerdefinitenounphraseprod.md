# VagueContainerDefiniteNounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3456)


A definite vague container phrase. This selects a single object in a given container ("the one in the box"). If more than one object is present, we'll try to disambiguate it.


**Superclass chain:** [VagueContainerNounPhraseProd](vaguecontainernounphraseprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **VagueContainerDefiniteNounPhraseProdSubclasses:** [qualifiedSingularNounPhrase(theOneIn)](qualifiedsingularnounphrase%28theonein%29.md)


## Properties


### `npKeeper`

Defined in parser.t, line 3505

our disambiguation result keeper


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `checkContentsList(resolver, results, lst, cont)` *(overridden)*

Defined in parser.t, line 3464

check a contents list


### `construct`

Defined in parser.t, line 3457


## Inherited Methods


*From [VagueContainerNounPhraseProd](vaguecontainernounphraseprod.md):* [`resolveNouns`](vaguecontainernounphraseprod.md#resolveNouns)


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
