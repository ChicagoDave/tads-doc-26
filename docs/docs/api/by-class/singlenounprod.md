# SingleNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1309)


A single noun is sometimes required where, structurally, a list is not allowed. Single nouns should not be used to prohibit lists where there is no structural reason for the prohibition - these should be used only where it doesn't make sense to use a list structurally.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **SingleNounProd**


<details><summary>Subclasses (17)</summary>

- [PrepSingleNounProd](prepsinglenounprod.md)
- [atSingleNoun(main)](atsinglenoun%28main%29.md)
- [forSingleNoun(main)](forsinglenoun%28main%29.md)
- [fromSingleNoun(main)](fromsinglenoun%28main%29.md)
- [inSingleNoun(main)](insinglenoun%28main%29.md)
- [onSingleNoun(main)](onsinglenoun%28main%29.md)
- [outOfSingleNoun(main)](outofsinglenoun%28main%29.md)
- [throughSingleNoun(main)](throughsinglenoun%28main%29.md)
- [toSingleNoun(main)](tosinglenoun%28main%29.md)
- [withSingleNoun(main)](withsinglenoun%28main%29.md)
- [singleNounOnly(main)](singlenounonly%28main%29.md)
- [TopicProd](topicprod.md)
- [EmptyTopicPhraseProd](emptytopicphraseprod.md)
- [PrepSingleTopicProd](prepsingletopicprod.md)
- [aboutTopicPhrase(main)](abouttopicphrase%28main%29.md)
- [topicPhrase(main)](topicphrase%28main%29.md)
- [topicPhrase(misc)](topicphrase%28misc%29.md)

</details>


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1310


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
