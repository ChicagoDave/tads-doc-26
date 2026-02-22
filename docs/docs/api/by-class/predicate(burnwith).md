# predicate(BurnWith)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 10342)


**Superclass chain:** [BurnWithAction](burnwithaction.md) > [TIAction](tiaction.md) > [TAction](taction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > [Resolver](resolver.md) > **predicate(BurnWith)**


## Properties


### `askDobjResponseProd` *(overridden)*

Defined in en_us.t, line 10348


### `askIobjResponseProd` *(overridden)*

Defined in en_us.t, line 10349


### `omitIobjInDobjQuery` *(overridden)*

Defined in en_us.t, line 10347


### `verbPhrase`

Defined in en_us.t, line 10346


## Inherited Properties


*From [BurnWithAction](burnwithaction.md):* [`resolveFirst`](burnwithaction.md#resolveFirst)


*From [TIAction](tiaction.md):* [`actionIobjProp`](tiaction.md#actionIobjProp), [`checkIobjProp`](tiaction.md#checkIobjProp), [`execFirst`](tiaction.md#execFirst), [`iobjCur_`](tiaction.md#iobjCur_), [`iobjInfoCur_`](tiaction.md#iobjInfoCur_), [`iobjList_`](tiaction.md#iobjList_), [`iobjMatch`](tiaction.md#iobjMatch), [`iobjResolver_`](tiaction.md#iobjResolver_), [`isPrepositionalPhrasing`](tiaction.md#isPrepositionalPhrasing), [`lastObjList_`](tiaction.md#lastObjList_), [`needAnaphoricBinding_`](tiaction.md#needAnaphoricBinding_), [`preCondIobjProp`](tiaction.md#preCondIobjProp), [`predicateNounPhrases`](tiaction.md#predicateNounPhrases), [`remapIobjProp`](tiaction.md#remapIobjProp), [`resolveFirstEmpty`](tiaction.md#resolveFirstEmpty), [`tentativeDobj_`](tiaction.md#tentativeDobj_), [`tentativeIobj_`](tiaction.md#tentativeIobj_), [`verIobjProp`](tiaction.md#verIobjProp)


*From [TAction](taction.md):* [`actionAllowsAll`](taction.md#actionAllowsAll), [`actionDobjProp`](taction.md#actionDobjProp), [`actor_`](taction.md#actor_), [`checkDobjProp`](taction.md#checkDobjProp), [`dobjCur_`](taction.md#dobjCur_), [`dobjInfoCur_`](taction.md#dobjInfoCur_), [`dobjList_`](taction.md#dobjList_), [`dobjMatch`](taction.md#dobjMatch), [`dobjResolver_`](taction.md#dobjResolver_), [`issuer_`](taction.md#issuer_), [`preCondDobjProp`](taction.md#preCondDobjProp), [`remapDobjProp`](taction.md#remapDobjProp), [`verDobjProp`](taction.md#verDobjProp), [`whichMessageObject`](taction.md#whichMessageObject)


*From [Action](action.md):* [`actionTime`](action.md#actionTime), [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`scope_`](resolver.md#scope_), [`whichObject`](resolver.md#whichObject)


## Inherited Methods


*From [BurnWithAction](burnwithaction.md):* [`getAllIobj`](burnwithaction.md#getAllIobj)


<details><summary>From [TIAction](tiaction.md) (58)</summary>

[`announceAllDefaultObjects`](tiaction.md#announceAllDefaultObjects), [`announceDefaultObject`](tiaction.md#announceDefaultObject), [`canIobjResolveTo`](tiaction.md#canIobjResolveTo), [`checkAction`](tiaction.md#checkAction), [`checkRemapping`](tiaction.md#checkRemapping), [`copyTentativeObjs`](tiaction.md#copyTentativeObjs), [`createForMissingIobj`](tiaction.md#createForMissingIobj), [`createIobjResolver`](tiaction.md#createIobjResolver), [`doActionMain`](tiaction.md#doActionMain), [`execAction`](tiaction.md#execAction), [`filterAmbiguousIobj`](tiaction.md#filterAmbiguousIobj), [`filterPluralIobj`](tiaction.md#filterPluralIobj), [`getAnaphoricBinding`](tiaction.md#getAnaphoricBinding), [`getCurrentObjects`](tiaction.md#getCurrentObjects), [`getDefaultIobj`](tiaction.md#getDefaultIobj), [`getIobj`](tiaction.md#getIobj), [`getIobjCount`](tiaction.md#getIobjCount), [`getIobjFlags`](tiaction.md#getIobjFlags), [`getIobjInfo`](tiaction.md#getIobjInfo), [`getIobjResolver`](tiaction.md#getIobjResolver), [`getIobjTokens`](tiaction.md#getIobjTokens), [`getIobjWords`](tiaction.md#getIobjWords), [`getMatchForRole`](tiaction.md#getMatchForRole), [`getMessageParam`](tiaction.md#getMessageParam), [`getObjectForRole`](tiaction.md#getObjectForRole), [`getObjResponseProd`](tiaction.md#getObjResponseProd), [`getOtherMessageObjectPronoun`](tiaction.md#getOtherMessageObjectPronoun), [`getOtherObjectRole`](tiaction.md#getOtherObjectRole), [`getPreCondDescList`](tiaction.md#getPreCondDescList), [`getPreCondPropForRole`](tiaction.md#getPreCondPropForRole), [`getQuestionInf`](tiaction.md#getQuestionInf), [`getRemapPropForRole`](tiaction.md#getRemapPropForRole), [`getResolvedIobjList`](tiaction.md#getResolvedIobjList), [`getResolvedObjList`](tiaction.md#getResolvedObjList), [`getResolveInfo`](tiaction.md#getResolveInfo), [`getRoleFromIndex`](tiaction.md#getRoleFromIndex), [`getTentativeDobj`](tiaction.md#getTentativeDobj), [`getTentativeIobj`](tiaction.md#getTentativeIobj), [`getVerbPhrase`](tiaction.md#getVerbPhrase), [`getVerbPhrase2`](tiaction.md#getVerbPhrase2), [`getVerifyPropForRole`](tiaction.md#getVerifyPropForRole), [`initForMissingDobj`](tiaction.md#initForMissingDobj), [`initForMissingIobj`](tiaction.md#initForMissingIobj), [`initTentative`](tiaction.md#initTentative), [`needRemappedAnnouncement`](tiaction.md#needRemappedAnnouncement), [`resetAction`](tiaction.md#resetAction), [`resolvedObjectsInScope`](tiaction.md#resolvedObjectsInScope), [`resolveNouns`](tiaction.md#resolveNouns), [`retryWithAmbiguousIobj`](tiaction.md#retryWithAmbiguousIobj), [`retryWithMissingIobj`](tiaction.md#retryWithMissingIobj), [`setCurrentObjects`](tiaction.md#setCurrentObjects), [`setObjectMatches`](tiaction.md#setObjectMatches), [`setPronounByInput`](tiaction.md#setPronounByInput), [`setResolvedIobj`](tiaction.md#setResolvedIobj), [`setResolvedObjects`](tiaction.md#setResolvedObjects), [`testRetryDefaultIobj`](tiaction.md#testRetryDefaultIobj), [`verifyAction`](tiaction.md#verifyAction), [`whatObj`](tiaction.md#whatObj)

</details>


<details><summary>From [TAction](taction.md) (24)</summary>

[`adjustDefaultObjectPrep`](taction.md#adjustDefaultObjectPrep), [`canDobjResolveTo`](taction.md#canDobjResolveTo), [`construct`](taction.md#construct), [`createDobjResolver`](taction.md#createDobjResolver), [`createForMissingDobj`](taction.md#createForMissingDobj), [`createForRetry`](taction.md#createForRetry), [`filterAmbiguousDobj`](taction.md#filterAmbiguousDobj), [`filterPluralDobj`](taction.md#filterPluralDobj), [`getAllDobj`](taction.md#getAllDobj), [`getDefaultDobj`](taction.md#getDefaultDobj), [`getDobj`](taction.md#getDobj), [`getDobjCount`](taction.md#getDobjCount), [`getDobjFlags`](taction.md#getDobjFlags), [`getDobjInfo`](taction.md#getDobjInfo), [`getDobjResolver`](taction.md#getDobjResolver), [`getDobjTokens`](taction.md#getDobjTokens), [`getDobjWords`](taction.md#getDobjWords), [`getResolvedDobjList`](taction.md#getResolvedDobjList), [`getVerbPhrase1`](taction.md#getVerbPhrase1), [`initResolver`](taction.md#initResolver), [`retryWithAmbiguousDobj`](taction.md#retryWithAmbiguousDobj), [`retryWithMissingDobj`](taction.md#retryWithMissingDobj), [`setResolvedDobj`](taction.md#setResolvedDobj), [`testRetryDefaultDobj`](taction.md#testRetryDefaultDobj)

</details>


<details><summary>From [Action](action.md) (72)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkPreConditions`](action.md#checkPreConditions), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getNotifyTable`](action.md#getNotifyTable), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getRemappedFrom`](action.md#getRemappedFrom), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resolveAction`](action.md#resolveAction), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


<details><summary>From [Resolver](resolver.md) (25)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterAmbiguousNounPhrase`](resolver.md#filterAmbiguousNounPhrase), [`filterPluralPhrase`](resolver.md#filterPluralPhrase), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getAll`](resolver.md#getAll), [`getAllDefaults`](resolver.md#getAllDefaults), [`getDefaultObject`](resolver.md#getDefaultObject), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
