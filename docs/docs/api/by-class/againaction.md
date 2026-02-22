# AgainAction

*class* — defined in [actions.t](../by-file/actions.t.md) (line 70)


Special "again" action. This command repeats the previous command.


**Superclass chain:** [IAction](iaction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > **AgainActionSubclasses:** [predicate(Again)](predicate%28again%29.md)


## Properties


### `actionTime` *(overridden)*

Defined in actions.t, line 172

this command itself consumes no time on the game clock (although the action we perform might)


### `includeInUndo` *(overridden)*

Defined in actions.t, line 78

the undo command itself is not undoable (but the underlying command that we repeat might be)


### `isRepeatable` *(overridden)*

Defined in actions.t, line 72

for obvious reasons, 'again' is not itself repeatable with 'again'


### `lastAction`

Defined in actions.t, line 84


### `lastIssuingActor`

Defined in actions.t, line 81

information on the most recent command


### `lastTargetActor`

Defined in actions.t, line 82


### `lastTargetActorPhrase`

Defined in actions.t, line 83


## Inherited Properties


*From [Action](action.md):* [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`isImplicit`](action.md#isImplicit), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`predicateNounPhrases`](action.md#predicateNounPhrases), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `clearForAgain`

Defined in actions.t, line 97

forget the last command, so that AGAIN cannot be used


### `doAction(issuingActor, targetActor, targetActorPhrase, countsAsIssuerTurn)` *(overridden)*

Defined in actions.t, line 107

Execute the 'again' command. This action is special enough that we override its entire action processing sequence - this is necessary in case we're repeating another special command, such as 'again', and in any case is desirable because we don't want 'again' to count as a command in its own right; it's essentially just a macro that we replace with the original command.


### `saveForAgain(issuingActor, targetActor, targetActorPhrase, action)`

Defined in actions.t, line 87

save the most recent command so that it can be repeated if desired


## Inherited Methods


*From [IAction](iaction.md):* [`doActionMain`](iaction.md#doActionMain), [`resolveNouns`](iaction.md#resolveNouns)


<details><summary>From [Action](action.md) (100)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`announceAllDefaultObjects`](action.md#announceAllDefaultObjects), [`announceDefaultObject`](action.md#announceDefaultObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkAction`](action.md#checkAction), [`checkPreConditions`](action.md#checkPreConditions), [`checkRemapping`](action.md#checkRemapping), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doActionOnce`](action.md#doActionOnce), [`execAction`](action.md#execAction), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getCurrentObjects`](action.md#getCurrentObjects), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getMatchForRole`](action.md#getMatchForRole), [`getMessageParam`](action.md#getMessageParam), [`getNotifyTable`](action.md#getNotifyTable), [`getObjectForRole`](action.md#getObjectForRole), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getObjResponseProd`](action.md#getObjResponseProd), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getOtherObjectRole`](action.md#getOtherObjectRole), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPreCondDescList`](action.md#getPreCondDescList), [`getPreCondPropForRole`](action.md#getPreCondPropForRole), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getQuestionInf`](action.md#getQuestionInf), [`getRemappedFrom`](action.md#getRemappedFrom), [`getRemapPropForRole`](action.md#getRemapPropForRole), [`getResolvedObjList`](action.md#getResolvedObjList), [`getResolveInfo`](action.md#getResolveInfo), [`getRoleFromIndex`](action.md#getRoleFromIndex), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`getVerbPhrase`](action.md#getVerbPhrase), [`getVerifyPropForRole`](action.md#getVerifyPropForRole), [`initTentative`](action.md#initTentative), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resetAction`](action.md#resetAction), [`resolveAction`](action.md#resolveAction), [`resolvedObjectsInScope`](action.md#resolvedObjectsInScope), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setCurrentObjects`](action.md#setCurrentObjects), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setObjectMatches`](action.md#setObjectMatches), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`setResolvedObjects`](action.md#setResolvedObjects), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyAction`](action.md#verifyAction), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatObj`](action.md#whatObj), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
