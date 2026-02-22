# ByeTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3371)


A goodbye topic - this handles both explicit GOODBYE commands and implied goodbyes. Implied goodbyes happen when a conversation ends without an explicit GOODBYE command, such as when the player character walks away from the NPC, or the NPC gets bored and wanders off, or the NPC terminates the conversation of its own volition.


**Superclass chain:** [MiscTopic](misctopic.md) > [TopicEntry](topicentry.md) > `object` > **ByeTopic**


## Properties


### `impliesGreeting` *(overridden)*

Defined in actor.t, line 3385

If we're not already in a conversation when we say GOODBYE, don't bother saying HELLO implicitly - if the player is saying GOODBYE explicitly, she probably has the impression that there's some kind of interaction already going on with the NPC. If we didn't override this, you'd get an automatic HELLO followed by the explicit GOODBYE when not already in conversation, which is a little weird.


### `includeInList` *(overridden)*

Defined in actor.t, line 3372


### `matchList`

Defined in actor.t, line 3373


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Inherited Methods


*From [MiscTopic](misctopic.md):* [`isMatchPossible`](misctopic.md#isMatchPossible), [`matchTopic`](misctopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
