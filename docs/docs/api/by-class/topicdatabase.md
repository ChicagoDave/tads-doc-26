# TopicDatabase

*class* — defined in [actor.t](../by-file/actor.t.md) (line 551)


A plug-in topic database. The topic database is a set of TopicEntry objects that specify the responses to queries on particular topics. The exact nature of the queries that a particular topic database handles is up to the database subclass to define; we just provide the abstract mechanism for finding and displaying responses.


**Superclass chain:** `object` > **TopicDatabase**


<details><summary>Subclasses (14)</summary>

- [ActorTopicDatabase](actortopicdatabase.md)
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
- [Consultable](consultable.md)

</details>


## Properties


### `limitSuggestions`

Defined in actor.t, line 911

Flag: this database level should limit topic suggestions (for the TOPICS and TALK TO commands) to its own topics, excluding any topics inherited from the "broader" context. If this property is set to true, then we won't include suggestions from any lower level of the database hierarchy. If this property is nil, we'll also include any topic suggestions from the broader context.


### `suggestedTopics`

Defined in actor.t, line 975

Our list of suggested topics. These are SuggestedTopic objects that describe things that another actor wants to ask or tell this actor about.


### `topicGroupActive`

Defined in actor.t, line 557

Is the topic group active? A TopicEntry always checks with its container to see if the children of the container are active. By default, everything in the database is active.


### `topicGroupScoreAdjustment`

Defined in actor.t, line 564

Get the score adjustment for all topic entries contained within. The default adjustment is zero; TopicGroup objects can use this to adjust the score for their nested entries.


## Methods


### `addSuggestedTopic(topic)`

Defined in actor.t, line 934

add a suggested topic


### `addTopic(topic)`

Defined in actor.t, line 918

Add a topic to our topic database. We'll add it to the appropriate list or lists as indicated in the topic itself. 'topic' is a TopicEntry object.


### `addTopicToList(topic, listProp)`

Defined in actor.t, line 952

Add a topic to the given topic list. The topic list is given as a property point; for example, we'd specify &askTopics to add the topic to our ASK list.


### `compareVocabMatch(a, b)`

Defined in actor.t, line 810

Compare the vocabulary match strengths of two ResolveInfo objects, for the purposes of breaking ties in topic matching. Uses the usual comparison/sorting return value conventions: -1 means that a is weaker than b, 0 means they're equivalent, 1 means a is stronger than b.


### `findTopicResponse(fromActor, topic, convType, path)`

Defined in actor.t, line 606

find the best response (a TopicEntry object) for the given topic (a ResolvedTopic object)


### `getTopicOwner`

Defined in actor.t, line 985

Get the "owner" of the topics in this database. The meaning of "owner" varies according to the topic database type; for actor topic databases, for example, this is the actor. Generally, the owner is the object being queried about the topic, from the player's perspective. Each type of database should define this method to return the appropriate object.


### `handleTopic(fromActor, topic, convType, path)`

Defined in actor.t, line 572

Handle a topic. Look up the topic in our topic list for the given conversational action type. If we find a match, we'll invoke the matching topic list entry to handle it. We'll return true if we find a match, nil if not.


### `removeSuggestedTopic(topic)`

Defined in actor.t, line 941

remove a suggested topic


### `removeTopic(topic)`

Defined in actor.t, line 926

remove a topic from our topic database


### `removeTopicFromList(topic, listProp)`

Defined in actor.t, line 963

remove a topic from the given topic list


### `showSuggestedTopicList(lst, asker, askee, explicit)`

Defined in actor.t, line 846

show our suggested topic list


### `showTopicResponse(fromActor, topic, resp)`

Defined in actor.t, line 596

show the response we found for a topic
