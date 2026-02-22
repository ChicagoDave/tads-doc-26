# HelloTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3283)


A greeting topic - this handles a HELLO or TALK TO command, as well as implied greetings (the kind of greeting generated when we jump directly into a conversation with an actor that uses stateful conversations, by typing a command like ASK ABOUT or TELL ABOUT without first saying HELLO explicitly).


**Superclass chain:** [MiscTopic](misctopic.md) > [TopicEntry](topicentry.md) > `object` > **HelloTopic**


## Properties


### `impliesGreeting` *(overridden)*

Defined in actor.t, line 3291

this is an explicit greeting, so it obviously shouldn't trigger an implied greeting, regardless of how conversational we are


### `includeInList` *(overridden)*

Defined in actor.t, line 3284


### `matchList`

Defined in actor.t, line 3285


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `noteInvocation(fromActor)` *(overridden)*

Defined in actor.t, line 3297

if we use this as a greeting upon entering a ConvNode, we'll want to stay in the node afterward


## Inherited Methods


*From [MiscTopic](misctopic.md):* [`isMatchPossible`](misctopic.md#isMatchPossible), [`matchTopic`](misctopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
