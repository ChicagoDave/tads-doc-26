# LiteralTAction

*class* — defined in [action.t](../by-file/action.t.md) (line 5311)


An action with a direct object and a literal, such as "turn dial to <setting>" or "type <string> on keypad". We'll accept anything as the literal phrase - a number, a quoted string, or arbitrary words - and treat them all simply as text.


**Superclass chain:** [LiteralActionBase](literalactionbase.md) > `object` > [TAction](taction.md) > [Action](action.md) > [BasicProd](basicprod.md) > [Resolver](resolver.md) > **LiteralTActionSubclasses:** [EnterOnAction](enteronaction.md), [predicate(EnterOn)](predicate%28enteron%29.md), [predicate(EnterOnWhat)](predicate%28enteronwhat%29.md), [SetToAction](settoaction.md), [predicate(SetTo)](predicate%28setto%29.md), [TurnToAction](turntoaction.md), [predicate(TurnTo)](predicate%28turnto%29.md), [TypeLiteralOnAction](typeliteralonaction.md), [predicate(TypeLiteralOn)](predicate%28typeliteralon%29.md), [predicate(TypeLiteralOnWhat)](predicate%28typeliteralonwhat%29.md)


## Properties


### `predicateNounPhrases` *(overridden)*

Defined in action.t, line 5353

we have a direct object and a literal phrase


### `whichMessageLiteral`

Defined in action.t, line 5480

object role played by the literal phrase


### `whichMessageObject` *(overridden)*

Defined in action.t, line 5506

What we call our direct object might actually be playing the grammatical role of the indirect object - in order to inherit easily from TAction, we call our resolved object our direct object, regardless of which grammatical role it actually plays. For the most part it doesn't matter which is which; but for the purposes of our resolver, we actually do care about its real role. So, override the resolver method whichMessageObject so that it returns whichever role is NOT served by the topic object.


### `whichObject` *(overridden)*

Defined in action.t, line 5494

the true grammatical role of the resolved object is always the direct object


## Inherited Properties


*From [LiteralActionBase](literalactionbase.md):* [`text_`](literalactionbase.md#text_)


*From [TAction](taction.md):* [`actionAllowsAll`](taction.md#actionAllowsAll), [`actionDobjProp`](taction.md#actionDobjProp), [`actor_`](taction.md#actor_), [`askDobjResponseProd`](taction.md#askDobjResponseProd), [`checkDobjProp`](taction.md#checkDobjProp), [`dobjCur_`](taction.md#dobjCur_), [`dobjInfoCur_`](taction.md#dobjInfoCur_), [`dobjList_`](taction.md#dobjList_), [`dobjMatch`](taction.md#dobjMatch), [`dobjResolver_`](taction.md#dobjResolver_), [`issuer_`](taction.md#issuer_), [`preCondDobjProp`](taction.md#preCondDobjProp), [`remapDobjProp`](taction.md#remapDobjProp), [`verDobjProp`](taction.md#verDobjProp)


*From [Action](action.md):* [`actionTime`](action.md#actionTime), [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`scope_`](resolver.md#scope_)


## Methods


### `announceDefaultObject(obj, whichObj, resolvedAllObjects)` *(overridden)*

Defined in en_us.t, line 9015


### `getCurrentObjects` *(overridden)*

Defined in action.t, line 5417

Get a list of the current objects. We include only the direct object here, since the literal text is not a resolved object but simply literal text.


### `getMatchForRole(role)` *(overridden)*

Defined in action.t, line 5383

get the match tree for the given role


### `getObjectForRole(role)` *(overridden)*

Defined in action.t, line 5373

get the resolved object in a given role


### `getOtherMessageObjectPronoun(which)`

Defined in en_us.t, line 9049

When we want to show a verb infinitive phrase that involves a pronoun for the literal phrase, refer to the literal as 'that' rather than 'it' or anything else.


### `getOtherObjectRole(role)` *(overridden)*

Defined in action.t, line 5366

get the OtherObject role for the given role


### `getQuestionInf(which)` *(overridden)*

Defined in en_us.t, line 9034

use the same handling we use for a regular two-object action


### `getRoleFromIndex(idx)` *(overridden)*

Defined in action.t, line 5356

get an object role


### `getVerbPhrase(inf, ctx)` *(overridden)*

Defined in en_us.t, line 9083

We're asking about the resolved object, so the other pronoun is for the literal phrase: always use 'that' to refer to the literal phrase.


### `initForMissingDobj(orig)` *(overridden)*

Defined in action.t, line 5453

initialize with a missing direct object phrase


### `initForMissingLiteral(orig)`

Defined in action.t, line 5465

initialize for a missing literal phrase


### `resolveNouns(issuingActor, targetActor, results)` *(overridden)*

Defined in action.t, line 5315

Resolve objects.


### `retryWithMissingLiteral(orig)`

Defined in action.t, line 5435

Retry a single-object action as an action taking both an object and a literal phrase. We'll treat the original action's direct object list as our direct object list, and obtain a literal phrase interactively.


### `setCurrentObjects(lst)` *(overridden)*

Defined in action.t, line 5420

set the current objects


### `setObjectMatches(dobj, lit)` *(overridden)*

Defined in action.t, line 5403

manually set the pre-resolved match trees


### `setResolvedObjects(dobj, txt)` *(overridden)*

Defined in action.t, line 5393

manually set the resolved objects


### `whatObj(which)` *(overridden)*

Defined in en_us.t, line 9028

Use the same handling as for a regular two-object action. We can only default the actual object in this kind of verb; the actual object always fills the DirectObject slot, but in message generation it might use a different slot, so use the message generation slot here.


## Inherited Methods


*From [LiteralActionBase](literalactionbase.md):* [`getLiteral`](literalactionbase.md#getLiteral), [`getMessageParam`](literalactionbase.md#getMessageParam)


<details><summary>From [TAction](taction.md) (40)</summary>

[`adjustDefaultObjectPrep`](taction.md#adjustDefaultObjectPrep), [`announceAllDefaultObjects`](taction.md#announceAllDefaultObjects), [`canDobjResolveTo`](taction.md#canDobjResolveTo), [`checkAction`](taction.md#checkAction), [`checkRemapping`](taction.md#checkRemapping), [`construct`](taction.md#construct), [`createDobjResolver`](taction.md#createDobjResolver), [`createForMissingDobj`](taction.md#createForMissingDobj), [`createForRetry`](taction.md#createForRetry), [`doActionMain`](taction.md#doActionMain), [`execAction`](taction.md#execAction), [`filterAmbiguousDobj`](taction.md#filterAmbiguousDobj), [`filterPluralDobj`](taction.md#filterPluralDobj), [`getAllDobj`](taction.md#getAllDobj), [`getDefaultDobj`](taction.md#getDefaultDobj), [`getDobj`](taction.md#getDobj), [`getDobjCount`](taction.md#getDobjCount), [`getDobjFlags`](taction.md#getDobjFlags), [`getDobjInfo`](taction.md#getDobjInfo), [`getDobjResolver`](taction.md#getDobjResolver), [`getDobjTokens`](taction.md#getDobjTokens), [`getDobjWords`](taction.md#getDobjWords), [`getObjResponseProd`](taction.md#getObjResponseProd), [`getPreCondDescList`](taction.md#getPreCondDescList), [`getPreCondPropForRole`](taction.md#getPreCondPropForRole), [`getRemapPropForRole`](taction.md#getRemapPropForRole), [`getResolvedDobjList`](taction.md#getResolvedDobjList), [`getResolvedObjList`](taction.md#getResolvedObjList), [`getResolveInfo`](taction.md#getResolveInfo), [`getVerbPhrase1`](taction.md#getVerbPhrase1), [`getVerifyPropForRole`](taction.md#getVerifyPropForRole), [`initResolver`](taction.md#initResolver), [`initTentative`](taction.md#initTentative), [`resetAction`](taction.md#resetAction), [`resolvedObjectsInScope`](taction.md#resolvedObjectsInScope), [`retryWithAmbiguousDobj`](taction.md#retryWithAmbiguousDobj), [`retryWithMissingDobj`](taction.md#retryWithMissingDobj), [`setResolvedDobj`](taction.md#setResolvedDobj), [`testRetryDefaultDobj`](taction.md#testRetryDefaultDobj), [`verifyAction`](taction.md#verifyAction)

</details>


<details><summary>From [Action](action.md) (73)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkPreConditions`](action.md#checkPreConditions), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getNotifyTable`](action.md#getNotifyTable), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getRemappedFrom`](action.md#getRemappedFrom), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resolveAction`](action.md#resolveAction), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


<details><summary>From [Resolver](resolver.md) (25)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterAmbiguousNounPhrase`](resolver.md#filterAmbiguousNounPhrase), [`filterPluralPhrase`](resolver.md#filterPluralPhrase), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getAll`](resolver.md#getAll), [`getAllDefaults`](resolver.md#getAllDefaults), [`getDefaultObject`](resolver.md#getDefaultObject), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
