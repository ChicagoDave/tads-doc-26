# AccompanyingState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5286)


The basic "accompanying" state. In this state, whenever the actor we're accompanying travels to a location we want to follow, we'll travel at the same time with the other actor.


**Superclass chain:** [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **AccompanyingStateSubclasses:** [GuidedTourState](guidedtourstate.md)


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`getImpliedConvState`](actorstate.md#getImpliedConvState), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc), [`stateSuggestedTopics`](actorstate.md#stateSuggestedTopics)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `accompanyTravel(traveler, conn)`

Defined in actor.t, line 5302

Check to see if we are to accompany the given traveler on the given travel. 'traveler' is the Traveler performing the travel, and 'conn' is the connector that the traveler is about to take.


### `beforeTravel(traveler, connector)` *(overridden)*

Defined in actor.t, line 5326

handle a before-travel notification for my actor


### `getAccompanyingTravelState(traveler, connector)`

Defined in actor.t, line 5311

Get our accompanying state object. We'll create a basic accompanying in-travel state object, returning to the current state when we're done. 'traveler' is the Traveler object that's performing the travel; this might be an Actor, but could also be a Vehicle or other Traveler subclass.


## Inherited Methods


<details><summary>From [ActorState](actorstate.md) (25)</summary>

[`activateState`](actorstate.md#activateState), [`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`construct`](actorstate.md#construct), [`deactivateState`](actorstate.md#deactivateState), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`endConversation`](actorstate.md#endConversation), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`handleConversation`](actorstate.md#handleConversation), [`initializeActorState`](actorstate.md#initializeActorState), [`justFollowed`](actorstate.md#justFollowed), [`notifyTopicResponse`](actorstate.md#notifyTopicResponse), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDesc`](actorstate.md#specialDesc), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor), [`takeTurn`](actorstate.md#takeTurn)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
