# AskTellShowTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3179)


A combined ASK/TELL/SHOW topic. Players will sometimes want to point something out when it's visible, rather than asking about it; this allows SHOW TO to be used as a synonym for ASK ABOUT for these cases.


**Superclass chain:** [TopicOrThingMatchTopic](topicorthingmatchtopic.md) > [ThingMatchTopic](thingmatchtopic.md) > [TopicEntry](topicentry.md) > `object` > [TopicMatchTopic](topicmatchtopic.md) > **AskTellShowTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3180


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


*From [TopicMatchTopic](topicmatchtopic.md):* [`matchExactCase`](topicmatchtopic.md#matchExactCase), [`matchPattern`](topicmatchtopic.md#matchPattern)


## Inherited Methods


*From [TopicOrThingMatchTopic](topicorthingmatchtopic.md):* [`isMatchPossible`](topicorthingmatchtopic.md#isMatchPossible), [`matchTopic`](topicorthingmatchtopic.md#matchTopic), [`setTopicPronouns`](topicorthingmatchtopic.md#setTopicPronouns)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)


*From [TopicMatchTopic](topicmatchtopic.md):* [`findMatchObj`](topicmatchtopic.md#findMatchObj)
