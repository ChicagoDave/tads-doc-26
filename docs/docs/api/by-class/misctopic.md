# MiscTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3259)


A base class for simple miscellaneous topics. These handle things like YES, NO, HELLO, and GOODBYE, where the topic is entirely contained in the verb, and there's no separate noun phrase needed to indicate the topic.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **MiscTopic**


<details><summary>Subclasses (12)</summary>

- [ActorByeTopic](actorbyetopic.md)
- [ActorHelloTopic](actorhellotopic.md)
- [BoredByeTopic](boredbyetopic.md)
- [ByeTopic](byetopic.md)
- [HelloGoodbyeTopic](hellogoodbyetopic.md)
- [HelloTopic](hellotopic.md)
- [ImpByeTopic](impbyetopic.md)
- [ImpHelloTopic](imphellotopic.md)
- [LeaveByeTopic](leavebyetopic.md)
- [YesNoTopic](yesnotopic.md)
- [NoTopic](notopic.md)
- [YesTopic](yestopic.md)

</details>


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`includeInList`](topicentry.md#includeInList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3273

a match is always possible for simple verb topics (since the player could always type the verb)


### `matchTopic(fromActor, obj)` *(overridden)*

Defined in actor.t, line 3260


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)
