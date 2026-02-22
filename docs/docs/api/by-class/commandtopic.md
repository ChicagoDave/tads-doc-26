# CommandTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3214)


A command topic. This is used to respond to orders given to an NPC, as in "BOB, GO EAST." The match object for this kind of topic entry is an Action class; for example, to create a response to "BOB, LOOK", we'd create a CommandTopic that matches LookAction.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **CommandTopic**


## Properties


### `includeInList` *(overridden)*

Defined in actor.t, line 3216

we go in the command topics list


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3247

we can always match, since the player can always type in any possible action


### `matchTopic(fromActor, obj)` *(overridden)*

Defined in actor.t, line 3219

match the topic


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 3250

we have no pronouns to set


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
