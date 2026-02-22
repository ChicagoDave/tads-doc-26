# ButPossessiveProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3060)


Possessive noun used in an exclusion list. This is for things like the "mine" in a phrase like "take keys except mine".


**Superclass chain:** [BasicPossessiveProd](basicpossessiveprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **ButPossessiveProdSubclasses:** [exceptNounPhrase(singlePossessive)](exceptnounphrase%28singlepossessive%29.md)


## Inherited Properties


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`npKeeper`](basicpossessiveprod.md#npKeeper)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 3061


## Inherited Methods


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`construct`](basicpossessiveprod.md#construct), [`resolvePossessive`](basicpossessiveprod.md#resolvePossessive), [`selectWithPossessive`](basicpossessiveprod.md#selectWithPossessive)


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
