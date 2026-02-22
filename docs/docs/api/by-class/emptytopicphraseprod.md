# EmptyTopicPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4275)


Empty topic phrase production. This is the topic equivalent of EmptyNounPhraseProd.


**Superclass chain:** [TopicProd](topicprod.md) > [SingleNounProd](singlenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **EmptyTopicPhraseProd**


## Properties


### `asker_`

Defined in parser.t, line 4326

our ResolveAsker object - this is for customizing the prompt


### `newMatch`

Defined in parser.t, line 4317

our new underlying topic phrase


### `responseProd`

Defined in parser.t, line 4323

by default, parse our interactive response as an ordinary topic phrase


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getOrigText` *(overridden)*

Defined in parser.t, line 4311

get my original text - use the new match tree if we have one


### `getOrigTokenList` *(overridden)*

Defined in parser.t, line 4305

get my tokens - use the underlying new match tree if we have one


### `isEmptyPhrase`

Defined in parser.t, line 4302

we're an empty phrase if we don't have a new topic yet


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 4276


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
