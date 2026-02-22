# ImpByeTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3399)


An implied goodbye topic. This handles ONLY automatic (implied) conversation endings, which happen when we walk away from an actor we're talking to, or the other actor ends the conversation after being ignored for too long, or the other actor ends the conversation of its own volition via npc.endConversation().


**Superclass chain:** [MiscTopic](misctopic.md) > [TopicEntry](topicentry.md) > `object` > **ImpByeTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3400


### `matchList`

Defined in actor.t, line 3401


### `matchScore` *(overridden)*

Defined in actor.t, line 3402


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [MiscTopic](misctopic.md):* [`isMatchPossible`](misctopic.md#isMatchPossible), [`matchTopic`](misctopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
