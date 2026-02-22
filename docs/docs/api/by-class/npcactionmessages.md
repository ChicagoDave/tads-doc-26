# npcActionMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4152)


Non-player character verb messages. By default, we inherit all of the messages defined for the player character, but we override some that must be rephrased slightly to make sense for NPC's.


**Superclass chain:** [playerActionMessages](playeractionmessages.md) > [MessageHelper](messagehelper.md) > `object` > **npcActionMessages**


## Properties


### `alreadyFollowModeMsg`

Defined in msg_neu.t, line 4323

note that we're already in "follow" mode


### `cannotAskSelfForMsg`

Defined in msg_neu.t, line 4344


### `cannotAskSelfMsg`

Defined in msg_neu.t, line 4342


### `cannotGiveToSelfMsg`

Defined in msg_neu.t, line 4348


### `cannotJumpOffHereMsg`

Defined in msg_neu.t, line 4283

cannot jump off (with no direct object) from here


### `cannotMoveFixtureMsg`

Defined in msg_neu.t, line 4157

trying to move a Fixture/Immovable


### `cannotMoveHeavyMsg`

Defined in msg_neu.t, line 4163


### `cannotMoveImmovableMsg`

Defined in msg_neu.t, line 4158


### `cannotPutHeavyMsg`

Defined in msg_neu.t, line 4165


### `cannotShowToSelfMsg`

Defined in msg_neu.t, line 4350


### `cannotTakeHeavyMsg`

Defined in msg_neu.t, line 4161

trying to take/move/put a Heavy object


### `cannotTalkToSelfMsg`

Defined in msg_neu.t, line 4340

the PC's responses to conversational actions applied to oneself need some reworking for NPC's


### `cannotTellSelfMsg`

Defined in msg_neu.t, line 4346


### `keyDoesNotFitLockMsg`

Defined in msg_neu.t, line 4316

the key (iobj) does not fit the lock (dobj)


### `moveNoEffectMsg`

Defined in msg_neu.t, line 4215


### `moveToNoEffectMsg`

Defined in msg_neu.t, line 4217


### `objNotForKeyringMsg`

Defined in msg_neu.t, line 4263

the dobj doesn't fit on this keyring


### `okayAttachToMsg`

Defined in msg_neu.t, line 4329

acknowledge attachment


### `okayCloseMsg`

Defined in msg_neu.t, line 4204


### `okayDetachFromMsg`

Defined in msg_neu.t, line 4333

acknowledge detachment


### `okayDoffMsg`

Defined in msg_neu.t, line 4200

default successful response to 'doff obj'


### `okayDropMsg`

Defined in msg_neu.t, line 4179

default successful 'drop' response


### `okayExtinguishCandleMsg`

Defined in msg_neu.t, line 4326

extinguishing a candle


### `okayFollowModeMsg`

Defined in msg_neu.t, line 4320

acknowledge entering "follow" mode


### `okayLockMsg`

Defined in msg_neu.t, line 4207

default successful responses to lock/unlock


### `okayNotStandingOnMsg`

Defined in msg_neu.t, line 4302

report for getting off a platform


### `okayOpenMsg`

Defined in msg_neu.t, line 4203

default successful responses to open/close


### `okayPushButtonMsg`

Defined in msg_neu.t, line 4309

default 'push button' acknowledgment


### `okayPutBehindMsg`

Defined in msg_neu.t, line 4192

default successful 'put behind' response


### `okayPutInMsg`

Defined in msg_neu.t, line 4182

default successful 'put in' response


### `okayPutOnMsg`

Defined in msg_neu.t, line 4185

default successful 'put on' response


### `okayPutUnderMsg`

Defined in msg_neu.t, line 4188

default successful 'put under' response


### `okayTakeMsg`

Defined in msg_neu.t, line 4176

default successful 'take' response


### `okayTurnOffMsg`

Defined in msg_neu.t, line 4313


### `okayTurnOnMsg`

Defined in msg_neu.t, line 4312

default acknowledgment for switching on/off


### `okayUnlockMsg`

Defined in msg_neu.t, line 4208


### `okayWearMsg`

Defined in msg_neu.t, line 4196

default succesful response to 'wear obj'


### `pullNoEffectMsg`

Defined in msg_neu.t, line 4213


### `pushNoEffectMsg`

Defined in msg_neu.t, line 4211

push/pull/move with no effect


### `shouldNotBreakMsg`

Defined in msg_neu.t, line 4287

should not break object


### `takeFromNotBehindMsg`

Defined in msg_neu.t, line 4279

taking dobj from behind something, but dobj isn't behind iobj


### `takeFromNotInMsg`

Defined in msg_neu.t, line 4267

taking dobj from iobj, but dobj isn't in iobj


### `takeFromNotOnMsg`

Defined in msg_neu.t, line 4271

taking dobj from surface, but dobj isn't on iobj


### `takeFromNotUnderMsg`

Defined in msg_neu.t, line 4275

taking dobj under something, but dobj isn't under iobj


### `timePassesMsg`

Defined in msg_neu.t, line 4154

"wait"


### `whereToGoMsg`

Defined in msg_neu.t, line 4219


## Inherited Properties


*From [playerActionMessages](playeractionmessages.md):* [`alreadyAttachedMsg`](playeractionmessages.md#alreadyAttachedMsg), [`alreadyBurningMsg`](playeractionmessages.md#alreadyBurningMsg), [`alreadyClosedMsg`](playeractionmessages.md#alreadyClosedMsg), [`alreadyHoldingMsg`](playeractionmessages.md#alreadyHoldingMsg), [`alreadyInLocMsg`](playeractionmessages.md#alreadyInLocMsg), [`alreadyLockedMsg`](playeractionmessages.md#alreadyLockedMsg), [`alreadyLyingMsg`](playeractionmessages.md#alreadyLyingMsg), [`alreadyLyingOnMsg`](playeractionmessages.md#alreadyLyingOnMsg), [`alreadyOpenMsg`](playeractionmessages.md#alreadyOpenMsg), [`alreadyPulledMsg`](playeractionmessages.md#alreadyPulledMsg), [`alreadyPushedMsg`](playeractionmessages.md#alreadyPushedMsg), [`alreadyPutBehindMsg`](playeractionmessages.md#alreadyPutBehindMsg), [`alreadyPutInMsg`](playeractionmessages.md#alreadyPutInMsg), [`alreadyPutOnMsg`](playeractionmessages.md#alreadyPutOnMsg), [`alreadyPutUnderMsg`](playeractionmessages.md#alreadyPutUnderMsg), [`alreadySittingMsg`](playeractionmessages.md#alreadySittingMsg), [`alreadySittingOnMsg`](playeractionmessages.md#alreadySittingOnMsg), [`alreadyStandingMsg`](playeractionmessages.md#alreadyStandingMsg), [`alreadyStandingOnMsg`](playeractionmessages.md#alreadyStandingOnMsg), [`alreadySwitchedOffMsg`](playeractionmessages.md#alreadySwitchedOffMsg), [`alreadySwitchedOnMsg`](playeractionmessages.md#alreadySwitchedOnMsg), [`alreadyUnlockedMsg`](playeractionmessages.md#alreadyUnlockedMsg), [`alreadyWearingMsg`](playeractionmessages.md#alreadyWearingMsg), [`askVagueMsg`](playeractionmessages.md#askVagueMsg), [`candleNotLitMsg`](playeractionmessages.md#candleNotLitMsg), [`candleOutOfFuelMsg`](playeractionmessages.md#candleOutOfFuelMsg), [`cannotAttachKeyToMsg`](playeractionmessages.md#cannotAttachKeyToMsg), [`cannotAttachMsg`](playeractionmessages.md#cannotAttachMsg), [`cannotAttachToMsg`](playeractionmessages.md#cannotAttachToMsg), [`cannotAttachToSelfMsg`](playeractionmessages.md#cannotAttachToSelfMsg), [`cannotBoardMsg`](playeractionmessages.md#cannotBoardMsg), [`cannotBurnDobjWithMsg`](playeractionmessages.md#cannotBurnDobjWithMsg), [`cannotBurnMsg`](playeractionmessages.md#cannotBurnMsg), [`cannotBurnWithMsg`](playeractionmessages.md#cannotBurnWithMsg), [`cannotCleanMsg`](playeractionmessages.md#cannotCleanMsg), [`cannotCleanWithMsg`](playeractionmessages.md#cannotCleanWithMsg), [`cannotClimbMsg`](playeractionmessages.md#cannotClimbMsg), [`cannotCloseMsg`](playeractionmessages.md#cannotCloseMsg), [`cannotConsultMsg`](playeractionmessages.md#cannotConsultMsg), [`cannotCutWithMsg`](playeractionmessages.md#cannotCutWithMsg), [`cannotDetachFromMsg`](playeractionmessages.md#cannotDetachFromMsg), [`cannotDetachMsg`](playeractionmessages.md#cannotDetachMsg), [`cannotDetachPermanentMsg`](playeractionmessages.md#cannotDetachPermanentMsg), [`cannotDigMsg`](playeractionmessages.md#cannotDigMsg), [`cannotDigWithMsg`](playeractionmessages.md#cannotDigWithMsg), [`cannotDoFromHereMsg`](playeractionmessages.md#cannotDoFromHereMsg), [`cannotDoThatMsg`](playeractionmessages.md#cannotDoThatMsg), [`cannotDrinkMsg`](playeractionmessages.md#cannotDrinkMsg), [`cannotEatMsg`](playeractionmessages.md#cannotEatMsg), [`cannotEnterHeldMsg`](playeractionmessages.md#cannotEnterHeldMsg), [`cannotEnterMsg`](playeractionmessages.md#cannotEnterMsg), [`cannotEnterOnMsg`](playeractionmessages.md#cannotEnterOnMsg), [`cannotExtinguishMsg`](playeractionmessages.md#cannotExtinguishMsg), [`cannotFastenMsg`](playeractionmessages.md#cannotFastenMsg), [`cannotFastenToMsg`](playeractionmessages.md#cannotFastenToMsg), [`cannotFindTopicMsg`](playeractionmessages.md#cannotFindTopicMsg), [`cannotFlipMsg`](playeractionmessages.md#cannotFlipMsg), [`cannotFollowSelfMsg`](playeractionmessages.md#cannotFollowSelfMsg), [`cannotGetOffOfMsg`](playeractionmessages.md#cannotGetOffOfMsg), [`cannotGetOutMsg`](playeractionmessages.md#cannotGetOutMsg), [`cannotGiveToItselfMsg`](playeractionmessages.md#cannotGiveToItselfMsg), [`cannotGiveToMsg`](playeractionmessages.md#cannotGiveToMsg), [`cannotGoBackMsg`](playeractionmessages.md#cannotGoBackMsg), [`cannotGoThatWayInDarkMsg`](playeractionmessages.md#cannotGoThatWayInDarkMsg), [`cannotGoThatWayMsg`](playeractionmessages.md#cannotGoThatWayMsg), [`cannotGoThroughMsg`](playeractionmessages.md#cannotGoThroughMsg), [`cannotJumpOffMsg`](playeractionmessages.md#cannotJumpOffMsg), [`cannotJumpOverMsg`](playeractionmessages.md#cannotJumpOverMsg), [`cannotKissMsg`](playeractionmessages.md#cannotKissMsg), [`cannotKissSelfMsg`](playeractionmessages.md#cannotKissSelfMsg), [`cannotLieOnMsg`](playeractionmessages.md#cannotLieOnMsg), [`cannotLightMsg`](playeractionmessages.md#cannotLightMsg), [`cannotLockMsg`](playeractionmessages.md#cannotLockMsg), [`cannotLockWithMsg`](playeractionmessages.md#cannotLockWithMsg), [`cannotLookBehindMsg`](playeractionmessages.md#cannotLookBehindMsg), [`cannotLookInClosedMsg`](playeractionmessages.md#cannotLookInClosedMsg), [`cannotLookThroughMsg`](playeractionmessages.md#cannotLookThroughMsg), [`cannotLookUnderMsg`](playeractionmessages.md#cannotLookUnderMsg), [`cannotMoveActorMsg`](playeractionmessages.md#cannotMoveActorMsg), [`cannotMovePersonMsg`](playeractionmessages.md#cannotMovePersonMsg), [`cannotMovePushableMsg`](playeractionmessages.md#cannotMovePushableMsg), [`cannotMoveWithMsg`](playeractionmessages.md#cannotMoveWithMsg), [`cannotOpenLockedMsg`](playeractionmessages.md#cannotOpenLockedMsg), [`cannotOpenMsg`](playeractionmessages.md#cannotOpenMsg), [`cannotPlugInMsg`](playeractionmessages.md#cannotPlugInMsg), [`cannotPlugInToMsg`](playeractionmessages.md#cannotPlugInToMsg), [`cannotPourIntoMsg`](playeractionmessages.md#cannotPourIntoMsg), [`cannotPourMsg`](playeractionmessages.md#cannotPourMsg), [`cannotPourOntoMsg`](playeractionmessages.md#cannotPourOntoMsg), [`cannotPushTravelMsg`](playeractionmessages.md#cannotPushTravelMsg), [`cannotPutActorMsg`](playeractionmessages.md#cannotPutActorMsg), [`cannotPutBehindMsg`](playeractionmessages.md#cannotPutBehindMsg), [`cannotPutBehindRestrictedMsg`](playeractionmessages.md#cannotPutBehindRestrictedMsg), [`cannotPutBehindSelfMsg`](playeractionmessages.md#cannotPutBehindSelfMsg), [`cannotPutFixtureMsg`](playeractionmessages.md#cannotPutFixtureMsg), [`cannotPutImmovableMsg`](playeractionmessages.md#cannotPutImmovableMsg), [`cannotPutInDispenserMsg`](playeractionmessages.md#cannotPutInDispenserMsg), [`cannotPutInRestrictedMsg`](playeractionmessages.md#cannotPutInRestrictedMsg), [`cannotPutInSelfMsg`](playeractionmessages.md#cannotPutInSelfMsg), [`cannotPutOnRestrictedMsg`](playeractionmessages.md#cannotPutOnRestrictedMsg), [`cannotPutOnSelfMsg`](playeractionmessages.md#cannotPutOnSelfMsg), [`cannotPutPersonMsg`](playeractionmessages.md#cannotPutPersonMsg), [`cannotPutPushableMsg`](playeractionmessages.md#cannotPutPushableMsg), [`cannotPutUnderMsg`](playeractionmessages.md#cannotPutUnderMsg), [`cannotPutUnderRestrictedMsg`](playeractionmessages.md#cannotPutUnderRestrictedMsg), [`cannotPutUnderSelfMsg`](playeractionmessages.md#cannotPutUnderSelfMsg), [`cannotRemoveHeldMsg`](playeractionmessages.md#cannotRemoveHeldMsg), [`cannotReturnToDispenserMsg`](playeractionmessages.md#cannotReturnToDispenserMsg), [`cannotScrewMsg`](playeractionmessages.md#cannotScrewMsg), [`cannotScrewWithMsg`](playeractionmessages.md#cannotScrewWithMsg), [`cannotSetToMsg`](playeractionmessages.md#cannotSetToMsg), [`cannotShowToItselfMsg`](playeractionmessages.md#cannotShowToItselfMsg), [`cannotShowToMsg`](playeractionmessages.md#cannotShowToMsg), [`cannotSitOnMsg`](playeractionmessages.md#cannotSitOnMsg), [`cannotSleepMsg`](playeractionmessages.md#cannotSleepMsg), [`cannotStandOnMsg`](playeractionmessages.md#cannotStandOnMsg), [`cannotStandOnPathMsg`](playeractionmessages.md#cannotStandOnPathMsg), [`cannotSwitchMsg`](playeractionmessages.md#cannotSwitchMsg), [`cannotTakeActorMsg`](playeractionmessages.md#cannotTakeActorMsg), [`cannotTakeFixtureMsg`](playeractionmessages.md#cannotTakeFixtureMsg), [`cannotTakeImmovableMsg`](playeractionmessages.md#cannotTakeImmovableMsg), [`cannotTakeLocationMsg`](playeractionmessages.md#cannotTakeLocationMsg), [`cannotTakePersonMsg`](playeractionmessages.md#cannotTakePersonMsg), [`cannotTakePushableMsg`](playeractionmessages.md#cannotTakePushableMsg), [`cannotTasteActorMsg`](playeractionmessages.md#cannotTasteActorMsg), [`cannotTastePersonMsg`](playeractionmessages.md#cannotTastePersonMsg), [`cannotThrowAtContentsMsg`](playeractionmessages.md#cannotThrowAtContentsMsg), [`cannotThrowAtSelfMsg`](playeractionmessages.md#cannotThrowAtSelfMsg), [`cannotThrowToMsg`](playeractionmessages.md#cannotThrowToMsg), [`cannotTurnMsg`](playeractionmessages.md#cannotTurnMsg), [`cannotTurnOffMsg`](playeractionmessages.md#cannotTurnOffMsg), [`cannotTurnOnMsg`](playeractionmessages.md#cannotTurnOnMsg), [`cannotTurnWithMsg`](playeractionmessages.md#cannotTurnWithMsg), [`cannotTypeOnMsg`](playeractionmessages.md#cannotTypeOnMsg), [`cannotUnboardMsg`](playeractionmessages.md#cannotUnboardMsg), [`cannotUnfastenFromMsg`](playeractionmessages.md#cannotUnfastenFromMsg), [`cannotUnfastenMsg`](playeractionmessages.md#cannotUnfastenMsg), [`cannotUnlockMsg`](playeractionmessages.md#cannotUnlockMsg), [`cannotUnlockWithMsg`](playeractionmessages.md#cannotUnlockWithMsg), [`cannotUnplugFromMsg`](playeractionmessages.md#cannotUnplugFromMsg), [`cannotUnplugMsg`](playeractionmessages.md#cannotUnplugMsg), [`cannotUnscrewMsg`](playeractionmessages.md#cannotUnscrewMsg), [`cannotUnscrewWithMsg`](playeractionmessages.md#cannotUnscrewWithMsg), [`cutNoEffectMsg`](playeractionmessages.md#cutNoEffectMsg), [`dontThrowDirMsg`](playeractionmessages.md#dontThrowDirMsg), [`droppingSelfMsg`](playeractionmessages.md#droppingSelfMsg), [`flashlightOnButDarkMsg`](playeractionmessages.md#flashlightOnButDarkMsg), [`followAlreadyHereInDarkMsg`](playeractionmessages.md#followAlreadyHereInDarkMsg), [`followAlreadyHereMsg`](playeractionmessages.md#followAlreadyHereMsg), [`followUnknownMsg`](playeractionmessages.md#followUnknownMsg), [`giveAlreadyHasMsg`](playeractionmessages.md#giveAlreadyHasMsg), [`keyNotDetachableMsg`](playeractionmessages.md#keyNotDetachableMsg), [`keyNotOnKeyringMsg`](playeractionmessages.md#keyNotOnKeyringMsg), [`matchNotLitMsg`](playeractionmessages.md#matchNotLitMsg), [`mustBeStandingMsg`](playeractionmessages.md#mustBeStandingMsg), [`mustSpecifyTurnToMsg`](playeractionmessages.md#mustSpecifyTurnToMsg), [`newlyDarkMsg`](playeractionmessages.md#newlyDarkMsg), [`noKeyNeededMsg`](playeractionmessages.md#noKeyNeededMsg), [`noRoomToLieMsg`](playeractionmessages.md#noRoomToLieMsg), [`noRoomToSitMsg`](playeractionmessages.md#noRoomToSitMsg), [`noRoomToStandMsg`](playeractionmessages.md#noRoomToStandMsg), [`notAContainerMsg`](playeractionmessages.md#notAContainerMsg), [`notASurfaceMsg`](playeractionmessages.md#notASurfaceMsg), [`notAttachedToMsg`](playeractionmessages.md#notAttachedToMsg), [`notAWeaponMsg`](playeractionmessages.md#notAWeaponMsg), [`notCarryingMsg`](playeractionmessages.md#notCarryingMsg), [`notDoffableMsg`](playeractionmessages.md#notDoffableMsg), [`notFollowableMsg`](playeractionmessages.md#notFollowableMsg), [`nothingBehindMsg`](playeractionmessages.md#nothingBehindMsg), [`nothingBeyondDoorMsg`](playeractionmessages.md#nothingBeyondDoorMsg), [`nothingInsideMsg`](playeractionmessages.md#nothingInsideMsg), [`nothingThroughMsg`](playeractionmessages.md#nothingThroughMsg), [`nothingThroughPassageMsg`](playeractionmessages.md#nothingThroughPassageMsg), [`nothingToHearMsg`](playeractionmessages.md#nothingToHearMsg), [`nothingToSmellMsg`](playeractionmessages.md#nothingToSmellMsg), [`nothingUnderMsg`](playeractionmessages.md#nothingUnderMsg), [`notOnPlatformMsg`](playeractionmessages.md#notOnPlatformMsg), [`notWearableMsg`](playeractionmessages.md#notWearableMsg), [`notWearingMsg`](playeractionmessages.md#notWearingMsg), [`okayBurnCandleMsg`](playeractionmessages.md#okayBurnCandleMsg), [`okayBurnMatchMsg`](playeractionmessages.md#okayBurnMatchMsg), [`okayEatMsg`](playeractionmessages.md#okayEatMsg), [`okayExtinguishMatchMsg`](playeractionmessages.md#okayExtinguishMatchMsg), [`okayJumpMsg`](playeractionmessages.md#okayJumpMsg), [`okayPullLeverMsg`](playeractionmessages.md#okayPullLeverMsg), [`okayPullSpringLeverMsg`](playeractionmessages.md#okayPullSpringLeverMsg), [`okayPushLeverMsg`](playeractionmessages.md#okayPushLeverMsg), [`okayYellMsg`](playeractionmessages.md#okayYellMsg), [`puttingSelfMsg`](playeractionmessages.md#puttingSelfMsg), [`sayGoodbyeMsg`](playeractionmessages.md#sayGoodbyeMsg), [`sayHelloMsg`](playeractionmessages.md#sayHelloMsg), [`sayNoMsg`](playeractionmessages.md#sayNoMsg), [`sayYesMsg`](playeractionmessages.md#sayYesMsg), [`setToInvalidMsg`](playeractionmessages.md#setToInvalidMsg), [`shouldNotThrowAtFloorMsg`](playeractionmessages.md#shouldNotThrowAtFloorMsg), [`stairwayNotDownMsg`](playeractionmessages.md#stairwayNotDownMsg), [`stairwayNotUpMsg`](playeractionmessages.md#stairwayNotUpMsg), [`takeFromNotInActorMsg`](playeractionmessages.md#takeFromNotInActorMsg), [`takingSelfMsg`](playeractionmessages.md#takingSelfMsg), [`tellVagueMsg`](playeractionmessages.md#tellVagueMsg), [`throwingSelfMsg`](playeractionmessages.md#throwingSelfMsg), [`tooDarkMsg`](playeractionmessages.md#tooDarkMsg), [`turnToInvalidMsg`](playeractionmessages.md#turnToInvalidMsg), [`unknownHowToLockMsg`](playeractionmessages.md#unknownHowToLockMsg), [`unknownHowToUnlockMsg`](playeractionmessages.md#unknownHowToUnlockMsg), [`unlockRequiresKeyMsg`](playeractionmessages.md#unlockRequiresKeyMsg), [`uselessToAttackMsg`](playeractionmessages.md#uselessToAttackMsg), [`wrongAttachmentMsg`](playeractionmessages.md#wrongAttachmentMsg), [`wrongDetachmentMsg`](playeractionmessages.md#wrongDetachmentMsg)


## Methods


### `cannotMoveComponentMsg(loc)`

Defined in msg_neu.t, line 4169

trying to move a component object


### `containerTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 4247

container doesn't have room for object


### `okayPostureChangeMsg(posture)`

Defined in msg_neu.t, line 4291

report for standing up/sitting down/lying down


### `okayTurnToMsg(val)`

Defined in msg_neu.t, line 4305

default 'turn to' acknowledgment


### `roomOkayPostureChangeMsg(posture, obj)`

Defined in msg_neu.t, line 4295

report for standing/sitting/lying in/on something


### `surfaceTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 4255

surface doesn't have room for object


### `tooLargeForContainerMsg(obj, cont)`

Defined in msg_neu.t, line 4223

object is too large for container


### `tooLargeForRearMsg(obj, cont)`

Defined in msg_neu.t, line 4239

object is too large to fit behind something


### `tooLargeForUndersideMsg(obj, cont)`

Defined in msg_neu.t, line 4231

object is too large for underside


## Inherited Methods


<details><summary>From [playerActionMessages](playeractionmessages.md) (98)</summary>

[`actorCannotSeeMsg`](playeractionmessages.md#actorCannotSeeMsg), [`becomingTooLargeForActorMsg`](playeractionmessages.md#becomingTooLargeForActorMsg), [`becomingTooLargeForContainerMsg`](playeractionmessages.md#becomingTooLargeForContainerMsg), [`cannotBeWearingMsg`](playeractionmessages.md#cannotBeWearingMsg), [`cannotDoFromMsg`](playeractionmessages.md#cannotDoFromMsg), [`cannotEnterExitOnlyMsg`](playeractionmessages.md#cannotEnterExitOnlyMsg), [`cannotFitIntoOpeningMsg`](playeractionmessages.md#cannotFitIntoOpeningMsg), [`cannotFitOutOfOpeningMsg`](playeractionmessages.md#cannotFitOutOfOpeningMsg), [`cannotFollowFromHereMsg`](playeractionmessages.md#cannotFollowFromHereMsg), [`cannotGoThatWayInVehicleMsg`](playeractionmessages.md#cannotGoThatWayInVehicleMsg), [`cannotGoThroughClosedDoorMsg`](playeractionmessages.md#cannotGoThroughClosedDoorMsg), [`cannotHearMsg`](playeractionmessages.md#cannotHearMsg), [`cannotMoveThroughClosedMsg`](playeractionmessages.md#cannotMoveThroughClosedMsg), [`cannotMoveThroughContainerMsg`](playeractionmessages.md#cannotMoveThroughContainerMsg), [`cannotMoveThroughMsg`](playeractionmessages.md#cannotMoveThroughMsg), [`cannotPushObjectNestedMsg`](playeractionmessages.md#cannotPushObjectNestedMsg), [`cannotPushObjectThatWayMsg`](playeractionmessages.md#cannotPushObjectThatWayMsg), [`cannotPutComponentMsg`](playeractionmessages.md#cannotPutComponentMsg), [`cannotReachIntoOpeningMsg`](playeractionmessages.md#cannotReachIntoOpeningMsg), [`cannotReachObjectMsg`](playeractionmessages.md#cannotReachObjectMsg), [`cannotReachOutOfOpeningMsg`](playeractionmessages.md#cannotReachOutOfOpeningMsg), [`cannotReachThroughMsg`](playeractionmessages.md#cannotReachThroughMsg), [`cannotSmellMsg`](playeractionmessages.md#cannotSmellMsg), [`cannotTakeComponentMsg`](playeractionmessages.md#cannotTakeComponentMsg), [`cannotTasteMsg`](playeractionmessages.md#cannotTasteMsg), [`cannotThrowThroughMsg`](playeractionmessages.md#cannotThrowThroughMsg), [`cannotTouchThroughClosedMsg`](playeractionmessages.md#cannotTouchThroughClosedMsg), [`cannotTouchThroughContainerMsg`](playeractionmessages.md#cannotTouchThroughContainerMsg), [`circularlyBehindMsg`](playeractionmessages.md#circularlyBehindMsg), [`circularlyInMsg`](playeractionmessages.md#circularlyInMsg), [`circularlyOnMsg`](playeractionmessages.md#circularlyOnMsg), [`circularlyUnderMsg`](playeractionmessages.md#circularlyUnderMsg), [`containerBecomingTooFullMsg`](playeractionmessages.md#containerBecomingTooFullMsg), [`decorationNotImportantMsg`](playeractionmessages.md#decorationNotImportantMsg), [`doorClosesBehindMsg`](playeractionmessages.md#doorClosesBehindMsg), [`droppingObjMsg`](playeractionmessages.md#droppingObjMsg), [`floorlessDropMsg`](playeractionmessages.md#floorlessDropMsg), [`foundKeyOnKeyringMsg`](playeractionmessages.md#foundKeyOnKeyringMsg), [`foundNoKeyOnKeyringMsg`](playeractionmessages.md#foundNoKeyOnKeyringMsg), [`handsBecomingTooFullForMsg`](playeractionmessages.md#handsBecomingTooFullForMsg), [`handsTooFullForMsg`](playeractionmessages.md#handsTooFullForMsg), [`heardButNotSeenMsg`](playeractionmessages.md#heardButNotSeenMsg), [`invalidStagingContainerActorMsg`](playeractionmessages.md#invalidStagingContainerActorMsg), [`invalidStagingContainerMsg`](playeractionmessages.md#invalidStagingContainerMsg), [`invalidStagingLocationMsg`](playeractionmessages.md#invalidStagingLocationMsg), [`lookInVaporousMsg`](playeractionmessages.md#lookInVaporousMsg), [`movedKeysToKeyringMsg`](playeractionmessages.md#movedKeysToKeyringMsg), [`movedKeyToKeyringMsg`](playeractionmessages.md#movedKeyToKeyringMsg), [`mustBeBurningMsg`](playeractionmessages.md#mustBeBurningMsg), [`mustBeCarryingMsg`](playeractionmessages.md#mustBeCarryingMsg), [`mustBeClosedMsg`](playeractionmessages.md#mustBeClosedMsg), [`mustBeEmptyMsg`](playeractionmessages.md#mustBeEmptyMsg), [`mustBeHoldingMsg`](playeractionmessages.md#mustBeHoldingMsg), [`mustBeInMsg`](playeractionmessages.md#mustBeInMsg), [`mustBeOpenMsg`](playeractionmessages.md#mustBeOpenMsg), [`mustBeUnlockedMsg`](playeractionmessages.md#mustBeUnlockedMsg), [`mustBeVisibleMsg`](playeractionmessages.md#mustBeVisibleMsg), [`mustDetachMsg`](playeractionmessages.md#mustDetachMsg), [`mustGetOnMsg`](playeractionmessages.md#mustGetOnMsg), [`mustLieOnMsg`](playeractionmessages.md#mustLieOnMsg), [`mustOpenDoorMsg`](playeractionmessages.md#mustOpenDoorMsg), [`mustSitOnMsg`](playeractionmessages.md#mustSitOnMsg), [`nestedRoomTooHighMsg`](playeractionmessages.md#nestedRoomTooHighMsg), [`nestedRoomTooHighToExitMsg`](playeractionmessages.md#nestedRoomTooHighToExitMsg), [`noiseSourceMsg`](playeractionmessages.md#noiseSourceMsg), [`noResponseFromMsg`](playeractionmessages.md#noResponseFromMsg), [`notAddressableMsg`](playeractionmessages.md#notAddressableMsg), [`notInterestedMsg`](playeractionmessages.md#notInterestedMsg), [`notWithIntangibleMsg`](playeractionmessages.md#notWithIntangibleMsg), [`notWithVaporousMsg`](playeractionmessages.md#notWithVaporousMsg), [`npcDescMsg`](playeractionmessages.md#npcDescMsg), [`objCannotHearActorMsg`](playeractionmessages.md#objCannotHearActorMsg), [`odorSourceMsg`](playeractionmessages.md#odorSourceMsg), [`okayFollowInSightMsg`](playeractionmessages.md#okayFollowInSightMsg), [`okayPushTravelMsg`](playeractionmessages.md#okayPushTravelMsg), [`okaySetToMsg`](playeractionmessages.md#okaySetToMsg), [`rearTooFullMsg`](playeractionmessages.md#rearTooFullMsg), [`refuseCommand`](playeractionmessages.md#refuseCommand), [`smelledButNotSeenMsg`](playeractionmessages.md#smelledButNotSeenMsg), [`takenAndMovedToKeyringMsg`](playeractionmessages.md#takenAndMovedToKeyringMsg), [`thingDescMsg`](playeractionmessages.md#thingDescMsg), [`thingSmellDescMsg`](playeractionmessages.md#thingSmellDescMsg), [`thingSoundDescMsg`](playeractionmessages.md#thingSoundDescMsg), [`throwCatchMsg`](playeractionmessages.md#throwCatchMsg), [`throwFallMsg`](playeractionmessages.md#throwFallMsg), [`throwFallShortMsg`](playeractionmessages.md#throwFallShortMsg), [`throwHitFallMsg`](playeractionmessages.md#throwHitFallMsg), [`throwHitMsg`](playeractionmessages.md#throwHitMsg), [`throwShortMsg`](playeractionmessages.md#throwShortMsg), [`tooDistantMsg`](playeractionmessages.md#tooDistantMsg), [`tooHeavyForActorMsg`](playeractionmessages.md#tooHeavyForActorMsg), [`tooLargeForActorMsg`](playeractionmessages.md#tooLargeForActorMsg), [`totalTooHeavyForMsg`](playeractionmessages.md#totalTooHeavyForMsg), [`undersideTooFullMsg`](playeractionmessages.md#undersideTooFullMsg), [`unthingNotHereMsg`](playeractionmessages.md#unthingNotHereMsg), [`vehicleCannotDoFromMsg`](playeractionmessages.md#vehicleCannotDoFromMsg), [`willNotCatchMsg`](playeractionmessages.md#willNotCatchMsg), [`willNotLetGoMsg`](playeractionmessages.md#willNotLetGoMsg)

</details>


*From [MessageHelper](messagehelper.md):* [`askDisambigList`](messagehelper.md#askDisambigList), [`shortTIMsg`](messagehelper.md#shortTIMsg), [`shortTMsg`](messagehelper.md#shortTMsg)
