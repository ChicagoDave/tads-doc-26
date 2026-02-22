# PossessiveNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2987)


Possessive phrase + singular noun phrase. The language grammar rule must map poss_ to the possessive production and np_ to the noun phrase being qualified.


**Superclass chain:** [BasicPossessiveProd](basicpossessiveprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **PossessiveNounProdSubclasses:** [qualifiedSingularNounPhrase(possessive)](qualifiedsingularnounphrase%28possessive%29.md)


## Properties


### `npKeeper` *(overridden)*

Defined in parser.t, line 3005

our AmbigResponseKeeper for the qualified noun phrase


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 2988


## Inherited Methods


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`construct`](basicpossessiveprod.md#construct), [`resolvePossessive`](basicpossessiveprod.md#resolvePossessive), [`selectWithPossessive`](basicpossessiveprod.md#selectWithPossessive)


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
