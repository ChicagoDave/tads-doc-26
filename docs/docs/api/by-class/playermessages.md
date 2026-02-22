# playerMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 1758)


Player Character messages. These messages are generated when the player issues a regular command to the player character (i.e., without specifying a target actor).


**Superclass chain:** [libMessages](libmessages.md) > [MessageHelper](messagehelper.md) > `object` > **playerMessages**


## Inherited Properties


*From [libMessages](libmessages.md):* [`commandFullScore`](libmessages.md#commandFullScore), [`commandInterruptionPrefix`](libmessages.md#commandInterruptionPrefix), [`commandLookAround`](libmessages.md#commandLookAround), [`commandNotPresent`](libmessages.md#commandNotPresent), [`commandResultsEmpty`](libmessages.md#commandResultsEmpty), [`commandResultsPrefix`](libmessages.md#commandResultsPrefix), [`commandResultsSeparator`](libmessages.md#commandResultsSeparator), [`commandResultsSuffix`](libmessages.md#commandResultsSuffix), [`complexResultsSeparator`](libmessages.md#complexResultsSeparator), [`currentlyClosed`](libmessages.md#currentlyClosed), [`currentlyLocked`](libmessages.md#currentlyLocked), [`currentlyNoHints`](libmessages.md#currentlyNoHints), [`currentlyOpen`](libmessages.md#currentlyOpen), [`currentlyUnlocked`](libmessages.md#currentlyUnlocked), [`defaultsFileNotSupported`](libmessages.md#defaultsFileNotSupported), [`defaultsFileWriteError`](libmessages.md#defaultsFileWriteError), [`dlgButtonCancel`](libmessages.md#dlgButtonCancel), [`dlgButtonNo`](libmessages.md#dlgButtonNo), [`dlgButtonOk`](libmessages.md#dlgButtonOk), [`dlgButtonYes`](libmessages.md#dlgButtonYes), [`dlgTitleError`](libmessages.md#dlgTitleError), [`dlgTitleInfo`](libmessages.md#dlgTitleInfo), [`dlgTitleNone`](libmessages.md#dlgTitleNone), [`dlgTitleQuestion`](libmessages.md#dlgTitleQuestion), [`dlgTitleWarning`](libmessages.md#dlgTitleWarning), [`emptyCommandResponse`](libmessages.md#emptyCommandResponse), [`finishDeathMsg`](libmessages.md#finishDeathMsg), [`finishFailureMsg`](libmessages.md#finishFailureMsg), [`finishGameOverMsg`](libmessages.md#finishGameOverMsg), [`finishVictoryMsg`](libmessages.md#finishVictoryMsg), [`getRecordingPrompt`](libmessages.md#getRecordingPrompt), [`getReplayPrompt`](libmessages.md#getReplayPrompt), [`getRestorePrompt`](libmessages.md#getRestorePrompt), [`getSavePrompt`](libmessages.md#getSavePrompt), [`getScriptingPrompt`](libmessages.md#getScriptingPrompt), [`hintsDisabled`](libmessages.md#hintsDisabled), [`hintsDone`](libmessages.md#hintsDone), [`hintsNotPresent`](libmessages.md#hintsNotPresent), [`inputFileScriptWarningButtons`](libmessages.md#inputFileScriptWarningButtons), [`inputScriptFailed`](libmessages.md#inputScriptFailed), [`internalResultsSeparator`](libmessages.md#internalResultsSeparator), [`intraCommandSeparator`](libmessages.md#intraCommandSeparator), [`listSepEnd`](libmessages.md#listSepEnd), [`listSepMiddle`](libmessages.md#listSepMiddle), [`listSepTwo`](libmessages.md#listSepTwo), [`longListSepEnd`](libmessages.md#longListSepEnd), [`longListSepMiddle`](libmessages.md#longListSepMiddle), [`longListSepTwo`](libmessages.md#longListSepTwo), [`menuKeyList`](libmessages.md#menuKeyList), [`menuLongTopicEnd`](libmessages.md#menuLongTopicEnd), [`menuTopicListEnd`](libmessages.md#menuTopicListEnd), [`nextMenuTopicLink`](libmessages.md#nextMenuTopicLink), [`noAboutInfo`](libmessages.md#noAboutInfo), [`noteWithoutScript`](libmessages.md#noteWithoutScript), [`noteWithoutScriptWarning`](libmessages.md#noteWithoutScriptWarning), [`noteWithScript`](libmessages.md#noteWithScript), [`notOnboardShip`](libmessages.md#notOnboardShip), [`noTopicsNotTalking`](libmessages.md#noTopicsNotTalking), [`offerOopsNote`](libmessages.md#offerOopsNote), [`oopsMissingWord`](libmessages.md#oopsMissingWord), [`oopsOutOfContext`](libmessages.md#oopsOutOfContext), [`prevMenuLink`](libmessages.md#prevMenuLink), [`recordingCanceled`](libmessages.md#recordingCanceled), [`recordingFailed`](libmessages.md#recordingFailed), [`recordingOkay`](libmessages.md#recordingOkay), [`recordOffIgnored`](libmessages.md#recordOffIgnored), [`recordOffOkay`](libmessages.md#recordOffOkay), [`replayCanceled`](libmessages.md#replayCanceled), [`roomDarkDesc`](libmessages.md#roomDarkDesc), [`roomDarkName`](libmessages.md#roomDarkName), [`scoreNotPresent`](libmessages.md#scoreNotPresent), [`scriptingCanceled`](libmessages.md#scriptingCanceled), [`scriptingFailed`](libmessages.md#scriptingFailed), [`scriptOffIgnored`](libmessages.md#scriptOffIgnored), [`scriptOffOkay`](libmessages.md#scriptOffOkay), [`settingsItemSeparator`](libmessages.md#settingsItemSeparator), [`showFullScorePrefix`](libmessages.md#showFullScorePrefix), [`showHintWarning`](libmessages.md#showHintWarning), [`sorryHintsDisabled`](libmessages.md#sorryHintsDisabled), [`webUploadTooBig`](libmessages.md#webUploadTooBig), [`whomPronoun`](libmessages.md#whomPronoun)


## Methods


### `allNotAllowed(actor)`

Defined in msg_neu.t, line 1793

'all' is not allowed with the attempted action


### `ambiguousNounPhrase(actor, originalText, matchList, fullMatchList)`

Defined in msg_neu.t, line 2057

we found an ambiguous noun phrase, but we were unable to perform interactive disambiguation


### `askDisambig(actor, originalText, matchList, fullMatchList, requiredNum, askingAgain, dist)`

Defined in msg_neu.t, line 1990

Ask the canonical disambiguation question: "Which x do you mean...?". 'matchList' is the list of ambiguous objects with any redundant equivalents removed; and 'fullMatchList' is the full list, including redundant equivalents that were removed from 'matchList'.


### `askMissingLiteral(actor, action, which)`

Defined in msg_neu.t, line 1853

Ask for a missing literal phrase.


### `askMissingObject(actor, action, which)`

Defined in msg_neu.t, line 1826

Ask for a missing object - this is called when a command is completely missing a noun phrase for one of its objects.


### `askUnknownWord(actor, txt)`

Defined in msg_neu.t, line 2087

tell the user they entered a word we don't know, offering the chance to correct it with "oops"


### `cannotAddressMultiple(actor)`

Defined in msg_neu.t, line 2115

cannot speak to multiple actors


### `cannotChangeActor`

Defined in msg_neu.t, line 2077

cannot change actor mid-command


### `commandNotUnderstood(actor)`

Defined in msg_neu.t, line 1760

invalid command syntax


### `disambigOrdinalOutOfRange(actor, ordinalWord, originalText)`

Defined in msg_neu.t, line 1967

The answer to a disambiguation question specifies an invalid ordinal ("the fourth one" when only three choices were offered).


### `emptyNounPhrase(actor)`

Defined in msg_neu.t, line 1927

empty noun phrase ('take the')


### `explainCancelCommandLine`

Defined in msg_neu.t, line 2130

Remaining actions on the command line were aborted due to the failure of the current action. This is just a hook for the game's use, if it wants to provide an explanation; by default, we do nothing. Note that games that override this will probably want to use a flag property so that they only show this message once - it's really only desirable to explain the the mechanism, not to flag it every time it's used.


### `insufficientQuantity(actor, txt, matchList, requiredNum)`

Defined in msg_neu.t, line 1940

insufficient quantity to meet a command request ('take five books')


### `missingActor(actor)`

Defined in msg_neu.t, line 2064

the actor is missing in a command


### `missingLiteral(actor, action, which)`

Defined in msg_neu.t, line 1862

Show the message for a missing literal phrase.


### `missingObject(actor, action, which)`

Defined in msg_neu.t, line 1842

An object was missing - this is called under essentially the same circumstances as askMissingObject, but in cases where interactive resolution is impossible and we simply wish to report the problem and do not wish to ask for help.


### `noMatch(actor, action, txt)`

Defined in msg_neu.t, line 1773

no match for a noun phrase


### `noMatchCannotSee(actor, txt)`

Defined in msg_neu.t, line 1779

No match message - we can't see a match for the noun phrase. This is the default for most verbs.


### `noMatchDisambig(actor, origPhrase, disambigResponse)`

Defined in msg_neu.t, line 1916

no match for the response to a disambiguation question


### `noMatchForAll(actor)`

Defined in msg_neu.t, line 1799

no match for 'all'


### `noMatchForAllBut(actor)`

Defined in msg_neu.t, line 1805

nothing left for 'all' after removing 'except' items


### `noMatchForListBut(actor)`

Defined in msg_neu.t, line 1812

nothing left in a plural phrase after removing 'except' items


### `noMatchForLocation(actor, loc, txt)`

Defined in msg_neu.t, line 1902

no match for a containment phrase


### `noMatchForPluralPossessive(actor, txt)`

Defined in msg_neu.t, line 1895

no match for a plural possessive phrase


### `noMatchForPossessive(actor, owner, txt)`

Defined in msg_neu.t, line 1888

no match for a possessive phrase


### `noMatchForPronoun(actor, typ, pronounWord)`

Defined in msg_neu.t, line 1815

no match for a pronoun


### `noMatchNotAware(actor, txt)`

Defined in msg_neu.t, line 1789

No match message - we're not aware of a match for the noun phrase. Some sensory actions, such as LISTEN TO and SMELL, use this variation instead of the normal version; the things these commands refer to tend to be intangible, so "you can't see that" tends to be nonsensical.


### `nothingInLocation(actor, loc)`

Defined in msg_neu.t, line 1909

nothing in a container whose contents are specifically requested


### `reflexiveNotAllowed(actor, typ, pronounWord)`

Defined in msg_neu.t, line 1871

reflexive pronoun not allowed


### `refuseCommandBusy(targetActor, issuingActor)`

Defined in msg_neu.t, line 2109

the actor refuses the command because it's busy with something else


### `singleActorRequired(actor)`

Defined in msg_neu.t, line 2071

only a single actor can be addressed at a time


### `singleObjectRequired(actor, txt)`

Defined in msg_neu.t, line 1953

a single noun phrase is required, but a noun list was used


### `specialTopicInactive(actor)`

Defined in msg_neu.t, line 1767

a special topic can't be used right now, because it's inactive


### `uniqueObjectRequired(actor, txt, matchList)`

Defined in msg_neu.t, line 1947

a unique object is required, but multiple objects were specified


### `wordIsUnknown(actor, txt)`

Defined in msg_neu.t, line 2102

tell the user they entered a word we don't know, but don't offer an interactive way to fix it (i.e., we can't use OOPS at this point)


### `wrongReflexive(actor, typ, pronounWord)`

Defined in msg_neu.t, line 1881

a reflexive pronoun disagrees in gender, number, or something else with its referent


### `zeroQuantity(actor, txt)`

Defined in msg_neu.t, line 1933

'take zero books'


## Inherited Methods


<details><summary>From [libMessages](libmessages.md) (167)</summary>

[`acknowledgeFootnoteStatus`](libmessages.md#acknowledgeFootnoteStatus), [`acknowledgeNotifyStatus`](libmessages.md#acknowledgeNotifyStatus), [`acknowledgeTipStatus`](libmessages.md#acknowledgeTipStatus), [`acknowledgeVerboseMode`](libmessages.md#acknowledgeVerboseMode), [`actorHereGroupPrefix`](libmessages.md#actorHereGroupPrefix), [`actorHereGroupSuffix`](libmessages.md#actorHereGroupSuffix), [`actorInGroupPrefix`](libmessages.md#actorInGroupPrefix), [`actorInGroupSuffix`](libmessages.md#actorInGroupSuffix), [`actorInRemoteGroupPrefix`](libmessages.md#actorInRemoteGroupPrefix), [`actorInRemoteGroupSuffix`](libmessages.md#actorInRemoteGroupSuffix), [`actorInRemoteNestedRoom`](libmessages.md#actorInRemoteNestedRoom), [`actorInRemoteRoom`](libmessages.md#actorInRemoteRoom), [`actorInRoom`](libmessages.md#actorInRoom), [`actorInRoomPosture`](libmessages.md#actorInRoomPosture), [`actorInRoomStatus`](libmessages.md#actorInRoomStatus), [`actorThereGroupPrefix`](libmessages.md#actorThereGroupPrefix), [`actorThereGroupSuffix`](libmessages.md#actorThereGroupSuffix), [`againCannotChangeActor`](libmessages.md#againCannotChangeActor), [`againCannotTalkToTarget`](libmessages.md#againCannotTalkToTarget), [`againNotPossible`](libmessages.md#againNotPossible), [`allInSameListState`](libmessages.md#allInSameListState), [`alreadyTalkingTo`](libmessages.md#alreadyTalkingTo), [`announceAmbigActionObject`](libmessages.md#announceAmbigActionObject), [`announceDefaultObject`](libmessages.md#announceDefaultObject), [`announceImplicitAction`](libmessages.md#announceImplicitAction), [`announceMoveToBag`](libmessages.md#announceMoveToBag), [`announceMultiActionObject`](libmessages.md#announceMultiActionObject), [`announceRemappedAction`](libmessages.md#announceRemappedAction), [`basicScoreChange`](libmessages.md#basicScoreChange), [`candleBurnedOut`](libmessages.md#candleBurnedOut), [`cannotReachContents`](libmessages.md#cannotReachContents), [`cannotReachObject`](libmessages.md#cannotReachObject), [`cannotReachOutside`](libmessages.md#cannotReachOutside), [`cannotTalkTo`](libmessages.md#cannotTalkTo), [`closedMsg`](libmessages.md#closedMsg), [`confirmQuit`](libmessages.md#confirmQuit), [`confirmRestart`](libmessages.md#confirmRestart), [`currentExitsSettings`](libmessages.md#currentExitsSettings), [`defaultsFileReadError`](libmessages.md#defaultsFileReadError), [`dimReadDesc`](libmessages.md#dimReadDesc), [`distantThingDesc`](libmessages.md#distantThingDesc), [`distantThingSmellDesc`](libmessages.md#distantThingSmellDesc), [`distantThingSoundDesc`](libmessages.md#distantThingSoundDesc), [`exitsOnOffOkay`](libmessages.md#exitsOnOffOkay), [`explainExitsOnOff`](libmessages.md#explainExitsOnOff), [`filePromptFailed`](libmessages.md#filePromptFailed), [`filePromptFailedMsg`](libmessages.md#filePromptFailedMsg), [`firstFootnote`](libmessages.md#firstFootnote), [`firstScoreChange`](libmessages.md#firstScoreChange), [`footnoteRef`](libmessages.md#footnoteRef), [`fullScoreItemPoints`](libmessages.md#fullScoreItemPoints), [`inputFileScriptWarning`](libmessages.md#inputFileScriptWarning), [`inputScriptFailedException`](libmessages.md#inputScriptFailedException), [`inputScriptOkay`](libmessages.md#inputScriptOkay), [`invalidCommandToken`](libmessages.md#invalidCommandToken), [`invalidFinishOption`](libmessages.md#invalidFinishOption), [`litCandleDesc`](libmessages.md#litCandleDesc), [`litMatchDesc`](libmessages.md#litMatchDesc), [`lockedMsg`](libmessages.md#lockedMsg), [`mainCommandPrompt`](libmessages.md#mainCommandPrompt), [`makeSentence`](libmessages.md#makeSentence), [`matchBurnedOut`](libmessages.md#matchBurnedOut), [`mentionFullScore`](libmessages.md#mentionFullScore), [`menuInstructions`](libmessages.md#menuInstructions), [`menuNextChapter`](libmessages.md#menuNextChapter), [`menuTopicProgress`](libmessages.md#menuTopicProgress), [`noCommandForAgain`](libmessages.md#noCommandForAgain), [`noSuchFootnote`](libmessages.md#noSuchFootnote), [`noteMainRestore`](libmessages.md#noteMainRestore), [`notRestarting`](libmessages.md#notRestarting), [`notTerminating`](libmessages.md#notTerminating), [`objBurnedOut`](libmessages.md#objBurnedOut), [`obscuredReadDesc`](libmessages.md#obscuredReadDesc), [`obscuredThingDesc`](libmessages.md#obscuredThingDesc), [`obscuredThingSmellDesc`](libmessages.md#obscuredThingSmellDesc), [`obscuredThingSoundDesc`](libmessages.md#obscuredThingSoundDesc), [`offMsg`](libmessages.md#offMsg), [`okayQuitting`](libmessages.md#okayQuitting), [`onMsg`](libmessages.md#onMsg), [`oopsNote`](libmessages.md#oopsNote), [`openMsg`](libmessages.md#openMsg), [`openStatusMsg`](libmessages.md#openStatusMsg), [`parserErrorString`](libmessages.md#parserErrorString), [`pauseEnded`](libmessages.md#pauseEnded), [`pausePrompt`](libmessages.md#pausePrompt), [`pauseSaving`](libmessages.md#pauseSaving), [`pcDesc`](libmessages.md#pcDesc), [`putDestBehind`](libmessages.md#putDestBehind), [`putDestContainer`](libmessages.md#putDestContainer), [`putDestFloor`](libmessages.md#putDestFloor), [`putDestRoom`](libmessages.md#putDestRoom), [`putDestSurface`](libmessages.md#putDestSurface), [`putDestUnder`](libmessages.md#putDestUnder), [`recordingFailedException`](libmessages.md#recordingFailedException), [`restoreCanceled`](libmessages.md#restoreCanceled), [`restoreCorruptedFile`](libmessages.md#restoreCorruptedFile), [`restoredDefaults`](libmessages.md#restoredDefaults), [`restoreFailed`](libmessages.md#restoreFailed), [`restoreFailedOnServer`](libmessages.md#restoreFailedOnServer), [`restoreInvalidFile`](libmessages.md#restoreInvalidFile), [`restoreInvalidMatch`](libmessages.md#restoreInvalidMatch), [`restoreOkay`](libmessages.md#restoreOkay), [`roomActorHereDesc`](libmessages.md#roomActorHereDesc), [`roomActorPostureDesc`](libmessages.md#roomActorPostureDesc), [`roomActorStatus`](libmessages.md#roomActorStatus), [`roomActorThereDesc`](libmessages.md#roomActorThereDesc), [`saveCanceled`](libmessages.md#saveCanceled), [`savedDefaults`](libmessages.md#savedDefaults), [`saveFailed`](libmessages.md#saveFailed), [`saveFailedOnServer`](libmessages.md#saveFailedOnServer), [`saveOkay`](libmessages.md#saveOkay), [`sayArriving`](libmessages.md#sayArriving), [`sayArrivingDir`](libmessages.md#sayArrivingDir), [`sayArrivingDownStairs`](libmessages.md#sayArrivingDownStairs), [`sayArrivingLocally`](libmessages.md#sayArrivingLocally), [`sayArrivingShipDir`](libmessages.md#sayArrivingShipDir), [`sayArrivingThroughPassage`](libmessages.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](libmessages.md#sayArrivingUpStairs), [`sayArrivingViaPath`](libmessages.md#sayArrivingViaPath), [`sayDeparting`](libmessages.md#sayDeparting), [`sayDepartingAft`](libmessages.md#sayDepartingAft), [`sayDepartingDir`](libmessages.md#sayDepartingDir), [`sayDepartingDownStairs`](libmessages.md#sayDepartingDownStairs), [`sayDepartingFore`](libmessages.md#sayDepartingFore), [`sayDepartingLocally`](libmessages.md#sayDepartingLocally), [`sayDepartingShipDir`](libmessages.md#sayDepartingShipDir), [`sayDepartingThroughPassage`](libmessages.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](libmessages.md#sayDepartingUpStairs), [`sayDepartingViaPath`](libmessages.md#sayDepartingViaPath), [`sayDepartingWith`](libmessages.md#sayDepartingWith), [`sayDepartingWithGuide`](libmessages.md#sayDepartingWithGuide), [`sayOpenDoorRemotely`](libmessages.md#sayOpenDoorRemotely), [`sayTravelingRemotely`](libmessages.md#sayTravelingRemotely), [`scoreChange`](libmessages.md#scoreChange), [`scriptingFailedException`](libmessages.md#scriptingFailedException), [`scriptingOkay`](libmessages.md#scriptingOkay), [`scriptingOkayWebTemp`](libmessages.md#scriptingOkayWebTemp), [`shortFootnoteStatus`](libmessages.md#shortFootnoteStatus), [`shortNotifyStatus`](libmessages.md#shortNotifyStatus), [`shortVerboseStatus`](libmessages.md#shortVerboseStatus), [`showCredit`](libmessages.md#showCredit), [`showFinishMsg`](libmessages.md#showFinishMsg), [`showFootnoteStatus`](libmessages.md#showFootnoteStatus), [`showListState`](libmessages.md#showListState), [`showNotifyStatus`](libmessages.md#showNotifyStatus), [`showScoreMessage`](libmessages.md#showScoreMessage), [`showScoreNoMaxMessage`](libmessages.md#showScoreNoMaxMessage), [`showScoreRankMessage`](libmessages.md#showScoreRankMessage), [`showVersion`](libmessages.md#showVersion), [`silentImplicitAction`](libmessages.md#silentImplicitAction), [`smellDescSeparator`](libmessages.md#smellDescSeparator), [`smellIsFromWithin`](libmessages.md#smellIsFromWithin), [`smellIsFromWithout`](libmessages.md#smellIsFromWithout), [`soundDescSeparator`](libmessages.md#soundDescSeparator), [`soundIsFromWithin`](libmessages.md#soundIsFromWithin), [`soundIsFromWithout`](libmessages.md#soundIsFromWithout), [`systemActionToNPC`](libmessages.md#systemActionToNPC), [`textMenuMainPrompt`](libmessages.md#textMenuMainPrompt), [`textMenuTopicPrompt`](libmessages.md#textMenuTopicPrompt), [`thingFeelDesc`](libmessages.md#thingFeelDesc), [`thingTasteDesc`](libmessages.md#thingTasteDesc), [`tipStatusShort`](libmessages.md#tipStatusShort), [`undoFailed`](libmessages.md#undoFailed), [`undoOkay`](libmessages.md#undoOkay), [`unlitMatchDesc`](libmessages.md#unlitMatchDesc), [`unlockedMsg`](libmessages.md#unlockedMsg), [`webNewUser`](libmessages.md#webNewUser)

</details>


*From [MessageHelper](messagehelper.md):* [`askDisambigList`](messagehelper.md#askDisambigList), [`shortTIMsg`](messagehelper.md#shortTIMsg), [`shortTMsg`](messagehelper.md#shortTMsg)
