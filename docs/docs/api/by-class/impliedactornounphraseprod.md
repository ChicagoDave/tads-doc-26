# ImpliedActorNounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4168)


An empty noun phrase production for verb phrasings that imply an actor, but don't actually include one by name.


**Superclass chain:** [EmptyNounPhraseProd](emptynounphraseprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ImpliedActorNounPhraseProd**


## Inherited Properties


*From [EmptyNounPhraseProd](emptynounphraseprod.md):* [`asker_`](emptynounphraseprod.md#asker_), [`fallbackResponseProd`](emptynounphraseprod.md#fallbackResponseProd), [`newMatch`](emptynounphraseprod.md#newMatch), [`responseProd`](emptynounphraseprod.md#responseProd)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getImpliedObject(resolver, results)` *(overridden)*

Defined in parser.t, line 4170

get my implied object


## Inherited Methods


*From [EmptyNounPhraseProd](emptynounphraseprod.md):* [`getOrigText`](emptynounphraseprod.md#getOrigText), [`getOrigTokenList`](emptynounphraseprod.md#getOrigTokenList), [`isEmptyPhrase`](emptynounphraseprod.md#isEmptyPhrase), [`resolveNouns`](emptynounphraseprod.md#resolveNouns), [`setPrompt`](emptynounphraseprod.md#setPrompt)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
