# InitiateTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 4066)


An "initiate" topic entry. This is a rather different kind of topic entry from the ones we've defined so far; an initiate topic is for cases where the NPC itself wants to initiate a conversation in response to something in the environment.


**Superclass chain:** [ThingMatchTopic](thingmatchtopic.md) > [TopicEntry](topicentry.md) > `object` > **InitiateTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 4068

include in the initiateTopics list


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 4075

since this kind of topic is triggered by internal calculations in the game, and not on anything the player is doing, there's no reason that our match object should be a pronoun antecedent


## Inherited Methods


*From [ThingMatchTopic](thingmatchtopic.md):* [`isMatchPossible`](thingmatchtopic.md#isMatchPossible), [`matchTopic`](thingmatchtopic.md#matchTopic)


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
