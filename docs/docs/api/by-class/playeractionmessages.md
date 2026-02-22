# playerActionMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 2561)


Verb messages for standard library verb implementations for actions performed by the player character. These return strings suitable for use in VerifyResult objects as well as for action reports (defaultReport, mainReport, and so on).


**Superclass chain:** [MessageHelper](messagehelper.md) > `object` > **playerActionMessages**


## Properties


### `alreadyAttachedMsg`

Defined in msg_neu.t, line 3827

cannot attach because we're already attached to the given object


### `alreadyBurningMsg`

Defined in msg_neu.t, line 3804

object is already burning


### `alreadyClosedMsg`

Defined in msg_neu.t, line 3889


### `alreadyHoldingMsg`

Defined in msg_neu.t, line 2877

taking something already being held


### `alreadyInLocMsg`

Defined in msg_neu.t, line 3983

actor is already in a location


### `alreadyLockedMsg`

Defined in msg_neu.t, line 3892

already locked/unlocked


### `alreadyLyingMsg`

Defined in msg_neu.t, line 3990


### `alreadyLyingOnMsg`

Defined in msg_neu.t, line 3991


### `alreadyOpenMsg`

Defined in msg_neu.t, line 3888

already open/closed


### `alreadyPulledMsg`

Defined in msg_neu.t, line 3663

lever is already in pulled state


### `alreadyPushedMsg`

Defined in msg_neu.t, line 3652

lever is already in pushed state


### `alreadyPutBehindMsg`

Defined in msg_neu.t, line 2904

we can't put the dobj behind the iobj because it's already there


### `alreadyPutInMsg`

Defined in msg_neu.t, line 2895

we can't put the dobj in the iobj because it's already there


### `alreadyPutOnMsg`

Defined in msg_neu.t, line 2898

we can't put the dobj on the iobj because it's already there


### `alreadyPutUnderMsg`

Defined in msg_neu.t, line 2901

we can't put the dobj under the iobj because it's already there


### `alreadySittingMsg`

Defined in msg_neu.t, line 3988


### `alreadySittingOnMsg`

Defined in msg_neu.t, line 3989


### `alreadyStandingMsg`

Defined in msg_neu.t, line 3986

actor is already standing/sitting on/lying on


### `alreadyStandingOnMsg`

Defined in msg_neu.t, line 3987


### `alreadySwitchedOffMsg`

Defined in msg_neu.t, line 3725


### `alreadySwitchedOnMsg`

Defined in msg_neu.t, line 3724

switch is already on/off


### `alreadyUnlockedMsg`

Defined in msg_neu.t, line 3893


### `alreadyWearingMsg`

Defined in msg_neu.t, line 2846

already wearing item


### `askVagueMsg`

Defined in msg_neu.t, line 3581

vague ASK/TELL (for ASK/TELL <actor> <topic> syntax errors)


### `candleNotLitMsg`

Defined in msg_neu.t, line 3764

extinguishing a candle that isn't lit


### `candleOutOfFuelMsg`

Defined in msg_neu.t, line 3757

trying to light a candle with no fuel


### `cannotAskSelfForMsg`

Defined in msg_neu.t, line 3547

can't ask yourself for anything


### `cannotAskSelfMsg`

Defined in msg_neu.t, line 3543

can't ask yourself about anything


### `cannotAttachKeyToMsg`

Defined in msg_neu.t, line 3955

cannot attach key (dobj) to (iobj)


### `cannotAttachMsg`

Defined in msg_neu.t, line 3817

cannot attach object to object


### `cannotAttachToMsg`

Defined in msg_neu.t, line 3819


### `cannotAttachToSelfMsg`

Defined in msg_neu.t, line 3823

cannot attach to self


### `cannotBoardMsg`

Defined in msg_neu.t, line 3967


### `cannotBurnDobjWithMsg`

Defined in msg_neu.t, line 3800

cannot burn this specific direct object with this specific iobj


### `cannotBurnMsg`

Defined in msg_neu.t, line 3795

cannot burn


### `cannotBurnWithMsg`

Defined in msg_neu.t, line 3796


### `cannotCleanMsg`

Defined in msg_neu.t, line 3948

cannot clean object


### `cannotCleanWithMsg`

Defined in msg_neu.t, line 3951


### `cannotClimbMsg`

Defined in msg_neu.t, line 3879

cannot climb object


### `cannotCloseMsg`

Defined in msg_neu.t, line 3884


### `cannotConsultMsg`

Defined in msg_neu.t, line 3770

cannot consult object


### `cannotCutWithMsg`

Defined in msg_neu.t, line 3876

can't use iobj to cut anything


### `cannotDetachFromMsg`

Defined in msg_neu.t, line 3857


### `cannotDetachMsg`

Defined in msg_neu.t, line 3856

cannot detach object from object


### `cannotDetachPermanentMsg`

Defined in msg_neu.t, line 3861

no obvious way to detach a permanent attachment


### `cannotDigMsg`

Defined in msg_neu.t, line 2870

cannot dig here


### `cannotDigWithMsg`

Defined in msg_neu.t, line 2873

not a digging implement


### `cannotDoFromHereMsg`

Defined in msg_neu.t, line 3364

cannot carry out a command from this location


### `cannotDoThatMsg`

Defined in msg_neu.t, line 2567

generic "can't do that" message - this is used when verification fails because an object doesn't define the action ("doXxx") method for the verb


### `cannotDrinkMsg`

Defined in msg_neu.t, line 3944


### `cannotEatMsg`

Defined in msg_neu.t, line 3943

not edible/drinkable


### `cannotEnterHeldMsg`

Defined in msg_neu.t, line 3976

cannot sit/lie/stand on something being held


### `cannotEnterMsg`

Defined in msg_neu.t, line 4043

cannot enter/go through


### `cannotEnterOnMsg`

Defined in msg_neu.t, line 3777

cannot enter anything on object


### `cannotExtinguishMsg`

Defined in msg_neu.t, line 3807

cannot extinguish


### `cannotFastenMsg`

Defined in msg_neu.t, line 4019

cannot fasten/unfasten


### `cannotFastenToMsg`

Defined in msg_neu.t, line 4020


### `cannotFindTopicMsg`

Defined in msg_neu.t, line 3511

failed to find a topic in a consultable object


### `cannotFlipMsg`

Defined in msg_neu.t, line 3783

cannot flip object


### `cannotFollowSelfMsg`

Defined in msg_neu.t, line 3604

cannot follow yourself


### `cannotGetOffOfMsg`

Defined in msg_neu.t, line 3969


### `cannotGetOutMsg`

Defined in msg_neu.t, line 3980

cannot get out (of current location)


### `cannotGiveToItselfMsg`

Defined in msg_neu.t, line 3559

can't give something to itself


### `cannotGiveToMsg`

Defined in msg_neu.t, line 3571

can't give/show something to a non-actor


### `cannotGiveToSelfMsg`

Defined in msg_neu.t, line 3555

can't give yourself something


### `cannotGoBackMsg`

Defined in msg_neu.t, line 3360

we don't know the way back for a GO BACK


### `cannotGoThatWayInDarkMsg`

Defined in msg_neu.t, line 3356

travel attempted in the dark in a direction with no exit


### `cannotGoThatWayMsg`

Defined in msg_neu.t, line 3353

travel attempted in a direction with no exit


### `cannotGoThroughMsg`

Defined in msg_neu.t, line 4045


### `cannotJumpOffHereMsg`

Defined in msg_neu.t, line 3507

cannot jump off (with no direct object) from here


### `cannotJumpOffMsg`

Defined in msg_neu.t, line 3504

cannot jump off object


### `cannotJumpOverMsg`

Defined in msg_neu.t, line 3501

cannot jump over object


### `cannotKissMsg`

Defined in msg_neu.t, line 4134

cannot kiss something


### `cannotKissSelfMsg`

Defined in msg_neu.t, line 4141

cannot kiss yourself


### `cannotLieOnMsg`

Defined in msg_neu.t, line 3964


### `cannotLightMsg`

Defined in msg_neu.t, line 3792

cannot light


### `cannotLockMsg`

Defined in msg_neu.t, line 3899

object is not lockable/unlockable


### `cannotLockWithMsg`

Defined in msg_neu.t, line 3912

object is not a key


### `cannotLookBehindMsg`

Defined in msg_neu.t, line 2804

this is an object we can't look behind/through


### `cannotLookInClosedMsg`

Defined in msg_neu.t, line 3896

cannot look in container because it's closed


### `cannotLookThroughMsg`

Defined in msg_neu.t, line 2806


### `cannotLookUnderMsg`

Defined in msg_neu.t, line 2805


### `cannotMoveActorMsg`

Defined in msg_neu.t, line 3006


### `cannotMoveFixtureMsg`

Defined in msg_neu.t, line 2910

trying to move a Fixture to a new container by some means (take, drop, put in, put on, etc)


### `cannotMoveHeavyMsg`

Defined in msg_neu.t, line 2925


### `cannotMoveImmovableMsg`

Defined in msg_neu.t, line 2920


### `cannotMovePersonMsg`

Defined in msg_neu.t, line 3013


### `cannotMovePushableMsg`

Defined in msg_neu.t, line 2951


### `cannotMoveWithMsg`

Defined in msg_neu.t, line 3692

cannot use object as an implement to move something


### `cannotOpenLockedMsg`

Defined in msg_neu.t, line 3905

attempting to open a locked object


### `cannotOpenMsg`

Defined in msg_neu.t, line 3883

object is not openable/closable


### `cannotPlugInMsg`

Defined in msg_neu.t, line 4027

cannot plug/unplug


### `cannotPlugInToMsg`

Defined in msg_neu.t, line 4028


### `cannotPourIntoMsg`

Defined in msg_neu.t, line 3811


### `cannotPourMsg`

Defined in msg_neu.t, line 3810

cannot pour/pour in/pour on


### `cannotPourOntoMsg`

Defined in msg_neu.t, line 3813


### `cannotPushTravelMsg`

Defined in msg_neu.t, line 3682

cannot push an object through travel


### `cannotPutActorMsg`

Defined in msg_neu.t, line 3007


### `cannotPutBehindMsg`

Defined in msg_neu.t, line 3223

nothing can be put behind the given object


### `cannotPutBehindRestrictedMsg`

Defined in msg_neu.t, line 3247


### `cannotPutBehindSelfMsg`

Defined in msg_neu.t, line 3237

trying to put something behind itself


### `cannotPutFixtureMsg`

Defined in msg_neu.t, line 2916

trying to put a Fixture in something


### `cannotPutHeavyMsg`

Defined in msg_neu.t, line 2926


### `cannotPutImmovableMsg`

Defined in msg_neu.t, line 2921


### `cannotPutInDispenserMsg`

Defined in msg_neu.t, line 3255

wrong item type for dispenser


### `cannotPutInRestrictedMsg`

Defined in msg_neu.t, line 3241

can't put something in/on/etc a restricted container/surface/etc


### `cannotPutInSelfMsg`

Defined in msg_neu.t, line 3227

trying to put something in itself


### `cannotPutOnRestrictedMsg`

Defined in msg_neu.t, line 3243


### `cannotPutOnSelfMsg`

Defined in msg_neu.t, line 3230

trying to put something on itself


### `cannotPutPersonMsg`

Defined in msg_neu.t, line 3015


### `cannotPutPushableMsg`

Defined in msg_neu.t, line 2955


### `cannotPutUnderMsg`

Defined in msg_neu.t, line 3219

can't put anything under iobj


### `cannotPutUnderRestrictedMsg`

Defined in msg_neu.t, line 3245


### `cannotPutUnderSelfMsg`

Defined in msg_neu.t, line 3233

trying to put something under itself


### `cannotRemoveHeldMsg`

Defined in msg_neu.t, line 2963

can't REMOVE something that's being held


### `cannotReturnToDispenserMsg`

Defined in msg_neu.t, line 3251

trying to return something to a remove-only dispenser


### `cannotScrewMsg`

Defined in msg_neu.t, line 4035

cannot screw/unscrew


### `cannotScrewWithMsg`

Defined in msg_neu.t, line 4036


### `cannotSetToMsg`

Defined in msg_neu.t, line 3696

cannot set object to setting


### `cannotShowToItselfMsg`

Defined in msg_neu.t, line 3567

can't show something to itself


### `cannotShowToMsg`

Defined in msg_neu.t, line 3572


### `cannotShowToSelfMsg`

Defined in msg_neu.t, line 3563

can't show yourself something


### `cannotSitOnMsg`

Defined in msg_neu.t, line 3962

cannot sit/lie/stand/get on/get out of


### `cannotSleepMsg`

Defined in msg_neu.t, line 3959

actor cannot sleep


### `cannotStandOnMsg`

Defined in msg_neu.t, line 3966


### `cannotStandOnPathMsg`

Defined in msg_neu.t, line 3972

standing on a PathPassage


### `cannotSwitchMsg`

Defined in msg_neu.t, line 3780

cannot switch object


### `cannotTakeActorMsg`

Defined in msg_neu.t, line 3005

try to take/move/put/taste an untakeable actor


### `cannotTakeFixtureMsg`

Defined in msg_neu.t, line 2913

trying to take a Fixture


### `cannotTakeHeavyMsg`

Defined in msg_neu.t, line 2924

trying to take/move/put a Heavy object


### `cannotTakeImmovableMsg`

Defined in msg_neu.t, line 2919

trying to take/move/put an Immovable object


### `cannotTakeLocationMsg`

Defined in msg_neu.t, line 2959

can't take something while occupying it


### `cannotTakePersonMsg`

Defined in msg_neu.t, line 3011

trying to take/move/put/taste a person


### `cannotTakePushableMsg`

Defined in msg_neu.t, line 2949

specialized Immovable messages for TravelPushables


### `cannotTalkToSelfMsg`

Defined in msg_neu.t, line 3539

can't talk to yourself


### `cannotTasteActorMsg`

Defined in msg_neu.t, line 3008


### `cannotTastePersonMsg`

Defined in msg_neu.t, line 3017


### `cannotTellSelfMsg`

Defined in msg_neu.t, line 3551

can't tell yourself about anything


### `cannotThrowAtContentsMsg`

Defined in msg_neu.t, line 4053

can't throw something at an object inside itself


### `cannotThrowAtSelfMsg`

Defined in msg_neu.t, line 4049

can't throw something at itself


### `cannotThrowToMsg`

Defined in msg_neu.t, line 4123

we're not a suitable target for THROW TO (because we're not an NPC)


### `cannotTurnMsg`

Defined in msg_neu.t, line 3706

cannot turn object


### `cannotTurnOffMsg`

Defined in msg_neu.t, line 3788


### `cannotTurnOnMsg`

Defined in msg_neu.t, line 3786

cannot turn object on/off


### `cannotTurnWithMsg`

Defined in msg_neu.t, line 3713

cannot turn anything with object


### `cannotTypeOnMsg`

Defined in msg_neu.t, line 3774

cannot type anything on object


### `cannotUnboardMsg`

Defined in msg_neu.t, line 3968


### `cannotUnfastenFromMsg`

Defined in msg_neu.t, line 4023


### `cannotUnfastenMsg`

Defined in msg_neu.t, line 4022


### `cannotUnlockMsg`

Defined in msg_neu.t, line 3901


### `cannotUnlockWithMsg`

Defined in msg_neu.t, line 3914


### `cannotUnplugFromMsg`

Defined in msg_neu.t, line 4031


### `cannotUnplugMsg`

Defined in msg_neu.t, line 4030


### `cannotUnscrewMsg`

Defined in msg_neu.t, line 4038


### `cannotUnscrewWithMsg`

Defined in msg_neu.t, line 4039


### `cutNoEffectMsg`

Defined in msg_neu.t, line 3873

cannot cut that


### `dontThrowDirMsg`

Defined in msg_neu.t, line 4068

THROW <obj> <direction> isn't supported; use THROW AT instead


### `droppingSelfMsg`

Defined in msg_neu.t, line 2886

actor dropping self


### `flashlightOnButDarkMsg`

Defined in msg_neu.t, line 3732

flashlight is on but doesn't light up


### `followAlreadyHereInDarkMsg`

Defined in msg_neu.t, line 3615

following an object that we *think* is in our same location (in other words, we're already in the location where we thought we last saw the object go), but it's too dark to see if that's really true


### `followAlreadyHereMsg`

Defined in msg_neu.t, line 3607

following an object that's in the same location as the actor


### `followUnknownMsg`

Defined in msg_neu.t, line 3619

trying to follow an object, but don't know where it went from here


### `giveAlreadyHasMsg`

Defined in msg_neu.t, line 3536

trying to give something to someone who already has the object


### `keyDoesNotFitLockMsg`

Defined in msg_neu.t, line 3924

the key (iobj) does not fit the lock (dobj)


### `keyNotDetachableMsg`

Defined in msg_neu.t, line 3266

can't detach key (with no iobj specified) because it's not on a ring


### `keyNotOnKeyringMsg`

Defined in msg_neu.t, line 3263

the dobj isn't on the keyring


### `matchNotLitMsg`

Defined in msg_neu.t, line 3746

match not lit


### `moveNoEffectMsg`

Defined in msg_neu.t, line 3676

moving object has no effect


### `moveToNoEffectMsg`

Defined in msg_neu.t, line 3679

cannot move object to other object


### `mustBeStandingMsg`

Defined in msg_neu.t, line 2667

actor must be standing before doing that


### `mustSpecifyTurnToMsg`

Defined in msg_neu.t, line 3709

must specify setting to turn object to


### `newlyDarkMsg`

Defined in msg_neu.t, line 4144

it is now dark at actor's location


### `noKeyNeededMsg`

Defined in msg_neu.t, line 2664

no key is needed to lock or unlock this object


### `noRoomToLieMsg`

Defined in msg_neu.t, line 4001


### `noRoomToSitMsg`

Defined in msg_neu.t, line 3999


### `noRoomToStandMsg`

Defined in msg_neu.t, line 3997

no room to stand/sit/lie on dobj


### `notAContainerMsg`

Defined in msg_neu.t, line 3212

trying to put an object in a non-container


### `notASurfaceMsg`

Defined in msg_neu.t, line 3215

trying to put an object on a non-surface


### `notAttachedToMsg`

Defined in msg_neu.t, line 3865

dobj isn't attached to iobj


### `notAWeaponMsg`

Defined in msg_neu.t, line 3640

obj is not a weapon


### `notCarryingMsg`

Defined in msg_neu.t, line 2883

dropping an object not being carried


### `notDoffableMsg`

Defined in msg_neu.t, line 2842

doffing something that isn't wearable


### `notFollowableMsg`

Defined in msg_neu.t, line 3601

not a followable object


### `nothingBehindMsg`

Defined in msg_neu.t, line 2798


### `nothingBeyondDoorMsg`

Defined in msg_neu.t, line 2813

there's nothing on the other side of a door we just opened


### `nothingInsideMsg`

Defined in msg_neu.t, line 2794

generic messages for looking prepositionally


### `nothingThroughMsg`

Defined in msg_neu.t, line 2800


### `nothingThroughPassageMsg`

Defined in msg_neu.t, line 2809

looking through an open passage


### `nothingToHearMsg`

Defined in msg_neu.t, line 2821

there's nothing here with a specific noise


### `nothingToSmellMsg`

Defined in msg_neu.t, line 2817

there's nothing here with a specific odor


### `nothingUnderMsg`

Defined in msg_neu.t, line 2796


### `notOnPlatformMsg`

Defined in msg_neu.t, line 3994

getting off something you're not on


### `notWearableMsg`

Defined in msg_neu.t, line 2838

an item is not wearable


### `notWearingMsg`

Defined in msg_neu.t, line 2849

not wearing (item being doffed)


### `objNotForKeyringMsg`

Defined in msg_neu.t, line 3259

the dobj doesn't fit on this keyring


### `okayAttachToMsg`

Defined in msg_neu.t, line 3850

default message for successful Attachable attachment


### `okayBurnCandleMsg`

Defined in msg_neu.t, line 3761

lighting a candle


### `okayBurnMatchMsg`

Defined in msg_neu.t, line 3749

lighting a match


### `okayCloseMsg`

Defined in msg_neu.t, line 2860


### `okayDetachFromMsg`

Defined in msg_neu.t, line 3853

default message for successful Attachable detachment


### `okayDoffMsg`

Defined in msg_neu.t, line 2855

default response to 'doff obj'


### `okayDropMsg`

Defined in msg_neu.t, line 2971

default 'drop' response


### `okayEatMsg`

Defined in msg_neu.t, line 3736

default acknowledgment for eating something


### `okayExtinguishCandleMsg`

Defined in msg_neu.t, line 3767

extinguishing a candle


### `okayExtinguishMatchMsg`

Defined in msg_neu.t, line 3753

extinguishing a match


### `okayJumpMsg`

Defined in msg_neu.t, line 3497

"jump"


### `okayLockMsg`

Defined in msg_neu.t, line 2864

default response to lock/unlock


### `okayNotStandingOnMsg`

Defined in msg_neu.t, line 4016

default report for getting off of a platform


### `okayOpenMsg`

Defined in msg_neu.t, line 2858

default response to open/close


### `okayPullLeverMsg`

Defined in msg_neu.t, line 3667

default acknowledgment to pulling a lever


### `okayPullSpringLeverMsg`

Defined in msg_neu.t, line 3671

default acknowledgment to pulling a spring-loaded lever


### `okayPushButtonMsg`

Defined in msg_neu.t, line 3649

default 'push button' acknowledgment


### `okayPushLeverMsg`

Defined in msg_neu.t, line 3656

default acknowledgment to pushing a lever


### `okayPutBehindMsg`

Defined in msg_neu.t, line 3001

default successful 'put behind' response


### `okayPutInMsg`

Defined in msg_neu.t, line 2989

default successful 'put in' response


### `okayPutOnMsg`

Defined in msg_neu.t, line 2993

default successful 'put on' response


### `okayPutUnderMsg`

Defined in msg_neu.t, line 2997

default successful 'put under' response


### `okayTakeMsg`

Defined in msg_neu.t, line 2967

default 'take' response


### `okayTurnOffMsg`

Defined in msg_neu.t, line 3729


### `okayTurnOnMsg`

Defined in msg_neu.t, line 3728

default acknowledgment for switching on/off


### `okayUnlockMsg`

Defined in msg_neu.t, line 2866


### `okayWearMsg`

Defined in msg_neu.t, line 2852

default response to 'wear obj'


### `okayYellMsg`

Defined in msg_neu.t, line 3494

"yell"


### `pullNoEffectMsg`

Defined in msg_neu.t, line 3660

pulling object has no effect


### `pushNoEffectMsg`

Defined in msg_neu.t, line 3646

pushing object has no effect


### `puttingSelfMsg`

Defined in msg_neu.t, line 2889

actor putting self in something


### `sayGoodbyeMsg`

Defined in msg_neu.t, line 3479

"goodbye" with no target actor


### `sayHelloMsg`

Defined in msg_neu.t, line 3476

"hello" with no target actor


### `sayNoMsg`

Defined in msg_neu.t, line 3483


### `sayYesMsg`

Defined in msg_neu.t, line 3482

"yes"/"no" with no target actor


### `setToInvalidMsg`

Defined in msg_neu.t, line 3699

invalid setting for generic Settable


### `shouldNotBreakMsg`

Defined in msg_neu.t, line 3869

breaking object would serve no purpose


### `shouldNotThrowAtFloorMsg`

Defined in msg_neu.t, line 4064

shouldn't throw something at the floor


### `stairwayNotDownMsg`

Defined in msg_neu.t, line 3470


### `stairwayNotUpMsg`

Defined in msg_neu.t, line 3469

the stairway does not go up/down


### `takeFromNotBehindMsg`

Defined in msg_neu.t, line 3335

taking dobj from behind something, but dobj isn't behind iobj


### `takeFromNotInActorMsg`

Defined in msg_neu.t, line 3339

taking dobj from an actor, but actor doesn't have iobj


### `takeFromNotInMsg`

Defined in msg_neu.t, line 3325

taking dobj from iobj, but dobj isn't in iobj


### `takeFromNotOnMsg`

Defined in msg_neu.t, line 3328

taking dobj from surface, but dobj isn't on iobj


### `takeFromNotUnderMsg`

Defined in msg_neu.t, line 3331

taking dobj from under something, but dobj isn't under iobj


### `takingSelfMsg`

Defined in msg_neu.t, line 2880

actor taking self ("take me")


### `tellVagueMsg`

Defined in msg_neu.t, line 3583


### `throwingSelfMsg`

Defined in msg_neu.t, line 2892

actor throwing self


### `timePassesMsg`

Defined in msg_neu.t, line 3473

"wait"


### `tooDarkMsg`

Defined in msg_neu.t, line 2577

it's too dark to do that


### `turnToInvalidMsg`

Defined in msg_neu.t, line 3717

invalid setting for dial


### `unknownHowToLockMsg`

Defined in msg_neu.t, line 3918

we don't know how to lock/unlock this


### `unknownHowToUnlockMsg`

Defined in msg_neu.t, line 3920


### `unlockRequiresKeyMsg`

Defined in msg_neu.t, line 3908

object requires a key to unlock


### `uselessToAttackMsg`

Defined in msg_neu.t, line 3643

no effect attacking obj


### `whereToGoMsg`

Defined in msg_neu.t, line 3350

must say which way to go


### `wrongAttachmentMsg`

Defined in msg_neu.t, line 3834

dobj and/or iobj can be attached to certain things, but not to each other


### `wrongDetachmentMsg`

Defined in msg_neu.t, line 3838

dobj and iobj are attached, but they can't be taken apart


## Methods


### `actorCannotSeeMsg(actor, obj)`

Defined in msg_neu.t, line 3594

actor cannot see object being shown to actor


### `becomingTooLargeForActorMsg(obj)`

Defined in msg_neu.t, line 3107

the object is becoming too large for the actor to hold


### `becomingTooLargeForContainerMsg(obj, cont)`

Defined in msg_neu.t, line 3193

the current action would make obj too large for its container


### `cannotBeWearingMsg(obj)`

Defined in msg_neu.t, line 2624

must remove an article of clothing before a command


### `cannotDoFromMsg(obj)`

Defined in msg_neu.t, line 3411

cannot carry out a command from a nested room


### `cannotEnterExitOnlyMsg(obj)`

Defined in msg_neu.t, line 3447

cannot enter an exit-only passage


### `cannotFitIntoOpeningMsg(obj, cont)`

Defined in msg_neu.t, line 3045

cannot fit obj into cont through cont's opening


### `cannotFitOutOfOpeningMsg(obj, cont)`

Defined in msg_neu.t, line 3053

cannot fit obj out of cont through cont's opening


### `cannotFollowFromHereMsg(srcLoc)`

Defined in msg_neu.t, line 3626

we're trying to follow an actor, but we last saw the actor in the given other location, so we have to go there to follow


### `cannotGoThatWayInVehicleMsg(traveler)`

Defined in msg_neu.t, line 3426

cannot go that way in a vehicle


### `cannotGoThroughClosedDoorMsg(door)`

Defined in msg_neu.t, line 3367

can't travel through a close door


### `cannotHearMsg(obj)`

Defined in msg_neu.t, line 2603

cannot hear object


### `cannotMoveComponentMsg(loc)`

Defined in msg_neu.t, line 2929

trying to move a component object


### `cannotMoveThroughClosedMsg(obj, cont)`

Defined in msg_neu.t, line 3037

cannot move obj because cont is closed


### `cannotMoveThroughContainerMsg(obj, cont)`

Defined in msg_neu.t, line 3029

cannot move obj in our out of container cont


### `cannotMoveThroughMsg(obj, obs)`

Defined in msg_neu.t, line 3021

cannot move obj through obstructor


### `cannotPushObjectNestedMsg(obj)`

Defined in msg_neu.t, line 3440

cannot push an object to a nested room


### `cannotPushObjectThatWayMsg(obj)`

Defined in msg_neu.t, line 3433

cannot push an object that way


### `cannotPutComponentMsg(loc)`

Defined in msg_neu.t, line 2942

trying to put a component in something


### `cannotReachIntoOpeningMsg(obj, cont)`

Defined in msg_neu.t, line 3077

actor cannot fit hand into cont through cont's opening


### `cannotReachObjectMsg(obj)`

Defined in msg_neu.t, line 2755

cannot reach (i.e., touch) an object that is to be manipulated in a command - this is a generic message used when we cannot identify the specific reason that the object is in scope but cannot be touched


### `cannotReachOutOfOpeningMsg(obj, cont)`

Defined in msg_neu.t, line 3085

actor cannot fit hand into cont through cont's opening


### `cannotReachThroughMsg(obj, loc)`

Defined in msg_neu.t, line 2762

cannot reach an object through an obstructor


### `cannotSmellMsg(obj)`

Defined in msg_neu.t, line 2610

cannot smell object


### `cannotTakeComponentMsg(loc)`

Defined in msg_neu.t, line 2935

trying to take a component object


### `cannotTasteMsg(obj)`

Defined in msg_neu.t, line 2617

cannot taste object


### `cannotThrowThroughMsg(target, loc)`

Defined in msg_neu.t, line 4057

can't throw through a sense connector


### `cannotTouchThroughClosedMsg(obj, cont)`

Defined in msg_neu.t, line 3069

actor 'obj' cannot reach through cont because cont is closed


### `cannotTouchThroughContainerMsg(obj, cont)`

Defined in msg_neu.t, line 3061

actor 'obj' cannot reach in our out of container 'cont'


### `circularlyBehindMsg(x, y)`

Defined in msg_neu.t, line 3317

putting y in x when x is already behind y


### `circularlyInMsg(x, y)`

Defined in msg_neu.t, line 3293

putting y in x when x is already in y


### `circularlyOnMsg(x, y)`

Defined in msg_neu.t, line 3301

putting y in x when x is already on y


### `circularlyUnderMsg(x, y)`

Defined in msg_neu.t, line 3309

putting y in x when x is already under y


### `containerBecomingTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 3204

the current action would increase obj's bulk so that container is too full


### `containerTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 3162

container doesn't have room for object


### `decorationNotImportantMsg(obj)`

Defined in msg_neu.t, line 2708

generic "that's not important" message for decorations


### `doorClosesBehindMsg(obj)`

Defined in msg_neu.t, line 3461

door closes behind actor during travel through door


### `droppingObjMsg(dropobj)`

Defined in msg_neu.t, line 2975

dropping an object


### `floorlessDropMsg(dropobj)`

Defined in msg_neu.t, line 2982

default receiveDrop suffix for floorless rooms


### `foundKeyOnKeyringMsg(ring, key)`

Defined in msg_neu.t, line 3927

found key on keyring


### `foundNoKeyOnKeyringMsg(ring)`

Defined in msg_neu.t, line 3935

failed to find a key on keyring


### `handsBecomingTooFullForMsg(obj)`

Defined in msg_neu.t, line 3115

the object is becoming large enough that the actor's hands are full


### `handsTooFullForMsg(obj)`

Defined in msg_neu.t, line 3100

the actor doesn't have room to hold the object


### `heardButNotSeenMsg(obj)`

Defined in msg_neu.t, line 2587

object can be heard but not seen


### `invalidStagingContainerActorMsg(cont, dest)`

Defined in msg_neu.t, line 3383

cannot carry out travel while 'cont' (an actor) is holding 'dest'


### `invalidStagingContainerMsg(cont, dest)`

Defined in msg_neu.t, line 3375

cannot carry out travel while 'dest' is within 'cont'


### `invalidStagingLocationMsg(dest)`

Defined in msg_neu.t, line 3391

can't carry out travel because 'dest' isn't a valid staging location


### `lookInVaporousMsg(obj)`

Defined in msg_neu.t, line 2743

look in/look under/look through/look behind/search vaporous


### `movedKeysToKeyringMsg(keyring, keys)`

Defined in msg_neu.t, line 3284

we moved several keys to a keyring automatically


### `movedKeyToKeyringMsg(keyring)`

Defined in msg_neu.t, line 3277

we attached a key to a keyring automatically


### `mustBeBurningMsg(obj)`

Defined in msg_neu.t, line 3739

object must be burning before doing that


### `mustBeCarryingMsg(obj, actor)`

Defined in msg_neu.t, line 2700

actor must be holding the object before we can do that


### `mustBeClosedMsg(obj)`

Defined in msg_neu.t, line 2648

object must be closed before doing that


### `mustBeEmptyMsg(obj)`

Defined in msg_neu.t, line 2632

all contents must be removed from object before doing that


### `mustBeHoldingMsg(obj)`

Defined in msg_neu.t, line 2570

must be holding something before a command


### `mustBeInMsg(obj, loc)`

Defined in msg_neu.t, line 2692

object must be in loc before doing that


### `mustBeOpenMsg(obj)`

Defined in msg_neu.t, line 2640

object must be opened before doing that


### `mustBeUnlockedMsg(obj)`

Defined in msg_neu.t, line 2656

object must be unlocked before doing that


### `mustBeVisibleMsg(obj)`

Defined in msg_neu.t, line 2580

object must be visible


### `mustDetachMsg(obj)`

Defined in msg_neu.t, line 3842

must detach the object before proceeding


### `mustGetOnMsg(obj)`

Defined in msg_neu.t, line 2685

must get on/in object


### `mustLieOnMsg(obj)`

Defined in msg_neu.t, line 2678

must be lying on/in object


### `mustOpenDoorMsg(obj)`

Defined in msg_neu.t, line 3454

must open door before going that way


### `mustSitOnMsg(obj)`

Defined in msg_neu.t, line 2671

must be sitting on/in chair


### `nestedRoomTooHighMsg(obj)`

Defined in msg_neu.t, line 3398

destination is too high to enter from here


### `nestedRoomTooHighToExitMsg(obj)`

Defined in msg_neu.t, line 3405

enclosing room is too high to reach by GETTING OUT OF here


### `noiseSourceMsg(src)`

Defined in msg_neu.t, line 2824

a sound appears to be coming from a source


### `noResponseFromMsg(other)`

Defined in msg_neu.t, line 3529

actor won't respond to a request or other communicative gesture


### `notAddressableMsg(obj)`

Defined in msg_neu.t, line 3522

cannot talk to an object (because it makes no sense to do so)


### `notInterestedMsg(actor)`

Defined in msg_neu.t, line 3575

actor isn't interested in something being given/shown


### `notWithIntangibleMsg(obj)`

Defined in msg_neu.t, line 2729

generic "no can do" message for intangibles


### `notWithVaporousMsg(obj)`

Defined in msg_neu.t, line 2736

generic failure message for varporous objects


### `npcDescMsg(npc)`

Defined in msg_neu.t, line 2786

default description of a non-player character


### `objCannotHearActorMsg(obj)`

Defined in msg_neu.t, line 3587

object cannot hear actor


### `odorSourceMsg(src)`

Defined in msg_neu.t, line 2831

an odor appears to be coming from a source


### `okayFollowInSightMsg(loc)`

Defined in msg_neu.t, line 3633

acknowledge a 'follow' for a target that was in sight


### `okayPostureChangeMsg(posture)`

Defined in msg_neu.t, line 4005

default report for standing up/sitting down/lying down


### `okayPushTravelMsg(obj)`

Defined in msg_neu.t, line 3685

acknowledge pushing an object through travel


### `okaySetToMsg(val)`

Defined in msg_neu.t, line 3702

default 'set to' acknowledgment


### `okayTurnToMsg(val)`

Defined in msg_neu.t, line 3720

default 'turn to' acknowledgment


### `rearTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 3185

rear surface/space doesn't have room for object


### `refuseCommand(targetActor, issuingActor)`

Defined in msg_neu.t, line 3515

an actor doesn't accept a command from another actor


### `roomOkayPostureChangeMsg(posture, obj)`

Defined in msg_neu.t, line 4009

default report for standing/sitting/lying in/on something


### `smelledButNotSeenMsg(obj)`

Defined in msg_neu.t, line 2595

object can be smelled but not seen


### `surfaceTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 3169

surface doesn't have room for object


### `takenAndMovedToKeyringMsg(keyring)`

Defined in msg_neu.t, line 3269

we took a key and attached it to a keyring


### `thingDescMsg(obj)`

Defined in msg_neu.t, line 2770

generic long description of a Thing


### `thingSmellDescMsg(obj)`

Defined in msg_neu.t, line 2782

generic "smell" description of a Thing


### `thingSoundDescMsg(obj)`

Defined in msg_neu.t, line 2778

generic LISTEN TO description of a Thing


### `throwCatchMsg(obj, target)`

Defined in msg_neu.t, line 4115

target catches object


### `throwFallMsg(projectile, target)`

Defined in msg_neu.t, line 4083

thrown object lands on target


### `throwFallShortMsg(projectile, target, dest)`

Defined in msg_neu.t, line 4107

thrown object falls short of distant target


### `throwHitFallMsg(projectile, target, dest)`

Defined in msg_neu.t, line 4090

thrown object bounces off target and falls to destination


### `throwHitMsg(projectile, target)`

Defined in msg_neu.t, line 4075

thrown object bounces off target (short report)


### `throwShortMsg(projectile, target)`

Defined in msg_neu.t, line 4099

thrown object falls short of distant target (sentence prefix only)


### `tooDistantMsg(obj)`

Defined in msg_neu.t, line 2722

generic "that's too far away" message for Distant items


### `tooHeavyForActorMsg(obj)`

Defined in msg_neu.t, line 3123

the object is too heavy (all by itself) for the actor to hold


### `tooLargeForActorMsg(obj)`

Defined in msg_neu.t, line 3093

the object is too large for the actor to hold


### `tooLargeForContainerMsg(obj, cont)`

Defined in msg_neu.t, line 3141

object is too large for container


### `tooLargeForRearMsg(obj, cont)`

Defined in msg_neu.t, line 3155

object is too large to fit behind object


### `tooLargeForUndersideMsg(obj, cont)`

Defined in msg_neu.t, line 3148

object is too large to fit under object


### `totalTooHeavyForMsg(obj)`

Defined in msg_neu.t, line 3133

the object is too heavy (in combination with everything else being carried) for the actor to pick up


### `undersideTooFullMsg(obj, cont)`

Defined in msg_neu.t, line 3177

underside doesn't have room for object


### `unthingNotHereMsg(obj)`

Defined in msg_neu.t, line 2715

generic "you don't see that" message for "unthings"


### `vehicleCannotDoFromMsg(obj)`

Defined in msg_neu.t, line 3418

cannot carry out a command from within a vehicle in a nested room


### `willNotCatchMsg(catcher)`

Defined in msg_neu.t, line 4126

target does not want to catch anything


### `willNotLetGoMsg(holder, obj)`

Defined in msg_neu.t, line 3343

actor won't let go of a possession


## Inherited Methods


*From [MessageHelper](messagehelper.md):* [`askDisambigList`](messagehelper.md#askDisambigList), [`shortTIMsg`](messagehelper.md#shortTIMsg), [`shortTMsg`](messagehelper.md#shortTMsg)
