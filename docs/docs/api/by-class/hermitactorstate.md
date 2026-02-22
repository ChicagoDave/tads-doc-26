# HermitActorState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5228)


A "hermit" actor state is a state where the actor is unresponsive to conversational overtures (ASK ABOUT, TELL ABOUT, HELLO, GOODBYE, YES, NO, SHOW TO, GIVE TO, and any orders directed to the actor). Any attempt at conversation will be met with the 'noResponse' message.


**Superclass chain:** [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **HermitActorState**


## Properties


### `limitSuggestions` *(overridden)*

Defined in actor.t, line 5278

Since the hermit state blocks topics from outside the state, don't offer suggestions for other topics while in this state.


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`getImpliedConvState`](actorstate.md#getImpliedConvState), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc), [`stateSuggestedTopics`](actorstate.md#stateSuggestedTopics)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `handleConversation(otherActor, topic, convType)` *(overridden)*

Defined in actor.t, line 5251

all conversation actions get the same default response


### `noResponse`

Defined in actor.t, line 5248

Show our response to any conversational command. We'll simply show the standard "there's no response" message by default, but subclasses can (and usually should) override this to explain what's really going on. Note that this routine will be invoked for any sort of conversation command, so any override needs to be generic enough that it's equally good for ASK, TELL, and everything else.


## Inherited Methods


<details><summary>From [ActorState](actorstate.md) (25)</summary>

[`activateState`](actorstate.md#activateState), [`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`beforeTravel`](actorstate.md#beforeTravel), [`construct`](actorstate.md#construct), [`deactivateState`](actorstate.md#deactivateState), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`endConversation`](actorstate.md#endConversation), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`initializeActorState`](actorstate.md#initializeActorState), [`justFollowed`](actorstate.md#justFollowed), [`notifyTopicResponse`](actorstate.md#notifyTopicResponse), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDesc`](actorstate.md#specialDesc), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor), [`takeTurn`](actorstate.md#takeTurn)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
