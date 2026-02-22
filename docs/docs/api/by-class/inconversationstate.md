# InConversationState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 4967)


The "in-conversation" state. This works with ConversationReadyState to handle transitions in and out of conversations. In this state, we are actively engaged in a conversation.


**Superclass chain:** [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **InConversationState**


## Properties


### `attentionSpan`

Defined in actor.t, line 4979

Our attention span, in turns. This is the number of turns that we'll be willing to stay in the conversation while the other character is ignoring us. After the conversation has been idle this long, we'll assume the other actor is no longer talking to us, so we'll terminate the conversation ourselves.


### `nextState`

Defined in actor.t, line 4987

The state to switch to when the conversation ends. Instances can override this to select the next state. By default, we'll return to the state that we were in immediately before the conversation started.


### `previousState`

Defined in actor.t, line 5170

The previous state - this is the state we were in before the conversation began, and the one we'll return to by default when the conversation ends. We'll set this automatically on activation.


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`getImpliedConvState`](actorstate.md#getImpliedConvState), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc), [`stateSuggestedTopics`](actorstate.md#stateSuggestedTopics)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `activateState(actor, oldState)` *(overridden)*

Defined in actor.t, line 5118

activate this state


### `deactivateState(actor, newState)` *(overridden)*

Defined in actor.t, line 5152

deactivate this state


### `defaultGreetingResponse(actor)`

Defined in actor.t, line 5094

provide a default HELLO response, if we don't have a special TopicEntry for it


### `endConversation(actor, reason)` *(overridden)*

Defined in actor.t, line 5005

End the current conversation. 'reason' indicates why we're leaving the conversation - this is one of the endConvXxx enums defined in adv3.h.


### `handleConversation(otherActor, topic, convType)` *(overridden)*

Defined in actor.t, line 5051

handle a conversational command


### `takeTurn` *(overridden)*

Defined in actor.t, line 5105

As our default response, point out that we're already at the actor's service. (This isn't an error, because the other actor might not have been talking to us, even though we thought we were talking to them.)


## Inherited Methods


<details><summary>From [ActorState](actorstate.md) (21)</summary>

[`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`beforeTravel`](actorstate.md#beforeTravel), [`construct`](actorstate.md#construct), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`initializeActorState`](actorstate.md#initializeActorState), [`justFollowed`](actorstate.md#justFollowed), [`notifyTopicResponse`](actorstate.md#notifyTopicResponse), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDesc`](actorstate.md#specialDesc), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
