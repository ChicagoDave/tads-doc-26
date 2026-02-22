# TopicTAction

*class* — defined in [action.t](../by-file/action.t.md) (line 5786)


An Action with a direct object and a topic, such as "ask <actor> about <topic>". Topics differ from ordinary noun phrases in scope: rather than resolving to simulation objects based on location, we resolve these based on the actor's knowledge.


**Superclass chain:** [TopicActionBase](topicactionbase.md) > `object` > [TAction](taction.md) > [Action](action.md) > [BasicProd](basicprod.md) > [Resolver](resolver.md) > **TopicTAction**


<details><summary>Subclasses (19)</summary>

- [AskVagueAction](askvagueaction.md)
- [predicate(AskVague)](predicate%28askvague%29.md)
- [predicate(TellVague)](predicate%28tellvague%29.md)
- [ConsultAboutAction](consultaboutaction.md)
- [predicate(ConsultAbout)](predicate%28consultabout%29.md)
- [predicate(ConsultWhatAbout)](predicate%28consultwhatabout%29.md)
- [ConvTopicTAction](convtopictaction.md)
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
- [TellVagueAction](tellvagueaction.md)

</details>


## Properties


### `needAnaphoricBinding_`

Defined in action.t, line 5944

Flag: we have been asked for an anaphoric binding, but we don't have a binding available. We'll check this after resolving the first-resolved noun phrase so that we can go back and re-resolve it again after resolving the other noun phrase.


### `predicateNounPhrases` *(overridden)*

Defined in action.t, line 5947

we have a direct object and a topic phrase


### `topicList_` *(overridden)*

Defined in action.t, line 6026

the resolved topic object list


### `topicResolver_` *(overridden)*

Defined in action.t, line 6029

my cached topic resolver


### `whichMessageObject` *(overridden)*

Defined in action.t, line 6054

What we call our direct object might actually be playing the grammatical role of the indirect object - in order to inherit easily from TAction, we call our resolved object our direct object, regardless of which grammatical role it actually plays. For the most part it doesn't matter which is which; but for the purposes of our resolver, we actually do care about its real role. So, override the resolver method whichMessageObject so that it returns whichever role is NOT served by the topic object.


### `whichMessageTopic`

Defined in action.t, line 6032

grammatical role played by topic phrase in generated messages


### `whichObject` *(overridden)*

Defined in action.t, line 6042

the true role of the resolved object is always as the direct object


## Inherited Properties


*From [TopicActionBase](topicactionbase.md):* [`topicQualResolver_`](topicactionbase.md#topicQualResolver_)


*From [TAction](taction.md):* [`actionAllowsAll`](taction.md#actionAllowsAll), [`actionDobjProp`](taction.md#actionDobjProp), [`actor_`](taction.md#actor_), [`askDobjResponseProd`](taction.md#askDobjResponseProd), [`checkDobjProp`](taction.md#checkDobjProp), [`dobjCur_`](taction.md#dobjCur_), [`dobjInfoCur_`](taction.md#dobjInfoCur_), [`dobjList_`](taction.md#dobjList_), [`dobjMatch`](taction.md#dobjMatch), [`dobjResolver_`](taction.md#dobjResolver_), [`issuer_`](taction.md#issuer_), [`preCondDobjProp`](taction.md#preCondDobjProp), [`remapDobjProp`](taction.md#remapDobjProp), [`verDobjProp`](taction.md#verDobjProp)


*From [Action](action.md):* [`actionTime`](action.md#actionTime), [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`scope_`](resolver.md#scope_)


## Methods


### `announceDefaultObject(obj, whichObj, resolvedAllObjects)` *(overridden)*

Defined in en_us.t, line 9152


### `createTopicResolver(issuingActor, targetActor)` *(overridden)*

Defined in action.t, line 5908

create our TAction topic resolver


### `filterTopic(lst, np, resolver)`

Defined in action.t, line 5848

Filter the resolved topic. This is called by our TActionTopicResolver, which refers the resolution back to us.


### `getAnaphoricBinding(typ)` *(overridden)*

Defined in action.t, line 5922

In the topic phrase, we can use an anaphoric pronoun to refer back to the direct object. Since we resolve the direct object phrase first, we can simply return the direct object list as the binding. If the direct object isn't resolved yet, make a note to come back and re-bind the anaphor.


### `getCurrentObjects` *(overridden)*

Defined in action.t, line 6013

Get the list of active objects. We return only our direct object, since our topic isn't actually a simulation object.


### `getMatchForRole(role)` *(overridden)*

Defined in action.t, line 5977

get the match tree for the given role


### `getObjectForRole(role)` *(overridden)*

Defined in action.t, line 5967

get the resolved object in a given role


### `getOtherMessageObjectPronoun(which)`

Defined in en_us.t, line 9177

use the same handling as for a regular two-object action


### `getOtherObjectRole(role)` *(overridden)*

Defined in action.t, line 5960

get the OtherObject role for the given role


### `getQuestionInf(which)` *(overridden)*

Defined in en_us.t, line 9171

use the same handling we use for a regular two-object action


### `getRoleFromIndex(idx)` *(overridden)*

Defined in action.t, line 5950

get an object role


### `getVerbPhrase(inf, ctx)` *(overridden)*

Defined in en_us.t, line 9201

return a generic pronoun for the topic


### `initForMissingDobj(orig)` *(overridden)*

Defined in action.t, line 5881

initialize a new action we're retrying for a missing direct object


### `initForMissingTopic(orig)`

Defined in action.t, line 5893

initialize for retrying with a missing topic phrase


### `resetAction` *(overridden)*

Defined in action.t, line 5790

reset the action


### `resolveNouns(issuingActor, targetActor, results)` *(overridden)*

Defined in action.t, line 5802

resolve our noun phrases to objects


### `retryWithMissingTopic(orig)`

Defined in action.t, line 5863

Retry a single-object action as an action taking both an object and a topic phrase. We'll treat the original action's direct object list as our direct object list, and we'll obtain a topic phrase interactively.


### `setCurrentObjects(lst)` *(overridden)*

Defined in action.t, line 6019

set the current objects


### `setObjectMatches(dobj, topic)` *(overridden)*

Defined in action.t, line 6000

manually set the pre-resolved match trees


### `setResolvedObjects(dobj, topic)` *(overridden)*

Defined in action.t, line 5990

Manually set the resolved objects. We'll set our direct and indirect objects.


### `whatObj(which)` *(overridden)*

Defined in en_us.t, line 9165

Use the same handling as for a regular two-object action. We can only default the actual object in this kind of verb; the actual object always fills the DirectObject slot, but in message generation it might use a different slot, so use the message generation slot here.


## Inherited Methods


*From [TopicActionBase](topicactionbase.md):* [`getMessageParam`](topicactionbase.md#getMessageParam), [`getTopic`](topicactionbase.md#getTopic), [`getTopicQualifierResolver`](topicactionbase.md#getTopicQualifierResolver), [`getTopicResolver`](topicactionbase.md#getTopicResolver), [`reparseMatchAsTopic`](topicactionbase.md#reparseMatchAsTopic), [`resolveTopic`](topicactionbase.md#resolveTopic), [`setResolvedTopic`](topicactionbase.md#setResolvedTopic), [`setTopicMatch`](topicactionbase.md#setTopicMatch)


<details><summary>From [TAction](taction.md) (39)</summary>

[`adjustDefaultObjectPrep`](taction.md#adjustDefaultObjectPrep), [`announceAllDefaultObjects`](taction.md#announceAllDefaultObjects), [`canDobjResolveTo`](taction.md#canDobjResolveTo), [`checkAction`](taction.md#checkAction), [`checkRemapping`](taction.md#checkRemapping), [`construct`](taction.md#construct), [`createDobjResolver`](taction.md#createDobjResolver), [`createForMissingDobj`](taction.md#createForMissingDobj), [`createForRetry`](taction.md#createForRetry), [`doActionMain`](taction.md#doActionMain), [`execAction`](taction.md#execAction), [`filterAmbiguousDobj`](taction.md#filterAmbiguousDobj), [`filterPluralDobj`](taction.md#filterPluralDobj), [`getAllDobj`](taction.md#getAllDobj), [`getDefaultDobj`](taction.md#getDefaultDobj), [`getDobj`](taction.md#getDobj), [`getDobjCount`](taction.md#getDobjCount), [`getDobjFlags`](taction.md#getDobjFlags), [`getDobjInfo`](taction.md#getDobjInfo), [`getDobjResolver`](taction.md#getDobjResolver), [`getDobjTokens`](taction.md#getDobjTokens), [`getDobjWords`](taction.md#getDobjWords), [`getObjResponseProd`](taction.md#getObjResponseProd), [`getPreCondDescList`](taction.md#getPreCondDescList), [`getPreCondPropForRole`](taction.md#getPreCondPropForRole), [`getRemapPropForRole`](taction.md#getRemapPropForRole), [`getResolvedDobjList`](taction.md#getResolvedDobjList), [`getResolvedObjList`](taction.md#getResolvedObjList), [`getResolveInfo`](taction.md#getResolveInfo), [`getVerbPhrase1`](taction.md#getVerbPhrase1), [`getVerifyPropForRole`](taction.md#getVerifyPropForRole), [`initResolver`](taction.md#initResolver), [`initTentative`](taction.md#initTentative), [`resolvedObjectsInScope`](taction.md#resolvedObjectsInScope), [`retryWithAmbiguousDobj`](taction.md#retryWithAmbiguousDobj), [`retryWithMissingDobj`](taction.md#retryWithMissingDobj), [`setResolvedDobj`](taction.md#setResolvedDobj), [`testRetryDefaultDobj`](taction.md#testRetryDefaultDobj), [`verifyAction`](taction.md#verifyAction)

</details>


<details><summary>From [Action](action.md) (72)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkPreConditions`](action.md#checkPreConditions), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getNotifyTable`](action.md#getNotifyTable), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getRemappedFrom`](action.md#getRemappedFrom), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resolveAction`](action.md#resolveAction), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


<details><summary>From [Resolver](resolver.md) (25)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterAmbiguousNounPhrase`](resolver.md#filterAmbiguousNounPhrase), [`filterPluralPhrase`](resolver.md#filterPluralPhrase), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getAll`](resolver.md#getAll), [`getAllDefaults`](resolver.md#getAllDefaults), [`getDefaultObject`](resolver.md#getDefaultObject), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
