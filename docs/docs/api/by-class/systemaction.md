# SystemAction

*class* — defined in [action.t](../by-file/action.t.md) (line 6612)


System action. These actions are for out-of-game meta-verbs (save, restore, undo). These verbs take no objects, must be performed by the player (thus by the player character, not an NPC), and consume no game clock time.


**Superclass chain:** [IAction](iaction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > **SystemAction**


<details><summary>Subclasses (85)</summary>

- [AboutAction](aboutaction.md)
- [predicate(About)](predicate%28about%29.md)
- [CreditsAction](creditsaction.md)
- [predicate(Credits)](predicate%28credits%29.md)
- [ExitsModeAction](exitsmodeaction.md)
- [predicate(ExitsMode)](predicate%28exitsmode%29.md)
- [FileOpAction](fileopaction.md)
- [RecordAction](recordaction.md)
- [predicate(Record)](predicate%28record%29.md)
- [RecordEventsAction](recordeventsaction.md)
- [predicate(RecordEvents)](predicate%28recordevents%29.md)
- [RecordStringAction](recordstringaction.md)
- [predicate(RecordString)](predicate%28recordstring%29.md)
- [RecordEventsStringAction](recordeventsstringaction.md)
- [predicate(RecordEventsString)](predicate%28recordeventsstring%29.md)
- [ReplayAction](replayaction.md)
- [ReplayStringAction](replaystringaction.md)
- [predicate(ReplayQuiet)](predicate%28replayquiet%29.md)
- [predicate(ReplayString)](predicate%28replaystring%29.md)
- [SaveAction](saveaction.md)
- [predicate(Save)](predicate%28save%29.md)
- [SaveStringAction](savestringaction.md)
- [predicate(SaveString)](predicate%28savestring%29.md)
- [ScriptAction](scriptaction.md)
- [predicate(Script)](predicate%28script%29.md)
- [ScriptStringAction](scriptstringaction.md)
- [predicate(ScriptString)](predicate%28scriptstring%29.md)
- [FootnoteAction](footnoteaction.md)
- [predicate(Footnote)](predicate%28footnote%29.md)
- [FootnotesAction](footnotesaction.md)
- [FootnotesFullAction](footnotesfullaction.md)
- [predicate(FootnotesFull)](predicate%28footnotesfull%29.md)
- [FootnotesMediumAction](footnotesmediumaction.md)
- [predicate(FootnotesMedium)](predicate%28footnotesmedium%29.md)
- [FootnotesOffAction](footnotesoffaction.md)
- [predicate(FootnotesOff)](predicate%28footnotesoff%29.md)
- [FootnotesStatusAction](footnotesstatusaction.md)
- [predicate(FootnotesStatus)](predicate%28footnotesstatus%29.md)
- [FullScoreAction](fullscoreaction.md)
- [predicate(FullScore)](predicate%28fullscore%29.md)
- [HintAction](hintaction.md)
- [predicate(Hint)](predicate%28hint%29.md)
- [HintsOffAction](hintsoffaction.md)
- [predicate(HintsOff)](predicate%28hintsoff%29.md)
- [InstructionsAction](instructionsaction.md)
- [predicate(instructions)](predicate%28instructions%29.md)
- [NotifyAction](notifyaction.md)
- [predicate(Notify)](predicate%28notify%29.md)
- [NotifyOffAction](notifyoffaction.md)
- [predicate(NotifyOff)](predicate%28notifyoff%29.md)
- [NotifyOnAction](notifyonaction.md)
- [predicate(NotifyOn)](predicate%28notifyon%29.md)
- [PauseAction](pauseaction.md)
- [predicate(Pause)](predicate%28pause%29.md)
- [QuitAction](quitaction.md)
- [predicate(Quit)](predicate%28quit%29.md)
- [RecordOffAction](recordoffaction.md)
- [predicate(RecordOff)](predicate%28recordoff%29.md)
- [RestartAction](restartaction.md)
- [predicate(Restart)](predicate%28restart%29.md)
- [RestoreAction](restoreaction.md)
- [predicate(Restore)](predicate%28restore%29.md)
- [RestoreStringAction](restorestringaction.md)
- [predicate(RestoreString)](predicate%28restorestring%29.md)
- [RestoreDefaultsAction](restoredefaultsaction.md)
- [predicate(RestoreDefaults)](predicate%28restoredefaults%29.md)
- [SaveDefaultsAction](savedefaultsaction.md)
- [predicate(SaveDefaults)](predicate%28savedefaults%29.md)
- [ScoreAction](scoreaction.md)
- [predicate(Score)](predicate%28score%29.md)
- [ScriptOffAction](scriptoffaction.md)
- [predicate(ScriptOff)](predicate%28scriptoff%29.md)
- [TerseAction](terseaction.md)
- [predicate(Terse)](predicate%28terse%29.md)
- [TipModeAction](tipmodeaction.md)
- [predicate(TipsOff)](predicate%28tipsoff%29.md)
- [predicate(TipsOn)](predicate%28tipson%29.md)
- [TopicsAction](topicsaction.md)
- [predicate(Topics)](predicate%28topics%29.md)
- [UndoAction](undoaction.md)
- [predicate(Undo)](predicate%28undo%29.md)
- [VerboseAction](verboseaction.md)
- [predicate(Verbose)](predicate%28verbose%29.md)
- [VersionAction](versionaction.md)
- [predicate(Version)](predicate%28version%29.md)

</details>


## Properties


### `actionTime` *(overridden)*

Defined in action.t, line 6661

system actions consume no game time


## Inherited Properties


*From [Action](action.md):* [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`predicateNounPhrases`](action.md#predicateNounPhrases), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execAction` *(overridden)*

Defined in action.t, line 6614

execute the action


### `execSystemAction`

Defined in action.t, line 6648

each subclass must override this to perform its actual action


### `getInputFile(prompt, dialogType, fileType, flags)`

Defined in action.t, line 6655

Ask for an input file. We call the input manager, which freezes the real-time clock, displays the appropriate local file selector dialog, and restarts the clock.


## Inherited Methods


*From [IAction](iaction.md):* [`doActionMain`](iaction.md#doActionMain), [`resolveNouns`](iaction.md#resolveNouns)


<details><summary>From [Action](action.md) (100)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`announceAllDefaultObjects`](action.md#announceAllDefaultObjects), [`announceDefaultObject`](action.md#announceDefaultObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkAction`](action.md#checkAction), [`checkPreConditions`](action.md#checkPreConditions), [`checkRemapping`](action.md#checkRemapping), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getCurrentObjects`](action.md#getCurrentObjects), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getMatchForRole`](action.md#getMatchForRole), [`getMessageParam`](action.md#getMessageParam), [`getNotifyTable`](action.md#getNotifyTable), [`getObjectForRole`](action.md#getObjectForRole), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getObjResponseProd`](action.md#getObjResponseProd), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getOtherObjectRole`](action.md#getOtherObjectRole), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPreCondDescList`](action.md#getPreCondDescList), [`getPreCondPropForRole`](action.md#getPreCondPropForRole), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getQuestionInf`](action.md#getQuestionInf), [`getRemappedFrom`](action.md#getRemappedFrom), [`getRemapPropForRole`](action.md#getRemapPropForRole), [`getResolvedObjList`](action.md#getResolvedObjList), [`getResolveInfo`](action.md#getResolveInfo), [`getRoleFromIndex`](action.md#getRoleFromIndex), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`getVerbPhrase`](action.md#getVerbPhrase), [`getVerifyPropForRole`](action.md#getVerifyPropForRole), [`initTentative`](action.md#initTentative), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resetAction`](action.md#resetAction), [`resolveAction`](action.md#resolveAction), [`resolvedObjectsInScope`](action.md#resolvedObjectsInScope), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setCurrentObjects`](action.md#setCurrentObjects), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setObjectMatches`](action.md#setObjectMatches), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`setResolvedObjects`](action.md#setResolvedObjects), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyAction`](action.md#verifyAction), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatObj`](action.md#whatObj), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
