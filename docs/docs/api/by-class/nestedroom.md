# NestedRoom

*class* — defined in [travel.t](../by-file/travel.t.md) (line 5590)


A Nested Room is any object that isn't a room but which can contain an actor: chairs, beds, platforms, vehicles, and the like.


**Superclass chain:** [BasicLocation](basiclocation.md) > [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > **NestedRoomSubclasses:** [BasicChair](basicchair.md), [BasicBed](basicbed.md), [BasicPlatform](basicplatform.md), [Booth](booth.md), [Platform](platform.md), [NominalPlatform](nominalplatform.md), [Bed](bed.md), [Chair](chair.md), [HighNestedRoom](highnestedroom.md), [Vehicle](vehicle.md)


## Properties


### `bulkCapacity`

Defined in travel.t, line 5634

The maximum bulk the room can hold. We'll define this to a large number by default so that bulk isn't a concern.


### `exitDestination`

Defined in travel.t, line 6132

Our exit destination. This is where an actor ends up when the actor is immediately inside this nested room and uses a "get out of" or equivalent command to exit the nested room.


### `mustMoveIntoProp`

Defined in travel.t, line 5770

message property to use for reportFailure when tryMovingIntoNested fails


### `out`

Defined in travel.t, line 5688

By default, 'out' within a nested room should take us out of the nested room itself. The easy way to accomplish this is to set up a 'nestedRoomOut' connector for the nested room, which will automatically try a GET OUT command. If we didn't do this, we'd *usually* pick up the noTravelOut from our enclosing room, but only when the enclosing room didn't override 'out' to point somewhere else. Explicitly setting up a 'noTravelOut' here ensures that we'll consistently GET OUT of the nested room even if the enclosing room has its own 'out' destination.


### `roomName` *(overridden)*

Defined in travel.t, line 5600

Our interior room name. This is the status line name we display when an actor is within this object and can't see out to the enclosing room. Since we can't rely on the enclosing room's status line name if we can't see the enclosing room, we must provide one of our own.


### `stagingLocations`

Defined in travel.t, line 6122

The valid "staging locations" for this nested room. This is a list of the rooms from which an actor can DIRECTLY reach this nested room; in other words, the actor will be allowed to enter 'self', with no intervening travel, if the actor is directly in any of these locations.


## Inherited Properties


*From [BasicLocation](basiclocation.md):* [`cannotGoThatWayMsg`](basiclocation.md#cannotGoThatWayMsg), [`defaultPosture`](basiclocation.md#defaultPosture), [`effectiveFollowLocation`](basiclocation.md#effectiveFollowLocation), [`listWithActorInTable`](basiclocation.md#listWithActorInTable), [`mustDefaultPostureProp`](basiclocation.md#mustDefaultPostureProp), [`notTravelReadyMsg`](basiclocation.md#notTravelReadyMsg), [`roomLocation`](basiclocation.md#roomLocation), [`roomNotifyList`](basiclocation.md#roomNotifyList), [`roomTravelPreCond`](basiclocation.md#roomTravelPreCond)


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorInPrep`](thing.md#actorInPrep), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`actorOutOfPrep`](thing.md#actorOutOfPrep), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`brightness`](thing.md#brightness), [`bulk`](thing.md#bulk), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`canMatchHer`](thing.md#canMatchHer), [`canMatchHim`](thing.md#canMatchHim), [`canMatchIt`](thing.md#canMatchIt), [`canMatchThem`](thing.md#canMatchThem), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListed`](thing.md#contentsListed), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`contentsLister`](thing.md#contentsLister), [`descContentsLister`](thing.md#descContentsLister), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isLikelyCommandTarget`](thing.md#isLikelyCommandTarget), [`isListedAboardVehicle`](thing.md#isListedAboardVehicle), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`isTopLevel`](thing.md#isTopLevel), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`lookInLister`](thing.md#lookInLister), [`moved`](thing.md#moved), [`name`](thing.md#name), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`objectNotifyList`](thing.md#objectNotifyList), [`objInPrep`](thing.md#objInPrep), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`sightSize`](thing.md#sightSize), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialContentsLister`](thing.md#specialContentsLister), [`specialDesc`](thing.md#specialDesc), [`specialDescBeforeContents`](thing.md#specialDescBeforeContents), [`specialDescListWith`](thing.md#specialDescListWith), [`specialDescOrder`](thing.md#specialDescOrder), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`takeFromNotInMessage`](thing.md#takeFromNotInMessage), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont), [`weight`](thing.md#weight)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `cannotMoveActorOutOf`

Defined in travel.t, line 6087

Report that we are unable to move an actor out of this nested room, because there's no valid 'exit destination'. This is called when we attempt to GET OUT OF the nested room, and the 'exitDestination' property is nil.


### `cannotMoveActorToStagingLocation`

Defined in travel.t, line 6075

Report that we are unable to move an actor to any staging location for this nested room. By default, we'll generate the message "you can't do that from here," but this can overridden to provide a more specific if desired.


### `checkActorInStagingLocation(allowImplicit)`

Defined in travel.t, line 5927

Check, using precondition rules, that the actor is in a valid "staging location" for entering this nested room. We'll ensure that the actor is directly in one of the locations in our stagingLocations list, running an appropriate implicit command to move the actor to the first item in that list if the actor isn't in any of them.


### `checkActorOutOfNested(allowImplicit)` *(overridden)*

Defined in travel.t, line 5862

Check, using pre-condition rules, that the actor is removed from this nested location and moved to my immediate location. This is used to enforce a precondition that the actor is in the enclosing location.


### `checkActorReadyToEnterNestedRoom(allowImplicit)` *(overridden)*

Defined in travel.t, line 5889

Check, using pre-condition rules, that the actor is ready to enter this room as a nested location.


### `checkMovingActorInto(allowImplicit)` *(overridden)*

Defined in travel.t, line 5814

Try moving the actor into this location. This is used to move the actor into this location as part of meeting preconditions, and we use the normal precondition check protocol: we return nil if the condition (actor is in this room) is already met; we return true if we successfully execute an implied command to meet the condition; and we report a failure message and terminate the command with 'exit' if we don't know how to meet the condition or the implied command we try to execute fails or fails to satisfy the condition.


### `chooseStagingLocation`

Defined in travel.t, line 6022

Choose an intermediate staging location, given the actor's current location. This routine is called when the actor is attempting to move into 'self', but isn't in any of the allowed staging locations for 'self'; this routine's purpose is to choose the staging location that the actor should implicitly try to reach on the way to 'self'.


### `defaultStagingLocation`

Defined in travel.t, line 6050

The default staging location for this nested room. This is the staging location we'll attempt to reach implicitly if the actor isn't in any of the rooms in the stagingLocations list already. We'll return the first element of our stagingLocations list for which isStagingLocationKnown returns true.


### `disembarkRoom` *(overridden)*

Defined in travel.t, line 5695

An actor is attempting to "get out" while in this location. By default, we'll treat this as getting out of this object. This can be overridden if "get out" should do something different.


### `dobjFor(GetOutOf)` *(overridden)*

Defined in travel.t, line 6201

"get out of" action - exit the nested room


### `dobjFor(Take)` *(overridden)*

Defined in travel.t, line 6185

We cannot take a nested room that the actor is occupying


### `getExtraScopeItems(actor)` *(overridden)*

Defined in travel.t, line 5663

Get the extra scope items within this room. Normally, the immediately enclosing nested room is in scope for an actor in the room. So, if the actor is directly in 'self', return 'self'.


### `isOwnedBy(obj)` *(overridden)*

Defined in travel.t, line 5645

Check for ownership. For a nested room, an actor can be taken to own the nested room by virtue of being inside the room - the chair Bob is sitting in can be called "bob's chair".


### `isStagingLocationKnown(loc)`

Defined in travel.t, line 6154

Is the given staging location "known"? This returns true if the staging location is usable as a default, nil if not. If this returns true, then the location can be used in an implied command to move the actor to the staging location in order to move the actor into self.


### `makeStandingUp` *(overridden)*

Defined in travel.t, line 5706

Make the actor stand up from this location. By default, we'll cause the actor to travel (using travelWithin) to our container, and assume the appropriate posture for the container.


### `mapPushTravelIobj(PushTravelGetOutOf, TravelVia)`

Defined in travel.t, line 6249

explicitly define the push-travel indirect object mappings


### `removeFromNested`

Defined in travel.t, line 5796

Replace the current action with one that removes the actor from this nested room. This is used to implement the GET OUT command when the actor is directly in this nested room. In most cases, this should simply be implemented with a call to replaceAction() with the appropriate command.


### `roomTravelPreCond` *(overridden)*

Defined in travel.t, line 6162

Get the travel preconditions for an actor in this location. By default, if we have a container, and the actor can see the container, we'll return its travel preconditions; otherwise, we'll use our inherited preconditions.


### `tryMovingIntoNested`

Defined in travel.t, line 5760

Try an implied command to move the actor from outside of this nested room into this nested room. This must be overridden in subclasses to carry out the appropriate implied command. Returns the result of tryImplicitAction().


### `tryRemovingFromNested`

Defined in travel.t, line 5783

Try an implied command to remove an actor from this location and place the actor in my immediate containing location. This must be overridden in subclasses to carry out the appropriate implied command. Returns the result of tryImplicitAction().


## Inherited Methods


<details><summary>From [BasicLocation](basiclocation.md) (39)</summary>

[`actorInGroupPrefix`](basiclocation.md#actorInGroupPrefix), [`actorInGroupSuffix`](basiclocation.md#actorInGroupSuffix), [`actorIsFamiliar`](basiclocation.md#actorIsFamiliar), [`actorKnowsDestination`](basiclocation.md#actorKnowsDestination), [`actorTravelingWithin`](basiclocation.md#actorTravelingWithin), [`addRoomNotifyItem`](basiclocation.md#addRoomNotifyItem), [`cannotGoShowExits`](basiclocation.md#cannotGoShowExits), [`cannotGoThatWay`](basiclocation.md#cannotGoThatWay), [`cannotGoThatWayInDark`](basiclocation.md#cannotGoThatWayInDark), [`cannotTravel`](basiclocation.md#cannotTravel), [`checkStagingLocation`](basiclocation.md#checkStagingLocation), [`checkTravelerDirectlyInRoom`](basiclocation.md#checkTravelerDirectlyInRoom), [`dispatchRoomDaemon`](basiclocation.md#dispatchRoomDaemon), [`enteringRoom`](basiclocation.md#enteringRoom), [`getDropDestination`](basiclocation.md#getDropDestination), [`getNominalActorContainer`](basiclocation.md#getNominalActorContainer), [`getNominalDropDestination`](basiclocation.md#getNominalDropDestination), [`getRoomNotifyList`](basiclocation.md#getRoomNotifyList), [`getStatuslineExitsHeight`](basiclocation.md#getStatuslineExitsHeight), [`isActorTravelReady`](basiclocation.md#isActorTravelReady), [`leavingRoom`](basiclocation.md#leavingRoom), [`listWithActorIn`](basiclocation.md#listWithActorIn), [`removeRoomNotifyItem`](basiclocation.md#removeRoomNotifyItem), [`roomActorHereDesc`](basiclocation.md#roomActorHereDesc), [`roomActorPostureDesc`](basiclocation.md#roomActorPostureDesc), [`roomActorStatus`](basiclocation.md#roomActorStatus), [`roomActorThereDesc`](basiclocation.md#roomActorThereDesc), [`roomAfterAction`](basiclocation.md#roomAfterAction), [`roomBeforeAction`](basiclocation.md#roomBeforeAction), [`roomDarkTravel`](basiclocation.md#roomDarkTravel), [`roomDesc`](basiclocation.md#roomDesc), [`roomListActorPosture`](basiclocation.md#roomListActorPosture), [`roomOkayPostureChange`](basiclocation.md#roomOkayPostureChange), [`showStatuslineExits`](basiclocation.md#showStatuslineExits), [`travelerArriving`](basiclocation.md#travelerArriving), [`travelerLeaving`](basiclocation.md#travelerLeaving), [`tryMakingDefaultPosture`](basiclocation.md#tryMakingDefaultPosture), [`tryMakingTravelReady`](basiclocation.md#tryMakingTravelReady), [`wouldBeLitFor`](basiclocation.md#wouldBeLitFor)

</details>


<details><summary>From [Thing](thing.md) (427)</summary>

[`acceptCommand`](thing.md#acceptCommand), [`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToContents`](thing.md#addToContents), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustLookAroundTable`](thing.md#adjustLookAroundTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`afterAction`](thing.md#afterAction), [`afterTravel`](thing.md#afterTravel), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameObj`](thing.md#aNameObj), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`beforeAction`](thing.md#beforeAction), [`beforeTravel`](thing.md#beforeTravel), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canHear`](thing.md#canHear), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canOwn`](thing.md#canOwn), [`canSee`](thing.md#canSee), [`canSmell`](thing.md#canSmell), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkBulkChange`](thing.md#checkBulkChange), [`checkBulkChangeWithin`](thing.md#checkBulkChangeWithin), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`childInName`](thing.md#childInName), [`childInNameGen`](thing.md#childInNameGen), [`childInNameWithOwner`](thing.md#childInNameWithOwner), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`conjugateRegularVerb`](thing.md#conjugateRegularVerb), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`contentsInFixedIn`](thing.md#contentsInFixedIn), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskAbout)`](thing.md#dobjFor(AskAbout)), [`dobjFor(AskFor)`](thing.md#dobjFor(AskFor)), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Board)`](thing.md#dobjFor(Board)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Drop)`](thing.md#dobjFor(Drop)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(Enter)`](thing.md#dobjFor(Enter)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Examine)`](thing.md#dobjFor(Examine)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(Kiss)`](thing.md#dobjFor(Kiss)), [`dobjFor(LieOn)`](thing.md#dobjFor(LieOn)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(ListenTo)`](thing.md#dobjFor(ListenTo)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookBehind)`](thing.md#dobjFor(LookBehind)), [`dobjFor(LookIn)`](thing.md#dobjFor(LookIn)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(LookUnder)`](thing.md#dobjFor(LookUnder)), [`dobjFor(Move)`](thing.md#dobjFor(Move)), [`dobjFor(MoveTo)`](thing.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](thing.md#dobjFor(MoveWith)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Pull)`](thing.md#dobjFor(Pull)), [`dobjFor(Push)`](thing.md#dobjFor(Push)), [`dobjFor(PushTravel)`](thing.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](thing.md#dobjFor(PutBehind)), [`dobjFor(PutIn)`](thing.md#dobjFor(PutIn)), [`dobjFor(PutOn)`](thing.md#dobjFor(PutOn)), [`dobjFor(PutUnder)`](thing.md#dobjFor(PutUnder)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(ShowTo)`](thing.md#dobjFor(ShowTo)), [`dobjFor(SitOn)`](thing.md#dobjFor(SitOn)), [`dobjFor(Smell)`](thing.md#dobjFor(Smell)), [`dobjFor(StandOn)`](thing.md#dobjFor(StandOn)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(TakeFrom)`](thing.md#dobjFor(TakeFrom)), [`dobjFor(TalkTo)`](thing.md#dobjFor(TalkTo)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellAbout)`](thing.md#dobjFor(TellAbout)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Throw)`](thing.md#dobjFor(Throw)), [`dobjFor(ThrowAt)`](thing.md#dobjFor(ThrowAt)), [`dobjFor(ThrowDir)`](thing.md#dobjFor(ThrowDir)), [`dobjFor(ThrowTo)`](thing.md#dobjFor(ThrowTo)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContents`](thing.md#examineListContents), [`examineListContentsWith`](thing.md#examineListContentsWith), [`examineSpecialContents`](thing.md#examineSpecialContents), [`examineStatus`](thing.md#examineStatus), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDestName`](thing.md#getDestName), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getHitFallDestination`](thing.md#getHitFallDestination), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomPartLocation`](thing.md#getRoomPartLocation), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`hideFromAll`](thing.md#hideFromAll), [`hideFromDefault`](thing.md#hideFromDefault), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`initializeThing`](thing.md#initializeThing), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(GiveTo)`](thing.md#iobjFor(GiveTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutOn)`](thing.md#iobjFor(PutOn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(ShowTo)`](thing.md#iobjFor(ShowTo)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowAt)`](thing.md#iobjFor(ThrowAt)), [`iobjFor(ThrowTo)`](thing.md#iobjFor(ThrowTo)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isHeldBy`](thing.md#isHeldBy), [`isIn`](thing.md#isIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAround`](thing.md#lookAround), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`meetsObjHeld`](thing.md#meetsObjHeld), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`mustMoveObjInto`](thing.md#mustMoveObjInto), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`noteSeenBy`](thing.md#noteSeenBy), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`remoteSpecialDesc`](thing.md#remoteSpecialDesc), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDaemon`](thing.md#roomDaemon), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContents`](thing.md#showSpecialDescInContents), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`tryMovingObjInto`](thing.md#tryMovingObjInto), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyFollowable`](thing.md#verifyFollowable), [`verifyInsert`](thing.md#verifyInsert), [`verifyMoveTo`](thing.md#verifyMoveTo), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
