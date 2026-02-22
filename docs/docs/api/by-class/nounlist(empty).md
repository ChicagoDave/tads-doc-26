# nounList(empty)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5272)


An empty noun list is one with no words at all. This is matched when a command requires a noun list but the player doesn't include one; this construct has "badness" because we only want to match it when we have no choice.


**Superclass chain:** [EmptyNounPhraseProd](emptynounphraseprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **nounList(empty)**


## Properties


### `responseProd` *(overridden)*

Defined in en_us.t, line 5273


## Inherited Properties


*From [EmptyNounPhraseProd](emptynounphraseprod.md):* [`asker_`](emptynounphraseprod.md#asker_), [`fallbackResponseProd`](emptynounphraseprod.md#fallbackResponseProd), [`newMatch`](emptynounphraseprod.md#newMatch)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [EmptyNounPhraseProd](emptynounphraseprod.md):* [`getImpliedObject`](emptynounphraseprod.md#getImpliedObject), [`getOrigText`](emptynounphraseprod.md#getOrigText), [`getOrigTokenList`](emptynounphraseprod.md#getOrigTokenList), [`isEmptyPhrase`](emptynounphraseprod.md#isEmptyPhrase), [`resolveNouns`](emptynounphraseprod.md#resolveNouns), [`setPrompt`](emptynounphraseprod.md#setPrompt)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
