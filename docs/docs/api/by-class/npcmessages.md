# npcMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 2150)


Standard Non-Player Character (NPC) messages. These messages are generated when the player issues a command to a specific non-player character.


**Superclass chain:** [playerMessages](playermessages.md) > [libMessages](libmessages.md) > [MessageHelper](messagehelper.md) > `object` > **npcMessages**


## Inherited Properties


*From [libMessages](libmessages.md):* [`commandFullScore`](libmessages.md#commandFullScore), [`commandInterruptionPrefix`](libmessages.md#commandInterruptionPrefix), [`commandLookAround`](libmessages.md#commandLookAround), [`commandNotPresent`](libmessages.md#commandNotPresent), [`commandResultsEmpty`](libmessages.md#commandResultsEmpty), [`commandResultsPrefix`](libmessages.md#commandResultsPrefix), [`commandResultsSeparator`](libmessages.md#commandResultsSeparator), [`commandResultsSuffix`](libmessages.md#commandResultsSuffix), [`complexResultsSeparator`](libmessages.md#complexResultsSeparator), [`currentlyClosed`](libmessages.md#currentlyClosed), [`currentlyLocked`](libmessages.md#currentlyLocked), [`currentlyNoHints`](libmessages.md#currentlyNoHints), [`currentlyOpen`](libmessages.md#currentlyOpen), [`currentlyUnlocked`](libmessages.md#currentlyUnlocked), [`defaultsFileNotSupported`](libmessages.md#defaultsFileNotSupported), [`defaultsFileWriteError`](libmessages.md#defaultsFileWriteError), [`dlgButtonCancel`](libmessages.md#dlgButtonCancel), [`dlgButtonNo`](libmessages.md#dlgButtonNo), [`dlgButtonOk`](libmessages.md#dlgButtonOk), [`dlgButtonYes`](libmessages.md#dlgButtonYes), [`dlgTitleError`](libmessages.md#dlgTitleError), [`dlgTitleInfo`](libmessages.md#dlgTitleInfo), [`dlgTitleNone`](libmessages.md#dlgTitleNone), [`dlgTitleQuestion`](libmessages.md#dlgTitleQuestion), [`dlgTitleWarning`](libmessages.md#dlgTitleWarning), [`emptyCommandResponse`](libmessages.md#emptyCommandResponse), [`finishDeathMsg`](libmessages.md#finishDeathMsg), [`finishFailureMsg`](libmessages.md#finishFailureMsg), [`finishGameOverMsg`](libmessages.md#finishGameOverMsg), [`finishVictoryMsg`](libmessages.md#finishVictoryMsg), [`getRecordingPrompt`](libmessages.md#getRecordingPrompt), [`getReplayPrompt`](libmessages.md#getReplayPrompt), [`getRestorePrompt`](libmessages.md#getRestorePrompt), [`getSavePrompt`](libmessages.md#getSavePrompt), [`getScriptingPrompt`](libmessages.md#getScriptingPrompt), [`hintsDisabled`](libmessages.md#hintsDisabled), [`hintsDone`](libmessages.md#hintsDone), [`hintsNotPresent`](libmessages.md#hintsNotPresent), [`inputFileScriptWarningButtons`](libmessages.md#inputFileScriptWarningButtons), [`inputScriptFailed`](libmessages.md#inputScriptFailed), [`internalResultsSeparator`](libmessages.md#internalResultsSeparator), [`intraCommandSeparator`](libmessages.md#intraCommandSeparator), [`listSepEnd`](libmessages.md#listSepEnd), [`listSepMiddle`](libmessages.md#listSepMiddle), [`listSepTwo`](libmessages.md#listSepTwo), [`longListSepEnd`](libmessages.md#longListSepEnd), [`longListSepMiddle`](libmessages.md#longListSepMiddle), [`longListSepTwo`](libmessages.md#longListSepTwo), [`menuKeyList`](libmessages.md#menuKeyList), [`menuLongTopicEnd`](libmessages.md#menuLongTopicEnd), [`menuTopicListEnd`](libmessages.md#menuTopicListEnd), [`nextMenuTopicLink`](libmessages.md#nextMenuTopicLink), [`noAboutInfo`](libmessages.md#noAboutInfo), [`noteWithoutScript`](libmessages.md#noteWithoutScript), [`noteWithoutScriptWarning`](libmessages.md#noteWithoutScriptWarning), [`noteWithScript`](libmessages.md#noteWithScript), [`notOnboardShip`](libmessages.md#notOnboardShip), [`noTopicsNotTalking`](libmessages.md#noTopicsNotTalking), [`offerOopsNote`](libmessages.md#offerOopsNote), [`oopsMissingWord`](libmessages.md#oopsMissingWord), [`oopsOutOfContext`](libmessages.md#oopsOutOfContext), [`prevMenuLink`](libmessages.md#prevMenuLink), [`recordingCanceled`](libmessages.md#recordingCanceled), [`recordingFailed`](libmessages.md#recordingFailed), [`recordingOkay`](libmessages.md#recordingOkay), [`recordOffIgnored`](libmessages.md#recordOffIgnored), [`recordOffOkay`](libmessages.md#recordOffOkay), [`replayCanceled`](libmessages.md#replayCanceled), [`roomDarkDesc`](libmessages.md#roomDarkDesc), [`roomDarkName`](libmessages.md#roomDarkName), [`scoreNotPresent`](libmessages.md#scoreNotPresent), [`scriptingCanceled`](libmessages.md#scriptingCanceled), [`scriptingFailed`](libmessages.md#scriptingFailed), [`scriptOffIgnored`](libmessages.md#scriptOffIgnored), [`scriptOffOkay`](libmessages.md#scriptOffOkay), [`settingsItemSeparator`](libmessages.md#settingsItemSeparator), [`showFullScorePrefix`](libmessages.md#showFullScorePrefix), [`showHintWarning`](libmessages.md#showHintWarning), [`sorryHintsDisabled`](libmessages.md#sorryHintsDisabled), [`webUploadTooBig`](libmessages.md#webUploadTooBig), [`whomPronoun`](libmessages.md#whomPronoun)


## Methods


### `ambiguousNounPhrase(actor, originalText, matchList, fullMatchList)`

Defined in msg_neu.t, line 2188

we found an ambiguous noun phrase, but we were unable to perform interactive disambiguation


### `askMissingObject(actor, action, which)`

Defined in msg_neu.t, line 2197

Missing object query and error message templates


### `commandNotHeard(actor)`

Defined in msg_neu.t, line 2152

the target cannot hear a command we gave


### `insufficientQuantity(actor, txt, matchList, requiredNum)`

Defined in msg_neu.t, line 2178

insufficient quantity to meet a command request ('take five books')


### `missingLiteral(actor, action, which)`

Defined in msg_neu.t, line 2211

missing literal phrase query and error message templates


### `missingObject(actor, action, which)`

Defined in msg_neu.t, line 2203


### `noMatchCannotSee(actor, txt)`

Defined in msg_neu.t, line 2158

no match for a noun phrase


### `noMatchForAll(actor)`

Defined in msg_neu.t, line 2164

no match for 'all'


### `noMatchForAllBut(actor)`

Defined in msg_neu.t, line 2171

nothing left for 'all' after removing 'except' items


### `noMatchNotAware(actor, txt)`

Defined in msg_neu.t, line 2160


## Inherited Methods


<details><summary>From [playerMessages](playermessages.md) (28)</summary>

[`allNotAllowed`](playermessages.md#allNotAllowed), [`askDisambig`](playermessages.md#askDisambig), [`askMissingLiteral`](playermessages.md#askMissingLiteral), [`askUnknownWord`](playermessages.md#askUnknownWord), [`cannotAddressMultiple`](playermessages.md#cannotAddressMultiple), [`cannotChangeActor`](playermessages.md#cannotChangeActor), [`commandNotUnderstood`](playermessages.md#commandNotUnderstood), [`disambigOrdinalOutOfRange`](playermessages.md#disambigOrdinalOutOfRange), [`emptyNounPhrase`](playermessages.md#emptyNounPhrase), [`explainCancelCommandLine`](playermessages.md#explainCancelCommandLine), [`missingActor`](playermessages.md#missingActor), [`noMatch`](playermessages.md#noMatch), [`noMatchDisambig`](playermessages.md#noMatchDisambig), [`noMatchForListBut`](playermessages.md#noMatchForListBut), [`noMatchForLocation`](playermessages.md#noMatchForLocation), [`noMatchForPluralPossessive`](playermessages.md#noMatchForPluralPossessive), [`noMatchForPossessive`](playermessages.md#noMatchForPossessive), [`noMatchForPronoun`](playermessages.md#noMatchForPronoun), [`nothingInLocation`](playermessages.md#nothingInLocation), [`reflexiveNotAllowed`](playermessages.md#reflexiveNotAllowed), [`refuseCommandBusy`](playermessages.md#refuseCommandBusy), [`singleActorRequired`](playermessages.md#singleActorRequired), [`singleObjectRequired`](playermessages.md#singleObjectRequired), [`specialTopicInactive`](playermessages.md#specialTopicInactive), [`uniqueObjectRequired`](playermessages.md#uniqueObjectRequired), [`wordIsUnknown`](playermessages.md#wordIsUnknown), [`wrongReflexive`](playermessages.md#wrongReflexive), [`zeroQuantity`](playermessages.md#zeroQuantity)

</details>


<details><summary>From [libMessages](libmessages.md) (167)</summary>

[`acknowledgeFootnoteStatus`](libmessages.md#acknowledgeFootnoteStatus), [`acknowledgeNotifyStatus`](libmessages.md#acknowledgeNotifyStatus), [`acknowledgeTipStatus`](libmessages.md#acknowledgeTipStatus), [`acknowledgeVerboseMode`](libmessages.md#acknowledgeVerboseMode), [`actorHereGroupPrefix`](libmessages.md#actorHereGroupPrefix), [`actorHereGroupSuffix`](libmessages.md#actorHereGroupSuffix), [`actorInGroupPrefix`](libmessages.md#actorInGroupPrefix), [`actorInGroupSuffix`](libmessages.md#actorInGroupSuffix), [`actorInRemoteGroupPrefix`](libmessages.md#actorInRemoteGroupPrefix), [`actorInRemoteGroupSuffix`](libmessages.md#actorInRemoteGroupSuffix), [`actorInRemoteNestedRoom`](libmessages.md#actorInRemoteNestedRoom), [`actorInRemoteRoom`](libmessages.md#actorInRemoteRoom), [`actorInRoom`](libmessages.md#actorInRoom), [`actorInRoomPosture`](libmessages.md#actorInRoomPosture), [`actorInRoomStatus`](libmessages.md#actorInRoomStatus), [`actorThereGroupPrefix`](libmessages.md#actorThereGroupPrefix), [`actorThereGroupSuffix`](libmessages.md#actorThereGroupSuffix), [`againCannotChangeActor`](libmessages.md#againCannotChangeActor), [`againCannotTalkToTarget`](libmessages.md#againCannotTalkToTarget), [`againNotPossible`](libmessages.md#againNotPossible), [`allInSameListState`](libmessages.md#allInSameListState), [`alreadyTalkingTo`](libmessages.md#alreadyTalkingTo), [`announceAmbigActionObject`](libmessages.md#announceAmbigActionObject), [`announceDefaultObject`](libmessages.md#announceDefaultObject), [`announceImplicitAction`](libmessages.md#announceImplicitAction), [`announceMoveToBag`](libmessages.md#announceMoveToBag), [`announceMultiActionObject`](libmessages.md#announceMultiActionObject), [`announceRemappedAction`](libmessages.md#announceRemappedAction), [`basicScoreChange`](libmessages.md#basicScoreChange), [`candleBurnedOut`](libmessages.md#candleBurnedOut), [`cannotReachContents`](libmessages.md#cannotReachContents), [`cannotReachObject`](libmessages.md#cannotReachObject), [`cannotReachOutside`](libmessages.md#cannotReachOutside), [`cannotTalkTo`](libmessages.md#cannotTalkTo), [`closedMsg`](libmessages.md#closedMsg), [`confirmQuit`](libmessages.md#confirmQuit), [`confirmRestart`](libmessages.md#confirmRestart), [`currentExitsSettings`](libmessages.md#currentExitsSettings), [`defaultsFileReadError`](libmessages.md#defaultsFileReadError), [`dimReadDesc`](libmessages.md#dimReadDesc), [`distantThingDesc`](libmessages.md#distantThingDesc), [`distantThingSmellDesc`](libmessages.md#distantThingSmellDesc), [`distantThingSoundDesc`](libmessages.md#distantThingSoundDesc), [`exitsOnOffOkay`](libmessages.md#exitsOnOffOkay), [`explainExitsOnOff`](libmessages.md#explainExitsOnOff), [`filePromptFailed`](libmessages.md#filePromptFailed), [`filePromptFailedMsg`](libmessages.md#filePromptFailedMsg), [`firstFootnote`](libmessages.md#firstFootnote), [`firstScoreChange`](libmessages.md#firstScoreChange), [`footnoteRef`](libmessages.md#footnoteRef), [`fullScoreItemPoints`](libmessages.md#fullScoreItemPoints), [`inputFileScriptWarning`](libmessages.md#inputFileScriptWarning), [`inputScriptFailedException`](libmessages.md#inputScriptFailedException), [`inputScriptOkay`](libmessages.md#inputScriptOkay), [`invalidCommandToken`](libmessages.md#invalidCommandToken), [`invalidFinishOption`](libmessages.md#invalidFinishOption), [`litCandleDesc`](libmessages.md#litCandleDesc), [`litMatchDesc`](libmessages.md#litMatchDesc), [`lockedMsg`](libmessages.md#lockedMsg), [`mainCommandPrompt`](libmessages.md#mainCommandPrompt), [`makeSentence`](libmessages.md#makeSentence), [`matchBurnedOut`](libmessages.md#matchBurnedOut), [`mentionFullScore`](libmessages.md#mentionFullScore), [`menuInstructions`](libmessages.md#menuInstructions), [`menuNextChapter`](libmessages.md#menuNextChapter), [`menuTopicProgress`](libmessages.md#menuTopicProgress), [`noCommandForAgain`](libmessages.md#noCommandForAgain), [`noSuchFootnote`](libmessages.md#noSuchFootnote), [`noteMainRestore`](libmessages.md#noteMainRestore), [`notRestarting`](libmessages.md#notRestarting), [`notTerminating`](libmessages.md#notTerminating), [`objBurnedOut`](libmessages.md#objBurnedOut), [`obscuredReadDesc`](libmessages.md#obscuredReadDesc), [`obscuredThingDesc`](libmessages.md#obscuredThingDesc), [`obscuredThingSmellDesc`](libmessages.md#obscuredThingSmellDesc), [`obscuredThingSoundDesc`](libmessages.md#obscuredThingSoundDesc), [`offMsg`](libmessages.md#offMsg), [`okayQuitting`](libmessages.md#okayQuitting), [`onMsg`](libmessages.md#onMsg), [`oopsNote`](libmessages.md#oopsNote), [`openMsg`](libmessages.md#openMsg), [`openStatusMsg`](libmessages.md#openStatusMsg), [`parserErrorString`](libmessages.md#parserErrorString), [`pauseEnded`](libmessages.md#pauseEnded), [`pausePrompt`](libmessages.md#pausePrompt), [`pauseSaving`](libmessages.md#pauseSaving), [`pcDesc`](libmessages.md#pcDesc), [`putDestBehind`](libmessages.md#putDestBehind), [`putDestContainer`](libmessages.md#putDestContainer), [`putDestFloor`](libmessages.md#putDestFloor), [`putDestRoom`](libmessages.md#putDestRoom), [`putDestSurface`](libmessages.md#putDestSurface), [`putDestUnder`](libmessages.md#putDestUnder), [`recordingFailedException`](libmessages.md#recordingFailedException), [`restoreCanceled`](libmessages.md#restoreCanceled), [`restoreCorruptedFile`](libmessages.md#restoreCorruptedFile), [`restoredDefaults`](libmessages.md#restoredDefaults), [`restoreFailed`](libmessages.md#restoreFailed), [`restoreFailedOnServer`](libmessages.md#restoreFailedOnServer), [`restoreInvalidFile`](libmessages.md#restoreInvalidFile), [`restoreInvalidMatch`](libmessages.md#restoreInvalidMatch), [`restoreOkay`](libmessages.md#restoreOkay), [`roomActorHereDesc`](libmessages.md#roomActorHereDesc), [`roomActorPostureDesc`](libmessages.md#roomActorPostureDesc), [`roomActorStatus`](libmessages.md#roomActorStatus), [`roomActorThereDesc`](libmessages.md#roomActorThereDesc), [`saveCanceled`](libmessages.md#saveCanceled), [`savedDefaults`](libmessages.md#savedDefaults), [`saveFailed`](libmessages.md#saveFailed), [`saveFailedOnServer`](libmessages.md#saveFailedOnServer), [`saveOkay`](libmessages.md#saveOkay), [`sayArriving`](libmessages.md#sayArriving), [`sayArrivingDir`](libmessages.md#sayArrivingDir), [`sayArrivingDownStairs`](libmessages.md#sayArrivingDownStairs), [`sayArrivingLocally`](libmessages.md#sayArrivingLocally), [`sayArrivingShipDir`](libmessages.md#sayArrivingShipDir), [`sayArrivingThroughPassage`](libmessages.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](libmessages.md#sayArrivingUpStairs), [`sayArrivingViaPath`](libmessages.md#sayArrivingViaPath), [`sayDeparting`](libmessages.md#sayDeparting), [`sayDepartingAft`](libmessages.md#sayDepartingAft), [`sayDepartingDir`](libmessages.md#sayDepartingDir), [`sayDepartingDownStairs`](libmessages.md#sayDepartingDownStairs), [`sayDepartingFore`](libmessages.md#sayDepartingFore), [`sayDepartingLocally`](libmessages.md#sayDepartingLocally), [`sayDepartingShipDir`](libmessages.md#sayDepartingShipDir), [`sayDepartingThroughPassage`](libmessages.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](libmessages.md#sayDepartingUpStairs), [`sayDepartingViaPath`](libmessages.md#sayDepartingViaPath), [`sayDepartingWith`](libmessages.md#sayDepartingWith), [`sayDepartingWithGuide`](libmessages.md#sayDepartingWithGuide), [`sayOpenDoorRemotely`](libmessages.md#sayOpenDoorRemotely), [`sayTravelingRemotely`](libmessages.md#sayTravelingRemotely), [`scoreChange`](libmessages.md#scoreChange), [`scriptingFailedException`](libmessages.md#scriptingFailedException), [`scriptingOkay`](libmessages.md#scriptingOkay), [`scriptingOkayWebTemp`](libmessages.md#scriptingOkayWebTemp), [`shortFootnoteStatus`](libmessages.md#shortFootnoteStatus), [`shortNotifyStatus`](libmessages.md#shortNotifyStatus), [`shortVerboseStatus`](libmessages.md#shortVerboseStatus), [`showCredit`](libmessages.md#showCredit), [`showFinishMsg`](libmessages.md#showFinishMsg), [`showFootnoteStatus`](libmessages.md#showFootnoteStatus), [`showListState`](libmessages.md#showListState), [`showNotifyStatus`](libmessages.md#showNotifyStatus), [`showScoreMessage`](libmessages.md#showScoreMessage), [`showScoreNoMaxMessage`](libmessages.md#showScoreNoMaxMessage), [`showScoreRankMessage`](libmessages.md#showScoreRankMessage), [`showVersion`](libmessages.md#showVersion), [`silentImplicitAction`](libmessages.md#silentImplicitAction), [`smellDescSeparator`](libmessages.md#smellDescSeparator), [`smellIsFromWithin`](libmessages.md#smellIsFromWithin), [`smellIsFromWithout`](libmessages.md#smellIsFromWithout), [`soundDescSeparator`](libmessages.md#soundDescSeparator), [`soundIsFromWithin`](libmessages.md#soundIsFromWithin), [`soundIsFromWithout`](libmessages.md#soundIsFromWithout), [`systemActionToNPC`](libmessages.md#systemActionToNPC), [`textMenuMainPrompt`](libmessages.md#textMenuMainPrompt), [`textMenuTopicPrompt`](libmessages.md#textMenuTopicPrompt), [`thingFeelDesc`](libmessages.md#thingFeelDesc), [`thingTasteDesc`](libmessages.md#thingTasteDesc), [`tipStatusShort`](libmessages.md#tipStatusShort), [`undoFailed`](libmessages.md#undoFailed), [`undoOkay`](libmessages.md#undoOkay), [`unlitMatchDesc`](libmessages.md#unlitMatchDesc), [`unlockedMsg`](libmessages.md#unlockedMsg), [`webNewUser`](libmessages.md#webNewUser)

</details>


*From [MessageHelper](messagehelper.md):* [`askDisambigList`](messagehelper.md#askDisambigList), [`shortTIMsg`](messagehelper.md#shortTIMsg), [`shortTMsg`](messagehelper.md#shortTMsg)
