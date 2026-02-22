# AskForTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3014)


An ASK FOR topic database entry. This type of topic entry is included in the ASK FOR list only.


**Superclass chain:** [AskTellTopic](asktelltopic.md) > [TopicMatchTopic](topicmatchtopic.md) > [TopicEntry](topicentry.md) > `object` > **AskForTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3015


## Inherited Properties


*From [TopicMatchTopic](topicmatchtopic.md):* [`matchExactCase`](topicmatchtopic.md#matchExactCase), [`matchPattern`](topicmatchtopic.md#matchPattern)


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [TopicMatchTopic](topicmatchtopic.md):* [`findMatchObj`](topicmatchtopic.md#findMatchObj), [`isMatchPossible`](topicmatchtopic.md#isMatchPossible), [`matchTopic`](topicmatchtopic.md#matchTopic), [`setTopicPronouns`](topicmatchtopic.md#setTopicPronouns)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
