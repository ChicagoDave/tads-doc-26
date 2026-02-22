# ActorState

*class* — defined in [actor.t](../by-file/actor.t.md) (line 4116)


An ActorState represents the current state of an Actor.


**Superclass chain:** [TravelMessageHandler](travelmessagehandler.md) > `object` > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **ActorStateSubclasses:** [AccompanyingInTravelState](accompanyingintravelstate.md), [GuidedInTravelState](guidedintravelstate.md), [AccompanyingState](accompanyingstate.md), [GuidedTourState](guidedtourstate.md), [ConversationReadyState](conversationreadystate.md), [HermitActorState](hermitactorstate.md), [InConversationState](inconversationstate.md)


## Properties


### `autoSuggest`

Defined in actor.t, line 4156

Should we automatically suggest topics when the player greets our actor? By default, we show our "topic inventory" (the list of currently active topics marked as "suggested"). This can be set to nil to suppress this automatic suggestion list.


### `getImpliedConvState`

Defined in actor.t, line 4374

Get my implied in-conversation state. This is used when our actor initiates a conversation without specifying a particular conversation state to enter (i.e., actor.initiateConversation() is called with 'state' set to nil). By default, we don't have an implied conversation state, so we just return 'self' to indicate that we want to stay in the current state. States that are coupled with separate in-conversation states, such as ConversationReadyState, should return their associated conversation states here.


### `isInitState`

Defined in actor.t, line 4140

Is this the actor's initial state? If so, we'll automatically set the actor's curState to point to 'self' during pre-initialization. For obvious reasons, this should be set to true for only one state for each actor; if multiple states are all flagged as initial for the same actor, we'll pick on arbitrarily as the actual initial state.


### `location`

Defined in actor.t, line 4167

The 'location' is the actor that we're associated with.


### `stateDesc`

Defined in actor.t, line 4251

Our "state" description. This shows information on what the actor is *currently* doing; we display this after the static part of the actor's description on EXAMINE <ACTOR>. By default, we add nothing here, but state objects that represent scripted activies should override this to describe their scripted activities.


### `stateSuggestedTopics`

Defined in actor.t, line 4361

get the topic suggestions for this state - by default, we just return our own suggestedTopics list


## Inherited Properties


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `activateState(actor, oldState)`

Defined in actor.t, line 4123

Activate the state - this is called when we're about to become the active state for an actor. We do nothing by default.


### `afterAction`

Defined in actor.t, line 4491

handle an after-action notification for our actor


### `afterTravel(traveler, connector)`

Defined in actor.t, line 4521

handle an after-travel notification


### `arrivingTurn`

Defined in actor.t, line 4706

Perform any special action on a group-travel arrival. When group travel is performed using the AccompanyingInTravelState class, this is essentially called in lieu of the regular takeTurn() method on the state that is coming into effect after the group travel. (Not really, but effectively: the accompanying travel state will still be in effect, so its takeTurn() method is what's really called, but that method will call this method explicitly.) By default, we do nothing. Since this runs on our turn, it's a good place to put any scripted behavior we perform on arriving at our new destination after the group travel.


### `arrivingWithDesc`

Defined in actor.t, line 4692

Our group-travel arrival description. By default, when we perform an accompanying travel with another actor as the lead actor, the accompanying travel state will display this message instead of our specialDesc when the lead actor first arrives in the new location. We'll just display our own specialDesc by default, but this should usually be overridden to say something specific to the group travel arrival. The actual message is entirely dependent on the nature of the group travel, which is why we don't provide a special message by default.


### `beforeAction`

Defined in actor.t, line 4485

Handle a before-action notification for our actor. By default, we do nothing.


### `beforeTravel(traveler, connector)`

Defined in actor.t, line 4496

handle a before-travel notification


### `construct(actor)`

Defined in actor.t, line 4117


### `deactivateState(actor, newState)`

Defined in actor.t, line 4130

Deactivate the state - this is called when we're the active state for an actor, and the actor is about to switch to a new state. We do nothing by default.


### `distantSpecialDesc`

Defined in actor.t, line 4210

show the special description for the actor at a distance


### `endConversation(actor, reason)`

Defined in actor.t, line 4534

End the current conversation. 'reason' indicates why we're leaving the conversation - this is one of the endConvXxx enums defined in adv3.h. beforeTravel() calls this automatically when the other party is trying to depart, and they're talking to us.


### `getActor`

Defined in actor.t, line 4174

Get the actor associated with the state - this is simply the 'location' property. If we're nested inside another ActorState, then our actor is our enclosing ActorState's actor.


### `getNominalTraveler` *(overridden)*

Defined in actor.t, line 4714

For our TravelMessageHandler implementation, the nominal traveler is our actor. Note that this is all we need to implement for travel message handling, since we simply inherit the default handling for all of the arrival/departure messages.


### `getSuggestedTopicList`

Defined in actor.t, line 4315

Get our suggested topic list. The suggested topic list consists of the union of the current ConvNode's suggestion list, the ActorState list, and the Actor's suggestion list. In each case, the suggestion list is the list of all SuggestedTopic objects at each database level.


### `getTopicOwner` *(overridden)*

Defined in actor.t, line 4183

the owner of any topic entries within the state is just my actor


### `handleConversation(otherActor, topic, convType)`

Defined in actor.t, line 4397

General conversation handler. This can be used to process most conversational commands - ASK, TELL, GIVE, SHOW, etc. The standard sequence of processing is as follows:


### `initializeActorState`

Defined in actor.t, line 4186

initialize the actor state


### `justFollowed(success)`

Defined in actor.t, line 4667

Receive notification that we just followed another actor as part of our programmed following behavior (in other words, due to our 'followingActor' property, not due to an explicit FOLLOW command directed to us). 'success' is true if we ended up in the actor's location, nil if not.


### `notifyTopicResponse(fromActor, entry)`

Defined in actor.t, line 4479

Receive notification that a TopicEntry is being used (via its handleTopic method) to respond to a command. The TopicEntry will call this before it shows its message or takes any other action. By default, we do nothing.


### `obeyCommand(issuingActor, action)`

Defined in actor.t, line 4259

Should we obey an action? If so, returns true; if not, displays an appropriate response and returns nil. This will only be called when the issuing actor is different from our actor, since a command to oneself is implicitly always obeyed.


### `remoteSpecialDesc(actor)`

Defined in actor.t, line 4213

show the special description for the actor in a remote location


### `showSpecialDescInContents(actor, cont)`

Defined in actor.t, line 4238

show the special description when we appear in a contents listing


### `specialDesc`

Defined in actor.t, line 4207

Show the special description for the actor when the actor is associated with this state. By default, we use the actor's actorHereDesc message, which usually shows a generic message (something like "Bob is here" or "Bob is sitting on the chair") to indicate that the actor is present.


### `specialDescListWith`

Defined in actor.t, line 4224

The list group(s) for the special description. By default, if our specialDesc isn't overridden, we'll keep this in sync with the specialDesc by returning our actor's actorListWith. And if specialDesc *is* overridden, we'll just return an empty list to indicate that we're not part of any list group. If you want to provide your own listing group special to the state, simply override this and speicfy the custom list group.


### `suggestTopicsFor(actor, explicit)`

Defined in actor.t, line 4278

Suggest topics for the given actor to talk to us about. This is called when the given actor enters a TOPICS command (in which case 'explicit' will be true) or enters a conversation with us via TALK TO or the like (in which case 'explicit' will be nil).


### `takeTurn`

Defined in actor.t, line 4619

Take a turn. This is called when it's the actor's turn and there's not something else the actor needs to be doing (such as following another actor, or carrying out a command in the actor's pending command queue).


## Inherited Methods


*From [TravelMessageHandler](travelmessagehandler.md):* [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
