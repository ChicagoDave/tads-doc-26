# ThingMatchTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3036)


A base class for topic entries that match simple simulation objects.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **ThingMatchTopicSubclasses:** [GiveShowTopic](giveshowtopic.md), [GiveTopic](givetopic.md), [ShowTopic](showtopic.md), [InitiateTopic](initiatetopic.md), [TopicOrThingMatchTopic](topicorthingmatchtopic.md), [AskTellGiveShowTopic](asktellgiveshowtopic.md), [AskTellShowTopic](asktellshowtopic.md)


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`includeInList`](topicentry.md#includeInList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3068

It's possible for us to match if any of our matchObj objects are in scope.


### `matchTopic(fromActor, obj)` *(overridden)*

Defined in actor.t, line 3041

Match the topic. We'll match the simulation object in 'obj' to our matchObj object or list.


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 3084

set the topic pronouns


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
