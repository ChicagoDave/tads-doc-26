# ConvNode

*class* — defined in [actor.t](../by-file/actor.t.md) (line 1479)


A conversation node. Conversation nodes are supplemental topic databases that represent a point in time in a conversation - a particular context that arises from what came immediately before in the conversation. A conversation node is used to set up a group of special responses that make sense only in a momentary context within a conversation.


**Superclass chain:** [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > `object` > **ConvNode**


## Properties


### `activeSpecialTopic`

Defined in actor.t, line 1842

The active special topic. This is the SpecialTopic object that we matched during pre-parsing, so it's the one whose response we wish to show while processing the command we pre-parsed.


### `isSticky`

Defined in actor.t, line 1509

Is this node "sticky"? If so, we'll stick to this node if we show a response that doesn't set a new node. By default, we're not sticky, so if we show a response that doesn't set a new node and doesn't use a <.convstay> tag, we'll simply forget the node and set the actor to no current ConvNode.


### `name`

Defined in actor.t, line 1495

Every ConvNode must have a name property. This is a string identifying the object. Use this name string instead of a regular object name (so ConvNode instances can essentially always be anonymous, as far as the compiler is concerned). This string is used to find the ConvNode in the master ConvNode database maintained in the conversationManager object.


### `npcContinueList`

Defined in actor.t, line 1552

An optional EventList containing NPC-initiated continuation messages. You can define an EventList here instead of defining npcContinueMsg, if you want more than one continuation message.


### `npcContinueMsg`

Defined in actor.t, line 1545

Our NPC-initiated conversation continuation message. This is invoked on each turn (during the NPC's takeTurn() daemon processing) that we're in this conversation node and the player character doesn't do anything conversational. This allows the NPC to carry on the conversation of its own volition. Define this as a double-quoted string if you want the NPC to say something to continue the conversation.


### `npcGreetingList`

Defined in actor.t, line 1534

an optional EventList containing our NPC-initiated greetings


### `patDelim`

Defined in actor.t, line 1784


### `patWhitespace`

Defined in actor.t, line 1783

proceed, treating the original input as an ordinary command


## Inherited Properties


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `autoShowTopics`

Defined in actor.t, line 1565

Flag: automatically show a topic inventory on activating this conversation node. Some conversation nodes have sufficiently obscure entries that it's desirable to show a topic inventory automatically when the node becomes active.


### `canEndConversation(actor, reason)`

Defined in actor.t, line 1680

Can we end the conversation? If so, return true; our caller will invoke our endConversation() to let us know that the conversation is over.


### `endConversation(actor, reason)`

Defined in actor.t, line 1697

Receive notification that our actor is ending a stateful conversation. This is called before the normal InConversationState disengagement operations. 'reason' is one of the endConvXxx enums, indicating why the conversation is ending.


### `getActor`

Defined in actor.t, line 1634

our actor is our location, or our location's actor


### `getTopicOwner` *(overridden)*

Defined in actor.t, line 1645

our actor is the "owner" of our topics


### `handleConversation(otherActor, topic, convType, path)`

Defined in actor.t, line 1655

Handle a conversation topic. The actor state object will call this to give the ConvNode the first crack at handling a conversation command. We'll return true if we handle the command, nil if not. Our default handling is to look up the topic in the given database list property, and handle it through the TopicEntry we find there, if any.


### `noteActive`

Defined in actor.t, line 1880

Note that we're becoming active, with a reason code. Our actor will call this method when we're becoming active, as long as we weren't already active.


### `noteActiveReason(reason)`

Defined in actor.t, line 1866

Note that we're becoming active, with a reason code. Our actor will call this method when we're becoming active, as long as we weren't already active.


### `noteLeaving`

Defined in actor.t, line 1892

Note that we're leaving this conversation node. This doesn't do anything by default, but individual instances might find the notification useful for triggering side effects.


### `npcContinueConversation`

Defined in actor.t, line 1597

Continue the conversation of the NPC's own volition. Returns true if we displayed anything, nil if not.


### `npcGreetingMsg`

Defined in actor.t, line 1526

Show our NPC-initiated greeting. This is invoked when our actor's initiateConversation() method is called to cause our actor to initiate a conversation with the player character. This method should show what our actor says to initiate the conversation. By default, we'll invoke our npcGreetingList's script, if the property is non-nil.


### `npcInitiateConversation`

Defined in actor.t, line 1573

our NPC is initiating a conversation starting with this node


### `processSpecialCmd(str, procStr)`

Defined in actor.t, line 1717

Process a special command. Check the given command line string against all of our topics, and see if we have a match to any topic that takes a special command syntax. If we find a matching special topic, we'll note the match, and turn the command into our secret internal pseudo-command "XSPCLTOPIC". That command will then go through the parser, which will recognize it and process it using the normal conversational mechanisms, which will find the SpecialTopic we noted earlier (in this method) and display its response.


### `saySpecialTopic(fromActor)`

Defined in actor.t, line 1801

Handle an XSPCLTOPIC command from the given actor. This is part two of the two-phase processing of SpecialTopic matches. Our pre-parser checks each SpecialTopic's custom syntax for a match to the player's text input, and if it finds a match, it sets our activeSpecialTopic property to the matching SpecialTopic, and changes the user's command to XSPCLTOPIC for processing by the regular parser. The regular parser sees the XSPCLTOPIC command, which is a valid verb that calls the issuing actor's saySpecialTopic() routine, which in turn forwards the request to the issuing actor's interlocutor's current conversation node - which is to say, 'self'. We complete the two-step procedure by going back to the active special topic object that we previously noted and showing its response.


## Inherited Methods


*From [ActorTopicDatabase](actortopicdatabase.md):* [`initiateTopic`](actortopicdatabase.md#initiateTopic), [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
