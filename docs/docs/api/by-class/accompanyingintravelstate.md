# AccompanyingInTravelState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5365)


"Accompanying in-travel" state - this is an actor state used when an actor is taking part in a group travel operation. This state lasts only as long as the single turn - which belongs to the lead actor - that it takes to carry out the group travel. Once our turn comes around, we'll restore the actor to the previous state - or, we can set the actor to a different state, if desired. Setting the actor to a different state is useful when the group travel triggers a new scripted activity in the new room.


**Superclass chain:** [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **AccompanyingInTravelStateSubclasses:** [GuidedInTravelState](guidedintravelstate.md)


## Properties


### `leadActor`

Defined in actor.t, line 5377

the lead actor of the group travel


### `nextState`

Defined in actor.t, line 5383

the next state - we'll switch our actor to this state after the travel has been completed


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`getImpliedConvState`](actorstate.md#getImpliedConvState), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc), [`stateSuggestedTopics`](actorstate.md#stateSuggestedTopics)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `construct(actor, lead, next)` *(overridden)*

Defined in actor.t, line 5366


### `initiateTopic(obj)` *(overridden)*

Defined in actor.t, line 5413

initiate a topic - defer to the next state


### `sayArrivingLocally(dest, conn)` *(overridden)*

Defined in actor.t, line 5454

Describe local travel using our standard departure message as well. This is used to describe our travel when our origin and destination locations are both visible to the PC; in these cases, we don't describe the departure separately because the whole process of travel from departure to arrival is visible to the PC and thus is best handled with a single message, which we generate here. In our case, since the "accompanying" state describes even normal travel as though it were visible all along, we can use our standard "departing" message to describe local travel as well.


### `sayDeparting(conn)` *(overridden)*

Defined in actor.t, line 5435

Override our departure messages. When we're accompanying another actor on a group travel, the lead actor will, as part of its turn, send each accompanying actor (including us) on ahead. This means that the lead actor will see us departing from the starting location, because we'll leave before the lead actor has itself departed. Rather than using the normal "Bob leaves to the west" departure report, customize the departure reports to indicate specifically that we're going with the lead actor. (Note that we only have to handle the departing messages, since group travel always sends accompanying actors on ahead of the main actor, hence the accompanying actors will always be seen departing, not arriving.)


### `sayDepartingDir(dir, conn)` *(overridden)*

Defined in actor.t, line 5437


### `sayDepartingDownStairs(conn)` *(overridden)*

Defined in actor.t, line 5441


### `sayDepartingLocally(dest, conn)` *(overridden)*

Defined in actor.t, line 5455


### `sayDepartingThroughPassage(conn)` *(overridden)*

Defined in actor.t, line 5438


### `sayDepartingUpStairs(conn)` *(overridden)*

Defined in actor.t, line 5440


### `sayDepartingViaPath(conn)` *(overridden)*

Defined in actor.t, line 5439


### `specialDesc` *(overridden)*

Defined in actor.t, line 5389

Show our "I am here" description. By default, we'll use the arrivingWithDesc of the *next* state object.


### `takeTurn` *(overridden)*

Defined in actor.t, line 5392

take our turn


## Inherited Methods


<details><summary>From [ActorState](actorstate.md) (23)</summary>

[`activateState`](actorstate.md#activateState), [`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`beforeTravel`](actorstate.md#beforeTravel), [`deactivateState`](actorstate.md#deactivateState), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`endConversation`](actorstate.md#endConversation), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`handleConversation`](actorstate.md#handleConversation), [`initializeActorState`](actorstate.md#initializeActorState), [`justFollowed`](actorstate.md#justFollowed), [`notifyTopicResponse`](actorstate.md#notifyTopicResponse), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
