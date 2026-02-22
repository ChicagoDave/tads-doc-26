# ConsultTopic

*class* — defined in [objects.t](../by-file/objects.t.md) (line 1666)


A consultation topic. You can place one or more of these inside a Consultable object (using the 'location' property, or the '+' notation), to create a database of topics that can be looked up in the consultable.


**Superclass chain:** [TopicMatchTopic](topicmatchtopic.md) > [TopicEntry](topicentry.md) > `object` > **ConsultTopic**


## Properties


### `includeInList` *(overridden)*

Defined in objects.t, line 1668

include in the consultation list


## Inherited Properties


*From [TopicMatchTopic](topicmatchtopic.md):* [`matchExactCase`](topicmatchtopic.md#matchExactCase), [`matchPattern`](topicmatchtopic.md#matchPattern)


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `setTopicPronouns(fromActor, obj)` *(overridden)*

Defined in objects.t, line 1674

don't set any pronouns for the topic - the consultable itself should be the pronoun antecedent


## Inherited Methods


*From [TopicMatchTopic](topicmatchtopic.md):* [`findMatchObj`](topicmatchtopic.md#findMatchObj), [`isMatchPossible`](topicmatchtopic.md#isMatchPossible), [`matchTopic`](topicmatchtopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
