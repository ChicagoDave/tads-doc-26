# TopicProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1366)


A topic is a noun phrase used in commands like "ask <person> about <topic>." For our purposes, this works as an ordinary single noun production.


**Superclass chain:** [SingleNounProd](singlenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **TopicProdSubclasses:** [EmptyTopicPhraseProd](emptytopicphraseprod.md), [PrepSingleTopicProd](prepsingletopicprod.md), [aboutTopicPhrase(main)](abouttopicphrase%28main%29.md), [topicPhrase(main)](topicphrase%28main%29.md), [topicPhrase(misc)](topicphrase%28misc%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getOrigText` *(overridden)*

Defined in parser.t, line 1369


### `getOrigTokenList` *(overridden)*

Defined in parser.t, line 1368

get the original text and tokens from the underlying phrase


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 1371


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
