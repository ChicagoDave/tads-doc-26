# Floor

*class* — defined in [travel.t](../by-file/travel.t.md) (line 5171)


Base class for the default floor and the default ground of a top-level room. The floor and ground are where things usually go when dropped, and they're the locations where actors within a room are normally standing.


**Superclass chain:** [RoomPart](roompart.md) > [Fixture](fixture.md) > [NonPortable](nonportable.md) > [Thing](thing.md) > [VocabObject](vocabobject.md) > `object` > **FloorGlobal objects:** [defaultFloor](defaultfloor.md), [defaultGround](defaultground.md)


## Properties


### `actorInPrep` *(overridden)*

Defined in en_us.t, line 3026


### `actorOutOfPrep` *(overridden)*

Defined in en_us.t, line 3027


### `objInPrep` *(overridden)*

Defined in en_us.t, line 3025


### `putDestMessage`

Defined in travel.t, line 5225

The message we use to describe this object prepositionally, as the destination of a throw or drop. This should be a gLibMessages property with the appropriate prepositional phrase. We use a custom message specific to floor-like objects.


## Inherited Properties


*From [RoomPart](roompart.md):* [`contentsLister`](roompart.md#contentsLister), [`descContentsLister`](roompart.md#descContentsLister), [`lookInLister`](roompart.md#lookInLister), [`nothingBehindMsg`](roompart.md#nothingBehindMsg), [`nothingThroughMsg`](roompart.md#nothingThroughMsg), [`nothingUnderMsg`](roompart.md#nothingUnderMsg), [`sightSize`](roompart.md#sightSize), [`specialContentsLister`](roompart.md#specialContentsLister)


*From [Fixture](fixture.md):* [`cannotMoveMsg`](fixture.md#cannotMoveMsg), [`cannotPutMsg`](fixture.md#cannotPutMsg), [`cannotTakeMsg`](fixture.md#cannotTakeMsg)


*From [NonPortable](nonportable.md):* [`bulk`](nonportable.md#bulk), [`contentsListed`](nonportable.md#contentsListed), [`isListed`](nonportable.md#isListed), [`isListedInContents`](nonportable.md#isListedInContents), [`isListedInInventory`](nonportable.md#isListedInInventory), [`weight`](nonportable.md#weight)


*From [Thing](thing.md):* [`actorInAName`](thing.md#actorInAName), [`actorInName`](thing.md#actorInName), [`actorIntoName`](thing.md#actorIntoName), [`actorOutOfName`](thing.md#actorOutOfName), [`aDisambigName`](thing.md#aDisambigName), [`allStates`](thing.md#allStates), [`aName`](thing.md#aName), [`brightness`](thing.md#brightness), [`canBeHeard`](thing.md#canBeHeard), [`canBeSeen`](thing.md#canBeSeen), [`canBeSmelled`](thing.md#canBeSmelled), [`canBeTouched`](thing.md#canBeTouched), [`canMatchHer`](thing.md#canMatchHer), [`canMatchHim`](thing.md#canMatchHim), [`canMatchIt`](thing.md#canMatchIt), [`canMatchThem`](thing.md#canMatchThem), [`circularlyInMessage`](thing.md#circularlyInMessage), [`collectiveGroup`](thing.md#collectiveGroup), [`collectiveGroups`](thing.md#collectiveGroups), [`contents`](thing.md#contents), [`contentsListedInExamine`](thing.md#contentsListedInExamine), [`contentsListedSeparately`](thing.md#contentsListedSeparately), [`described`](thing.md#described), [`disambigEquivName`](thing.md#disambigEquivName), [`disambigName`](thing.md#disambigName), [`distantDesc`](thing.md#distantDesc), [`distantInitSpecialDesc`](thing.md#distantInitSpecialDesc), [`distantSpecialDesc`](thing.md#distantSpecialDesc), [`distinguishers`](thing.md#distinguishers), [`dummyName`](thing.md#dummyName), [`effectiveFollowLocation`](thing.md#effectiveFollowLocation), [`equivalenceKey`](thing.md#equivalenceKey), [`equivalentGrouper`](thing.md#equivalentGrouper), [`equivalentGrouperClass`](thing.md#equivalentGrouperClass), [`equivalentGrouperTable`](thing.md#equivalentGrouperTable), [`esEndingPat`](thing.md#esEndingPat), [`explicitVisualSenseInfo`](thing.md#explicitVisualSenseInfo), [`getState`](thing.md#getState), [`globalParamName`](thing.md#globalParamName), [`holdingIndex`](thing.md#holdingIndex), [`iesEndingPat`](thing.md#iesEndingPat), [`initDesc`](thing.md#initDesc), [`initNominalRoomPartLocation`](thing.md#initNominalRoomPartLocation), [`initSpecialDesc`](thing.md#initSpecialDesc), [`inlineContentsLister`](thing.md#inlineContentsLister), [`isEquivalent`](thing.md#isEquivalent), [`isHer`](thing.md#isHer), [`isHim`](thing.md#isHim), [`isInInitState`](thing.md#isInInitState), [`isKnown`](thing.md#isKnown), [`isLikelyCommandTarget`](thing.md#isLikelyCommandTarget), [`isListedAboardVehicle`](thing.md#isListedAboardVehicle), [`isMassNoun`](thing.md#isMassNoun), [`isPlural`](thing.md#isPlural), [`isProperName`](thing.md#isProperName), [`isQualifiedName`](thing.md#isQualifiedName), [`isThingConstructed`](thing.md#isThingConstructed), [`isTopLevel`](thing.md#isTopLevel), [`listName`](thing.md#listName), [`listWith`](thing.md#listWith), [`location`](thing.md#location), [`moved`](thing.md#moved), [`name`](thing.md#name), [`nameDoes`](thing.md#nameDoes), [`nameSays`](thing.md#nameSays), [`nameSees`](thing.md#nameSees), [`notTravelReadyMsg`](thing.md#notTravelReadyMsg), [`objectNotifyList`](thing.md#objectNotifyList), [`obscuredInitSpecialDesc`](thing.md#obscuredInitSpecialDesc), [`obscuredSpecialDesc`](thing.md#obscuredSpecialDesc), [`owner`](thing.md#owner), [`patElevenEighteen`](thing.md#patElevenEighteen), [`patIsAlpha`](thing.md#patIsAlpha), [`patLeadingTagOrQuote`](thing.md#patLeadingTagOrQuote), [`patOfPhrase`](thing.md#patOfPhrase), [`patOneLetterAnWord`](thing.md#patOneLetterAnWord), [`patOneLetterWord`](thing.md#patOneLetterWord), [`patSingleApostropheS`](thing.md#patSingleApostropheS), [`patTagOrQuoteChar`](thing.md#patTagOrQuoteChar), [`patUpperOrDigit`](thing.md#patUpperOrDigit), [`patVowelY`](thing.md#patVowelY), [`pluralDisambigName`](thing.md#pluralDisambigName), [`pluralName`](thing.md#pluralName), [`pronounSelector`](thing.md#pronounSelector), [`roomDarkName`](thing.md#roomDarkName), [`roomLocation`](thing.md#roomLocation), [`roomName`](thing.md#roomName), [`seen`](thing.md#seen), [`sightPresence`](thing.md#sightPresence), [`smellPresence`](thing.md#smellPresence), [`smellSize`](thing.md#smellSize), [`soundPresence`](thing.md#soundPresence), [`soundSize`](thing.md#soundSize), [`specialDesc`](thing.md#specialDesc), [`specialDescBeforeContents`](thing.md#specialDescBeforeContents), [`specialDescListWith`](thing.md#specialDescListWith), [`specialDescOrder`](thing.md#specialDescOrder), [`specialNominalRoomPartLocation`](thing.md#specialNominalRoomPartLocation), [`suppressAutoSeen`](thing.md#suppressAutoSeen), [`takeFromNotInMessage`](thing.md#takeFromNotInMessage), [`theDisambigName`](thing.md#theDisambigName), [`theName`](thing.md#theName), [`theNamePossNoun`](thing.md#theNamePossNoun), [`tmpAmbient_`](thing.md#tmpAmbient_), [`tmpAmbientFill_`](thing.md#tmpAmbientFill_), [`tmpAmbientWithin_`](thing.md#tmpAmbientWithin_), [`tmpFillMedium_`](thing.md#tmpFillMedium_), [`tmpObstructor_`](thing.md#tmpObstructor_), [`tmpObstructorWithin_`](thing.md#tmpObstructorWithin_), [`tmpPathIsIn_`](thing.md#tmpPathIsIn_), [`tmpTrans_`](thing.md#tmpTrans_), [`tmpTransWithin_`](thing.md#tmpTransWithin_), [`touchPresence`](thing.md#touchPresence), [`touchSize`](thing.md#touchSize), [`verbCan`](thing.md#verbCan), [`verbCannot`](thing.md#verbCannot), [`verbCant`](thing.md#verbCant), [`verbEndingSD`](thing.md#verbEndingSD), [`verbEndingSEd`](thing.md#verbEndingSEd), [`verbEndingSMessageBuilder_`](thing.md#verbEndingSMessageBuilder_), [`verbMust`](thing.md#verbMust), [`verbToCome`](thing.md#verbToCome), [`verbToDo`](thing.md#verbToDo), [`verbToGo`](thing.md#verbToGo), [`verbToLeave`](thing.md#verbToLeave), [`verbToSay`](thing.md#verbToSay), [`verbToSee`](thing.md#verbToSee), [`verbWill`](thing.md#verbWill), [`verbWont`](thing.md#verbWont)


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `actorInGroupPrefix(pov, posture, remote, lst)`

Defined in travel.t, line 5440

Prefix and suffix messages for listing a group of actors nominally on the this floor. Actors are said to be on the floor when they're really in the location containing the floor.


### `actorInGroupSuffix(pov, posture, remote, lst)`

Defined in travel.t, line 5449


### `childInNameGen(childName, myName)` *(overridden)*

Defined in en_us.t, line 3024


### `dobjFor(LieOn)` *(overridden)*

Defined in travel.t, line 5336

'lie on floor' causes the actor to lie down in the room


### `dobjFor(SitOn)` *(overridden)*

Defined in travel.t, line 5326

'sit on floor' causes the actor to sit in the containing room


### `dobjFor(StandOn)` *(overridden)*

Defined in travel.t, line 5316

'stand on floor' causes actor to stand in the containing room


### `hideFromDefault(action)` *(overridden)*

Defined in travel.t, line 5173

specifically allow me as a default for STAND ON, SIT ON, and LIE ON


### `iobjFor(PutOn)` *(overridden)*

Defined in travel.t, line 5203

'put x on floor' equals 'drop x'. Add a precondition that the drop destination is the main room, since otherwise we could have strange results if we dropped something inside a nested room.


### `iobjFor(ThrowAt)` *(overridden)*

Defined in travel.t, line 5228

'throw x at floor'


### `isActorOnFloor(actor)`

Defined in travel.t, line 5250

is the given actor already on the floor?


### `isObjListedInRoomPart(obj)` *(overridden)*

Defined in travel.t, line 5192

When explicitly examining a Floor object, list any objects that are listed in the normal room description (as in LOOK AROUND). By default, the floor is the nominal container for anything directly in the room, so we'll normally want LOOK AROUND and LOOK AT FLOOR to produce the same list of objects.


### `performEntry(newPosture)`

Defined in travel.t, line 5302

perform sitting/standing/lying on the floor


### `roomActorHereDesc(actor)`

Defined in travel.t, line 5351

Mention that an actor is here, as part of a room description. When the actor is standing, just say that the actor is here, since it's overstating the obvious to say that the actor is standing on the floor. For other postures, do mention the floor.


### `roomActorPostureDesc(actor)`

Defined in travel.t, line 5389

Show the actor's posture here. When we're standing on the floor, don't mention the posture, as this is too trivial a condition to state. Otherwise, mention it as normal for a nested room.


### `roomActorStatus(actor)`

Defined in travel.t, line 5378

Show our room name status for an actor on the floor. Since standing on the floor is the trivial default for any room, we won't bother mentioning it. Other postures we'll mention the same way we would for any nested room.


### `roomActorThereDesc(actor)` *(overridden)*

Defined in travel.t, line 5370

Mention that an actor is here, as part of a room description. Since a floor is a trivial part of its enclosing room, there's no point in mentioning that we're on the floor, as that's stating the obvious; instead, simply describe the actor as being in the actor's actual enclosing room.


### `roomListActorPosture(actor)`

Defined in travel.t, line 5414

mention the actor as part of the EXAMINE description of a nested room containing the actor


### `roomOkayPostureChange(actor)`

Defined in travel.t, line 5402

Generate an acknowledgment for a posture change here. If the actor is standing, just say "okay, you're now standing" without mentioning the floor, since standing on the floor is the trivial default. For other postures, say that we're sitting/lying/etc on the floor.


### `verifyEntry(newPosture, alreadyMsg)`

Defined in travel.t, line 5260

verify sitting/standing/lying on the floor


## Inherited Methods


*From [RoomPart](roompart.md):* [`dobjFor(Examine)`](roompart.md#dobjFor(Examine)), [`dobjFor(LookIn)`](roompart.md#dobjFor(LookIn)), [`examinePartContents`](roompart.md#examinePartContents), [`examineSpecialContents`](roompart.md#examineSpecialContents), [`examineStatus`](roompart.md#examineStatus), [`filterResolveList`](roompart.md#filterResolveList), [`getHitFallDestination`](roompart.md#getHitFallDestination), [`hideFromAll`](roompart.md#hideFromAll), [`initializeThing`](roompart.md#initializeThing), [`isIn`](roompart.md#isIn), [`moveIntoAdd`](roompart.md#moveIntoAdd), [`moveOutOf`](roompart.md#moveOutOf)


*From [Fixture](fixture.md):* [`dobjFor(Move)`](fixture.md#dobjFor(Move)), [`dobjFor(MoveTo)`](fixture.md#dobjFor(MoveTo)), [`dobjFor(MoveWith)`](fixture.md#dobjFor(MoveWith)), [`dobjFor(Pull)`](fixture.md#dobjFor(Pull)), [`dobjFor(Push)`](fixture.md#dobjFor(Push)), [`dobjFor(PushTravel)`](fixture.md#dobjFor(PushTravel)), [`dobjFor(PutBehind)`](fixture.md#dobjFor(PutBehind)), [`dobjFor(PutIn)`](fixture.md#dobjFor(PutIn)), [`dobjFor(PutOn)`](fixture.md#dobjFor(PutOn)), [`dobjFor(PutUnder)`](fixture.md#dobjFor(PutUnder)), [`dobjFor(Take)`](fixture.md#dobjFor(Take)), [`dobjFor(TakeFrom)`](fixture.md#dobjFor(TakeFrom)), [`dobjFor(ThrowAt)`](fixture.md#dobjFor(ThrowAt)), [`dobjFor(ThrowDir)`](fixture.md#dobjFor(ThrowDir)), [`isOwnedBy`](fixture.md#isOwnedBy), [`verifyMoveTo`](fixture.md#verifyMoveTo)


*From [NonPortable](nonportable.md):* [`contentsInFixedIn`](nonportable.md#contentsInFixedIn), [`dobjFor(ShowTo)`](nonportable.md#dobjFor(ShowTo)), [`isHeldBy`](nonportable.md#isHeldBy), [`meetsObjHeld`](nonportable.md#meetsObjHeld)


<details><summary>From [Thing](thing.md) (408)</summary>

[`acceptCommand`](thing.md#acceptCommand), [`addAllContents`](thing.md#addAllContents), [`addDirectConnections`](thing.md#addDirectConnections), [`addObjectNotifyItem`](thing.md#addObjectNotifyItem), [`addToContents`](thing.md#addToContents), [`addToSenseInfoTable`](thing.md#addToSenseInfoTable), [`adjustLookAroundTable`](thing.md#adjustLookAroundTable), [`adjustThrowDestination`](thing.md#adjustThrowDestination), [`afterAction`](thing.md#afterAction), [`afterTravel`](thing.md#afterTravel), [`allContents`](thing.md#allContents), [`aNameFrom`](thing.md#aNameFrom), [`aNameObj`](thing.md#aNameObj), [`aNameOwnerLoc`](thing.md#aNameOwnerLoc), [`announceDefaultObject`](thing.md#announceDefaultObject), [`appendHeldContents`](thing.md#appendHeldContents), [`atmosphereList`](thing.md#atmosphereList), [`baseMoveInto`](thing.md#baseMoveInto), [`basicExamine`](thing.md#basicExamine), [`basicExamineFeel`](thing.md#basicExamineFeel), [`basicExamineListen`](thing.md#basicExamineListen), [`basicExamineSmell`](thing.md#basicExamineSmell), [`basicExamineTaste`](thing.md#basicExamineTaste), [`beforeAction`](thing.md#beforeAction), [`beforeTravel`](thing.md#beforeTravel), [`buildContainmentPaths`](thing.md#buildContainmentPaths), [`cacheAmbientInfo`](thing.md#cacheAmbientInfo), [`cacheSenseInfo`](thing.md#cacheSenseInfo), [`cacheSensePath`](thing.md#cacheSensePath), [`canBeHeardBy`](thing.md#canBeHeardBy), [`canBeSeenBy`](thing.md#canBeSeenBy), [`canBeSensed`](thing.md#canBeSensed), [`canBeSmelledBy`](thing.md#canBeSmelledBy), [`canBeTouchedBy`](thing.md#canBeTouchedBy), [`canDetailsBeSensed`](thing.md#canDetailsBeSensed), [`canHear`](thing.md#canHear), [`canMatchPronounType`](thing.md#canMatchPronounType), [`canMoveViaPath`](thing.md#canMoveViaPath), [`cannotGoShowExits`](thing.md#cannotGoShowExits), [`cannotReachObject`](thing.md#cannotReachObject), [`cannotSeeSmellSource`](thing.md#cannotSeeSmellSource), [`cannotSeeSoundSource`](thing.md#cannotSeeSoundSource), [`canOwn`](thing.md#canOwn), [`canSee`](thing.md#canSee), [`canSmell`](thing.md#canSmell), [`canThrowViaPath`](thing.md#canThrowViaPath), [`canTouch`](thing.md#canTouch), [`canTouchViaPath`](thing.md#canTouchViaPath), [`checkActorOutOfNested`](thing.md#checkActorOutOfNested), [`checkBulkChange`](thing.md#checkBulkChange), [`checkBulkChangeWithin`](thing.md#checkBulkChangeWithin), [`checkMoveViaPath`](thing.md#checkMoveViaPath), [`checkStagingLocation`](thing.md#checkStagingLocation), [`checkThrowViaPath`](thing.md#checkThrowViaPath), [`checkTouchViaPath`](thing.md#checkTouchViaPath), [`checkTravelerDirectlyInRoom`](thing.md#checkTravelerDirectlyInRoom), [`childInName`](thing.md#childInName), [`childInNameWithOwner`](thing.md#childInNameWithOwner), [`childInRemoteName`](thing.md#childInRemoteName), [`clearSenseInfo`](thing.md#clearSenseInfo), [`cloneForMultiInstanceContents`](thing.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](thing.md#cloneMultiInstanceContents), [`conjugateRegularVerb`](thing.md#conjugateRegularVerb), [`connectionTable`](thing.md#connectionTable), [`construct`](thing.md#construct), [`countDisambigName`](thing.md#countDisambigName), [`countListName`](thing.md#countListName), [`countName`](thing.md#countName), [`countNameFrom`](thing.md#countNameFrom), [`countNameOwnerLoc`](thing.md#countNameOwnerLoc), [`darkRoomContentsLister`](thing.md#darkRoomContentsLister), [`defaultDistantDesc`](thing.md#defaultDistantDesc), [`defaultObscuredDesc`](thing.md#defaultObscuredDesc), [`desc`](thing.md#desc), [`directionForConnector`](thing.md#directionForConnector), [`distantSmellDesc`](thing.md#distantSmellDesc), [`distantSoundDesc`](thing.md#distantSoundDesc), [`dobjFor(AskAbout)`](thing.md#dobjFor(AskAbout)), [`dobjFor(AskFor)`](thing.md#dobjFor(AskFor)), [`dobjFor(AskVague)`](thing.md#dobjFor(AskVague)), [`dobjFor(AttachTo)`](thing.md#dobjFor(AttachTo)), [`dobjFor(Attack)`](thing.md#dobjFor(Attack)), [`dobjFor(AttackWith)`](thing.md#dobjFor(AttackWith)), [`dobjFor(Board)`](thing.md#dobjFor(Board)), [`dobjFor(Break)`](thing.md#dobjFor(Break)), [`dobjFor(Burn)`](thing.md#dobjFor(Burn)), [`dobjFor(BurnWith)`](thing.md#dobjFor(BurnWith)), [`dobjFor(Clean)`](thing.md#dobjFor(Clean)), [`dobjFor(CleanWith)`](thing.md#dobjFor(CleanWith)), [`dobjFor(Climb)`](thing.md#dobjFor(Climb)), [`dobjFor(ClimbDown)`](thing.md#dobjFor(ClimbDown)), [`dobjFor(ClimbUp)`](thing.md#dobjFor(ClimbUp)), [`dobjFor(Close)`](thing.md#dobjFor(Close)), [`dobjFor(Consult)`](thing.md#dobjFor(Consult)), [`dobjFor(ConsultAbout)`](thing.md#dobjFor(ConsultAbout)), [`dobjFor(CutWith)`](thing.md#dobjFor(CutWith)), [`dobjFor(Detach)`](thing.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](thing.md#dobjFor(DetachFrom)), [`dobjFor(Dig)`](thing.md#dobjFor(Dig)), [`dobjFor(DigWith)`](thing.md#dobjFor(DigWith)), [`dobjFor(Doff)`](thing.md#dobjFor(Doff)), [`dobjFor(Drink)`](thing.md#dobjFor(Drink)), [`dobjFor(Drop)`](thing.md#dobjFor(Drop)), [`dobjFor(Eat)`](thing.md#dobjFor(Eat)), [`dobjFor(Enter)`](thing.md#dobjFor(Enter)), [`dobjFor(EnterOn)`](thing.md#dobjFor(EnterOn)), [`dobjFor(Extinguish)`](thing.md#dobjFor(Extinguish)), [`dobjFor(Fasten)`](thing.md#dobjFor(Fasten)), [`dobjFor(FastenTo)`](thing.md#dobjFor(FastenTo)), [`dobjFor(Feel)`](thing.md#dobjFor(Feel)), [`dobjFor(Flip)`](thing.md#dobjFor(Flip)), [`dobjFor(Follow)`](thing.md#dobjFor(Follow)), [`dobjFor(GetOffOf)`](thing.md#dobjFor(GetOffOf)), [`dobjFor(GetOutOf)`](thing.md#dobjFor(GetOutOf)), [`dobjFor(GiveTo)`](thing.md#dobjFor(GiveTo)), [`dobjFor(GoThrough)`](thing.md#dobjFor(GoThrough)), [`dobjFor(JumpOff)`](thing.md#dobjFor(JumpOff)), [`dobjFor(JumpOver)`](thing.md#dobjFor(JumpOver)), [`dobjFor(Kiss)`](thing.md#dobjFor(Kiss)), [`dobjFor(Light)`](thing.md#dobjFor(Light)), [`dobjFor(ListenTo)`](thing.md#dobjFor(ListenTo)), [`dobjFor(Lock)`](thing.md#dobjFor(Lock)), [`dobjFor(LockWith)`](thing.md#dobjFor(LockWith)), [`dobjFor(LookBehind)`](thing.md#dobjFor(LookBehind)), [`dobjFor(LookThrough)`](thing.md#dobjFor(LookThrough)), [`dobjFor(LookUnder)`](thing.md#dobjFor(LookUnder)), [`dobjFor(Open)`](thing.md#dobjFor(Open)), [`dobjFor(PlugIn)`](thing.md#dobjFor(PlugIn)), [`dobjFor(PlugInto)`](thing.md#dobjFor(PlugInto)), [`dobjFor(Pour)`](thing.md#dobjFor(Pour)), [`dobjFor(PourInto)`](thing.md#dobjFor(PourInto)), [`dobjFor(PourOnto)`](thing.md#dobjFor(PourOnto)), [`dobjFor(Read)`](thing.md#dobjFor(Read)), [`dobjFor(Remove)`](thing.md#dobjFor(Remove)), [`dobjFor(Screw)`](thing.md#dobjFor(Screw)), [`dobjFor(ScrewWith)`](thing.md#dobjFor(ScrewWith)), [`dobjFor(Search)`](thing.md#dobjFor(Search)), [`dobjFor(Set)`](thing.md#dobjFor(Set)), [`dobjFor(SetTo)`](thing.md#dobjFor(SetTo)), [`dobjFor(Smell)`](thing.md#dobjFor(Smell)), [`dobjFor(Strike)`](thing.md#dobjFor(Strike)), [`dobjFor(Switch)`](thing.md#dobjFor(Switch)), [`dobjFor(TalkTo)`](thing.md#dobjFor(TalkTo)), [`dobjFor(Taste)`](thing.md#dobjFor(Taste)), [`dobjFor(TellAbout)`](thing.md#dobjFor(TellAbout)), [`dobjFor(TellVague)`](thing.md#dobjFor(TellVague)), [`dobjFor(Throw)`](thing.md#dobjFor(Throw)), [`dobjFor(ThrowTo)`](thing.md#dobjFor(ThrowTo)), [`dobjFor(Turn)`](thing.md#dobjFor(Turn)), [`dobjFor(TurnOff)`](thing.md#dobjFor(TurnOff)), [`dobjFor(TurnOn)`](thing.md#dobjFor(TurnOn)), [`dobjFor(TurnTo)`](thing.md#dobjFor(TurnTo)), [`dobjFor(TurnWith)`](thing.md#dobjFor(TurnWith)), [`dobjFor(TypeLiteralOn)`](thing.md#dobjFor(TypeLiteralOn)), [`dobjFor(TypeOn)`](thing.md#dobjFor(TypeOn)), [`dobjFor(Unfasten)`](thing.md#dobjFor(Unfasten)), [`dobjFor(UnfastenFrom)`](thing.md#dobjFor(UnfastenFrom)), [`dobjFor(Unlock)`](thing.md#dobjFor(Unlock)), [`dobjFor(UnlockWith)`](thing.md#dobjFor(UnlockWith)), [`dobjFor(Unplug)`](thing.md#dobjFor(Unplug)), [`dobjFor(UnplugFrom)`](thing.md#dobjFor(UnplugFrom)), [`dobjFor(Unscrew)`](thing.md#dobjFor(Unscrew)), [`dobjFor(UnscrewWith)`](thing.md#dobjFor(UnscrewWith)), [`dobjFor(Wear)`](thing.md#dobjFor(Wear)), [`examineListContents`](thing.md#examineListContents), [`examineListContentsWith`](thing.md#examineListContentsWith), [`failCheck`](thing.md#failCheck), [`feelDesc`](thing.md#feelDesc), [`fillMedium`](thing.md#fillMedium), [`findOpaqueObstructor`](thing.md#findOpaqueObstructor), [`findTouchObstructor`](thing.md#findTouchObstructor), [`forEachConnectedContainer`](thing.md#forEachConnectedContainer), [`forEachContainer`](thing.md#forEachContainer), [`fromPOV`](thing.md#fromPOV), [`getAllForTakeFrom`](thing.md#getAllForTakeFrom), [`getAllPathsTo`](thing.md#getAllPathsTo), [`getAnnouncementDistinguisher`](thing.md#getAnnouncementDistinguisher), [`getBagAffinities`](thing.md#getBagAffinities), [`getBagsOfHolding`](thing.md#getBagsOfHolding), [`getBestDistinguisher`](thing.md#getBestDistinguisher), [`getBulk`](thing.md#getBulk), [`getBulkWithin`](thing.md#getBulkWithin), [`getCarryingActor`](thing.md#getCarryingActor), [`getCommonContainer`](thing.md#getCommonContainer), [`getCommonDirectContainer`](thing.md#getCommonDirectContainer), [`getConnectedContainers`](thing.md#getConnectedContainers), [`getConnectorTo`](thing.md#getConnectorTo), [`getContentsForExamine`](thing.md#getContentsForExamine), [`getDestName`](thing.md#getDestName), [`getDropDestination`](thing.md#getDropDestination), [`getEncumberingBulk`](thing.md#getEncumberingBulk), [`getEncumberingWeight`](thing.md#getEncumberingWeight), [`getExtraScopeItems`](thing.md#getExtraScopeItems), [`getIdentityObject`](thing.md#getIdentityObject), [`getInScopeDistinguisher`](thing.md#getInScopeDistinguisher), [`getListedContents`](thing.md#getListedContents), [`getLocPushTraveler`](thing.md#getLocPushTraveler), [`getLocTraveler`](thing.md#getLocTraveler), [`getMovePathTo`](thing.md#getMovePathTo), [`getNoise`](thing.md#getNoise), [`getNominalDropDestination`](thing.md#getNominalDropDestination), [`getNominalOwner`](thing.md#getNominalOwner), [`getObjectNotifyList`](thing.md#getObjectNotifyList), [`getOdor`](thing.md#getOdor), [`getOutermostRoom`](thing.md#getOutermostRoom), [`getOutermostVisibleRoom`](thing.md#getOutermostVisibleRoom), [`getRoomNotifyList`](thing.md#getRoomNotifyList), [`getRoomPartLocation`](thing.md#getRoomPartLocation), [`getStateWithInfo`](thing.md#getStateWithInfo), [`getStatuslineExitsHeight`](thing.md#getStatuslineExitsHeight), [`getThrowPathTo`](thing.md#getThrowPathTo), [`getTouchPathTo`](thing.md#getTouchPathTo), [`getTravelConnector`](thing.md#getTravelConnector), [`getVisualSenseInfo`](thing.md#getVisualSenseInfo), [`getWeight`](thing.md#getWeight), [`hasCollectiveGroup`](thing.md#hasCollectiveGroup), [`initializeEquivalent`](thing.md#initializeEquivalent), [`initializeLocation`](thing.md#initializeLocation), [`inRoomName`](thing.md#inRoomName), [`iobjFor(AttachTo)`](thing.md#iobjFor(AttachTo)), [`iobjFor(AttackWith)`](thing.md#iobjFor(AttackWith)), [`iobjFor(BurnWith)`](thing.md#iobjFor(BurnWith)), [`iobjFor(CleanWith)`](thing.md#iobjFor(CleanWith)), [`iobjFor(CutWith)`](thing.md#iobjFor(CutWith)), [`iobjFor(DetachFrom)`](thing.md#iobjFor(DetachFrom)), [`iobjFor(DigWith)`](thing.md#iobjFor(DigWith)), [`iobjFor(FastenTo)`](thing.md#iobjFor(FastenTo)), [`iobjFor(GiveTo)`](thing.md#iobjFor(GiveTo)), [`iobjFor(LockWith)`](thing.md#iobjFor(LockWith)), [`iobjFor(MoveWith)`](thing.md#iobjFor(MoveWith)), [`iobjFor(PlugInto)`](thing.md#iobjFor(PlugInto)), [`iobjFor(PourInto)`](thing.md#iobjFor(PourInto)), [`iobjFor(PourOnto)`](thing.md#iobjFor(PourOnto)), [`iobjFor(PutBehind)`](thing.md#iobjFor(PutBehind)), [`iobjFor(PutIn)`](thing.md#iobjFor(PutIn)), [`iobjFor(PutUnder)`](thing.md#iobjFor(PutUnder)), [`iobjFor(ScrewWith)`](thing.md#iobjFor(ScrewWith)), [`iobjFor(ShowTo)`](thing.md#iobjFor(ShowTo)), [`iobjFor(TakeFrom)`](thing.md#iobjFor(TakeFrom)), [`iobjFor(ThrowTo)`](thing.md#iobjFor(ThrowTo)), [`iobjFor(TurnWith)`](thing.md#iobjFor(TurnWith)), [`iobjFor(UnfastenFrom)`](thing.md#iobjFor(UnfastenFrom)), [`iobjFor(UnlockWith)`](thing.md#iobjFor(UnlockWith)), [`iobjFor(UnplugFrom)`](thing.md#iobjFor(UnplugFrom)), [`iobjFor(UnscrewWith)`](thing.md#iobjFor(UnscrewWith)), [`isActorTravelReady`](thing.md#isActorTravelReady), [`isComponentOf`](thing.md#isComponentOf), [`isDirectlyIn`](thing.md#isDirectlyIn), [`isInFixedIn`](thing.md#isInFixedIn), [`isListed`](thing.md#isListed), [`isListedInContents`](thing.md#isListedInContents), [`isListedInInventory`](thing.md#isListedInInventory), [`isListedInRoomPart`](thing.md#isListedInRoomPart), [`isLookAroundCeiling`](thing.md#isLookAroundCeiling), [`isNominallyIn`](thing.md#isNominallyIn), [`isNominallyInRoomPart`](thing.md#isNominallyInRoomPart), [`isOccludedBy`](thing.md#isOccludedBy), [`isOrIsIn`](thing.md#isOrIsIn), [`isShipboard`](thing.md#isShipboard), [`isVocabEquivalent`](thing.md#isVocabEquivalent), [`itIs`](thing.md#itIs), [`itNom`](thing.md#itNom), [`itObj`](thing.md#itObj), [`itPossAdj`](thing.md#itPossAdj), [`itPossNoun`](thing.md#itPossNoun), [`itVerb`](thing.md#itVerb), [`listCardinality`](thing.md#listCardinality), [`localDirectionLinkForConnector`](thing.md#localDirectionLinkForConnector), [`lookAround`](thing.md#lookAround), [`lookAroundPov`](thing.md#lookAroundPov), [`lookAroundWithin`](thing.md#lookAroundWithin), [`lookAroundWithinContents`](thing.md#lookAroundWithinContents), [`lookAroundWithinDesc`](thing.md#lookAroundWithinDesc), [`lookAroundWithinName`](thing.md#lookAroundWithinName), [`lookAroundWithinSense`](thing.md#lookAroundWithinSense), [`lookAroundWithinShowExits`](thing.md#lookAroundWithinShowExits), [`lookInDesc`](thing.md#lookInDesc), [`mainExamine`](thing.md#mainExamine), [`mainMoveInto`](thing.md#mainMoveInto), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mapPushTravelHandlers`](thing.md#mapPushTravelHandlers), [`mergeSenseInfo`](thing.md#mergeSenseInfo), [`mergeSenseInfoTable`](thing.md#mergeSenseInfoTable), [`moveInto`](thing.md#moveInto), [`moveIntoForTravel`](thing.md#moveIntoForTravel), [`moveIntoNotifyPath`](thing.md#moveIntoNotifyPath), [`mustMoveObjInto`](thing.md#mustMoveObjInto), [`nameIs`](thing.md#nameIs), [`nameIsnt`](thing.md#nameIsnt), [`nameVerb`](thing.md#nameVerb), [`normalizePath`](thing.md#normalizePath), [`notePromptByOwnerLoc`](thing.md#notePromptByOwnerLoc), [`notePromptByPossAdj`](thing.md#notePromptByPossAdj), [`noteSeenBy`](thing.md#noteSeenBy), [`notifyInsert`](thing.md#notifyInsert), [`notifyMoveInto`](thing.md#notifyMoveInto), [`notifyMoveViaPath`](thing.md#notifyMoveViaPath), [`notifyRemove`](thing.md#notifyRemove), [`obscuredDesc`](thing.md#obscuredDesc), [`obscuredSmellDesc`](thing.md#obscuredSmellDesc), [`obscuredSoundDesc`](thing.md#obscuredSoundDesc), [`pluralNameFrom`](thing.md#pluralNameFrom), [`processThrow`](thing.md#processThrow), [`propHidesProp`](thing.md#propHidesProp), [`propWithPresent`](thing.md#propWithPresent), [`putInName`](thing.md#putInName), [`receiveDrop`](thing.md#receiveDrop), [`remoteDesc`](thing.md#remoteDesc), [`remoteInitSpecialDesc`](thing.md#remoteInitSpecialDesc), [`remoteRoomContentsLister`](thing.md#remoteRoomContentsLister), [`remoteSpecialDesc`](thing.md#remoteSpecialDesc), [`removeFromContents`](thing.md#removeFromContents), [`removeObjectNotifyItem`](thing.md#removeObjectNotifyItem), [`restoreLocation`](thing.md#restoreLocation), [`roomContentsLister`](thing.md#roomContentsLister), [`roomDaemon`](thing.md#roomDaemon), [`roomDarkDesc`](thing.md#roomDarkDesc), [`roomDesc`](thing.md#roomDesc), [`roomFirstDesc`](thing.md#roomFirstDesc), [`roomRemoteDesc`](thing.md#roomRemoteDesc), [`roomTravelPreCond`](thing.md#roomTravelPreCond), [`saveLocation`](thing.md#saveLocation), [`selectPathTo`](thing.md#selectPathTo), [`sendNotifyInsert`](thing.md#sendNotifyInsert), [`sendNotifyRemove`](thing.md#sendNotifyRemove), [`senseAmbientMax`](thing.md#senseAmbientMax), [`senseInfoTable`](thing.md#senseInfoTable), [`senseObj`](thing.md#senseObj), [`sensePathFromWithin`](thing.md#sensePathFromWithin), [`sensePathFromWithout`](thing.md#sensePathFromWithout), [`sensePathToContents`](thing.md#sensePathToContents), [`sensePathToLoc`](thing.md#sensePathToLoc), [`sensePresenceList`](thing.md#sensePresenceList), [`setAllSeenBy`](thing.md#setAllSeenBy), [`setContentsSeenBy`](thing.md#setContentsSeenBy), [`setGlobalParamName`](thing.md#setGlobalParamName), [`setVisualSenseInfo`](thing.md#setVisualSenseInfo), [`shineFromWithin`](thing.md#shineFromWithin), [`shineFromWithout`](thing.md#shineFromWithout), [`shineOnContents`](thing.md#shineOnContents), [`shineOnLoc`](thing.md#shineOnLoc), [`showDistantSpecialDesc`](thing.md#showDistantSpecialDesc), [`showDistantSpecialDescInContents`](thing.md#showDistantSpecialDescInContents), [`showInventoryContents`](thing.md#showInventoryContents), [`showInventoryItem`](thing.md#showInventoryItem), [`showInventoryItemCounted`](thing.md#showInventoryItemCounted), [`showListItem`](thing.md#showListItem), [`showListItemCounted`](thing.md#showListItemCounted), [`showListItemCountedGen`](thing.md#showListItemCountedGen), [`showListItemGen`](thing.md#showListItemGen), [`showObjectContents`](thing.md#showObjectContents), [`showObscuredSpecialDesc`](thing.md#showObscuredSpecialDesc), [`showObscuredSpecialDescInContents`](thing.md#showObscuredSpecialDescInContents), [`showRemoteSpecialDesc`](thing.md#showRemoteSpecialDesc), [`showRemoteSpecialDescInContents`](thing.md#showRemoteSpecialDescInContents), [`showSpecialDesc`](thing.md#showSpecialDesc), [`showSpecialDescInContents`](thing.md#showSpecialDescInContents), [`showSpecialDescInContentsWithInfo`](thing.md#showSpecialDescInContentsWithInfo), [`showSpecialDescWithInfo`](thing.md#showSpecialDescWithInfo), [`showStatuslineExits`](thing.md#showStatuslineExits), [`showWornItem`](thing.md#showWornItem), [`showWornItemCounted`](thing.md#showWornItemCounted), [`smellDesc`](thing.md#smellDesc), [`smellHereDesc`](thing.md#smellHereDesc), [`soundDesc`](thing.md#soundDesc), [`soundHereDesc`](thing.md#soundHereDesc), [`specialDescList`](thing.md#specialDescList), [`specialPathFrom`](thing.md#specialPathFrom), [`statusName`](thing.md#statusName), [`stopThrowViaPath`](thing.md#stopThrowViaPath), [`superHidesSuper`](thing.md#superHidesSuper), [`tasteDesc`](thing.md#tasteDesc), [`thatNom`](thing.md#thatNom), [`thatObj`](thing.md#thatObj), [`theNameFrom`](thing.md#theNameFrom), [`theNameObj`](thing.md#theNameObj), [`theNameOwnerLoc`](thing.md#theNameOwnerLoc), [`theNameWithOwner`](thing.md#theNameWithOwner), [`throwTargetCatch`](thing.md#throwTargetCatch), [`throwTargetHitWith`](thing.md#throwTargetHitWith), [`throwViaPath`](thing.md#throwViaPath), [`transmitAmbient`](thing.md#transmitAmbient), [`transSensingIn`](thing.md#transSensingIn), [`transSensingOut`](thing.md#transSensingOut), [`traversePath`](thing.md#traversePath), [`tryHolding`](thing.md#tryHolding), [`tryImplicitRemoveObstructor`](thing.md#tryImplicitRemoveObstructor), [`tryMovingObjInto`](thing.md#tryMovingObjInto), [`useInitDesc`](thing.md#useInitDesc), [`useInitSpecialDesc`](thing.md#useInitSpecialDesc), [`useSpecialDesc`](thing.md#useSpecialDesc), [`useSpecialDescInContents`](thing.md#useSpecialDescInContents), [`useSpecialDescInRoom`](thing.md#useSpecialDescInRoom), [`useSpecialDescInRoomPart`](thing.md#useSpecialDescInRoomPart), [`verbEndingEs`](thing.md#verbEndingEs), [`verbEndingIes`](thing.md#verbEndingIes), [`verbEndingS`](thing.md#verbEndingS), [`verbToHave`](thing.md#verbToHave), [`verbWas`](thing.md#verbWas), [`verifyFollowable`](thing.md#verifyFollowable), [`verifyInsert`](thing.md#verifyInsert), [`verifyRemove`](thing.md#verifyRemove), [`whatIf`](thing.md#whatIf), [`whatIfHeldBy`](thing.md#whatIfHeldBy), [`withVisualSenseInfo`](thing.md#withVisualSenseInfo)

</details>


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
