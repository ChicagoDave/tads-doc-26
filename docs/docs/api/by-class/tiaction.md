# TIAction

*class* — defined in [action.t](../by-file/action.t.md) (line 3935)


Transitive-with-indirect Action class - this is an action that takes both a direct and indirect object. We subclass the basic one-object action to add the indirect object handling.


**Superclass chain:** [TAction](taction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > [Resolver](resolver.md) > **TIAction**


<details><summary>Subclasses (78)</summary>

- [AttachToAction](attachtoaction.md)
- [predicate(AttachTo)](predicate%28attachto%29.md)
- [predicate(AttachToWhat)](predicate%28attachtowhat%29.md)
- [AttackWithAction](attackwithaction.md)
- [predicate(AttackWith)](predicate%28attackwith%29.md)
- [BurnWithAction](burnwithaction.md)
- [predicate(BurnWith)](predicate%28burnwith%29.md)
- [CleanWithAction](cleanwithaction.md)
- [predicate(CleanWith)](predicate%28cleanwith%29.md)
- [CutWithAction](cutwithaction.md)
- [predicate(CutWith)](predicate%28cutwith%29.md)
- [predicate(CutWithWhat)](predicate%28cutwithwhat%29.md)
- [DetachFromAction](detachfromaction.md)
- [predicate(DetachFrom)](predicate%28detachfrom%29.md)
- [DigWithAction](digwithaction.md)
- [predicate(DigWith)](predicate%28digwith%29.md)
- [FastenToAction](fastentoaction.md)
- [predicate(FastenTo)](predicate%28fastento%29.md)
- [GiveToAction](givetoaction.md)
- [predicate(GiveTo)](predicate%28giveto%29.md)
- [predicate(GiveToType2)](predicate%28givetotype2%29.md)
- [predicate(GiveToWhom)](predicate%28givetowhom%29.md)
- [LockWithAction](lockwithaction.md)
- [predicate(LockWith)](predicate%28lockwith%29.md)
- [MoveToAction](movetoaction.md)
- [predicate(MoveTo)](predicate%28moveto%29.md)
- [MoveWithAction](movewithaction.md)
- [predicate(MoveWith)](predicate%28movewith%29.md)
- [PlugIntoAction](plugintoaction.md)
- [predicate(PlugInto)](predicate%28pluginto%29.md)
- [predicate(PlugIntoWhat)](predicate%28plugintowhat%29.md)
- [PourIntoAction](pourintoaction.md)
- [predicate(PourInto)](predicate%28pourinto%29.md)
- [PourOntoAction](pourontoaction.md)
- [predicate(PourOnto)](predicate%28pouronto%29.md)
- [PushTravelViaIobjAction](pushtravelviaiobjaction.md)
- [PushTravelClimbDownAction](pushtravelclimbdownaction.md)
- [predicate(PushTravelClimbDown)](predicate%28pushtravelclimbdown%29.md)
- [PushTravelClimbUpAction](pushtravelclimbupaction.md)
- [predicate(PushTravelClimbUp)](predicate%28pushtravelclimbup%29.md)
- [PushTravelEnterAction](pushtravelenteraction.md)
- [predicate(PushTravelEnter)](predicate%28pushtravelenter%29.md)
- [PushTravelGetOutOfAction](pushtravelgetoutofaction.md)
- [predicate(PushTravelGetOutOf)](predicate%28pushtravelgetoutof%29.md)
- [PushTravelThroughAction](pushtravelthroughaction.md)
- [predicate(PushTravelThrough)](predicate%28pushtravelthrough%29.md)
- [PutBehindAction](putbehindaction.md)
- [predicate(PutBehind)](predicate%28putbehind%29.md)
- [PutInAction](putinaction.md)
- [predicate(PutIn)](predicate%28putin%29.md)
- [predicate(PutInWhat)](predicate%28putinwhat%29.md)
- [PutOnAction](putonaction.md)
- [predicate(PutOn)](predicate%28puton%29.md)
- [PutUnderAction](putunderaction.md)
- [predicate(PutUnder)](predicate%28putunder%29.md)
- [ScrewWithAction](screwwithaction.md)
- [predicate(ScrewWith)](predicate%28screwwith%29.md)
- [ShowToAction](showtoaction.md)
- [predicate(ShowTo)](predicate%28showto%29.md)
- [predicate(ShowToType2)](predicate%28showtotype2%29.md)
- [predicate(ShowToWhom)](predicate%28showtowhom%29.md)
- [TakeFromAction](takefromaction.md)
- [predicate(TakeFrom)](predicate%28takefrom%29.md)
- [ThrowAtAction](throwataction.md)
- [predicate(ThrowAt)](predicate%28throwat%29.md)
- [ThrowToAction](throwtoaction.md)
- [predicate(ThrowTo)](predicate%28throwto%29.md)
- [predicate(ThrowToType2)](predicate%28throwtotype2%29.md)
- [TurnWithAction](turnwithaction.md)
- [predicate(TurnWith)](predicate%28turnwith%29.md)
- [UnfastenFromAction](unfastenfromaction.md)
- [predicate(UnfastenFrom)](predicate%28unfastenfrom%29.md)
- [UnlockWithAction](unlockwithaction.md)
- [predicate(UnlockWith)](predicate%28unlockwith%29.md)
- [UnplugFromAction](unplugfromaction.md)
- [predicate(UnplugFrom)](predicate%28unplugfrom%29.md)
- [UnscrewWithAction](unscrewwithaction.md)
- [predicate(UnscrewWith)](predicate%28unscrewwith%29.md)

</details>


## Properties


### `actionIobjProp`

Defined in action.t, line 5174


### `askIobjResponseProd`

Defined in action.t, line 4087

The root production to use to parse missing indirect object responses. By default, this is singleNoun, but individual actions can override this as appropriate.


### `checkIobjProp`

Defined in action.t, line 5173


### `execFirst`

Defined in action.t, line 4126

Determine which object to call first for action processing. By default, we execute in the same order as we resolve, but this can be overridden if necessary.


### `iobjCur_`

Defined in action.t, line 5149

current indirect object being executed


### `iobjInfoCur_`

Defined in action.t, line 5152

the full ResolveInfo associated with iobjCur_


### `iobjList_`

Defined in action.t, line 5146

the indirect object list


### `iobjMatch`

Defined in action.t, line 5143

the predicate grammar must assign the indirect object production tree to iobjMatch


### `iobjResolver_`

Defined in action.t, line 5155

my cached indirect object resolver


### `isPrepositionalPhrasing`

Defined in en_us.t, line 8646

For VerbRules: does this verb rule have a prepositional or structural phrasing of the direct and indirect object slots? That is, are the object slots determined by a prepositional marker, or purely by word order? For most English verbs with two objects, the indirect object is marked by a preposition: GIVE BOOK TO BOB, PUT BOOK IN BOX. There are a few English verbs that don't include any prespositional markers for the objects, though, and assign the noun phrase roles purely by the word order: GIVE BOB BOOK, SHOW BOB BOOK, THROW BOB BOOK. We define these phrasings with separate verb rules, which we mark with this property.


### `lastObjList_`

Defined in action.t, line 4500

The last object list we resolved. We keep track of this so that we can provide it as the anaphoric binding, if an anaphor binding is requested.


### `needAnaphoricBinding_`

Defined in action.t, line 4508

Flag: we have been asked for an anaphoric binding, but we don't have a binding available. We'll check this after resolving the first-resolved noun phrase so that we can go back and re-resolve it again after resolving the other noun phrase.


### `omitIobjInDobjQuery`

Defined in en_us.t, line 8616

Flag: omit the indirect object in a query for a missing direct object. For many verbs, if we already know the indirect object and we need to ask for the direct object, the query sounds best when it includes the indirect object: "what do you want to put in it?" or "what do you want to take from it?". This is the default phrasing.


### `preCondIobjProp`

Defined in action.t, line 5172


### `predicateNounPhrases` *(overridden)*

Defined in action.t, line 4322

we have a direct and indirect object


### `remapIobjProp`

Defined in action.t, line 5183

Action-remap properties for the indirect object. By convention, the remapper properties are named remapDobjAction and remapIobjAction, for the direct and indirect objects, respectively, where Action is replaced by the root name of the action.


### `resolveFirst`

Defined in action.t, line 4107

Resolution order - returns DirectObject or IndirectObject to indicate which noun phrase to resolve first in resolveNouns(). By default, we'll resolve the indirect object first, but individual actions can override this to resolve in a non-default order.


### `resolveFirstEmpty`

Defined in action.t, line 4119

Empty phrase resolution order. This is similar to the standard resolution order (resolveFirst), but is used only when both the direct and indirect objects are empty phrases.


### `tentativeDobj_`

Defined in action.t, line 5162

The tentative direct and indirect object lists. A tentative list is available for the later-resolved object while resolving the earlier-resolved object.


### `tentativeIobj_`

Defined in action.t, line 5163


### `verIobjProp`

Defined in action.t, line 5171

Verification and action properties for the indirect object. By convention, the verification method for the indirect object of a two-object action is verIobjXxx; the check method is checkIobjXxx; and the action method is actionIobjXxx.


## Inherited Properties


*From [TAction](taction.md):* [`actionAllowsAll`](taction.md#actionAllowsAll), [`actionDobjProp`](taction.md#actionDobjProp), [`actor_`](taction.md#actor_), [`askDobjResponseProd`](taction.md#askDobjResponseProd), [`checkDobjProp`](taction.md#checkDobjProp), [`dobjCur_`](taction.md#dobjCur_), [`dobjInfoCur_`](taction.md#dobjInfoCur_), [`dobjList_`](taction.md#dobjList_), [`dobjMatch`](taction.md#dobjMatch), [`dobjResolver_`](taction.md#dobjResolver_), [`issuer_`](taction.md#issuer_), [`preCondDobjProp`](taction.md#preCondDobjProp), [`remapDobjProp`](taction.md#remapDobjProp), [`verDobjProp`](taction.md#verDobjProp), [`whichMessageObject`](taction.md#whichMessageObject)


*From [Action](action.md):* [`actionTime`](action.md#actionTime), [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`includeInUndo`](action.md#includeInUndo), [`isImplicit`](action.md#isImplicit), [`isRepeatable`](action.md#isRepeatable), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`scope_`](resolver.md#scope_), [`whichObject`](resolver.md#whichObject)


## Methods


### `announceAllDefaultObjects(allResolved)` *(overridden)*

Defined in en_us.t, line 8767

announce all defaulted objects


### `announceDefaultObject(obj, whichObj, resolvedAllObjects)` *(overridden)*

Defined in en_us.t, line 8711

announce a default object used with this action


### `canIobjResolveTo(obj)`

Defined in action.t, line 4135

Can the indirect object potentially resolve to the given simulation object? This only determines if the object is a *syntactic* match, meaning that it can match at a vocabulary and grammar level. This doesn't test it for logicalness or check that it's an otherwise valid resolution.


### `checkAction` *(overridden)*

Defined in action.t, line 4976

Check the command.


### `checkRemapping` *(overridden)*

Defined in action.t, line 4935

Check for remapping


### `copyTentativeObjs`

Defined in action.t, line 5122

Copy one tentative object list to the other. This is useful when an object's verifier for one TIAction wants to forward the call to the other object verifier for a different TIAction.


### `createForMissingIobj(orig, asker)`

Defined in action.t, line 4010

Create an instance of this action for retrying a given single-object action with a missing indirect object.


### `createIobjResolver(issuingActor, targetActor)`

Defined in action.t, line 4544

Create our indirect object resolver. By default, we'll use a basic indirect object resolver.


### `doActionMain` *(overridden)*

Defined in action.t, line 4590

Execute the action. We'll run through the execution sequence once for each resolved object in our direct or indirect object list, depending on which one is the list and which one is the singleton.


### `execAction` *(overridden)*

Defined in action.t, line 5008

Execute the command.


### `filterAmbiguousIobj(lst, requiredNum, np)`

Defined in action.t, line 4560

filter an ambiguous indirect object noun phrase


### `filterPluralIobj(lst, np)`

Defined in action.t, line 4569

filter a plural phrase


### `getAllIobj(actor, scopeList)`

Defined in action.t, line 4554

Resolve 'all' for the indirect object. By default, we'll return everything in the scope list.


### `getAnaphoricBinding(typ)` *(overridden)*

Defined in action.t, line 4476

Get the anaphoric binding for the noun phrase we're currently resolving.


### `getCurrentObjects` *(overridden)*

Defined in action.t, line 5101

Get the list of active objects. We have a direct and indirect object.


### `getDefaultIobj(np, resolver)`

Defined in action.t, line 4577

get the default indirect object


### `getIobj`

Defined in action.t, line 5072

get the current indirect object being executed


### `getIobjCount`

Defined in action.t, line 5081

get the number of direct objects


### `getIobjFlags`

Defined in action.t, line 5078

get the object resolution flags for the indirect object


### `getIobjInfo`

Defined in action.t, line 5075

get the full ResolveInfo associated with the current indirect object


### `getIobjResolver(issuingActor, targetActor, reset)`

Defined in action.t, line 4526

get our indirect object resolver, or create one if we haven't already cached one


### `getIobjTokens`

Defined in action.t, line 5084

get the original token list of the current indirect object phrase


### `getIobjWords`

Defined in action.t, line 5091

get the original words (as a list of strings) of the current iobj


### `getMatchForRole(role)` *(overridden)*

Defined in action.t, line 4388

get the match tree for the noun phrase in the given role


### `getMessageParam(objName)` *(overridden)*

Defined in action.t, line 5057

Get a message parameter object for the action. We define 'dobj' as the direct object and 'iobj' as the indirect object, in addition to any inherited targets.


### `getObjectForRole(role)` *(overridden)*

Defined in action.t, line 4335

get the resolved object in a given role


### `getObjResponseProd(resolver)` *(overridden)*

Defined in action.t, line 4090

get the missing object response production for a given role


### `getOtherMessageObjectPronoun(which)`

Defined in en_us.t, line 8852

Get the pronoun for the message object in the given role.


### `getOtherObjectRole(role)` *(overridden)*

Defined in action.t, line 4381

get the OtherObject role for the given role


### `getPreCondDescList` *(overridden)*

Defined in action.t, line 5041

get the precondition descriptor list for the action


### `getPreCondPropForRole(role)` *(overridden)*

Defined in action.t, line 4401

get the 'preCond' property for a given object role


### `getQuestionInf(which)` *(overridden)*

Defined in en_us.t, line 8777

show the verb's basic infinitive form for an interrogative


### `getRemapPropForRole(role)` *(overridden)*

Defined in action.t, line 4407

get the 'remap' property for a given object role


### `getResolvedIobjList`

Defined in action.t, line 4420

get the list of resolved indirect objects


### `getResolvedObjList(which)` *(overridden)*

Defined in action.t, line 4413

get the list of resolved objects in the given role


### `getResolveInfo(obj, oldRole)` *(overridden)*

Defined in action.t, line 4342

get the ResolveInfo for the given resolved object


### `getRoleFromIndex(idx)` *(overridden)*

Defined in action.t, line 4325

get an object role


### `getTentativeDobj`

Defined in action.t, line 5136

Get the tentative direct/indirect object resolution lists. A tentative list is available for the later-resolved object while resolving the earlier-resolved object.


### `getTentativeIobj`

Defined in action.t, line 5137


### `getVerbPhrase(inf, ctx)` *(overridden)*

Defined in en_us.t, line 8883

get the verb phrase in infinitive or participle form


### `getVerbPhrase2(inf, vp, dobjText, dobjIsPronoun, iobjText)`

Defined in en_us.t, line 8927

Get the verb phrase for a two-object (dobj + iobj) phrasing. This is a class method, so that it can be reused by unrelated (i.e., non-TIAction) classes that also use two-object syntax but with other internal structures. This is the two-object equivalent of TAction.getVerbPhrase1().


### `getVerifyPropForRole(role)` *(overridden)*

Defined in action.t, line 4395

get the 'verify' property for a given object role


### `initForMissingDobj(orig)` *(overridden)*

Defined in action.t, line 4040

Initialize the action for retrying with a missing direct object.


### `initForMissingIobj(orig)`

Defined in action.t, line 4063

Initialize the action for retrying with a missing indirect object.


### `initTentative(issuingActor, targetActor, whichObj)` *(overridden)*

Defined in action.t, line 4869

initialize tentative resolutions for other noun phrases


### `needRemappedAnnouncement(info)`

Defined in action.t, line 4823

Determine if we need to announce this action when the action was remapped, based on the resolution information for one of our objects. We need to announce a remapped action when either object had unclear disambiguation or was defaulted.


### `resetAction` *(overridden)*

Defined in action.t, line 3936


### `resolvedObjectsInScope` *(overridden)*

Defined in action.t, line 4511

check that the resolved objects are in scope


### `resolveNouns(issuingActor, targetActor, results)` *(overridden)*

Defined in en_us.t, line 8649

resolve our noun phrases to objects


### `retryWithAmbiguousIobj(orig, objs, asker, objPhrase)`

Defined in action.t, line 3966

Retry an action as a two-object action with an ambiguous indirect object. We'll ask which of the given possible objects is intended.


### `retryWithMissingIobj(orig, asker)`

Defined in action.t, line 3955

Retry a single-object action as a two-object action. We'll treat the original action's direct object list as our direct object list, and obtain an indirect object using the normal means (first looking for a default, then prompting the player if we can't find a suitable default). 'orig' is the original single-object action.


### `setCurrentObjects(lst)` *(overridden)*

Defined in action.t, line 5107

set the current objects


### `setObjectMatches(dobj, iobj)` *(overridden)*

Defined in action.t, line 4457

manually set the unresolved object noun phrase match trees


### `setPronounByInput(lst)`

Defined in action.t, line 4766

Set the pronoun according to the pronoun type actually used in the input. For example, if we said PUT BOX ON IT, we want IT to continue referring to whatever IT referred to before this command - we specifically do NOT want IT to refer to the BOX in this case.


### `setResolvedIobj(iobj)`

Defined in action.t, line 4443

set a resolved iobj


### `setResolvedObjects(dobj, iobj)` *(overridden)*

Defined in action.t, line 4433

Manually set the resolved objects. We'll set our direct and indirect objects.


### `testRetryDefaultIobj(orig)`

Defined in action.t, line 3989

Test to see if askForIobj() would find a default indirect object. Returns true if there's a default, nil if not. If this returns true, then askForIobj() will simply take the default and proceed; otherwise, it will have to actually ask the user for the missing information.


### `verifyAction` *(overridden)*

Defined in action.t, line 4837

Verify the action.


### `whatObj(which)` *(overridden)*

Defined in en_us.t, line 8685

get the interrogative for one of our objects


## Inherited Methods


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
