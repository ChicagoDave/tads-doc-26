# TravelConnector

*class* — defined in [travel.t](../by-file/travel.t.md) (line 775)


A Travel Connector is a special connection interface that allows for travel from one location to another. Most actor movement, except for movement between locations related by containment (such as from a room to sitting in a chair within the room) are handled through travel connector objects.


**Superclass chain:** [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > **TravelConnector**


<details><summary>Subclasses (26)</summary>

- [AskConnector](askconnector.md)
- [DefaultAskConnector](defaultaskconnector.md)
- [Passage](passage.md)
- [Stairway](stairway.md)
- [StairwayDown](stairwaydown.md)
- [StairwayUp](stairwayup.md)
- [ThroughPassage](throughpassage.md)
- [BasicDoor](basicdoor.md)
- [Door](door.md)
- [AutoClosingDoor](autoclosingdoor.md)
- [SecretDoor](secretdoor.md)
- [HiddenDoor](hiddendoor.md)
- [ExitOnlyPassage](exitonlypassage.md)
- [PathPassage](pathpassage.md)
- [RoomConnector](roomconnector.md)
- [OneWayRoomConnector](onewayroomconnector.md)
- [RoomAutoConnector](roomautoconnector.md)
- [Room](room.md)
- [DarkRoom](darkroom.md)
- [FloorlessRoom](floorlessroom.md)
- [OutdoorRoom](outdoorroom.md)
- [ShipboardRoom](shipboardroom.md)
- [TravelMessage](travelmessage.md)
- [DeadEndConnector](deadendconnector.md)
- [NoTravelMessage](notravelmessage.md)
- [FakeConnector](fakeconnector.md)

</details>


**Global objects:** [noTravel](notravel.md)


## Properties


### `connectorStagingLocation`

Defined in travel.t, line 815

The "staging location" for travel through this connector. By default, if we have a location, that's our staging location; if we don't have a location (in which case we probably an outermost room), we don't have a staging location.


### `isCircularPassage`

Defined in travel.t, line 1218

Is this a "circular" passage? A circular passage is one that explicitly connects back to its origin, so that traveling through the connector leaves us where we started. When a passage is marked as circular, we'll describe travel through the passage exactly as though we had actually gone somewhere. By default, if traveling through a passage leaves us where we started, we assume that nothing happened, so we don't describe any travel.


### `isConnectorListed`

Defined in travel.t, line 963

Is this connector listed? This indicates whether or not the exit is allowed to be displayed in lists of exits, such as in the status line or in "you can't go that way" messages. By default, all exits are allowed to appear in listings.


### `rememberCircularPassage`

Defined in travel.t, line 1227

Should we remember a circular trip through this passage? By default, we remember the destination of a passage that takes us back to our origin only if we're explicitly marked as a circular passage; in other cases, we assume that the travel was blocked somehow instead.


### `travelBarrier`

Defined in travel.t, line 852

Barrier or barriers to travel. This property can be set to a single TravelBarrier object or to a list of TravelBarrier objects. checkTravelBarriers() checks each barrier specified here.


### `travelMemory`

Defined in travel.t, line 1202

Our "travel memory" table. If this contains a non-nil lookup table object, we'll store a record of each successful traversal of a travel connector here - we'll record the destination keyed by the combination of actor, origin, and connector, so that we can later check to see if the actor has any memory of where a given connector goes from a given origin.


## Inherited Properties


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorInPrep`](thing.md#actorInPrep), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`actorOutOfPrep`](thing.md#actorOutOfPrep), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`brightness`](thing.md#brightness), [`bulk`](thing.md#bulk), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`canMatchHer`](thing.md#canMatchHer), [`canMatchHim`](thing.md#canMatchHim), [`canMatchIt`](thing.md#canMatchIt), [`canMatchThem`](thing.md#canMatchThem), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListed`](thing.md#contentsListed), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`contentsLister`](thing.md#contentsLister), [`descContentsLister`](thing.md#descContentsLister), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`effectiveFollowLocation`](thing.md#effectiveFollowLocation), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isLikelyCommandTarget`](thing.md#isLikelyCommandTarget), [`isListedAboardVehicle`](thing.md#isListedAboardVehicle), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`isTopLevel`](thing.md#isTopLevel), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`lookInLister`](thing.md#lookInLister), [`moved`](thing.md#moved), [`name`](thing.md#name), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`notTravelReadyMsg`](thing.md#notTravelReadyMsg), [`objectNotifyList`](thing.md#objectNotifyList), [`objInPrep`](thing.md#objInPrep), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`roomLocation`](thing.md#roomLocation), [`roomName`](thing.md#roomName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`sightSize`](thing.md#sightSize), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialContentsLister`](thing.md#specialContentsLister), [`specialDesc`](thing.md#specialDesc), [`specialDescBeforeContents`](thing.md#specialDescBeforeContents), [`specialDescListWith`](thing.md#specialDescListWith), [`specialDescOrder`](thing.md#specialDescOrder), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`takeFromNotInMessage`](thing.md#takeFromNotInMessage), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont), [`weight`](thing.md#weight)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `actorTravelPreCond(actor)`

Defined in travel.t, line 836

Get the travel preconditions that this connector requires for travel by the given actor. In most cases, this won't depend on the actor, but it's provided as a parameter anyway; in most cases, this will just apply the conditions that are relevant to actors as travelers.


### `canTravelerPass(traveler)`

Defined in travel.t, line 936

Check to see if the Traveler object is allowed to travel through this connector. Returns true if travel is allowed, nil if not.


### `checkTravelBarriers(dest)`

Defined in travel.t, line 858

Check barriers. The TravelVia check() routine must call this to enforce barriers.


### `connectorBack(traveler, dest)`

Defined in travel.t, line 1400

Find a connector in the destination location that connects back as the source of travel from the given connector when traversed from the source location. Returns nil if there is no such connector. This must be called while the traveler is still in the source location; we'll attempt to find the connector back to the traveler's current location.


### `connectorGetConnectorTo(origin, traveler, dest)`

Defined in travel.t, line 1145

Get the travel connector leading to the given destination from the given origin and for the given travel. Return nil if we don't know a connector leading there.


### `connectorTravelPreCond`

Defined in travel.t, line 780

Get any connector-specific pre-conditions for travel via this connector.


### `createUnlistedProxy`

Defined in travel.t, line 970

Get an unlisted proxy for this connector. This is normally called from the asExit() macro to set up one room exit direction as an unlisted synonym for another.


### `darkTravel(actor, dest)`

Defined in travel.t, line 1541

Handle travel in the dark. Specifically, this is called when an actor attempts travel from one dark location to another dark location. (We don't invoke this in any other case: light-to-light, light-to-dark, and dark-to-light travel are all allowed without any special checks.)


### `describeArrival(traveler, origin, dest)`

Defined in travel.t, line 1287

Describe an actor's arrival through the connector from the given origin into the given destination. This description is from the point of view of another actor in the destination.


### `describeDeparture(traveler, origin, dest)`

Defined in travel.t, line 1234

Describe an actor's departure through the connector from the given origin to the given destination. This description is from the point of view of another actor in the origin location.


### `describeLocalArrival(traveler, origin, dest)`

Defined in travel.t, line 1346

Describe a "local arrival" via this connector. This is called when the traveler moves around entirely within the field of view of the player character, and comes *closer* to the PC - that is, the traveler's origin is visible to the player character when we arrive in our destination, AND the destination's top-level location contains the PC. We'll describe the travel not in terms of truly arriving, since the traveler was already here to start with, but rather as entering the destination, but just in terms of moving closer.


### `describeLocalDeparture(traveler, origin, dest)`

Defined in travel.t, line 1329

Describe a "local departure" via this connector. This is called when a traveler moves around entirely within the field of view of the player character, and move *further away* from the PC - that is, the traveler's destination is visible to the PC when we're leaving our origin, AND the origin's top-level location contains the PC. We'll describe the travel not in terms of truly departing, but simply in terms of moving away.


### `describeRemoteTravel(traveler, origin, dest)`

Defined in travel.t, line 1360

Describe "remote travel" via this connector. This is called when the traveler moves around entirely within the field of view of the PC, but between two "remote" top-level locations - "remote" means "does not contain the PC." In this case, the traveler isn't arriving or departing, exactly; it's just moving laterally from one top-level location to another.


### `dobjFor(TravelVia)`

Defined in travel.t, line 1561

Action handler for the internal "TravelVia" action. This is not a real action, but is instead a pseudo-action that we implement generically for travel via the connector. Subclasses that want to handle real actions by traveling via the connector can use remapTo(TravelVia) to implement the real action handlers. Note that remapTo should be used (rather than, say, asDobjFor), since this will ensure that every type of travel through the connector actually looks like a TravelVia action, which is useful for intercepting travel actions generically in other code.


### `explainTravelBarrier(traveler)`

Defined in travel.t, line 948

Explain why canTravelerPass() returned nil. This is called to display an explanation of why travel is not allowed by self.canTravelerPass().


### `fixedSource(dest, traveler)`

Defined in travel.t, line 1488

Get the "fixed" source for travelers emerging from this connector, if possible. This can return nil if the connector does not have a fixed relationship with another connector.


### `getApparentDestination(origin, actor)`

Defined in travel.t, line 1063

Get the apparent destination of travel by the actor to the given origin. This returns the location to which the connector travels, AS FAR AS THE ACTOR KNOWS. If the actor does not know and cannot tell where the connector leads, this should return nil.


### `getDestination(origin, traveler)`

Defined in travel.t, line 1123

Get our destination, given the traveler and the origin location.


### `isConnectorApparent(origin, actor)`

Defined in travel.t, line 987

Determine if the travel connection is apparent - as a travel connector - to the actor in the given origin location. This doesn't indicate whether or not travel is possible, or where travel goes, or that the actor can tell where the passage goes; this merely indicates whether or not the actor should realize that the passage exists at all.


### `isConnectorPassable(origin, traveler)`

Defined in travel.t, line 1007

Determine if the travel connection is passable by the given traveler in the current state. For example, a door would return true when open, nil when closed.


### `isConnectorVisibleInDark(origin, actor)`

Defined in travel.t, line 1507

Can the given actor see this connector in the dark, looking from the given origin? Returns true if so, nil if not.


### `noteTraversal(traveler)`

Defined in travel.t, line 1160

Note that the connector is being traversed. This is invoked just before the traveler is moved; this notification is fired after the other travel-related notifications (beforeTravel, actorTravel, travelerLeaving). This is a good place to display any special messages describing what happens during the travel, because any messages displayed here will come after any messages related to reactions from other objects.


### `rememberTravel(origin, actor, dest)`

Defined in travel.t, line 1173

Service routine: add a memory of a successful traversal of a travel connector. If we have a travel memory table, we'll add the traversal to the table, so that we can find it later.


## Inherited Methods


<details><summary>From [Thing](thing.md) (444)</summary>

[`acceptCommand`](thing.md#acceptCommand), [`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToContents`](thing.md#addToContents), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustLookAroundTable`](thing.md#adjustLookAroundTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`afterAction`](thing.md#afterAction), [`afterTravel`](thing.md#afterTravel), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameObj`](thing.md#aNameObj), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`beforeAction`](thing.md#beforeAction), [`beforeTravel`](thing.md#beforeTravel), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canHear`](thing.md#canHear), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotGoShowExits`](thing.md#cannotGoShowExits), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canOwn`](thing.md#canOwn), [`canSee`](thing.md#canSee), [`canSmell`](thing.md#canSmell), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkActorOutOfNested`](thing.md#checkActorOutOfNested), [`checkBulkChange`](thing.md#checkBulkChange), [`checkBulkChangeWithin`](thing.md#checkBulkChangeWithin), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkStagingLocation`](thing.md#checkStagingLocation), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`checkTravelerDirectlyInRoom`](thing.md#checkTravelerDirectlyInRoom), [`childInName`](thing.md#childInName), [`childInNameGen`](thing.md#childInNameGen), [`childInNameWithOwner`](thing.md#childInNameWithOwner), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`conjugateRegularVerb`](thing.md#conjugateRegularVerb), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`contentsInFixedIn`](thing.md#contentsInFixedIn), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskAbout)`](thing.md#dobjFor(AskAbout)), [`dobjFor(AskFor)`](thing.md#dobjFor(AskFor)), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Board)`](thing.md#dobjFor(Board)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Drop)`](thing.md#dobjFor(Drop)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(Enter)`](thing.md#dobjFor(Enter)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Examine)`](thing.md#dobjFor(Examine)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GetOutOf)`](thing.md#dobjFor(GetOutOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(Kiss)`](thing.md#dobjFor(Kiss)), [`dobjFor(LieOn)`](thing.md#dobjFor(LieOn)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(ListenTo)`](thing.md#dobjFor(ListenTo)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookBehind)`](thing.md#dobjFor(LookBehind)), [`dobjFor(LookIn)`](thing.md#dobjFor(LookIn)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(LookUnder)`](thing.md#dobjFor(LookUnder)), [`dobjFor(Move)`](thing.md#dobjFor(Move)), [`dobjFor(MoveTo)`](thing.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](thing.md#dobjFor(MoveWith)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Pull)`](thing.md#dobjFor(Pull)), [`dobjFor(Push)`](thing.md#dobjFor(Push)), [`dobjFor(PushTravel)`](thing.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](thing.md#dobjFor(PutBehind)), [`dobjFor(PutIn)`](thing.md#dobjFor(PutIn)), [`dobjFor(PutOn)`](thing.md#dobjFor(PutOn)), [`dobjFor(PutUnder)`](thing.md#dobjFor(PutUnder)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(ShowTo)`](thing.md#dobjFor(ShowTo)), [`dobjFor(SitOn)`](thing.md#dobjFor(SitOn)), [`dobjFor(Smell)`](thing.md#dobjFor(Smell)), [`dobjFor(StandOn)`](thing.md#dobjFor(StandOn)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(Take)`](thing.md#dobjFor(Take)), [`dobjFor(TakeFrom)`](thing.md#dobjFor(TakeFrom)), [`dobjFor(TalkTo)`](thing.md#dobjFor(TalkTo)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellAbout)`](thing.md#dobjFor(TellAbout)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Throw)`](thing.md#dobjFor(Throw)), [`dobjFor(ThrowAt)`](thing.md#dobjFor(ThrowAt)), [`dobjFor(ThrowDir)`](thing.md#dobjFor(ThrowDir)), [`dobjFor(ThrowTo)`](thing.md#dobjFor(ThrowTo)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContents`](thing.md#examineListContents), [`examineListContentsWith`](thing.md#examineListContentsWith), [`examineSpecialContents`](thing.md#examineSpecialContents), [`examineStatus`](thing.md#examineStatus), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDestName`](thing.md#getDestName), [`getDropDestination`](thing.md#getDropDestination), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getExtraScopeItems`](thing.md#getExtraScopeItems), [`getHitFallDestination`](thing.md#getHitFallDestination), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalDropDestination`](thing.md#getNominalDropDestination), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomNotifyList`](thing.md#getRoomNotifyList), [`getRoomPartLocation`](thing.md#getRoomPartLocation), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getStatuslineExitsHeight`](thing.md#getStatuslineExitsHeight), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`hideFromAll`](thing.md#hideFromAll), [`hideFromDefault`](thing.md#hideFromDefault), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`initializeThing`](thing.md#initializeThing), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(GiveTo)`](thing.md#iobjFor(GiveTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutOn)`](thing.md#iobjFor(PutOn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(ShowTo)`](thing.md#iobjFor(ShowTo)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowAt)`](thing.md#iobjFor(ThrowAt)), [`iobjFor(ThrowTo)`](thing.md#iobjFor(ThrowTo)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isActorTravelReady`](thing.md#isActorTravelReady), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isHeldBy`](thing.md#isHeldBy), [`isIn`](thing.md#isIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isOwnedBy`](thing.md#isOwnedBy), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAround`](thing.md#lookAround), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`meetsObjHeld`](thing.md#meetsObjHeld), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`mustMoveObjInto`](thing.md#mustMoveObjInto), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`noteSeenBy`](thing.md#noteSeenBy), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`remoteSpecialDesc`](thing.md#remoteSpecialDesc), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomActorThereDesc`](thing.md#roomActorThereDesc), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDaemon`](thing.md#roomDaemon), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomDesc`](thing.md#roomDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`roomTravelPreCond`](thing.md#roomTravelPreCond), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContents`](thing.md#showSpecialDescInContents), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showStatuslineExits`](thing.md#showStatuslineExits), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`tryMovingObjInto`](thing.md#tryMovingObjInto), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyFollowable`](thing.md#verifyFollowable), [`verifyInsert`](thing.md#verifyInsert), [`verifyMoveTo`](thing.md#verifyMoveTo), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
