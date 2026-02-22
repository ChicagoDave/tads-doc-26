# VagueContainerNounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3342)


A "vague" container noun phrase. This is a phrase that specifies a container but nothing else: "the one in the box", "the ones in the box", "everything in the box".


**Superclass chain:** [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **VagueContainerNounPhraseProdSubclasses:** [AllInContainerNounPhraseProd](allincontainernounphraseprod.md), [qualifiedPluralNounPhrase(theOnesIn)](qualifiedpluralnounphrase%28theonesin%29.md), [VagueContainerDefiniteNounPhraseProd](vaguecontainerdefinitenounphraseprod.md), [qualifiedSingularNounPhrase(theOneIn)](qualifiedsingularnounphrase%28theonein%29.md), [VagueContainerIndefiniteNounPhraseProd](vaguecontainerindefinitenounphraseprod.md), [qualifiedSingularNounPhrase(anyOneIn)](qualifiedsingularnounphrase%28anyonein%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `checkContentsList(resolver, results, lst, cont)`

Defined in parser.t, line 3417

check a contents list


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 3343


## Inherited Methods


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
