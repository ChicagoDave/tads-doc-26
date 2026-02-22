# GuidedTourState

*class* — defined in [extras.t](../by-file/extras.t.md) (line 2402)


Guided Tour state. This provides a simple way of defining a "guided tour," which is a series of locations to which we try to guide the player character. We don't force the player character to travel as specified; we merely try to lead the player. The actual travel is up to the player.


**Superclass chain:** [AccompanyingState](accompanyingstate.md) > [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **GuidedTourState**


## Properties


### `escortActor`

Defined in extras.t, line 2414

the actor we're escorting - this is usually the player character


### `escortDest`

Defined in extras.t, line 2404

the travel connector we're trying to show the player into


### `escortStateClass`

Defined in extras.t, line 2424

The class we use for our actor state during the escort travel. By default, we use the basic guided-tour accompanying travel state class, but games will probably want to use a customized subclass of this basic class in most cases. The main reason to use a custom subclass is to provide customized messages to describe the departure of the escorting actor.


### `stateAfterEscort`

Defined in extras.t, line 2411

The next state for our actor to assume after the travel. This should be overridden and set to the state object for the next stop on the tour.


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`getImpliedConvState`](actorstate.md#getImpliedConvState), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc), [`stateSuggestedTopics`](actorstate.md#stateSuggestedTopics)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `accompanyTravel(traveler, conn)` *(overridden)*

Defined in extras.t, line 2430

we should accompany the travel if the actor we're guiding will be traveling, and they're traveling to the next stop on our tour


### `getAccompanyingTravelState(traveler, conn)` *(overridden)*

Defined in extras.t, line 2439

get our accompanying state object - we'll create an instance of the class specified in our escortStateClass property


## Inherited Methods


*From [AccompanyingState](accompanyingstate.md):* [`beforeTravel`](accompanyingstate.md#beforeTravel)


<details><summary>From [ActorState](actorstate.md) (25)</summary>

[`activateState`](actorstate.md#activateState), [`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`construct`](actorstate.md#construct), [`deactivateState`](actorstate.md#deactivateState), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`endConversation`](actorstate.md#endConversation), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`handleConversation`](actorstate.md#handleConversation), [`initializeActorState`](actorstate.md#initializeActorState), [`justFollowed`](actorstate.md#justFollowed), [`notifyTopicResponse`](actorstate.md#notifyTopicResponse), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDesc`](actorstate.md#specialDesc), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor), [`takeTurn`](actorstate.md#takeTurn)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
