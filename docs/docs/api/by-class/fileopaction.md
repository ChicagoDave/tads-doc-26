# FileOpAction

*class* — defined in [actions.t](../by-file/actions.t.md) (line 1158)


A base class for file-oriented actions, such as SCRIPT, RECORD, and REPLAY. We provide common handling that prompts interactively for a filename; subclasses must override a few methods and properties to carry out the specific subclassed operation on the file.


**Superclass chain:** [SystemAction](systemaction.md) > [IAction](iaction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > **FileOpAction**


<details><summary>Subclasses (20)</summary>

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

</details>


## Properties


### `fileDisposition`

Defined in actions.t, line 1163

the file dialog open/save type


### `filePromptMsg`

Defined in actions.t, line 1160

our file dialog prompt message


### `fileTypeID`

Defined in actions.t, line 1166

the file dialog type ID


### `includeInUndo` *(overridden)*

Defined in actions.t, line 1245

we can't include this in undo, as it affects external files


### `isRepeatable` *(overridden)*

Defined in actions.t, line 1248

don't allow repeating with AGAIN


### `showCancelMsg`

Defined in actions.t, line 1169

show our cancellation mesage


## Inherited Properties


*From [SystemAction](systemaction.md):* [`actionTime`](systemaction.md#actionTime)


*From [Action](action.md):* [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`isImplicit`](action.md#isImplicit), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`predicateNounPhrases`](action.md#predicateNounPhrases), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execSystemAction` *(overridden)*

Defined in actions.t, line 1189

Each concrete action subclass must override this to carry out our operation. This is called when the user has successfully selected a filename for the operation.


### `performFileOp(fname, ack, desc, :?)`

Defined in actions.t, line 1180

Carry out our file operation.


### `setUpFileOp(ack)`

Defined in actions.t, line 1200

ask for a file, and carry out our operation is we get one


## Inherited Methods


*From [SystemAction](systemaction.md):* [`execAction`](systemaction.md#execAction), [`getInputFile`](systemaction.md#getInputFile)


*From [IAction](iaction.md):* [`doActionMain`](iaction.md#doActionMain), [`resolveNouns`](iaction.md#resolveNouns)


<details><summary>From [Action](action.md) (100)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`announceAllDefaultObjects`](action.md#announceAllDefaultObjects), [`announceDefaultObject`](action.md#announceDefaultObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkAction`](action.md#checkAction), [`checkPreConditions`](action.md#checkPreConditions), [`checkRemapping`](action.md#checkRemapping), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getCurrentObjects`](action.md#getCurrentObjects), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getMatchForRole`](action.md#getMatchForRole), [`getMessageParam`](action.md#getMessageParam), [`getNotifyTable`](action.md#getNotifyTable), [`getObjectForRole`](action.md#getObjectForRole), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getObjResponseProd`](action.md#getObjResponseProd), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getOtherObjectRole`](action.md#getOtherObjectRole), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPreCondDescList`](action.md#getPreCondDescList), [`getPreCondPropForRole`](action.md#getPreCondPropForRole), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getQuestionInf`](action.md#getQuestionInf), [`getRemappedFrom`](action.md#getRemappedFrom), [`getRemapPropForRole`](action.md#getRemapPropForRole), [`getResolvedObjList`](action.md#getResolvedObjList), [`getResolveInfo`](action.md#getResolveInfo), [`getRoleFromIndex`](action.md#getRoleFromIndex), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`getVerbPhrase`](action.md#getVerbPhrase), [`getVerifyPropForRole`](action.md#getVerifyPropForRole), [`initTentative`](action.md#initTentative), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resetAction`](action.md#resetAction), [`resolveAction`](action.md#resolveAction), [`resolvedObjectsInScope`](action.md#resolvedObjectsInScope), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setCurrentObjects`](action.md#setCurrentObjects), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setObjectMatches`](action.md#setObjectMatches), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`setResolvedObjects`](action.md#setResolvedObjects), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyAction`](action.md#verifyAction), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatObj`](action.md#whatObj), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
