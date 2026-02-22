# ActorTopicDatabase

*class* — defined in [actor.t](../by-file/actor.t.md) (line 1004)


A TopicDatabase for an Actor. This is used not only directly for an Actor but also for an actor's sub-databases, in ActorState and ConvNode.


**Superclass chain:** [TopicDatabase](topicdatabase.md) > `object` > **ActorTopicDatabase**


<details><summary>Subclasses (12)</summary>

- [Actor](actor.md)
- [UntakeableActor](untakeableactor.md)
- [Person](person.md)
- [ActorState](actorstate.md)
- [AccompanyingInTravelState](accompanyingintravelstate.md)
- [GuidedInTravelState](guidedintravelstate.md)
- [AccompanyingState](accompanyingstate.md)
- [GuidedTourState](guidedtourstate.md)
- [ConversationReadyState](conversationreadystate.md)
- [HermitActorState](hermitactorstate.md)
- [InConversationState](inconversationstate.md)
- [ConvNode](convnode.md)

</details>


## Properties


### `askForTopics`

Defined in actor.t, line 1077


### `askTopics`

Defined in actor.t, line 1076

Our 'ask about', 'ask for', 'tell about', 'give', 'show', miscellaneous, command, and self-initiated topic databases - these are vectors we initialize as needed. Since every actor and every actor state has its own separate topic database, it's likely that the bulk of these databases will be empty, so we don't bother even creating a vector for a topic list until the first topic is added. This means we have to be able to cope with these being nil anywhere we use them.


### `commandTopics`

Defined in actor.t, line 1082


### `giveTopics`

Defined in actor.t, line 1080


### `initiateTopics`

Defined in actor.t, line 1083


### `miscTopics`

Defined in actor.t, line 1081


### `showTopics`

Defined in actor.t, line 1079


### `specialTopics`

Defined in actor.t, line 1086

our special command database


### `tellTopics`

Defined in actor.t, line 1078


## Inherited Properties


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `initiateTopic(obj)`

Defined in actor.t, line 1011

Initiate conversation on the given simulation object. If we can find an InitiateTopic matching the given object, we'll show its topic response and return true; if we can't find a topic to initiate, we'll simply return nil.


### `showTopicResponse(fromActor, topic, resp)` *(overridden)*

Defined in actor.t, line 1031

show a topic response


## Inherited Methods


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`getTopicOwner`](topicdatabase.md#getTopicOwner), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
