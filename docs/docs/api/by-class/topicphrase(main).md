# topicPhrase(main)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7049)


A "topic" is a special type of noun phrase used in commands like "ask <actor> about <topic>." We define a topic as simply an ordinary single-noun phrase. We distinguish this in the grammar to allow games to add special syntax for these.


**Superclass chain:** [TopicProd](topicprod.md) > [SingleNounProd](singlenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **topicPhrase(main)**


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [TopicProd](topicprod.md):* [`getOrigText`](topicprod.md#getOrigText), [`getOrigTokenList`](topicprod.md#getOrigTokenList), [`resolveNouns`](topicprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
