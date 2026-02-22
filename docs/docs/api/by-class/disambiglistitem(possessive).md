# disambigListItem(possessive)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7538)


return the list


**Superclass chain:** [DisambigPossessiveProd](disambigpossessiveprod.md) > [BasicPossessiveProd](basicpossessiveprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > [DisambigProd](disambigprod.md) > **disambigListItem(possessive)**


## Inherited Properties


*From [DisambigPossessiveProd](disambigpossessiveprod.md):* [`qualifiedList_`](disambigpossessiveprod.md#qualifiedList_)


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`npKeeper`](basicpossessiveprod.md#npKeeper)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Inherited Methods


*From [DisambigPossessiveProd](disambigpossessiveprod.md):* [`reduceDefinite`](disambigpossessiveprod.md#reduceDefinite), [`resolveNouns`](disambigpossessiveprod.md#resolveNouns)


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`construct`](basicpossessiveprod.md#construct), [`resolvePossessive`](basicpossessiveprod.md#resolvePossessive), [`selectWithPossessive`](basicpossessiveprod.md#selectWithPossessive)


*From [DefiniteNounProd](definitenounprod.md):* [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)


*From [DisambigProd](disambigprod.md):* [`removeAmbigFlags`](disambigprod.md#removeAmbigFlags)
