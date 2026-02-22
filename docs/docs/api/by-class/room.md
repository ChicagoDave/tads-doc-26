# Room

*class* — defined in [travel.t](../by-file/travel.t.md) (line 4313)


Room: the basic class for top-level game locations (that is, game locations that aren't inside any other simulation objects, but are at the top level of the containment hierarchy). This is the smallest unit of movement; we do not distinguish among locations within a room, even if a Room represents a physically large location. If it is necessary to distinguish among different locations in a large physical room, simply divide the physical room into sections and represent each section with a separate Room object.


**Superclass chain:** [Fixture](fixture.md) > [NonPortable](nonportable.md) > [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > [BasicLocation](basiclocation.md) > [RoomAutoConnector](roomautoconnector.md) > [RoomConnector](roomconnector.md) > [TravelConnector](travelconnector.md) > **RoomSubclasses:** [DarkRoom](darkroom.md), [FloorlessRoom](floorlessroom.md), [OutdoorRoom](outdoorroom.md), [ShipboardRoom](shipboardroom.md)


## Properties


### `atmosphereList`

Defined in travel.t, line 4395

My "atmosphere" list. This can be set to an EventList object to provide atmosphere messages while the player character is within this room. The default roomDaemon will show one message from this EventList (by calling the EventList's doScript() method) on each turn the player character is in this location.


### `brightness` *(overridden)*

Defined in travel.t, line 4362

Most rooms provide their own implicit lighting. We'll use 'medium' lighting (level 3) by default, which provides enough light for all activities, but is reduced to dim light (level 2) when it goes through obscuring media or over distance.


### `destName`

Defined in travel.t, line 4386

Our destination name, if we have one. By default, we make this nil, which means the room cannot be described as a destination of connectors from adjoining locations.


### `isTopLevel` *(overridden)*

Defined in travel.t, line 4334

we're a "top-level" location: we don't have any other object containing us, but we're nonetheless part of the game world, so we're at the top level of the containment tree


### `name` *(overridden)*

Defined in en_us.t, line 2960

The ordinary 'name' property is used the same way it's used for any other object, to refer to the room when it shows up in library messages and the like: "You can't take the hallway."


### `putDestMessage`

Defined in travel.t, line 4438

Since we could be our own nominal drop destination, we need a message to describe things being put here.


### `roomFloor`

Defined in travel.t, line 4533

Get the room's floor. This looks for an object of class Floor in the roomParts list; if there is no such object, we'll return nil, indicating that the room has no floor at all.


### `roomParts`

Defined in travel.t, line 4524

Get the list of extra parts for the room. An indoor location has walls, floor, and ceiling; these are all generic objects that are included for completeness only.


## Inherited Properties


*From [Fixture](fixture.md):* [`cannotMoveMsg`](fixture.md#cannotMoveMsg), [`cannotPutMsg`](fixture.md#cannotPutMsg), [`cannotTakeMsg`](fixture.md#cannotTakeMsg)


*From [NonPortable](nonportable.md):* [`bulk`](nonportable.md#bulk), [`contentsListed`](nonportable.md#contentsListed), [`isListed`](nonportable.md#isListed), [`isListedInContents`](nonportable.md#isListedInContents), [`isListedInInventory`](nonportable.md#isListedInInventory), [`weight`](nonportable.md#weight)


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorInPrep`](thing.md#actorInPrep), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`actorOutOfPrep`](thing.md#actorOutOfPrep), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`canMatchHer`](thing.md#canMatchHer), [`canMatchHim`](thing.md#canMatchHim), [`canMatchIt`](thing.md#canMatchIt), [`canMatchThem`](thing.md#canMatchThem), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`contentsLister`](thing.md#contentsLister), [`descContentsLister`](thing.md#descContentsLister), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`effectiveFollowLocation`](thing.md#effectiveFollowLocation), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isLikelyCommandTarget`](thing.md#isLikelyCommandTarget), [`isListedAboardVehicle`](thing.md#isListedAboardVehicle), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`lookInLister`](thing.md#lookInLister), [`moved`](thing.md#moved), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`notTravelReadyMsg`](thing.md#notTravelReadyMsg), [`objectNotifyList`](thing.md#objectNotifyList), [`objInPrep`](thing.md#objInPrep), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`roomLocation`](thing.md#roomLocation), [`roomName`](thing.md#roomName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`sightSize`](thing.md#sightSize), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialContentsLister`](thing.md#specialContentsLister), [`specialDesc`](thing.md#specialDesc), [`specialDescBeforeContents`](thing.md#specialDescBeforeContents), [`specialDescListWith`](thing.md#specialDescListWith), [`specialDescOrder`](thing.md#specialDescOrder), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`takeFromNotInMessage`](thing.md#takeFromNotInMessage), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


*From [BasicLocation](basiclocation.md):* [`cannotGoThatWayMsg`](basiclocation.md#cannotGoThatWayMsg), [`defaultPosture`](basiclocation.md#defaultPosture), [`listWithActorInTable`](basiclocation.md#listWithActorInTable), [`mustDefaultPostureProp`](basiclocation.md#mustDefaultPostureProp), [`roomNotifyList`](basiclocation.md#roomNotifyList), [`roomTravelPreCond`](basiclocation.md#roomTravelPreCond)


*From [RoomConnector](roomconnector.md):* [`room1`](roomconnector.md#room1), [`room2`](roomconnector.md#room2)


*From [TravelConnector](travelconnector.md):* [`connectorStagingLocation`](travelconnector.md#connectorStagingLocation), [`isCircularPassage`](travelconnector.md#isCircularPassage), [`isConnectorListed`](travelconnector.md#isConnectorListed), [`rememberCircularPassage`](travelconnector.md#rememberCircularPassage), [`travelBarrier`](travelconnector.md#travelBarrier), [`travelMemory`](travelconnector.md#travelMemory)


## Methods


### `childInName(childName)` *(overridden)*

Defined in en_us.t, line 3000

For top-level rooms, describe an object as being in the room by describing it as being in the room's nominal drop destination, since that's the nominal location for the objects directly in the room. (In most cases, the nominal drop destination for a room is its floor.)


### `childInNameWithOwner(chiName)` *(overridden)*

Defined in en_us.t, line 3008

if the PC isn't inside us, we're viewing this remotely


### `dobjFor(Board)` *(overridden)*

Defined in travel.t, line 4660

for BOARD and ENTER, there are three possibilities:


### `dobjFor(Enter)` *(overridden)*

Defined in travel.t, line 4661


### `dobjFor(Examine)` *(overridden)*

Defined in travel.t, line 4570

When we're in the room, treat EXAMINE <ROOM> the same as LOOK AROUND. (This will only work if the room is given vocabulary like a normal object.)


### `dobjFor(GetOutOf)` *(overridden)*

Defined in travel.t, line 4624

treat an explicit GET OUT OF <ROOM> as OUT if there's an apparent destination for OUT; otherwise treat it as "vague travel," which simply tells the player that they need to specify a direction


### `dobjFor(LieOn)` *(overridden)*

Defined in travel.t, line 4617


### `dobjFor(ListenTo)` *(overridden)*

Defined in travel.t, line 4612


### `dobjFor(LookBehind)` *(overridden)*

Defined in travel.t, line 4608


### `dobjFor(LookIn)` *(overridden)*

Defined in travel.t, line 4604

treat LOOK IN <room> as EXAMINE <room>


### `dobjFor(LookUnder)` *(overridden)*

Defined in travel.t, line 4607

LOOK UNDER and BEHIND are illogical


### `dobjFor(SitOn)` *(overridden)*

Defined in travel.t, line 4616


### `dobjFor(Smell)` *(overridden)*

Defined in travel.t, line 4611

treat SMELL/LISTEN TO <room> as just SMELL/LISTEN


### `dobjFor(StandOn)` *(overridden)*

Defined in travel.t, line 4615

map STAND/SIT/LIE ON <room> to my default floor


### `getDestName(actor, origin)` *(overridden)*

Defined in travel.t, line 4379

Get my "destination name," as seen by the given actor from the given origin location. This gives the name we can use to describe this location from the perspective of an actor in an adjoining location looking at a travel connector from that location to here.


### `getExtraScopeItems(actor)` *(overridden)*

Defined in travel.t, line 4551

Get any extra items in scope in this location. These are items that are to be in scope even if they're not reachable through any of the normal sense paths (so they'll be in scope even in the dark, for example).


### `getNominalActorContainer(posture)` *(overridden)*

Defined in travel.t, line 4445

The nominal actor container. By default, this is the room's nominal drop destination, which is usually the floor or equivalent.


### `getNominalDropDestination` *(overridden)*

Defined in travel.t, line 4423

The nominal drop destination - this is the location where we describe objects as being when they're actually directly within the room.


### `getRoomPartLocation(part)` *(overridden)*

Defined in travel.t, line 4488

Get the apparent location of one of our room parts.


### `hideFromAll(action)` *(overridden)*

Defined in travel.t, line 4340

we generally do not want rooms to be included when a command refers to 'all'


### `hideFromDefault(action)` *(overridden)*

Defined in travel.t, line 4343

don't consider myself a default for STAND ON, SIT ON, or LIE ON


### `initializeThing` *(overridden)*

Defined in travel.t, line 4317

Initialize


### `mustMoveObjInto(obj)` *(overridden)*

Defined in travel.t, line 4463

explain that something must be in the room first


### `roomDaemon` *(overridden)*

Defined in travel.t, line 4401

Room daemon - this is invoked on the player character's immediate location once per turn in a daemon.


### `tryMovingObjInto(obj)` *(overridden)*

Defined in travel.t, line 4451

move something into a room is accomplished by putting the object on the floor


## Inherited Methods


*From [Fixture](fixture.md):* [`dobjFor(Move)`](fixture.md#dobjFor(Move)), [`dobjFor(MoveTo)`](fixture.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](fixture.md#dobjFor(MoveWith)), [`dobjFor(Pull)`](fixture.md#dobjFor(Pull)), [`dobjFor(Push)`](fixture.md#dobjFor(Push)), [`dobjFor(PushTravel)`](fixture.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](fixture.md#dobjFor(PutBehind)), [`dobjFor(PutIn)`](fixture.md#dobjFor(PutIn)), [`dobjFor(PutOn)`](fixture.md#dobjFor(PutOn)), [`dobjFor(PutUnder)`](fixture.md#dobjFor(PutUnder)), [`dobjFor(Take)`](fixture.md#dobjFor(Take)), [`dobjFor(TakeFrom)`](fixture.md#dobjFor(TakeFrom)), [`dobjFor(ThrowAt)`](fixture.md#dobjFor(ThrowAt)), [`dobjFor(ThrowDir)`](fixture.md#dobjFor(ThrowDir)), [`isOwnedBy`](fixture.md#isOwnedBy), [`verifyMoveTo`](fixture.md#verifyMoveTo)


*From [NonPortable](nonportable.md):* [`contentsInFixedIn`](nonportable.md#contentsInFixedIn), [`dobjFor(ShowTo)`](nonportable.md#dobjFor(ShowTo)), [`isHeldBy`](nonportable.md#isHeldBy), [`meetsObjHeld`](nonportable.md#meetsObjHeld)


<details><summary>From [Thing](thing.md) (400)</summary>

[`acceptCommand`](thing.md#acceptCommand), [`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToContents`](thing.md#addToContents), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustLookAroundTable`](thing.md#adjustLookAroundTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`afterAction`](thing.md#afterAction), [`afterTravel`](thing.md#afterTravel), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameObj`](thing.md#aNameObj), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`beforeAction`](thing.md#beforeAction), [`beforeTravel`](thing.md#beforeTravel), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canHear`](thing.md#canHear), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotGoShowExits`](thing.md#cannotGoShowExits), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canOwn`](thing.md#canOwn), [`canSee`](thing.md#canSee), [`canSmell`](thing.md#canSmell), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkActorOutOfNested`](thing.md#checkActorOutOfNested), [`checkBulkChange`](thing.md#checkBulkChange), [`checkBulkChangeWithin`](thing.md#checkBulkChangeWithin), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkStagingLocation`](thing.md#checkStagingLocation), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`checkTravelerDirectlyInRoom`](thing.md#checkTravelerDirectlyInRoom), [`childInNameGen`](thing.md#childInNameGen), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`conjugateRegularVerb`](thing.md#conjugateRegularVerb), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskAbout)`](thing.md#dobjFor(AskAbout)), [`dobjFor(AskFor)`](thing.md#dobjFor(AskFor)), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Drop)`](thing.md#dobjFor(Drop)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(Kiss)`](thing.md#dobjFor(Kiss)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(TalkTo)`](thing.md#dobjFor(TalkTo)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellAbout)`](thing.md#dobjFor(TellAbout)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Throw)`](thing.md#dobjFor(Throw)), [`dobjFor(ThrowTo)`](thing.md#dobjFor(ThrowTo)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContents`](thing.md#examineListContents), [`examineListContentsWith`](thing.md#examineListContentsWith), [`examineSpecialContents`](thing.md#examineSpecialContents), [`examineStatus`](thing.md#examineStatus), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDropDestination`](thing.md#getDropDestination), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getHitFallDestination`](thing.md#getHitFallDestination), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomNotifyList`](thing.md#getRoomNotifyList), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getStatuslineExitsHeight`](thing.md#getStatuslineExitsHeight), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(GiveTo)`](thing.md#iobjFor(GiveTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutOn)`](thing.md#iobjFor(PutOn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(ShowTo)`](thing.md#iobjFor(ShowTo)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowAt)`](thing.md#iobjFor(ThrowAt)), [`iobjFor(ThrowTo)`](thing.md#iobjFor(ThrowTo)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isActorTravelReady`](thing.md#isActorTravelReady), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isIn`](thing.md#isIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAround`](thing.md#lookAround), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`noteSeenBy`](thing.md#noteSeenBy), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`remoteSpecialDesc`](thing.md#remoteSpecialDesc), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomActorThereDesc`](thing.md#roomActorThereDesc), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomDesc`](thing.md#roomDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`roomTravelPreCond`](thing.md#roomTravelPreCond), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContents`](thing.md#showSpecialDescInContents), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showStatuslineExits`](thing.md#showStatuslineExits), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyFollowable`](thing.md#verifyFollowable), [`verifyInsert`](thing.md#verifyInsert), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)


<details><summary>From [BasicLocation](basiclocation.md) (31)</summary>

[`actorInGroupPrefix`](basiclocation.md#actorInGroupPrefix), [`actorInGroupSuffix`](basiclocation.md#actorInGroupSuffix), [`actorIsFamiliar`](basiclocation.md#actorIsFamiliar), [`actorKnowsDestination`](basiclocation.md#actorKnowsDestination), [`actorTravelingWithin`](basiclocation.md#actorTravelingWithin), [`addRoomNotifyItem`](basiclocation.md#addRoomNotifyItem), [`cannotGoThatWay`](basiclocation.md#cannotGoThatWay), [`cannotGoThatWayInDark`](basiclocation.md#cannotGoThatWayInDark), [`cannotTravel`](basiclocation.md#cannotTravel), [`checkActorReadyToEnterNestedRoom`](basiclocation.md#checkActorReadyToEnterNestedRoom), [`checkMovingActorInto`](basiclocation.md#checkMovingActorInto), [`disembarkRoom`](basiclocation.md#disembarkRoom), [`dispatchRoomDaemon`](basiclocation.md#dispatchRoomDaemon), [`enteringRoom`](basiclocation.md#enteringRoom), [`leavingRoom`](basiclocation.md#leavingRoom), [`listWithActorIn`](basiclocation.md#listWithActorIn), [`makeStandingUp`](basiclocation.md#makeStandingUp), [`removeRoomNotifyItem`](basiclocation.md#removeRoomNotifyItem), [`roomActorHereDesc`](basiclocation.md#roomActorHereDesc), [`roomActorPostureDesc`](basiclocation.md#roomActorPostureDesc), [`roomActorStatus`](basiclocation.md#roomActorStatus), [`roomAfterAction`](basiclocation.md#roomAfterAction), [`roomBeforeAction`](basiclocation.md#roomBeforeAction), [`roomDarkTravel`](basiclocation.md#roomDarkTravel), [`roomListActorPosture`](basiclocation.md#roomListActorPosture), [`roomOkayPostureChange`](basiclocation.md#roomOkayPostureChange), [`travelerArriving`](basiclocation.md#travelerArriving), [`travelerLeaving`](basiclocation.md#travelerLeaving), [`tryMakingDefaultPosture`](basiclocation.md#tryMakingDefaultPosture), [`tryMakingTravelReady`](basiclocation.md#tryMakingTravelReady), [`wouldBeLitFor`](basiclocation.md#wouldBeLitFor)

</details>


*From [RoomAutoConnector](roomautoconnector.md):* [`getDestination`](roomautoconnector.md#getDestination)


*From [RoomConnector](roomconnector.md):* [`connectorTravelPreCond`](roomconnector.md#connectorTravelPreCond), [`fixedSource`](roomconnector.md#fixedSource)


*From [TravelConnector](travelconnector.md):* [`actorTravelPreCond`](travelconnector.md#actorTravelPreCond), [`canTravelerPass`](travelconnector.md#canTravelerPass), [`checkTravelBarriers`](travelconnector.md#checkTravelBarriers), [`connectorBack`](travelconnector.md#connectorBack), [`connectorGetConnectorTo`](travelconnector.md#connectorGetConnectorTo), [`createUnlistedProxy`](travelconnector.md#createUnlistedProxy), [`darkTravel`](travelconnector.md#darkTravel), [`describeArrival`](travelconnector.md#describeArrival), [`describeDeparture`](travelconnector.md#describeDeparture), [`describeLocalArrival`](travelconnector.md#describeLocalArrival), [`describeLocalDeparture`](travelconnector.md#describeLocalDeparture), [`describeRemoteTravel`](travelconnector.md#describeRemoteTravel), [`dobjFor(TravelVia)`](travelconnector.md#dobjFor(TravelVia)), [`explainTravelBarrier`](travelconnector.md#explainTravelBarrier), [`getApparentDestination`](travelconnector.md#getApparentDestination), [`isConnectorApparent`](travelconnector.md#isConnectorApparent), [`isConnectorPassable`](travelconnector.md#isConnectorPassable), [`isConnectorVisibleInDark`](travelconnector.md#isConnectorVisibleInDark), [`noteTraversal`](travelconnector.md#noteTraversal), [`rememberTravel`](travelconnector.md#rememberTravel)
