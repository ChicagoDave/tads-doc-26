# DefaultTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3601)


A default topic entry. This is an easy way to create an entry that will be used as a last resort, if no other entry is found. This kind of entry will match *any* topic, but with the lowest possible score, so it will only be used if there's no other match for the topic.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **DefaultTopic**


<details><summary>Subclasses (11)</summary>

- [DefaultAnyTopic](defaultanytopic.md)
- [DefaultAskForTopic](defaultaskfortopic.md)
- [DefaultAskTellTopic](defaultasktelltopic.md)
- [DefaultAskTopic](defaultasktopic.md)
- [DefaultCommandTopic](defaultcommandtopic.md)
- [DefaultConsultTopic](defaultconsulttopic.md)
- [DefaultGiveShowTopic](defaultgiveshowtopic.md)
- [DefaultGiveTopic](defaultgivetopic.md)
- [DefaultInitiateTopic](defaultinitiatetopic.md)
- [DefaultShowTopic](defaultshowtopic.md)
- [DefaultTellTopic](defaulttelltopic.md)

</details>


## Properties


### `excludeMatch`

Defined in actor.t, line 3612

A list of objects to exclude from the default match. This can be used to create a default topic that matches everything EXCEPT a few specific topics that are handled in enclosing topic databases. For example, if you want to create a catch-all in a ConvNode's list of topics, but you want a particular topic to escape the catch-all and be sent instead to the Actor's topic database, you can put that topic in the exclude list for the catch-all, making it a catch-almost-all.


### `matchScore` *(overridden)*

Defined in actor.t, line 3638

use a low default matching score


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`includeInList`](topicentry.md#includeInList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3641

a match is always possible for a default topic


### `matchTopic(fromActor, topic)` *(overridden)*

Defined in actor.t, line 3615

match anything except topics in our exclude list


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 3644

set the topic pronoun


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
