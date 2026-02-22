# ConversationReadyState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 4742)


A "ready for conversation" state. This can be used as the base class for actor states when the actor is receptive to conversation, and we want to have the sense of a conversational context. The key feature that this class provides is the ability to provide messages when engaging and disengaging the conversation.


**Superclass chain:** [ActorState](actorstate.md) > [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **ConversationReadyState**


## Properties


### `getImpliedConvState` *(overridden)*

Defined in actor.t, line 4753

my implied conversational state is my in-conversation state


### `inConvState`

Defined in actor.t, line 4750

The associated in-conversation state. This should be set to an InConversationState object that controls the actor's behavior while carrying on a conversation. Note that the library will automatically set this if the instance is nested (via its 'location' property) inside an InConversationState object.


### `stateSuggestedTopics` *(overridden)*

Defined in actor.t, line 4934

Get this state's suggested topic list. ConversationReady states shouldn't normally have topic entries of their own, since a ConvversationReady state usually forwards conversation handling to its corresponding in-conversation state. So, simply return the suggestion list from our in-conversation state object.


## Inherited Properties


*From [ActorState](actorstate.md):* [`autoSuggest`](actorstate.md#autoSuggest), [`isInitState`](actorstate.md#isInitState), [`location`](actorstate.md#location), [`stateDesc`](actorstate.md#stateDesc)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `enterConversation(actor, entry)`

Defined in actor.t, line 4899

Enter a conversation with the given actor, either explicitly (via HELLO or TALK TO) or implicitly (by directly asking a question, etc). 'entry' gives the TopicEntry that's triggering the implicit conversation entry; if this is nil, it means that we're being triggered explicitly.


### `enterFromConversation(actor, reason, oldNode)`

Defined in actor.t, line 4815

Enter this state from a conversation. This should show any message we want to display when we're ending a conversation and switching from the conversation to this state. 'reason' is the endConvXxx enum indicating what triggered the termination of the conversation. 'oldNode' is the ConvNode we were in just before we initiated the termination - we need this information because we want to look in the ConvNode for a Bye topic message to display, but we can't just look in the actor for the node because it will already have been cleared out by the time we get here.


### `handleConversation(otherActor, topic, convType)` *(overridden)*

Defined in actor.t, line 4839

handle a conversational action directed to our actor


### `initializeActorState` *(overridden)*

Defined in actor.t, line 4937

initialize the actor state object


### `initiateTopic(obj)` *(overridden)*

Defined in actor.t, line 4875

Initiate conversation based on the given simulation object. This is an internal method that isn't usually called directly from game code; game code usually calls the Actor's initiateTopic(), which calls this routine to check for a topic that's part of the state object.


### `notifyTopicResponse(fromActor, entry)` *(overridden)*

Defined in actor.t, line 4886

Receive notification that a TopicEntry is being used (via its handleTopic method) to respond to a command. If the TopicEntry is conversational, automatically enter our in-conversation state.


### `showGreetingMsg(actor, explicit)`

Defined in actor.t, line 4783

Show our greeting message. If 'explicit' is true, it means that the player character is greeting us through an explicit greeting command, such as HELLO or TALK TO. Otherwise, the greeting is implied by some other conversational action, such a ASK ABOUT or SHOW TO. We do nothing by default; this should be overridden in most cases to show some sort of exchange of pleasantries - something like this:


## Inherited Methods


<details><summary>From [ActorState](actorstate.md) (23)</summary>

[`activateState`](actorstate.md#activateState), [`afterAction`](actorstate.md#afterAction), [`afterTravel`](actorstate.md#afterTravel), [`arrivingTurn`](actorstate.md#arrivingTurn), [`arrivingWithDesc`](actorstate.md#arrivingWithDesc), [`beforeAction`](actorstate.md#beforeAction), [`beforeTravel`](actorstate.md#beforeTravel), [`construct`](actorstate.md#construct), [`deactivateState`](actorstate.md#deactivateState), [`distantSpecialDesc`](actorstate.md#distantSpecialDesc), [`endConversation`](actorstate.md#endConversation), [`getActor`](actorstate.md#getActor), [`getNominalTraveler`](actorstate.md#getNominalTraveler), [`getSuggestedTopicList`](actorstate.md#getSuggestedTopicList), [`getTopicOwner`](actorstate.md#getTopicOwner), [`justFollowed`](actorstate.md#justFollowed), [`obeyCommand`](actorstate.md#obeyCommand), [`remoteSpecialDesc`](actorstate.md#remoteSpecialDesc), [`showSpecialDescInContents`](actorstate.md#showSpecialDescInContents), [`specialDesc`](actorstate.md#specialDesc), [`specialDescListWith`](actorstate.md#specialDescListWith), [`suggestTopicsFor`](actorstate.md#suggestTopicsFor), [`takeTurn`](actorstate.md#takeTurn)

</details>


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
