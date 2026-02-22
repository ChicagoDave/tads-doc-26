# YesNoTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3513)


A YES/NO topic. These handle YES and/or NO, which are normally used as responses to questions posed by the NPC. YesNoTopic is the base class, and can be used to create a single response for both YES and NO; YesTopic provides a response just for YES; and NoTopic provides a response just for NO. The only thing an instance of these classes should normally need to specify is the response text (or a list of response strings, by multiply inheriting from an EventList subclass as usual).


**Superclass chain:** [MiscTopic](misctopic.md) > [TopicEntry](topicentry.md) > `object` > **YesNoTopicSubclasses:** [NoTopic](notopic.md), [YesTopic](yestopic.md)


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3514


### `matchList`

Defined in actor.t, line 3521

our list of matching topic objects - we'll only ever be asked to match 'yesTopicObj' (for YES inputs) or 'noTopicObj' (for NO inputs)


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [MiscTopic](misctopic.md):* [`isMatchPossible`](misctopic.md#isMatchPossible), [`matchTopic`](misctopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
