# RecordOffAction

*class* — defined in [actions.t](../by-file/actions.t.md) (line 1465)


Turn command recording off. This stops recording the command log started with the most recent RECORD command.


**Superclass chain:** [SystemAction](systemaction.md) > [IAction](iaction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > **RecordOffActionSubclasses:** [predicate(RecordOff)](predicate%28recordoff%29.md)


## Properties


### `includeInUndo` *(overridden)*

Defined in actions.t, line 1494

we can't include this in undo, as it affects external files


## Inherited Properties


*From [SystemAction](systemaction.md):* [`actionTime`](systemaction.md#actionTime)


*From [Action](action.md):* [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`predicateNounPhrases`](action.md#predicateNounPhrases), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execSystemAction` *(overridden)*

Defined in actions.t, line 1466


### `turnOffRecording(ack)`

Defined in actions.t, line 1473

turn off recording


## Inherited Methods


*From [SystemAction](systemaction.md):* [`execAction`](systemaction.md#execAction), [`getInputFile`](systemaction.md#getInputFile)


*From [IAction](iaction.md):* [`doActionMain`](iaction.md#doActionMain), [`resolveNouns`](iaction.md#resolveNouns)


<details><summary>From [Action](action.md) (100)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`announceAllDefaultObjects`](action.md#announceAllDefaultObjects), [`announceDefaultObject`](action.md#announceDefaultObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkAction`](action.md#checkAction), [`checkPreConditions`](action.md#checkPreConditions), [`checkRemapping`](action.md#checkRemapping), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getCurrentObjects`](action.md#getCurrentObjects), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getMatchForRole`](action.md#getMatchForRole), [`getMessageParam`](action.md#getMessageParam), [`getNotifyTable`](action.md#getNotifyTable), [`getObjectForRole`](action.md#getObjectForRole), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getObjResponseProd`](action.md#getObjResponseProd), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getOtherObjectRole`](action.md#getOtherObjectRole), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPreCondDescList`](action.md#getPreCondDescList), [`getPreCondPropForRole`](action.md#getPreCondPropForRole), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getQuestionInf`](action.md#getQuestionInf), [`getRemappedFrom`](action.md#getRemappedFrom), [`getRemapPropForRole`](action.md#getRemapPropForRole), [`getResolvedObjList`](action.md#getResolvedObjList), [`getResolveInfo`](action.md#getResolveInfo), [`getRoleFromIndex`](action.md#getRoleFromIndex), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`getVerbPhrase`](action.md#getVerbPhrase), [`getVerifyPropForRole`](action.md#getVerifyPropForRole), [`initTentative`](action.md#initTentative), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resetAction`](action.md#resetAction), [`resolveAction`](action.md#resolveAction), [`resolvedObjectsInScope`](action.md#resolvedObjectsInScope), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setCurrentObjects`](action.md#setCurrentObjects), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setObjectMatches`](action.md#setObjectMatches), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`setResolvedObjects`](action.md#setResolvedObjects), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyAction`](action.md#verifyAction), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatObj`](action.md#whatObj), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
