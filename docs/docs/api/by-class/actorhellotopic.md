# ActorHelloTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3345)


Actor Hello topic - this handles greetings when an NPC initiates the conversation.


**Superclass chain:** [MiscTopic](misctopic.md) > [TopicEntry](topicentry.md) > `object` > **ActorHelloTopic**


## Properties


### `impliesGreeting` *(overridden)*

Defined in actor.t, line 3351

this is a greeting, so we don't want to trigger another greeting


### `includeInList` *(overridden)*

Defined in actor.t, line 3346


### `matchList`

Defined in actor.t, line 3347


### `matchScore` *(overridden)*

Defined in actor.t, line 3348


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `noteInvocation(fromActor)` *(overridden)*

Defined in actor.t, line 3357

if we use this as a greeting upon entering a ConvNode, we'll want to stay in the node afterward


## Inherited Methods


*From [MiscTopic](misctopic.md):* [`isMatchPossible`](misctopic.md#isMatchPossible), [`matchTopic`](misctopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
