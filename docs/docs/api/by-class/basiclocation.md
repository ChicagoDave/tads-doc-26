# BasicLocation

*class* — defined in [travel.t](../by-file/travel.t.md) (line 3468)


A basic location - this is the base class for locations that can contain actors.


**Superclass chain:** [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > **BasicLocation**


<details><summary>Subclasses (16)</summary>

- [NestedRoom](nestedroom.md)
- [BasicChair](basicchair.md)
- [BasicBed](basicbed.md)
- [BasicPlatform](basicplatform.md)
- [Booth](booth.md)
- [Platform](platform.md)
- [NominalPlatform](nominalplatform.md)
- [Bed](bed.md)
- [Chair](chair.md)
- [HighNestedRoom](highnestedroom.md)
- [Vehicle](vehicle.md)
- [Room](room.md)
- [DarkRoom](darkroom.md)
- [FloorlessRoom](floorlessroom.md)
- [OutdoorRoom](outdoorroom.md)
- [ShipboardRoom](shipboardroom.md)

</details>


## Properties


### `cannotGoThatWayMsg`

Defined in travel.t, line 4232

The message to display when it's not possible to travel in a given direction from this room; this is either a single-quoted string or an actor action messages property (by default, it's the latter, giving a default library message).


### `defaultPosture`

Defined in travel.t, line 3695

Default posture for an actor in the location. This is the posture assumed by an actor when moving out of a nested room within this location.


### `effectiveFollowLocation` *(overridden)*

Defined in travel.t, line 4268

Get the effective location of an actor directly within me, for the purposes of a "follow" command. To follow someone, we must have the same effective follow location that the target had when we last observed the target leaving.


### `listWithActorInTable`

Defined in travel.t, line 3503

our listWithActorIn table - this gets initialized to a LookupTable as soon as we need one (in listWithActorIn)


### `mustDefaultPostureProp`

Defined in travel.t, line 3698

failure report we issue when we can't return to default posture


### `notTravelReadyMsg` *(overridden)*

Defined in travel.t, line 3840

the message explaining what we must do to be travel-ready


### `roomLocation` *(overridden)*

Defined in travel.t, line 3988

Get the room location. Since we're capable of holding actors, we are our own room location.


### `roomNotifyList`

Defined in travel.t, line 3982

our list of registered notification items


### `roomTravelPreCond`

Defined in travel.t, line 4258

Get preconditions for travel for an actor in this location. These preconditions should be applied by any command that will involve travel from this location. By default, we impose no additional requirements.


## Inherited Properties


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorInPrep`](thing.md#actorInPrep), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`actorOutOfPrep`](thing.md#actorOutOfPrep), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`brightness`](thing.md#brightness), [`bulk`](thing.md#bulk), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`canMatchHer`](thing.md#canMatchHer), [`canMatchHim`](thing.md#canMatchHim), [`canMatchIt`](thing.md#canMatchIt), [`canMatchThem`](thing.md#canMatchThem), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListed`](thing.md#contentsListed), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`contentsLister`](thing.md#contentsLister), [`descContentsLister`](thing.md#descContentsLister), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isLikelyCommandTarget`](thing.md#isLikelyCommandTarget), [`isListedAboardVehicle`](thing.md#isListedAboardVehicle), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`isTopLevel`](thing.md#isTopLevel), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`lookInLister`](thing.md#lookInLister), [`moved`](thing.md#moved), [`name`](thing.md#name), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`objectNotifyList`](thing.md#objectNotifyList), [`objInPrep`](thing.md#objInPrep), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`roomName`](thing.md#roomName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`sightSize`](thing.md#sightSize), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialContentsLister`](thing.md#specialContentsLister), [`specialDesc`](thing.md#specialDesc), [`specialDescBeforeContents`](thing.md#specialDescBeforeContents), [`specialDescListWith`](thing.md#specialDescListWith), [`specialDescOrder`](thing.md#specialDescOrder), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`takeFromNotInMessage`](thing.md#takeFromNotInMessage), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont), [`weight`](thing.md#weight)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `actorInGroupPrefix(pov, posture, remote, lst)`

Defined in travel.t, line 3621

Prefix and suffix messages for listing a group of actors nominally in this location. 'posture' is the posture of the actors. 'remote' is the outermost visible room containing the actors, but only if that room is remote from the point-of-view actor; if everything is local, this will be nil. 'lst' is the list of actors being listed. By default, we'll just show the standard library messages.


### `actorInGroupSuffix(pov, posture, remote, lst)`

Defined in travel.t, line 3629


### `actorIsFamiliar(actor)`

Defined in travel.t, line 4154

Is the actor familiar with this location? In other words, is the actor supposed to know the location well at the start of the game?


### `actorKnowsDestination(actor, conn)`

Defined in travel.t, line 4122

Determine if the given actor has "intrinsic" knowledge of the destination of the given travel connector leading away from this location. This knowledge is independent of any memory the actor has of actual travel through the connector in the course of the game, which we track separately via the TravelConnector's travel memory mechanism.


### `actorTravelingWithin(origin, dest)`

Defined in travel.t, line 4085

Receive notification of travel among nested rooms. When an actor moves between two locations related directly by containing (such as from a chair to the room containing the chair, or vice versa), we first call this routine on the origin of the travel, then we move the actor, then we call this same routine on the destination of the travel.


### `addRoomNotifyItem(obj)`

Defined in travel.t, line 3970

Add an item to our registered notification list for actions in the room.


### `cannotGoShowExits(actor)` *(overridden)*

Defined in travel.t, line 3642

Show a list of exits from this room as part of failed travel ("you can't go that way").


### `cannotGoThatWay`

Defined in travel.t, line 4217

Show the default "you can't go that way" message for this location. By default, we show a generic message, but individual rooms might want to override this to provide a more specific description of why travel isn't allowed.


### `cannotGoThatWayInDark`

Defined in travel.t, line 4246

Show a version of the "you can't go that way" message for travel while in the dark. This is called when the actor is in the dark (i.e., there's no ambient light at the actor) and attempts to travel in a direction that doesn't allow travel. By default, we show a generic "you can't see where you're going in the dark" message.


### `cannotTravel`

Defined in travel.t, line 4170

The default "you can't go that way" message for travel within this location in directions that don't allow travel. This is shown whenever an actor tries to travel in one of the directions we have set to point to noTravel. A room can override this to produce a different, customized message for unset travel directions - this is an easy way to change the cannot-travel message for several directions at once.


### `checkActorOutOfNested(allowImplicit)` *(overridden)*

Defined in travel.t, line 3812

Check, using pre-condition rules, that the actor is removed from this nested location and moved to its exit destination. By default, we're not a nested location, so there's nothing for us to do.


### `checkActorReadyToEnterNestedRoom(allowImplicit)`

Defined in travel.t, line 3785

Check, using pre-condition rules, that the actor is ready to enter this room as a nested location. By default, we do nothing, since we're not designed as a nested location.


### `checkMovingActorInto(allowImplicit)`

Defined in travel.t, line 3718

Try moving the actor into this location.


### `checkStagingLocation(dest)` *(overridden)*

Defined in travel.t, line 3710

Check this object as a staging location. We're a valid location, so we allow this.


### `checkTravelerDirectlyInRoom(traveler, allowImplicit)` *(overridden)*

Defined in travel.t, line 3796

Check that the traveler is directly in the given room, using pre-condition rules. 'nested' is the nested location immediately within this room that contains the actor (directly or indirectly).


### `disembarkRoom`

Defined in travel.t, line 3846

An actor is attempting to disembark this location. By default, we'll simply turn this into an "exit" command.


### `dispatchRoomDaemon`

Defined in travel.t, line 4275

Dispatch the room daemon. This is a daemon routine invoked once per turn; we in turn invoke roomDaemon on the current player character's current location.


### `enteringRoom(traveler)`

Defined in travel.t, line 3998

Receive notification that a traveler is arriving. This is a convenience method that rooms can override to carry out side effects of arrival. This is called just before the room's arrival message (usually the location description) is displayed, so the method can make any adjustments to the room's status or contents needed for the arrival. By default, we do nothing.


### `getDropDestination(objToDrop, path)` *(overridden)*

Defined in travel.t, line 3862

The destination for objects explicitly dropped by an actor within this room. By default, we'll return self, because items dropped should simply go in the room itself. Some types of rooms will want to override this; for example, a room that represents the middle of a tightrope would probably want to set the drop destination to the location below the tightrope. Likewise, objects like chairs will usually prefer to have dropped items go into the enclosing room.


### `getExtraScopeItems(actor)` *(overridden)*

Defined in travel.t, line 3908

Get any extra items in scope for an actor in this location. These are items that are to be in scope even if they're not reachable through any of the normal sense paths (so they'll be in scope even in the dark, for example).


### `getNominalActorContainer(posture)`

Defined in travel.t, line 3894

The "nominal actor container" - this is the container which we'll say actors are in when we describe actors who are actually in this location. By default, this simply returns self, but it's sometimes useful to describe actors as being in some object other than self. The most common case is that normal top-level rooms usually want to describe actors as being "on the floor" or similar.


### `getNominalDropDestination` *(overridden)*

Defined in travel.t, line 3883

The nominal drop destination - this is the location where objects are *reported* to go when dropped by an actor in this location. By default, we simply return 'self'.


### `getRoomNotifyList` *(overridden)*

Defined in travel.t, line 3943

Get my notification list - this is a list of objects on which we must call beforeAction and afterAction when an action is performed within this room.


### `getStatuslineExitsHeight` *(overridden)*

Defined in travel.t, line 3664

Get the estimated height, in lines of text, of the exits display's contribution to the status line. This is used to calculate the extra height we need in the status line, if any, to display the exit list. If we're not configured to display exits in the status line, this should return zero.


### `isActorTravelReady(conn)` *(overridden)*

Defined in travel.t, line 3826

Determine if the current gActor, who is directly in this location, is "travel ready." This means that the actor is ready, as far as this location is concerned, to traverse the given connector. By default, we consider an actor to be travel-ready if the actor is standing; this takes care of most nested room situations, such as chairs and beds, automatically.


### `leavingRoom(traveler)`

Defined in travel.t, line 4006

Receive notification that a traveler is leaving. This is a convenience method that rooms can override to carry out side effects of departure. This is called just after any departure message is displayed. By default, we do nothing.


### `listWithActorIn(posture)`

Defined in travel.t, line 3484

Get the nested room list grouper for an actor in the given posture directly in this room. This is used when we're listing the actors within the nested room as


### `makeStandingUp`

Defined in travel.t, line 3681

Make the actor stand up from this location. By default, we'll simply change the actor's posture to "standing," and show a default success report.


### `removeRoomNotifyItem(obj)`

Defined in travel.t, line 3976

remove an item from the registered notification list


### `roomActorHereDesc(actor)`

Defined in travel.t, line 3557

as part of a room description, mention an actor in this room


### `roomActorPostureDesc(actor)`

Defined in travel.t, line 3598

describe the actor's posture while in this location


### `roomActorStatus(actor)`

Defined in travel.t, line 3595

show the status addendum for an actor in this location


### `roomActorThereDesc(actor)` *(overridden)*

Defined in travel.t, line 3566

Provide a default description for an actor in this location, as seen from a remote location (i.e., from a separate top-level room that's linked to our top-level room by a sense connector of some kind). By default, we'll describe the actor as being in this nested room.


### `roomAfterAction`

Defined in travel.t, line 3926

Receive notification that we've just finished a command within this location. This is called on the room immediately containing the actor performing the command, then on the room containing that room, and so on to the outermost room.


### `roomBeforeAction`

Defined in travel.t, line 3916

Receive notification that we're about to perform a command within this location. This is called on the outermost room first, then on the nested rooms, from the outside in, until reaching the room directly containing the actor performing the command.


### `roomDarkTravel(actor)`

Defined in travel.t, line 4199

Receive notification of travel from one dark location to another. This is called before the actor is moved from the source location, and can cancel the travel if desired by using 'exit' to terminate the command.


### `roomDesc` *(overridden)*

Defined in travel.t, line 3554

Show our room description: this is the interior description of the room, for use when the room is viewed by an actor within the room. By default, we show our ordinary 'desc'.


### `roomListActorPosture(actor)`

Defined in travel.t, line 3609

describe the actor's posture as part of the EXAMINE description of the nested room


### `roomOkayPostureChange(actor)`

Defined in travel.t, line 3602

acknowledge a posture change while in this location


### `showStatuslineExits` *(overridden)*

Defined in travel.t, line 3650

show the exit list in the status line


### `travelerArriving(traveler, origin, connector, backConnector)`

Defined in travel.t, line 4036

Receive notification that a traveler is arriving in the room. 'traveler' is the object actually traveling. In most cases this is simply the actor; but when the actor is in a vehicle, this is the vehicle instead.


### `travelerLeaving(traveler, dest, connector)`

Defined in travel.t, line 4017

Receive notification that a traveler is about to leave the room. 'traveler' is the object actually traveling. In most cases this is simply the actor; but when the actor is in a vehicle, this is the vehicle instead.


### `tryMakingDefaultPosture`

Defined in travel.t, line 3701

run the appropriate implied command to achieve our default posture


### `tryMakingTravelReady(conn)`

Defined in travel.t, line 3837

Run an implicit action, if possible, to make the current actor "travel ready." This will be called if the actor is directly in this location and isActorTravelReady() returns nil. By default, we try to make the actor stand up. This should always be paired with isActorTravelReady - the condition that routine tests should be the condition this routine tries to bring into effect. If no implicit action is possible, simply return nil.


### `wouldBeLitFor(actor)`

Defined in travel.t, line 3518

Check the ambient illumination level in the room for the given actor's senses to determine if the actor would be able to see if the actor were in this room without any additional light sources. Returns true if the room is lit for the purposes of the actor's visual senses, nil if not.


## Inherited Methods


<details><summary>From [Thing](thing.md) (431)</summary>

[`acceptCommand`](thing.md#acceptCommand), [`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToContents`](thing.md#addToContents), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustLookAroundTable`](thing.md#adjustLookAroundTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`afterAction`](thing.md#afterAction), [`afterTravel`](thing.md#afterTravel), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameObj`](thing.md#aNameObj), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`beforeAction`](thing.md#beforeAction), [`beforeTravel`](thing.md#beforeTravel), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canHear`](thing.md#canHear), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canOwn`](thing.md#canOwn), [`canSee`](thing.md#canSee), [`canSmell`](thing.md#canSmell), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkBulkChange`](thing.md#checkBulkChange), [`checkBulkChangeWithin`](thing.md#checkBulkChangeWithin), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`childInName`](thing.md#childInName), [`childInNameGen`](thing.md#childInNameGen), [`childInNameWithOwner`](thing.md#childInNameWithOwner), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`conjugateRegularVerb`](thing.md#conjugateRegularVerb), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`contentsInFixedIn`](thing.md#contentsInFixedIn), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskAbout)`](thing.md#dobjFor(AskAbout)), [`dobjFor(AskFor)`](thing.md#dobjFor(AskFor)), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Board)`](thing.md#dobjFor(Board)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Drop)`](thing.md#dobjFor(Drop)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(Enter)`](thing.md#dobjFor(Enter)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Examine)`](thing.md#dobjFor(Examine)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GetOutOf)`](thing.md#dobjFor(GetOutOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(Kiss)`](thing.md#dobjFor(Kiss)), [`dobjFor(LieOn)`](thing.md#dobjFor(LieOn)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(ListenTo)`](thing.md#dobjFor(ListenTo)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookBehind)`](thing.md#dobjFor(LookBehind)), [`dobjFor(LookIn)`](thing.md#dobjFor(LookIn)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(LookUnder)`](thing.md#dobjFor(LookUnder)), [`dobjFor(Move)`](thing.md#dobjFor(Move)), [`dobjFor(MoveTo)`](thing.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](thing.md#dobjFor(MoveWith)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Pull)`](thing.md#dobjFor(Pull)), [`dobjFor(Push)`](thing.md#dobjFor(Push)), [`dobjFor(PushTravel)`](thing.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](thing.md#dobjFor(PutBehind)), [`dobjFor(PutIn)`](thing.md#dobjFor(PutIn)), [`dobjFor(PutOn)`](thing.md#dobjFor(PutOn)), [`dobjFor(PutUnder)`](thing.md#dobjFor(PutUnder)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(ShowTo)`](thing.md#dobjFor(ShowTo)), [`dobjFor(SitOn)`](thing.md#dobjFor(SitOn)), [`dobjFor(Smell)`](thing.md#dobjFor(Smell)), [`dobjFor(StandOn)`](thing.md#dobjFor(StandOn)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(Take)`](thing.md#dobjFor(Take)), [`dobjFor(TakeFrom)`](thing.md#dobjFor(TakeFrom)), [`dobjFor(TalkTo)`](thing.md#dobjFor(TalkTo)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellAbout)`](thing.md#dobjFor(TellAbout)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Throw)`](thing.md#dobjFor(Throw)), [`dobjFor(ThrowAt)`](thing.md#dobjFor(ThrowAt)), [`dobjFor(ThrowDir)`](thing.md#dobjFor(ThrowDir)), [`dobjFor(ThrowTo)`](thing.md#dobjFor(ThrowTo)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContents`](thing.md#examineListContents), [`examineListContentsWith`](thing.md#examineListContentsWith), [`examineSpecialContents`](thing.md#examineSpecialContents), [`examineStatus`](thing.md#examineStatus), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDestName`](thing.md#getDestName), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getHitFallDestination`](thing.md#getHitFallDestination), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomPartLocation`](thing.md#getRoomPartLocation), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`hideFromAll`](thing.md#hideFromAll), [`hideFromDefault`](thing.md#hideFromDefault), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`initializeThing`](thing.md#initializeThing), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(GiveTo)`](thing.md#iobjFor(GiveTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutOn)`](thing.md#iobjFor(PutOn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(ShowTo)`](thing.md#iobjFor(ShowTo)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowAt)`](thing.md#iobjFor(ThrowAt)), [`iobjFor(ThrowTo)`](thing.md#iobjFor(ThrowTo)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isHeldBy`](thing.md#isHeldBy), [`isIn`](thing.md#isIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isOwnedBy`](thing.md#isOwnedBy), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAround`](thing.md#lookAround), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`meetsObjHeld`](thing.md#meetsObjHeld), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`mustMoveObjInto`](thing.md#mustMoveObjInto), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`noteSeenBy`](thing.md#noteSeenBy), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`remoteSpecialDesc`](thing.md#remoteSpecialDesc), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDaemon`](thing.md#roomDaemon), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`roomTravelPreCond`](thing.md#roomTravelPreCond), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContents`](thing.md#showSpecialDescInContents), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`tryMovingObjInto`](thing.md#tryMovingObjInto), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyFollowable`](thing.md#verifyFollowable), [`verifyInsert`](thing.md#verifyInsert), [`verifyMoveTo`](thing.md#verifyMoveTo), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
