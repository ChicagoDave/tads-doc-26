# ConvTopicTAction

*class* — defined in [action.t](../by-file/action.t.md) (line 6072)


"Conversation" TopicTAction. Many TopicTAction verbs involve conversation with an actor, who's specified as the direct object: ASK <actor> ABOUT <topic>, TELL <actor> ABOUT <topic>, ASK <actor> FOR <topic>. For these common cases, the most likely default direct object is the last interlocutor of the actor performing the command - that is, ASK ABOUT BOOK should by default be directed to whomever we were speaking to last.


**Superclass chain:** [TopicTAction](topictaction.md) > [TopicActionBase](topicactionbase.md) > `object` > [TAction](taction.md) > [Action](action.md) > [BasicProd](basicprod.md) > [Resolver](resolver.md) > **ConvTopicTAction**


<details><summary>Subclasses (11)</summary>

- [AskAboutAction](askaboutaction.md)
- [predicate(AskAbout)](predicate%28askabout%29.md)
- [predicate(AskAboutImplicit)](predicate%28askaboutimplicit%29.md)
- [predicate(AskAboutWhat)](predicate%28askaboutwhat%29.md)
- [AskForAction](askforaction.md)
- [predicate(AskFor)](predicate%28askfor%29.md)
- [predicate(AskWhomFor)](predicate%28askwhomfor%29.md)
- [TellAboutAction](tellaboutaction.md)
- [predicate(TellAbout)](predicate%28tellabout%29.md)
- [predicate(TellAboutImplicit)](predicate%28tellaboutimplicit%29.md)
- [predicate(TellAboutWhat)](predicate%28tellaboutwhat%29.md)

</details>


## Inherited Properties


*From [TopicTAction](topictaction.md):* [`needAnaphoricBinding_`](topictaction.md#needAnaphoricBinding_), [`predicateNounPhrases`](topictaction.md#predicateNounPhrases), [`topicList_`](topictaction.md#topicList_), [`topicResolver_`](topictaction.md#topicResolver_), [`whichMessageObject`](topictaction.md#whichMessageObject), [`whichMessageTopic`](topictaction.md#whichMessageTopic), [`whichObject`](topictaction.md#whichObject)


*From [TopicActionBase](topicactionbase.md):* [`topicQualResolver_`](topicactionbase.md#topicQualResolver_)


*From [TAction](taction.md):* [`actionAllowsAll`](taction.md#actionAllowsAll), [`actionDobjProp`](taction.md#actionDobjProp), [`actor_`](taction.md#actor_), [`askDobjResponseProd`](taction.md#askDobjResponseProd), [`checkDobjProp`](taction.md#checkDobjProp), [`dobjCur_`](taction.md#dobjCur_), [`dobjInfoCur_`](taction.md#dobjInfoCur_), [`dobjList_`](taction.md#dobjList_), [`dobjMatch`](taction.md#dobjMatch), [`dobjResolver_`](taction.md#dobjResolver_), [`issuer_`](taction.md#issuer_), [`preCondDobjProp`](taction.md#preCondDobjProp), [`remapDobjProp`](taction.md#remapDobjProp), [`verDobjProp`](taction.md#verDobjProp)


*From [Action](action.md):* [`actionTime`](action.md#actionTime), [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`scope_`](resolver.md#scope_)


## Methods


### `createTopicResolver(issuingActor, targetActor)` *(overridden)*

Defined in action.t, line 6091

Create the topic resolver. Use a conversational topic resolver for this type of action.


### `getDefaultDobj(np, resolver)` *(overridden)*

Defined in action.t, line 6073


## Inherited Methods


*From [TopicTAction](topictaction.md):* [`announceDefaultObject`](topictaction.md#announceDefaultObject), [`filterTopic`](topictaction.md#filterTopic), [`getAnaphoricBinding`](topictaction.md#getAnaphoricBinding), [`getCurrentObjects`](topictaction.md#getCurrentObjects), [`getMatchForRole`](topictaction.md#getMatchForRole), [`getObjectForRole`](topictaction.md#getObjectForRole), [`getOtherMessageObjectPronoun`](topictaction.md#getOtherMessageObjectPronoun), [`getOtherObjectRole`](topictaction.md#getOtherObjectRole), [`getQuestionInf`](topictaction.md#getQuestionInf), [`getRoleFromIndex`](topictaction.md#getRoleFromIndex), [`getVerbPhrase`](topictaction.md#getVerbPhrase), [`initForMissingDobj`](topictaction.md#initForMissingDobj), [`initForMissingTopic`](topictaction.md#initForMissingTopic), [`resetAction`](topictaction.md#resetAction), [`resolveNouns`](topictaction.md#resolveNouns), [`retryWithMissingTopic`](topictaction.md#retryWithMissingTopic), [`setCurrentObjects`](topictaction.md#setCurrentObjects), [`setObjectMatches`](topictaction.md#setObjectMatches), [`setResolvedObjects`](topictaction.md#setResolvedObjects), [`whatObj`](topictaction.md#whatObj)


*From [TopicActionBase](topicactionbase.md):* [`getMessageParam`](topicactionbase.md#getMessageParam), [`getTopic`](topicactionbase.md#getTopic), [`getTopicQualifierResolver`](topicactionbase.md#getTopicQualifierResolver), [`getTopicResolver`](topicactionbase.md#getTopicResolver), [`reparseMatchAsTopic`](topicactionbase.md#reparseMatchAsTopic), [`resolveTopic`](topicactionbase.md#resolveTopic), [`setResolvedTopic`](topicactionbase.md#setResolvedTopic), [`setTopicMatch`](topicactionbase.md#setTopicMatch)


<details><summary>From [TAction](taction.md) (38)</summary>

[`adjustDefaultObjectPrep`](taction.md#adjustDefaultObjectPrep), [`announceAllDefaultObjects`](taction.md#announceAllDefaultObjects), [`canDobjResolveTo`](taction.md#canDobjResolveTo), [`checkAction`](taction.md#checkAction), [`checkRemapping`](taction.md#checkRemapping), [`construct`](taction.md#construct), [`createDobjResolver`](taction.md#createDobjResolver), [`createForMissingDobj`](taction.md#createForMissingDobj), [`createForRetry`](taction.md#createForRetry), [`doActionMain`](taction.md#doActionMain), [`execAction`](taction.md#execAction), [`filterAmbiguousDobj`](taction.md#filterAmbiguousDobj), [`filterPluralDobj`](taction.md#filterPluralDobj), [`getAllDobj`](taction.md#getAllDobj), [`getDobj`](taction.md#getDobj), [`getDobjCount`](taction.md#getDobjCount), [`getDobjFlags`](taction.md#getDobjFlags), [`getDobjInfo`](taction.md#getDobjInfo), [`getDobjResolver`](taction.md#getDobjResolver), [`getDobjTokens`](taction.md#getDobjTokens), [`getDobjWords`](taction.md#getDobjWords), [`getObjResponseProd`](taction.md#getObjResponseProd), [`getPreCondDescList`](taction.md#getPreCondDescList), [`getPreCondPropForRole`](taction.md#getPreCondPropForRole), [`getRemapPropForRole`](taction.md#getRemapPropForRole), [`getResolvedDobjList`](taction.md#getResolvedDobjList), [`getResolvedObjList`](taction.md#getResolvedObjList), [`getResolveInfo`](taction.md#getResolveInfo), [`getVerbPhrase1`](taction.md#getVerbPhrase1), [`getVerifyPropForRole`](taction.md#getVerifyPropForRole), [`initResolver`](taction.md#initResolver), [`initTentative`](taction.md#initTentative), [`resolvedObjectsInScope`](taction.md#resolvedObjectsInScope), [`retryWithAmbiguousDobj`](taction.md#retryWithAmbiguousDobj), [`retryWithMissingDobj`](taction.md#retryWithMissingDobj), [`setResolvedDobj`](taction.md#setResolvedDobj), [`testRetryDefaultDobj`](taction.md#testRetryDefaultDobj), [`verifyAction`](taction.md#verifyAction)

</details>


<details><summary>From [Action](action.md) (72)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkPreConditions`](action.md#checkPreConditions), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getNotifyTable`](action.md#getNotifyTable), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getRemappedFrom`](action.md#getRemappedFrom), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resolveAction`](action.md#resolveAction), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


<details><summary>From [Resolver](resolver.md) (25)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterAmbiguousNounPhrase`](resolver.md#filterAmbiguousNounPhrase), [`filterPluralPhrase`](resolver.md#filterPluralPhrase), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getAll`](resolver.md#getAll), [`getAllDefaults`](resolver.md#getAllDefaults), [`getDefaultObject`](resolver.md#getDefaultObject), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
