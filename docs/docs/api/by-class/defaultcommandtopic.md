# DefaultCommandTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3687)


Default topic entries for different uses. We'll use a hierarchy of low match scores, in descending order of specificity: 3 for single-type defaults (ASK only, for example), 2 for multi-type defaults (ASK/TELL), and 1 for the ANY default.


**Superclass chain:** [DefaultTopic](defaulttopic.md) > [TopicEntry](topicentry.md) > `object` > **DefaultCommandTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3688


### `matchScore` *(overridden)*

Defined in actor.t, line 3689


## Inherited Properties


*From [DefaultTopic](defaulttopic.md):* [`excludeMatch`](defaulttopic.md#excludeMatch)


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [DefaultTopic](defaulttopic.md):* [`isMatchPossible`](defaulttopic.md#isMatchPossible), [`matchTopic`](defaulttopic.md#matchTopic), [`setTopicPronouns`](defaulttopic.md#setTopicPronouns)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
