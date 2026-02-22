# qualifiedSingularNounPhrase(theOneIn)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5781)


A singular object specified only by its containment, with a definite article.


**Superclass chain:** [VagueContainerDefiniteNounPhraseProd](vaguecontainerdefinitenounphraseprod.md) > [VagueContainerNounPhraseProd](vaguecontainernounphraseprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **qualifiedSingularNounPhrase(theOneIn)**


## Properties


### `mainPhraseText`

Defined in en_us.t, line 5791

our main phrase is simply 'one' (so disambiguation prompts will read "which one do you mean...")


## Inherited Properties


*From [VagueContainerDefiniteNounPhraseProd](vaguecontainerdefinitenounphraseprod.md):* [`npKeeper`](vaguecontainerdefinitenounphraseprod.md#npKeeper)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Inherited Methods


*From [VagueContainerDefiniteNounPhraseProd](vaguecontainerdefinitenounphraseprod.md):* [`checkContentsList`](vaguecontainerdefinitenounphraseprod.md#checkContentsList), [`construct`](vaguecontainerdefinitenounphraseprod.md#construct)


*From [VagueContainerNounPhraseProd](vaguecontainernounphraseprod.md):* [`resolveNouns`](vaguecontainernounphraseprod.md#resolveNouns)


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
