# DefaultAnyTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3719)


**Superclass chain:** [DefaultTopic](defaulttopic.md) > [TopicEntry](topicentry.md) > `object` > **DefaultAnyTopic**


## Properties


### `excludeMatch` *(overridden)*

Defined in actor.t, line 3727

exclude these from actor-initiated hellos & goodbyes - those should only match topics explicitly


### `includeInList` *(overridden)*

Defined in actor.t, line 3720


### `matchScore` *(overridden)*

Defined in actor.t, line 3728


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [DefaultTopic](defaulttopic.md):* [`isMatchPossible`](defaulttopic.md#isMatchPossible), [`matchTopic`](defaulttopic.md#matchTopic), [`setTopicPronouns`](defaulttopic.md#setTopicPronouns)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
