# PreResolvedAmbigProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1894)


A pre-resolved *ambiguous* noun phrase. This is used when the game or library wants to suggest a specific set of objects for a new action, then ask which one to use.


**Superclass chain:** [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **PreResolvedAmbigProd**


## Properties


### `asker_`

Defined in parser.t, line 1921

the ResolveAsker to use when prompting for the selection


### `objs_`

Defined in parser.t, line 1915

my pre-resolved list of ambiguous objects


### `phrase_`

Defined in parser.t, line 1918

the noun phrase to use in disambiguation questions


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `construct(objs, asker, phrase)`

Defined in parser.t, line 1895


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 1907

remember the noun phrase to use in disambiguation questions


## Inherited Methods


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
