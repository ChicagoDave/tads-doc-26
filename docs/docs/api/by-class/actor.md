# Actor

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5670)


An Actor is a living person, animal, or other entity with a will of its own. Actors can usually be addressed with targeted commands ("bob, go north"), and with commands like ASK ABOUT, TELL ABOUT, GIVE TO, and SHOW TO.


**Superclass chain:** [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > [Schedulable](schedulable.md) > [Traveler](traveler.md) > [TravelMessageHandler](travelmessagehandler.md) > [ActorTopicDatabase](actortopicdatabase.md) > [TopicDatabase](topicdatabase.md) > **ActorSubclasses:** [UntakeableActor](untakeableactor.md), [Person](person.md)


## Properties


### `accompanyingActors`

Defined in actor.t, line 7816

My vector of actors who are accompanying me.


### `actorNotifyList`

Defined in actor.t, line 8499

our list of registered actor notification items


### `agendaList`

Defined in actor.t, line 6922

The actor's "agenda." This is a list of AgendaItem objects that describe things the actor wants to do of its own volition on its own turn.


### `antecedentTable`

Defined in actor.t, line 9953

Antecedent lookup table. Each actor keeps its own table of antecedents indexed by pronoun type, so that we can simultaneously have different antecedents for different pronouns.


### `boredomAgendaItem`

Defined in actor.t, line 6929

our special "boredom" agenda item - this makes us initiate an end to an active conversation when the PC has ignored us for a given number of consecutive turns


### `boredomCount`

Defined in actor.t, line 6831

Our conversational "boredom" counter. While we're in a conversation, this tracks the number of turns since the last conversational command from the actor we're talking to.


### `bulkCapacity`

Defined in actor.t, line 6339

You can limit the cumulative amount of bulk an actor can hold, and the maximum bulk of any one object the actor can hold, using bulkCapacity and maxSingleBulk. These properties are analogous to the same ones in Container.


### `canMatch3rdPerson`

Defined in en_us.t, line 2391

Test to see if we can match a third-person pronoun ('it', 'him', 'her', 'them'). We can unless we're the player character and the player character is referred to in the first or second person.


### `canMatchHer` *(overridden)*

Defined in en_us.t, line 2382


### `canMatchHim` *(overridden)*

Defined in en_us.t, line 2381

Test to see if we can match the third-person pronouns. We'll match these if our inherited test says we match them AND we can be referred to in the third person.


### `canMatchIt` *(overridden)*

Defined in en_us.t, line 2383


### `canMatchThem` *(overridden)*

Defined in en_us.t, line 2384


### `commandReferralPerson`

Defined in actor.t, line 6238

The referral person of the current command targeting the actor. This is meaningful only when a command is being directed to this actor, and this actor is an NPC.


### `communicationSenses`

Defined in actor.t, line 7574

Communication senses: these are the senses through which the actor can communicate directly with other actors through commands and messages.


### `contentsListed` *(overridden)*

Defined in actor.t, line 5948

the contents of an actor aren't listed in a room's description


### `convMgrID`

Defined in actor.t, line 5778

conversation manager ID - this is assigned by the conversation manager to map to and from output stream references to the actor; this is only for internal use by the conversation manager


### `convNodeTab`

Defined in actor.t, line 5726

Our table of conversation nodes. At initialization, the conversation manager scans all ConvNode instances and adds each one to its actor's table. This table is keyed by the name of node, and the value for each entry is the ConvNode object - this lets us look up the ConvNode object by name. Because each actor has its own lookup table, ConvNode names only have to be unique within the actor's set of ConvNodes.


### `curConvNode`

Defined in actor.t, line 5715

Our current conversation node. This is a ConvNode object that keeps track of the flow of the conversation.


### `curState`

Defined in actor.t, line 5690

Our current state. This is an ActorState object representing what we're currently doing. Whenever the actor changes to a new state (for example, because of a scripted activity), this can be changed to reflect the actor's new state. The state object groups the parts of the actor's description and other methods that tend to vary according to what the actor's doing; it's easier to keep everything related to scripted activities together in a state object than it is to handle all of the variability with switch() statements of the like in methods directly in the actor.


### `excludeFromLookAroundList`

Defined in actor.t, line 7483

Our list of objects explicitly excluded from 'look around'. These objects will be suppressed from any sort of listing (including in the room's contents list and in special descriptions) in 'look around' when this actor is doing the looking.


### `followables_`

Defined in actor.t, line 8158

Our list of followable information. Each entry in this list is a FollowInfo object that tracks a particular followable.


### `followingActor`

Defined in actor.t, line 9235

If we're following an actor, this keeps track of the actor we're following. NPC's can use this to follow around another actor whenever possible.


### `getTravelerActors` *(overridden)*

Defined in actor.t, line 6435

Get the actors involved in travel, when we're acting in our role as a Traveler. When the Traveler is simply the Actor, the only actor involved in the travel is 'self'.


### `getTravelerMotiveActors` *(overridden)*

Defined in actor.t, line 6438

we're the self-motive actor doing the travel


### `hearinglikeSenses`

Defined in actor.t, line 7546

Hearing-like senses. These are senses that the actor can use to hear objects.


### `holdingDescInventoryLister`

Defined in actor.t, line 8927

The Lister for inventory listings, for use in a full description of the actor. By default, we use the "long form" inventory lister, on the assumption that most actors have relatively lengthy descriptive text. This can be overridden to use other formats; the short-form lister, for example, is useful for actors with only brief descriptions.


### `inventoryLister`

Defined in actor.t, line 8917

The Lister object that we use for inventory listings. By default, we use actorInventoryLister, but this can be overridden if desired to use a different listing style.


### `isActor`

Defined in actor.t, line 5672

flag: we're an actor


### `isLikelyCommandTarget` *(overridden)*

Defined in actor.t, line 9506

By default, all actors are likely command targets. This should be overridden for actors who are obviously not likely to accept commands of any kind.


### `isListed`

Defined in actor.t, line 5943

Actors are not listed with the ordinary objects in a room's description. However, an actor is listed as part of an inventory description.


### `isListedAboardVehicle` *(overridden)*

Defined in actor.t, line 6368

by default, actors are listed when they arrive aboard a vehicle


### `isListedInContents`

Defined in actor.t, line 5944


### `isListedInInventory`

Defined in actor.t, line 5945


### `issueCommandsSynchronously`

Defined in actor.t, line 7695

Flag: we wait for commands issued to other actors to complete before we get another turn. If this is true, then whenever we issue a command to another actor ("bob, go north"), we will not get another turn until the other actor has finished executing the full set of commands we issued.


### `knownProp`

Defined in actor.t, line 8228

My 'known' property. By default, this is simply 'known', which means that we don't distinguish who knows what.


### `lastConsulted`

Defined in actor.t, line 6915

the object we most recently consulted


### `lastConvTime`

Defined in actor.t, line 6837

game-clock time (Schedulable.gameClockTime) of the last conversational command addressed to us by the player character


### `lastDoorTraversed`

Defined in actor.t, line 6700

the last door I traversed


### `lastInterlocutor`

Defined in actor.t, line 6818

The most recent actor that we've interacted with through a conversational command (ASK, TELL, GIVE, SHOW, etc).


### `lastTravelBack`

Defined in actor.t, line 6704


### `lastTravelDest`

Defined in actor.t, line 6703

the destination and back connector for our last travel


### `locationBefore`

Defined in actor.t, line 9000

conditions we noted in noteConditionsBefore()


### `locationLitBefore`

Defined in actor.t, line 9001


### `maxSingleBulk`

Defined in actor.t, line 6340


### `mostRecentAction`

Defined in actor.t, line 9147

the action the actor performed most recently


### `name` *(overridden)*

Defined in en_us.t, line 2131

by default, use my pronoun for my name


### `nextHoldingIndex`

Defined in actor.t, line 7293

Next available "holding index" value. Each time we pick up an item, we'll assign it our current holding index value and then increment our value. This gives us a simple way to keep track of the order in which we picked up items we're carrying.


### `nextRunTime` *(overridden)*

Defined in actor.t, line 9004

let the actor have a turn as soon as the game starts


### `pcReferralPerson`

Defined in actor.t, line 6223

by default, refer to the player character in the second person


### `pendingCommand`

Defined in actor.t, line 9794

pending commands - this is a list of PendingCommandInfo objects


### `pendingConv`

Defined in actor.t, line 5911

Our list of pending conversation initiators. In our takeTurn() processing, we'll check this list for conversations that we can initiate.


### `pendingResponse`

Defined in actor.t, line 9801

pending response - this is a single PendingResponseInfo object, which we'll deliver as soon as the issuing actor is in a position to hear us


### `possAnaphorTable`

Defined in actor.t, line 9965

Possessive anaphor lookup table. In almost all cases, the possessive anaphor for a given pronoun will be the same as the corresponding regular pronoun: HIS indicates possession by HIM, for example. In a few cases, though, the anaphoric quality of possessives takes precedence, and these will differ. For example, in TELL BOB TO DROP HIS BOOK, "his" refers back to Bob, while in TELL BOB TO HIT HIM, "him" refers to whatever it referred to before the command.


### `posture`

Defined in actor.t, line 7322

My current "posture," which specifies how we're positioned with respect to our container; this is one of the standard library posture enum values (Standing, etc.) or another posture added by the game.


### `responseSetConvNode`

Defined in actor.t, line 5785

Flag indicating whether or not we've set a ConvNode in the course of the current response. This is for use by the converstaion manager.


### `revertTargetActorAtEndOfSentence`

Defined in actor.t, line 7722

Flag: the "target actor" of the command line automatically reverts to this actor at the end of a sentence, when this actor is the issuer of a command. If this flag is nil, an explicit target actor stays in effect until the next explicit target actor (or the end of the entire command line, if no other explicit target actors are named); if this flag is true, a target actor is in effect only until the end of a sentence.


### `scheduleOrder` *(overridden)*

Defined in actor.t, line 9028

Scheduling order - this determines the order of execution when several items are schedulable at the same game clock time.


### `scopeSenses`

Defined in actor.t, line 7514

The senses that determine scope for this actor. An actor might possess only a subset of the defined sense.


### `seenProp`

Defined in actor.t, line 8215

My 'seen' property. By default, this is simply 'seen', which means that we don't distinguish who's seen what - in other words, there's a single, global 'seen' flag per object, and if anyone's ever seen something, then we consider that to mean everyone has seen it.


### `sightlikeSenses`

Defined in actor.t, line 7540

"Sight-like" senses: these are the senses that operate like sight for the actor, and which the actor can use to determine the names of objects and the spatial relationships between objects. These senses should operate passively, in the sense that they should tend to collect sensory input continuously and without explicit action by the actor, the way sight does and the way touch, for example, does not. These senses should also operate instantly, in the sense that the sense can reasonably take in most or all of a location at one time.


### `smelllikeSenses`

Defined in actor.t, line 7552

Smell-like senses. These are senses that the actor can use to smell objects.


### `specialDescBeforeContents` *(overridden)*

Defined in actor.t, line 6063

By default, show the special description for an actor in the group of special descriptions that come *after* the room's portable contents listing. An actor's presence is usually a dynamic feature of a room, and so we don't want to suggest that the actor is a permanent feature of the room by describing the actor directly with the room's main description.


### `specialDescOrder` *(overridden)*

Defined in actor.t, line 6082

By default, put all of the actor special descriptions after the special descriptions of ordinary objects, by giving actors a higher listing order value.


### `specialTraveler`

Defined in actor.t, line 6462

our special traveler


### `takeFromNotInMessage` *(overridden)*

Defined in actor.t, line 10047

show a "take from" message as indicating I don't have the dobj


### `waitingForActor`

Defined in actor.t, line 7785

Synchronous command processing: the target actor and dummy pending command we're waiting for. When these are non-nil, we won't take another turn until the given PendingCommandInfo has been removed from the given target actor's command queue.


### `waitingForInfo`

Defined in actor.t, line 7786


### `weightCapacity`

Defined in actor.t, line 6348

An actor can limit the cumulative amount of weight being held, using weightCapacity. By default we make this so large that there is effectively no limit to how much weight an actor can carry.


## Inherited Properties


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorInPrep`](thing.md#actorInPrep), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`actorOutOfPrep`](thing.md#actorOutOfPrep), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`brightness`](thing.md#brightness), [`bulk`](thing.md#bulk), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`contentsLister`](thing.md#contentsLister), [`descContentsLister`](thing.md#descContentsLister), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`effectiveFollowLocation`](thing.md#effectiveFollowLocation), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`isTopLevel`](thing.md#isTopLevel), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`lookInLister`](thing.md#lookInLister), [`moved`](thing.md#moved), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`notTravelReadyMsg`](thing.md#notTravelReadyMsg), [`objectNotifyList`](thing.md#objectNotifyList), [`objInPrep`](thing.md#objInPrep), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`roomLocation`](thing.md#roomLocation), [`roomName`](thing.md#roomName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`sightSize`](thing.md#sightSize), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialContentsLister`](thing.md#specialContentsLister), [`specialDesc`](thing.md#specialDesc), [`specialDescListWith`](thing.md#specialDescListWith), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont), [`weight`](thing.md#weight)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


*From [Schedulable](schedulable.md):* [`allSchedulables`](schedulable.md#allSchedulables), [`gameClockTime`](schedulable.md#gameClockTime)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`askForTopics`](actortopicdatabase.md#askForTopics), [`askTopics`](actortopicdatabase.md#askTopics), [`commandTopics`](actortopicdatabase.md#commandTopics), [`giveTopics`](actortopicdatabase.md#giveTopics), [`initiateTopics`](actortopicdatabase.md#initiateTopics), [`miscTopics`](actortopicdatabase.md#miscTopics), [`showTopics`](actortopicdatabase.md#showTopics), [`specialTopics`](actortopicdatabase.md#specialTopics), [`tellTopics`](actortopicdatabase.md#tellTopics)


*From [TopicDatabase](topicdatabase.md):* [`limitSuggestions`](topicdatabase.md#limitSuggestions), [`suggestedTopics`](topicdatabase.md#suggestedTopics), [`topicGroupActive`](topicdatabase.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicdatabase.md#topicGroupScoreAdjustment)


## Methods


### `acceptCommand(issuingActor)` *(overridden)*

Defined in actor.t, line 9529

Determine if we should accept a command. 'issuingActor' is the actor who issued the command: if the player typed the command on the command line, this will be the player character actor.


### `acceptCommandBusy(issuingActor)`

Defined in actor.t, line 9573

Check to see if I'm busy with pending commands, and if so, whether or not I should accept a new command. Returns true if we should accept a command, nil if not. If we return nil, we must notify the issuer of the rejection.


### `actorAction`

Defined in actor.t, line 8373

Perform any actor-specific processing for an action. The main command processor invokes this on gActor after notifying nearby objects via beforeAction(), but before carrying out the main action of the command.


### `actorActionFollow(obj)`

Defined in actor.t, line 7990

Carry out a "follow" command being performed by this actor.


### `actorHereDesc`

Defined in actor.t, line 6117

Actor "I am here" description. This is displayed as part of the description of a room - it describes the actor as being present in the room. By default, we let the "nominal actor container" provide the description.


### `actorListWith`

Defined in actor.t, line 6089

Get my listing group for my special description as part of a room description. By default, we'll let our immediate location decide how we're grouped.


### `actorRoomNameStatus(room)`

Defined in actor.t, line 6145

Show our status, as an addendum to the given room's name (this is the room title, shown at the start of a room description and on the status line). By default, we'll let our nominal actor container provide the status, to indicate when we're standing/sitting/lying in a nested room.


### `actorThereDesc`

Defined in actor.t, line 6125

Actor's "I am over there" description. This is displayed in the room description when the actor is visible, but is either in a separate top-level room or is at a distance. By default, we let the "nominal actor container" provide the description.


### `actorTravel(traveler, connector)`

Defined in actor.t, line 8422

Receive notification that I'm initiating travel. This is called on the actor performing the travel action before the travel is actually carried out.


### `actorVerifyFollow(obj)`

Defined in actor.t, line 7934

Verify a "follow" command being performed by this actor.


### `addAccompanyingActor(actor)`

Defined in actor.t, line 7796

Add the given actor to the list of actors accompanying my travel on the current turn. This does NOT set an actor in "follow mode" or "accompany mode" or anything like that - don't use this to make an actor follow me around. Instead, this makes the given actor go with us for the CURRENT travel only - the travel we're already in the process of performing to process the current TravelVia action.


### `addActorNotifyItem(obj)`

Defined in actor.t, line 8487

Add an item to our registered notification items. These items are to receive notifications when we're the actor performing a command.


### `addBusyTime(action, units)`

Defined in actor.t, line 9154

Add busy time. An action calls this when we are the actor performing the action, and the action consumes game time. This marks us as busy for the given time units.


### `addFirstPendingAction(startOfSentence, issuer, action, [objs])`

Defined in actor.t, line 9785

Insert a resolved action at the start of our pending command list. The new command is specified as a resolved Action object; it is added before any commands already in our list.


### `addFirstPendingCommand(startOfSentence, issuer, toks)`

Defined in actor.t, line 9761

Insert a command at the head of our pending command list. The new command is specified as a list of tokens to parse, and it is inserted into our pending command list before any commands already in the list.


### `addPendingAction(startOfSentence, issuer, action, [objs])`

Defined in actor.t, line 9773

Add a resolved action to our pending command list. The new command is specified as a resolved Action object; it is added after any commands already in our list.


### `addPendingCommand(startOfSentence, issuer, toks)`

Defined in actor.t, line 9748

Add a command to our pending command list. The new command is specified as a list of tokens to be parsed, and it is added after any commands already in our pending list.


### `addToAgenda(item)`

Defined in actor.t, line 6932

add an agenda item


### `addToContents(obj)` *(overridden)*

Defined in actor.t, line 7296

add an object to my contents


### `adjustLookAroundTable(tab, pov, actor)` *(overridden)*

Defined in actor.t, line 7443

Adjust a table of visible objects for 'look around'. By default, we remove any explicitly excluded objects.


### `afterAction` *(overridden)*

Defined in actor.t, line 8382

Receive notification that a command has just been carried out in our presence.


### `afterTravel(traveler, connector)` *(overridden)*

Defined in actor.t, line 8411

receive a notification that someone has just traveled here


### `aName`

Defined in en_us.t, line 2316

Get the name with an indefinite article. Use the same rules of referral person as for definite articles.


### `aNameObj` *(overridden)*

Defined in en_us.t, line 2319

aName in objective case


### `beforeAction` *(overridden)*

Defined in actor.t, line 8349

Receive notification that a command is being carried out in our presence.


### `beforeTravel(traveler, connector)` *(overridden)*

Defined in actor.t, line 8389

receive a notification that someone is about to travel


### `bestVisualInfo(obj)`

Defined in actor.t, line 8559

Get the best (most transparent) sense information for one of our visual senses to the given object.


### `calcScheduleOrder` *(overridden)*

Defined in actor.t, line 9031

calculate the scheduling order


### `canBeTalkedTo(talker, sense, info)`

Defined in actor.t, line 7663

Determine whether or not I can understand an attempt by another actor to talk to me. 'talker' is the actor doing the talking. 'sense' is the sense we're testing; this will always be a sense in our communicationSenses list, and will always be a communications sense we have in common with the other actor. 'info' is a SenseInfo object giving information on the clarity of the sense path to the other actor.


### `canHear(obj)` *(overridden)*

Defined in actor.t, line 8685

Determine if I can hear the given object.


### `cannotFollow`

Defined in actor.t, line 9247

Handle a situation where we're trying to follow an actor but can't. By default, this simply cancels our follow mode.


### `cannotRespondToCommand(issuingActor, messageProp, args)`

Defined in actor.t, line 9912

We have a parser error to report to the player, but we cannot respond at the moment because the player is not capable of hearing us (there is no sense path for our communications senses from us to the player actor). Defer reporting the message until later.


### `canOwn(obj)` *(overridden)*

Defined in actor.t, line 6354

Can I own the given object? By default, an actor can own anything.


### `canSee(obj)` *(overridden)*

Defined in actor.t, line 8665

Determine if I can see the given object. This returns true if the object can be sensed at all in one of my sight-like senses, nil if not.


### `canSmell(obj)` *(overridden)*

Defined in actor.t, line 8705

Determine if I can smell the given object.


### `canTalkTo(actor)`

Defined in actor.t, line 7592

Determine if I can communicate with the given character via a natural, default form of communication that we share with the other character. This determines if I can talk to the other character. We'll return true if I can talk to the other actor, nil if not.


### `checkBulkChangeWithin(obj)` *(overridden)*

Defined in actor.t, line 7252

Check a bulk change of one of my direct contents.


### `checkDarkTravel(dest, connector)`

Defined in actor.t, line 6568

Check for travel in the dark. If we're in a dark room, and our destination is a dark room, ask the connector for guidance.


### `checkMovingTravelerInto(room, allowImplicit)` *(overridden)*

Defined in actor.t, line 6468

Try moving the actor into the given room in preparation for travel, using pre-condition rules.


### `checkReadyToEnterNestedRoom(dest, allowImplicit)`

Defined in actor.t, line 6479

Check to ensure the actor is ready to enter the given nested room, using pre-condition rules. By default, we'll ask the given nested room to handle it.


### `checkStagingLocation(dest)` *(overridden)*

Defined in actor.t, line 6710

use a custom message for cases where we're holding a destination object for BOARD, ENTER, etc


### `checkTakeFromInventory(actor, obj)`

Defined in actor.t, line 8459

Check to see if we want to allow another actor to take something from my inventory. By default, we won't allow it - we'll always fail the command.


### `checkWaitingForActor`

Defined in actor.t, line 9090

Check to see if we're waiting for another actor to do something. Return true if so, nil if not. If we've been waiting for another actor, and the actor has finished the task we've been waiting for since the last time we checked, we'll clean up our internal state relating to the wait and return nil.


### `conjugateRegularVerb(verb)` *(overridden)*

Defined in en_us.t, line 2265

Conjugate a regular verb in the present or past tense for our person and number.


### `conversedThisTurn`

Defined in actor.t, line 6845

Did we engage in any conversation on the current turn? This can be used as a quick check in background activity scripts when we want to run a step only in the absence of any conversation on the same turn.


### `copyPronounAntecedentsFrom(issuer)`

Defined in actor.t, line 10034

Copy pronoun antecedents from the given actor. This should be called whenever an actor issues a command to us, so that pronouns in the command are properly resolved relative to the issuer.


### `defaultAskForResponse(byActor, obj)`

Defined in actor.t, line 10390

the default response for ASK FOR


### `defaultAskResponse(fromActor, topic)`

Defined in actor.t, line 10362

Show the default answer to a question - this is called when we're the actor in ASK <actor> ABOUT <topic>, and we can't find a more specific response for the given topic.


### `defaultCommandResponse(fromActor, topic)`

Defined in actor.t, line 10402

default refusal of a command


### `defaultConvResponse(actor, topic, convType)`

Defined in actor.t, line 10307

Show a default response to a conversational action. By default, we'll show the default response for our conversation type.


### `defaultGiveResponse(byActor, topic)`

Defined in actor.t, line 10386

the default response for GIVE TO


### `defaultGoodbyeResponse(actor)`

Defined in actor.t, line 10336

show our default goodbye message


### `defaultGreetingResponse(actor)`

Defined in actor.t, line 10332

Show our default greeting message - this is used when the given another actor greets us with HELLO or TALK TO, and we don't otherwise handle it (such as via a topic database entry).


### `defaultNoResponse(fromActor)`

Defined in actor.t, line 10398

default response to being told NO


### `defaultShowResponse(byActor, topic)`

Defined in actor.t, line 10382

the default response for SHOW TO


### `defaultTellResponse(fromActor, topic)`

Defined in actor.t, line 10378

Show the default response to being told of a topic - this is called when we're the actor in TELL <actor> ABOUT <topic>, and we can't find a more specific response for the topic.


### `defaultYesResponse(fromActor)`

Defined in actor.t, line 10394

default response to being told YES


### `descViaActorContainer(prop, contToIgnore)`

Defined in actor.t, line 6171

Describe the actor via the "nominal actor container." The nominal container is determined by our direct location.


### `disembark`

Defined in actor.t, line 7387

Disembark. This is used by the 'Get out' action to carry out the command. By default, we'll let the room handle it.


### `distantSpecialDesc`

Defined in actor.t, line 6051


### `dobjFor(AskAbout)` *(overridden)*

Defined in actor.t, line 10230

also mark the visible contents of the object as having been seen


### `dobjFor(AskFor)` *(overridden)*

Defined in actor.t, line 10123

cannot kiss oneself


### `dobjFor(Drop)` *(overridden)*

Defined in actor.t, line 10073


### `dobjFor(Kiss)` *(overridden)*

Defined in actor.t, line 10112

do the normal work


### `dobjFor(PutIn)` *(overridden)*

Defined in actor.t, line 10092

treat PUT SELF IN FOO as GET IN FOO


### `dobjFor(PutOn)` *(overridden)*

Defined in actor.t, line 10074


### `dobjFor(PutUnder)` *(overridden)*

Defined in actor.t, line 10075


### `dobjFor(Take)` *(overridden)*

Defined in actor.t, line 10072

For the basic physical manipulation verbs (TAKE, DROP, PUT ON, etc), it's illogical to operate on myself, so check for this in verify(). Otherwise, handle these as we would ordinary objects, since we might be able to manipulate other actors in the normal manner, especially actors small enough that we can pick them up.


### `dobjFor(TalkTo)` *(overridden)*

Defined in actor.t, line 10141

let the state object handle it


### `dobjFor(TellAbout)` *(overridden)*

Defined in actor.t, line 10248

let our state object handle it


### `dobjFor(Throw)` *(overridden)*

Defined in actor.t, line 10076


### `dobjFor(ThrowAt)` *(overridden)*

Defined in actor.t, line 10077


### `dobjFor(ThrowDir)` *(overridden)*

Defined in actor.t, line 10078


### `dobjFor(ThrowTo)` *(overridden)*

Defined in actor.t, line 10079


### `endConversation`

Defined in actor.t, line 5897

Break off our current conversation, of the NPC's own volition. This is the opposite number of initiateConversation: this causes the NPC to effectively say BYE on its own, rather than waiting for the PC to decide to end the conversation.


### `examineListContents` *(overridden)*

Defined in actor.t, line 6037

examine my contents specially


### `examineStatus` *(overridden)*

Defined in actor.t, line 5978

show our status


### `excludeFromLookAround(obj)`

Defined in actor.t, line 7457

Add an object to the 'look around' exclusion list. Returns true if the object was already in the list, nil if not.


### `executeActorTurn`

Defined in actor.t, line 9297

The main processing for an actor's turn. In most cases, subclasses should override this method (rather than executeTurn) to specialize an actor's turn processing.


### `executeAgenda`

Defined in actor.t, line 6965

Execute the next item in our agenda, if there are any items in the agenda that are ready to execute. We'll return true if we found an item to execute, nil if not.


### `executeTurn` *(overridden)*

Defined in actor.t, line 9268

Execute one "turn" - this is a unit of time passing. The player character generally is allowed to execute one command in the course of a turn; a non-player character with a programmed task can perform an increment of the task.


### `findVisualObstructor(obj)`

Defined in actor.t, line 8725

Find the object that prevents us from seeing the given object.


### `forEachTravelingActor(func)` *(overridden)*

Defined in actor.t, line 6424

invoke a callback on each actor traveling with the traveler


### `forgetPossAnaphors`

Defined in actor.t, line 10022

forget the possessive anaphors


### `getActionMessageObj`

Defined in actor.t, line 9835

Get the library message object for action responses. This is used to generate library responses to verbs.


### `getActorNotifyList`

Defined in actor.t, line 8470

Build a list of the objects that are explicitly registered to receive notification when I'm the actor in a command.


### `getBulkHeld`

Defined in actor.t, line 7030

Calculate the amount of bulk I'm holding directly. By default, we'll simply add up the "actor-encumbering bulk" of each of our direct contents.


### `getCurrentInterlocutor`

Defined in actor.t, line 6765

Get the current interlocutor. By default, we'll address new conversational commands (ASK ABOUT, TELL ABOUT, SHOW TO) to the last conversational partner, if that actor is still within range.


### `getDefaultInterlocutor`

Defined in actor.t, line 6784

Get the default interlocutor. If there's a current interlocutor, and we can still talk to that actor, then that's the default interlocutor. If not, we'll return whatever actor is the default for a TALK TO command. Note that TALK TO won't necessarily have a default actor; if it doesn't, we'll simply return nil.


### `getDropDestination(objToDrop, path)` *(overridden)*

Defined in actor.t, line 7490

Get the location into which objects should be moved when the actor drops them with an explicit 'drop' command. By default, we return the drop destination of our current container.


### `getFollowables`

Defined in actor.t, line 7823

Get the list of objects I can follow. This is a list of all of the objects which I have seen departing a location - these are all in scope for 'follow' commands.


### `getFollowInfo(obj)`

Defined in actor.t, line 7918

Get information on what to do to make this actor follow the given object. This returns a FollowInfo object that reports our last knowledge of the given object's location and departure, or nil if we don't know anything about how to follow the actor.


### `getLookAroundName`

Defined in actor.t, line 7432

Get my "look around" location name as a string. This returns a string containing the location name that we display in the status line or at the start of a "look around" description of my location.


### `getParserDeferredMessageObj`

Defined in actor.t, line 9829

Get the deferred library message object for a parser message addressed to the player character. We only use this to generate messages deferred from non-player characters.


### `getParserMessageObj`

Defined in actor.t, line 9807

get the library message object for a parser message addressed to the player character


### `getPossAnaphor(typ)`

Defined in actor.t, line 10019

get a possessive anaphor value


### `getPronounAntecedent(typ)`

Defined in actor.t, line 9995

look up a pronoun's value


### `getPushTraveler(obj)`

Defined in actor.t, line 6401

Get the "push traveler" for the actor. This is the nominal traveler that we want to use when the actor enters a command like PUSH BOX NORTH. 'obj' is the object we're trying to push.


### `getTopicOwner` *(overridden)*

Defined in actor.t, line 8261

we are the owner of any TopicEntry objects contained within us


### `getTraveler(conn)`

Defined in actor.t, line 6381

Get the object that's actually going to move when this actor travels via the given connector. In most cases this is simply the actor; but when the actor is in a vehicle, travel commands move the vehicle, not the actor: the actor stays in the vehicle while the vehicle moves to a new location. We determine this by asking our immediate location what it thinks about the situation.


### `getVisualAmbient`

Defined in actor.t, line 8505

Get the ambient light level in the visual senses at this actor. This is the ambient level at the actor.


### `getWeightHeld`

Defined in actor.t, line 7056

Calculate the total weight I'm holding. By default, we'll add up the "actor-encumbering weight" of each of our direct contents.


### `goToSleep`

Defined in actor.t, line 7310

Go to sleep. This is used by the 'Sleep' action to carry out the command. By default, we simply say that we're not sleepy; actors can override this to cause other actions.


### `handleConversation(actor, topic, convType)`

Defined in actor.t, line 10293

Handle a conversational command. All of the conversational actions (HELLO, GOODBYE, YES, NO, ASK ABOUT, ASK FOR, TELL ABOUT, SHOW TO, GIVE TO) are routed here when we're the target of the action (for example, we're BOB in ASK BOB ABOUT TOPIC) AND the ActorState doesn't want to handle the action.


### `hasSeen(obj)`

Defined in actor.t, line 8161

determine if I've ever seen the given object


### `hideFromAll(action)` *(overridden)*

Defined in actor.t, line 5922

Hide actors from 'all' by default. The kinds of actions that normally apply to 'all' and the kinds that normally apply to actors have pretty low overlap.


### `hideFromDefault(action)` *(overridden)*

Defined in actor.t, line 5929

don't hide actors from defaulting, though - it's frequently convenient and appropriate to assume an actor by default, especially for commands like GIVE TO and SHOW TO


### `idleTurn`

Defined in actor.t, line 9168

When it's our turn and we don't have any command to perform, we'll call this routine, which can perform a scripted operation if desired.


### `impliedCommandMode`

Defined in actor.t, line 6273

Implicit command handling style for this actor. There are two styles for handling implied commands: "player" and "NPC", indicated by the enum codes ModePlayer and ModeNPC, respectively.


### `initializeActor`

Defined in actor.t, line 8932

Perform library pre-initialization on the actor


### `initiateConversation(state, node)`

Defined in actor.t, line 5818

Initiate a conversation with the player character. This lets the NPC initiate a conversation, in response to something the player character does, or as part of the NPC's scripted activity. This is only be used for situations where the NPC initiates the conversation - if the player character initiates conversation with TALK TO, ASK, TELL, etc., we handle the conversation through our normal handlers for those commands.


### `initiateTopic(obj)` *(overridden)*

Defined in actor.t, line 5853

Initiate a conversation based on the given simulation object. We'll look for an InitiateTopic matching the given object, and if we can find one, we'll show its topic response.


### `inventorySense(sense, lister)`

Defined in actor.t, line 8890

Add to an inventory description a list of things we notice through a specific sense.


### `inventorySenseInfoTable`

Defined in actor.t, line 8789

Build a lookup table of the objects that can be sensed for the purposes of taking inventory. We'll include everything in the normal visual sense table, plus everything directly held.


### `iobjFor(GiveTo)` *(overridden)*

Defined in actor.t, line 10159

handle it as a 'hello' topic


### `iobjFor(ShowTo)` *(overridden)*

Defined in actor.t, line 10183

let the state object handle it


### `iobjFor(ThrowTo)` *(overridden)*

Defined in actor.t, line 10082

customize the message for THROW TO <actor>


### `isActorTraveling(actor)` *(overridden)*

Defined in actor.t, line 6417

is an actor traveling with us?


### `isLikelyTopic(obj)`

Defined in actor.t, line 8254

Determine if the given object is a likely topic for a conversational action performed by this actor. By default, we'll return true if the topic is known, nil if not.


### `isLocationLit`

Defined in actor.t, line 8532

Determine if my location is lit for my sight-like senses.


### `isPlayerChar`

Defined in actor.t, line 6241

determine if I'm the player character


### `knowsAbout(obj)`

Defined in actor.t, line 8195

Determine if I know about the given object. I know about an object if it's specifically marked as known to me; I also know about the object if I can see it now, or if I've ever seen it in the past.


### `knowsTopic(obj)`

Defined in actor.t, line 8243

Determine if the actor recognizes the given object as a "topic," which is an object that represents some knowledge the actor can use in conversations, consultations, and the like.


### `listActorPosture(povActor)`

Defined in actor.t, line 7356

Describe the actor as part of the EXAMINE description of a nested room containing the actor. 'povActor' is the actor doing the looking.


### `lookAround(verbose)` *(overridden)*

Defined in actor.t, line 7413

Display a description of the actor's location from the actor's point of view.


### `makePosture(newPosture)`

Defined in actor.t, line 7398

Set our posture to the given status. By default, we'll simply set our posture property to the new status, but actors can override this to handle side effects of the change.


### `meetsObjHeld(actor)` *(overridden)*

Defined in actor.t, line 5936

We meet the objHeld precondition for ourself - that is, for any verb that requires holding an object, we can be considered to be holding ourself.


### `mustMoveObjInto(obj)` *(overridden)*

Defined in actor.t, line 6306

desribe our containment of an object as carrying the object


### `nonIdleTurn`

Defined in actor.t, line 9224

Receive notification that this is a non-idle turn. This is called whenever a command in our pending command queue is about to be executed.


### `noteConditionsAfter`

Defined in actor.t, line 8972

Note conditions after an action or other event. By default, if we are still in the same location we were in when noteConditionsBefore() was last called, and the light/dark status has changed, we'll mention the change in light/dark status.


### `noteConditionsBefore`

Defined in actor.t, line 8959

Note conditions before an action or other event. By default, we note our location and light/dark status, so that we comment on any change in the light/dark status after the event if we're still in the same location.


### `noteConsultation(obj)`

Defined in actor.t, line 6902

note that we're consulting an item


### `noteConvAction(other)`

Defined in actor.t, line 6883

Note that we're taking part in a conversational action with another character. This is symmetrical - it could mean we're the initiator of the conversation action or the target. We'll remember the person we're talking to, and reset our conversation time counters so we know we've conversed on this turn.


### `noteConversation(other)`

Defined in actor.t, line 6855

Note that we're performing a conversational command targeting the given actor. We'll make the actors point at each other with their 'lastInterlocutor' properties. This is called on the character performing the conversation command: if the player types ASK BOB ABOUT BOOK, this will be called on the player character actor, with 'other' set to Bob.


### `noteConversationFrom(other)`

Defined in actor.t, line 6870

Note that another actor is issuing a conversational command targeting us. For example, if the player types ASK BOB ABOUT BOOK, then this will be called on Bob, with the player character actor as 'other'.


### `noteObjectShown(obj)`

Defined in actor.t, line 10215

Note that the given object has been explicitly shown to me. By default, we'll mark the object and its visible contents as having been seen by me. This is called whenever we're the target of a SHOW TO or GIVE TO, since presumably such an explicit act of calling our attention to an object would make us consider the object as having been seen in the future.


### `noteSeenBy(actor, prop)` *(overridden)*

Defined in actor.t, line 8167

receive notification that another actor is observing us


### `notifyIssuerParseFailure(targetActor, messageProp, args)`

Defined in actor.t, line 9943

Receive notification that a command we sent to another NPC failed. This is only called when one NPC sends a command to another NPC; this is called on the issuer to let the issuer know that the target can't perform the command because of the given resolution failure.


### `notifyParseFailure(issuingActor, messageProp, args)`

Defined in actor.t, line 9853

Notify an issuer that a command sent to us resulted in a parsing failure. We are meant to reply to the issuer to let the issuer know about the problem. messageProp is the libGlobal message property describing the error, and args is a list with the (varargs) arguments to the message property.


### `notifyTopicResponse(fromActor, entry)`

Defined in actor.t, line 6908

Receive notification that a TopicEntry response in our database is being invoked. We'll just pass this along to our current state.


### `npcDesc`

Defined in actor.t, line 6034

Show the description of this actor when this actor is a non-player character.


### `obeyCommand(issuingActor, action)`

Defined in actor.t, line 9645

Determine whether or not we want to obey a command from the given actor to perform the given action. We only get this far when we determine that it's possible for us to accept a command, given the sense connections between us and the issuing actor, and given our pending command queue.


### `okayPostureChange`

Defined in actor.t, line 7333

Get a default acknowledgment of a change to our posture. This should acknowledge the posture so that it tells us the current posture. This is used for a command such as "stand up" from a chair, so that we can report the appropriate posture status in our acknowledgment; we might end up being inside another nested container after standing up from the chair, so we might not simply be standing when we're done.


### `orderingTime(targetActor)`

Defined in actor.t, line 7733

The amount of time, in game clock units, it takes me to issue an order to another actor. By default, it takes one unit (which is usually equal to one turn) to issue a command to another actor. However, if we are configured to wait for our issued commands to complete in full, the ordering time is zero; we don't need any extra wait time in this case because we'll wait the full length of the issued command to begin with.


### `pcDesc`

Defined in actor.t, line 6011

The default description when we examine this actor and the actor is serving as the player character. This should generally not include any temporary status information; just show constant, fixed features.


### `postureDesc`

Defined in actor.t, line 6003

Show my posture, as part of the full EXAMINE description of this actor. We'll let our nominal actor container handle it.


### `readyForTurn`

Defined in actor.t, line 9049

Determine if we're ready to do something on our turn. We're ready to do something if we're not waiting for another actor to finish doing something and either we're the player character or we already have a pending command in our command queue.


### `referralPerson`

Defined in actor.t, line 6220

refer to the player character with my player character referral person, and refer to all other characters in the third person


### `rememberLastDoor(obj)`

Defined in actor.t, line 6653

Remember the last door I traveled through. We use this information for disambiguation, to boost the likelihood that an actor that just traveled through a door is referring to the same door in a subsequent "close" command.


### `rememberTravel(origin, dest, backConnector)`

Defined in actor.t, line 6661

Remember our most recent travel. If we know the back connector (i.e., the connector that reverses the travel we're performing), then we'll be able to accept a GO BACK command to attempt to return to the previous location.


### `remoteSpecialDesc(actor)` *(overridden)*

Defined in actor.t, line 6052


### `removeActorNotifyItem(obj)`

Defined in actor.t, line 8493

remove an item from the registered notification list


### `removeFromAgenda(item)`

Defined in actor.t, line 6953

remove an agenda item


### `reverseLastTravel`

Defined in actor.t, line 6675

Reverse the most recent travel. If we're still within the same destination we reached in the last travel, and we know the connector we arrived through (i.e., the "back connector" for the last travel, which reverses the connector we took to get here), then try traveling via the connector.


### `sayArriving(conn)` *(overridden)*

Defined in actor.t, line 6729

Travel arrival/departure messages. Defer to the current state object on all of these.


### `sayArrivingDir(dir, conn)` *(overridden)*

Defined in actor.t, line 6739


### `sayArrivingDownStairs(conn)` *(overridden)*

Defined in actor.t, line 6753


### `sayArrivingLocally(dest, conn)` *(overridden)*

Defined in actor.t, line 6733


### `sayArrivingThroughPassage(conn)` *(overridden)*

Defined in actor.t, line 6743


### `sayArrivingUpStairs(conn)` *(overridden)*

Defined in actor.t, line 6751


### `sayArrivingViaPath(conn)` *(overridden)*

Defined in actor.t, line 6747


### `sayDeparting(conn)` *(overridden)*

Defined in actor.t, line 6731


### `sayDepartingDir(dir, conn)` *(overridden)*

Defined in actor.t, line 6741


### `sayDepartingDownStairs(conn)` *(overridden)*

Defined in actor.t, line 6757


### `sayDepartingLocally(dest, conn)` *(overridden)*

Defined in actor.t, line 6735


### `sayDepartingThroughPassage(conn)` *(overridden)*

Defined in actor.t, line 6745


### `sayDepartingUpStairs(conn)` *(overridden)*

Defined in actor.t, line 6755


### `sayDepartingViaPath(conn)` *(overridden)*

Defined in actor.t, line 6749


### `sayGoodbye(actor)`

Defined in actor.t, line 9661


### `sayHello(actor)`

Defined in actor.t, line 9660

Say hello/goodbye/yes/no to the given actor. We'll greet the target actor is the target actor was specified (i.e., actor != self); otherwise, we'll greet our current default conversational partner, if we have one.


### `sayNo(actor)`

Defined in actor.t, line 9663


### `saySpecialTopic`

Defined in actor.t, line 9715

Handle the XSPCLTOPIC pseudo-command. This command is generated by the SpecialTopic pre-parser when it recognizes the player's input as matching an active SpecialTopic's custom syntax. Our job is to route this back to our current interlocutor's active ConvNode, so that it can find the SpecialTopic that it matched in pre-parsing and show its response.


### `sayToActor(actor, topic, convType)`

Defined in actor.t, line 9666

handle one of the conversational addresses


### `sayTravelingRemotely(dest, conn)` *(overridden)*

Defined in actor.t, line 6737


### `sayYes(actor)`

Defined in actor.t, line 9662


### `scheduleInitiateConversation(state, node, turns)`

Defined in actor.t, line 5881

Schedule initiation of conversation. This allows the caller to set up a conversation to start on a future turn. The conversation will start after (1) the given number of turns has elapsed, and (2) the player didn't target this actor with a conversational command on the same turn. This allows us to set the NPC so that it *wants* to start a conversation, and will do so as soon as it has a chance to get a word in.


### `scopeList`

Defined in actor.t, line 8594

Build a list of all of the objects of which an actor is aware.


### `scriptedTravelTo(dest)`

Defined in actor.t, line 6635

Perform scripted travel to the given adjacent location. This looks for a directional connector in our current location whose destination is the given location, and for a corresponding back-connector in the destination location. If we can find the connectors, we'll perform the travel using travelTo().


### `setConvNode(node)`

Defined in actor.t, line 5729

set the current conversation node


### `setConvNodeReason(node, reason)`

Defined in actor.t, line 5732

set the current conversation node, with a reason code


### `setCurState(state)`

Defined in actor.t, line 5693

set the current state


### `setHasSeen(obj)`

Defined in actor.t, line 8164

mark the object to remember that I've seen it


### `setHer(obj)`

Defined in actor.t, line 9983

set the antecedent for the feminine singular ("her")


### `setHim(obj)`

Defined in actor.t, line 9977

set the antecedent for the masculine singular ("him")


### `setIt(obj)`

Defined in actor.t, line 9971

set the antecedent for the neuter singular pronoun ("it" in English)


### `setKnowsAbout(obj)`

Defined in actor.t, line 8198

mark the object as known to me


### `setPossAnaphor(typ, val)`

Defined in actor.t, line 10012

set a possessive anaphor value


### `setPossAnaphorObj(obj)`

Defined in en_us.t, line 2577

set a possessive anaphor


### `setPronoun(lst)`

Defined in en_us.t, line 2410

Set a pronoun antecedent to the given list of ResolveInfo objects. Pronoun handling is language-specific, so this implementation is part of the English library, not the generic library.


### `setPronounAntecedent(typ, val)`

Defined in actor.t, line 10002

set a pronoun's antecedent value


### `setPronounByType(typ, lst)`

Defined in en_us.t, line 2516

Set a pronoun antecedent to the given ResolveInfo list, for the specified type of pronoun. We don't have to worry about setting other types of pronouns to this antecedent - we specifically want to set the given pronoun type. This is language-dependent because we still have to figure out the number (i.e. singular or plural) of the pronoun type.


### `setPronounMulti([args])`

Defined in en_us.t, line 2463

Set a pronoun to refer to multiple potential antecedents. This is used when the verb has multiple noun slots - UNLOCK DOOR WITH KEY. For verbs like this, we have no way of knowing in advance whether a future pronoun will refer back to the direct object or the indirect object (etc) - we could just assume that 'it' will refer to the direct object, but this won't always be what the player intended. In natural English, pronoun antecedents must often be inferred from context at the time of use - so we use the same approach.


### `setPronounObj(obj)`

Defined in en_us.t, line 2535

Set a pronoun antecedent to the given simulation object (usually an object descended from Thing).


### `setSpecialTraveler(traveler)`

Defined in actor.t, line 6447

Set the "special traveler." When this is set, we explicitly perform travel through this object rather than through the traveler indicated by our location. Returns the old value, so that the old value can be restored when the caller has finished its need for the special traveler.


### `setThem(lst)`

Defined in actor.t, line 9989

set the antecedent list for the ungendered plural pronoun ("them")


### `showInventory(tall)`

Defined in actor.t, line 8851

Show what the actor is carrying.


### `showInventoryWith(tall, inventoryLister)`

Defined in actor.t, line 8867

Show what the actor is carrying, using the given listers.


### `showSpecialDescInContents(actor, cont)` *(overridden)*

Defined in actor.t, line 6071

When we're asked to show a special description as part of the description of a containing object (which will usually be a nested room of some kind), just show our posture in our container, rather than showing our full "I am here" description.


### `specialDesc`

Defined in actor.t, line 6050

Always list actors specially, rather than as ordinary items in contents listings. We'll send this to our current state object for processing, since our "I am here" description tends to vary by state.


### `specialDescListWith`

Defined in actor.t, line 6053


### `standUp`

Defined in actor.t, line 7370

Stand up. This is used by the 'Stand' action to carry out the command.


### `suggestTopics(explicit)`

Defined in actor.t, line 8309

Suggest topics of conversation. This is called by the TOPICS command (in which case 'explicit' is true), and whenever we first engage a character in a stateful conversation (in which case 'explicit' is nil).


### `suggestTopicsFor(actor, explicit)`

Defined in actor.t, line 8339

Suggest topics that the given actor might want to talk to us about. The given actor is almost always the player character, since generally NPC's don't talk to one another using conversation commands (there'd be no point; they're simple programmed automata, not full-blown AI's).


### `trackFollowInfo(obj, conn, from)`

Defined in actor.t, line 7879

Receive notification that an object is leaving its current location as a result of the action we're currently processing. Actors (and possibly other objects) will broadcast this notification to all Actor objects connected in any way by containment when they move under their own power (such as with Actor.travelTo) to a new location. We'll keep tracking information if we are configured to keep tracking information for the given object and we can see the given object. Note that this is called when the object is still at the source end of the travel - the important thing is that we see the object departing.


### `travelerName(arriving)`

Defined in en_us.t, line 2373

Show my name for an arrival/departure message. If we've been seen before by the player character, we'll show our definite name, otherwise our indefinite name.


### `travelerPreCond(conn)` *(overridden)*

Defined in actor.t, line 6365

Get the preconditions for travel. By default, we'll add the standard preconditions that the connector requires for actors.


### `travelerTravelWithin(actor, dest)` *(overridden)*

Defined in actor.t, line 6517

Traveler interface: perform local travel, between nested rooms within a single top-level location.


### `travelTo(dest, connector, backConnector)`

Defined in actor.t, line 6603

Travel to a new location.


### `travelWithin(dest)`

Defined in actor.t, line 6500

Travel within a location, as from a room to a contained nested room. This should generally be used in lieu of travelTo when traveling between locations that are related directly by containment rather than with TravelConnector objects.


### `tryMakingRoomToHold(obj, allowImplicit)`

Defined in actor.t, line 7086

Try making room to hold the given object. This is called when checking the "room to hold object" pre-condition, such as for the "take" verb.


### `tryMovingObjInto(obj)` *(overridden)*

Defined in actor.t, line 6283

Try moving the given object into this object. For an actor, this will do one of two things. If 'self' is the actor performing the action that's triggering this implied command, then we can achieve the goal simply by taking the object. Otherwise, the way to get an object into my possession is to have the actor performing the command give me the object.


### `unexcludeFromLookAround(obj)`

Defined in actor.t, line 7472

remove an object from the 'look around' exclusion list


### `verifyFollowable` *(overridden)*

Defined in actor.t, line 7926

By default, all actors are followable.


### `verifyNotSelf(msg)`

Defined in actor.t, line 10050

verify() handler to check against applying an action to 'self'


### `visibleInfoTable`

Defined in actor.t, line 8750

Build a table of full sensory information for all of the objects visible to the actor through the actor's sight-like senses. Returns a lookup table with the same set of information as senseInfoTable().


### `visibleInfoTableFromPov(pov)`

Defined in actor.t, line 8761

Build a table of full sensory information for all of the objects visible to me from a particular point of view through my sight-like senses.


### `waitForIssuedCommand(targetActor)`

Defined in actor.t, line 7747

Wait for completion of a command that we issued to another actor. The parser calls this routine after each time we issue a command to another actor.


### `wantsFollowInfo(obj)`

Defined in actor.t, line 7839

Do I track departing objects for following the given object?


## Inherited Methods


<details><summary>From [Thing](thing.md) (399)</summary>

[`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotGoShowExits`](thing.md#cannotGoShowExits), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkActorOutOfNested`](thing.md#checkActorOutOfNested), [`checkBulkChange`](thing.md#checkBulkChange), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`checkTravelerDirectlyInRoom`](thing.md#checkTravelerDirectlyInRoom), [`childInName`](thing.md#childInName), [`childInNameGen`](thing.md#childInNameGen), [`childInNameWithOwner`](thing.md#childInNameWithOwner), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`contentsInFixedIn`](thing.md#contentsInFixedIn), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Board)`](thing.md#dobjFor(Board)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(Enter)`](thing.md#dobjFor(Enter)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Examine)`](thing.md#dobjFor(Examine)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GetOutOf)`](thing.md#dobjFor(GetOutOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(LieOn)`](thing.md#dobjFor(LieOn)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(ListenTo)`](thing.md#dobjFor(ListenTo)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookBehind)`](thing.md#dobjFor(LookBehind)), [`dobjFor(LookIn)`](thing.md#dobjFor(LookIn)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(LookUnder)`](thing.md#dobjFor(LookUnder)), [`dobjFor(Move)`](thing.md#dobjFor(Move)), [`dobjFor(MoveTo)`](thing.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](thing.md#dobjFor(MoveWith)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Pull)`](thing.md#dobjFor(Pull)), [`dobjFor(Push)`](thing.md#dobjFor(Push)), [`dobjFor(PushTravel)`](thing.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](thing.md#dobjFor(PutBehind)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(ShowTo)`](thing.md#dobjFor(ShowTo)), [`dobjFor(SitOn)`](thing.md#dobjFor(SitOn)), [`dobjFor(Smell)`](thing.md#dobjFor(Smell)), [`dobjFor(StandOn)`](thing.md#dobjFor(StandOn)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(TakeFrom)`](thing.md#dobjFor(TakeFrom)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContentsWith`](thing.md#examineListContentsWith), [`examineSpecialContents`](thing.md#examineSpecialContents), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDestName`](thing.md#getDestName), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getExtraScopeItems`](thing.md#getExtraScopeItems), [`getHitFallDestination`](thing.md#getHitFallDestination), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalDropDestination`](thing.md#getNominalDropDestination), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomNotifyList`](thing.md#getRoomNotifyList), [`getRoomPartLocation`](thing.md#getRoomPartLocation), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getStatuslineExitsHeight`](thing.md#getStatuslineExitsHeight), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`initializeThing`](thing.md#initializeThing), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutOn)`](thing.md#iobjFor(PutOn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowAt)`](thing.md#iobjFor(ThrowAt)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isActorTravelReady`](thing.md#isActorTravelReady), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isHeldBy`](thing.md#isHeldBy), [`isIn`](thing.md#isIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isOwnedBy`](thing.md#isOwnedBy), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomActorThereDesc`](thing.md#roomActorThereDesc), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDaemon`](thing.md#roomDaemon), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomDesc`](thing.md#roomDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`roomTravelPreCond`](thing.md#roomTravelPreCond), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showStatuslineExits`](thing.md#showStatuslineExits), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyInsert`](thing.md#verifyInsert), [`verifyMoveTo`](thing.md#verifyMoveTo), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)


*From [Schedulable](schedulable.md):* [`execute`](schedulable.md#execute), [`getNextRunTime`](schedulable.md#getNextRunTime), [`incNextRunTime`](schedulable.md#incNextRunTime)


*From [Traveler](traveler.md):* [`canTravelVia`](traveler.md#canTravelVia), [`checkDirectlyInRoom`](traveler.md#checkDirectlyInRoom), [`describeArrival`](traveler.md#describeArrival), [`describeDeparture`](traveler.md#describeDeparture), [`describeNpcArrival`](traveler.md#describeNpcArrival), [`describeNpcDeparture`](traveler.md#describeNpcDeparture), [`explainNoTravelVia`](traveler.md#explainNoTravelVia), [`getNotifyTable`](traveler.md#getNotifyTable), [`isTravelerCarrying`](traveler.md#isTravelerCarrying), [`travelerLocName`](traveler.md#travelerLocName), [`travelerRemoteLocName`](traveler.md#travelerRemoteLocName), [`travelerSeenBy`](traveler.md#travelerSeenBy), [`travelerTravelTo`](traveler.md#travelerTravelTo)


*From [TravelMessageHandler](travelmessagehandler.md):* [`getNominalTraveler`](travelmessagehandler.md#getNominalTraveler)


*From [ActorTopicDatabase](actortopicdatabase.md):* [`showTopicResponse`](actortopicdatabase.md#showTopicResponse)


*From [TopicDatabase](topicdatabase.md):* [`addSuggestedTopic`](topicdatabase.md#addSuggestedTopic), [`addTopic`](topicdatabase.md#addTopic), [`addTopicToList`](topicdatabase.md#addTopicToList), [`compareVocabMatch`](topicdatabase.md#compareVocabMatch), [`findTopicResponse`](topicdatabase.md#findTopicResponse), [`handleTopic`](topicdatabase.md#handleTopic), [`removeSuggestedTopic`](topicdatabase.md#removeSuggestedTopic), [`removeTopic`](topicdatabase.md#removeTopic), [`removeTopicFromList`](topicdatabase.md#removeTopicFromList), [`showSuggestedTopicList`](topicdatabase.md#showSuggestedTopicList)
