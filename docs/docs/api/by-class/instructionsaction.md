# InstructionsAction

*class* — defined in [instruct.t](../by-file/instruct.t.md) (line 81)


The INSTRUCTIONS command. Make this a "system" action, because it's a meta-action outside of the story. System actions don't consume any game time.


**Superclass chain:** [SystemAction](systemaction.md) > [IAction](iaction.md) > [Action](action.md) > [BasicProd](basicprod.md) > `object` > **InstructionsActionSubclasses:** [predicate(instructions)](predicate%28instructions%29.md)


## Properties


### `allRequiredVerbsDisclosed`

Defined in instruct.t, line 97

This property tells us how complete the verb list is. By default, we'll assume that the instructions fail to disclose every required verb in the game, because the generic set we use here doesn't even try to anticipate the special verbs that most games include. If you provide your own list of game-specific verbs, and your custom list (taken together with the generic list) discloses every verb required to complete the game, you should set this property to true; if you set this to true, the instructions will assure the player that they will not need to think of any verbs besides the ones listed in the instructions. Authors are strongly encouraged to disclose a list of verbs that is sufficient by itself to complete the game, and to set this property to true once they've done so.


### `conversationAbbr`

Defined in instruct.t, line 129

conversation verb abbreviations


### `conversationInstructions`

Defined in instruct.t, line 219

Conversation system description. Several different conversation systems have come into relatively widespread use, so there isn't any single convention that's generic enough that we can assume it holds for all games. In deference to this variability, we provide this hook to make it easy to replace the instructions pertaining to the conversation system. If the game uses the standard ASK/TELL system, it can leave this list unchanged; if the game uses a different system, it can replace this with its own instructions.


### `conversationVerbs`

Defined in instruct.t, line 118

Verbs relating specifically to character interaction. This is in the same format as customVerbs, and has essentially the same purpose; however, we call these out separately to allow each game not only to supplement the default list we provide but to replace our default list. This is desirable for conversation-related commands in particular because some games will not use the ASK/TELL conversation system at all and will thus want to remove any mention of the standard set of verbs.


### `crueltyLevel`

Defined in instruct.t, line 188

This property should be set on a game-by-game basis to indicate the "cruelty level" of the game, which is a rough estimation of how likely it is that the player will encounter an unwinnable position in the game.


### `customVerbs`

Defined in instruct.t, line 106

A list of custom verbs. Each game should set this to a list of single-quoted strings; each string gives an example of a verb to display in the list of sample verbs. Something like this:


### `includeInUndo` *(overridden)*

Defined in instruct.t, line 992


### `isRealTime`

Defined in instruct.t, line 195

Does this game have any real-time features? If so, set this to true. By default, we'll explain that game time passes only in response to command input.


### `isRepeatable` *(overridden)*

Defined in instruct.t, line 991

INSTRUCTIONS doesn't affect UNDO or AGAIN


### `truncationLength`

Defined in instruct.t, line 141

Truncation length. If the game's parser allows words to be abbreviated to some minimum number of letters, this should indicate the minimum length. The English parser uses a truncation length of 6 letters by default.


## Inherited Properties


*From [SystemAction](systemaction.md):* [`actionTime`](systemaction.md#actionTime)


*From [Action](action.md):* [`afterActionMainList`](action.md#afterActionMainList), [`beforeAfterObjs`](action.md#beforeAfterObjs), [`defaultForRecursion`](action.md#defaultForRecursion), [`extraMessageParams`](action.md#extraMessageParams), [`implicitMsg`](action.md#implicitMsg), [`isImplicit`](action.md#isImplicit), [`iterationCanceled`](action.md#iterationCanceled), [`originalAction`](action.md#originalAction), [`parentAction`](action.md#parentAction), [`preCond`](action.md#preCond), [`predicateNounPhrases`](action.md#predicateNounPhrases), [`pronounOverride`](action.md#pronounOverride), [`remappedFrom`](action.md#remappedFrom), [`showDefaultReports`](action.md#showDefaultReports), [`synthParamID`](action.md#synthParamID), [`verbFlags`](action.md#verbFlags), [`verifiedOkay`](action.md#verifiedOkay)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execSystemAction` *(overridden)*

Defined in instruct.t, line 299

execute the command


### `showAbbrevChapter`

Defined in instruct.t, line 547

Abbreviations chapter


### `showAdvancedCmdChapter`

Defined in instruct.t, line 870

Advance Command Formats chapter


### `showAmbiguousCmdChapter`

Defined in instruct.t, line 831

Ambiguous Commands chapter


### `showCommandsChapter`

Defined in instruct.t, line 432

Entering Commands chapter


### `showConversationChapter`

Defined in instruct.t, line 659

show the Conversation chapter


### `showInstructions`

Defined in instruct.t, line 337

Show the instructions as a standard text display. Give the user the option of turning on a SCRIPT file to capture the text.


### `showObjectsChapter`

Defined in instruct.t, line 632

Objects chapter


### `showSaveRestoreChapter`

Defined in instruct.t, line 698

Saving, Restoring, and Undo chapter


### `showSpecialCmdChapter`

Defined in instruct.t, line 770

Other Special Commands chapter


### `showTimeChapter`

Defined in instruct.t, line 670

Time chapter


### `showTipsChapter`

Defined in instruct.t, line 933

General Tips chapter


### `showTravelChapter`

Defined in instruct.t, line 586

Travel chapter


### `showUnknownWordsChapter`

Defined in instruct.t, line 816

Unknown Words chapter


## Inherited Methods


*From [SystemAction](systemaction.md):* [`execAction`](systemaction.md#execAction), [`getInputFile`](systemaction.md#getInputFile)


*From [IAction](iaction.md):* [`doActionMain`](iaction.md#doActionMain), [`resolveNouns`](iaction.md#resolveNouns)


<details><summary>From [Action](action.md) (100)</summary>

[`actionOfKind`](action.md#actionOfKind), [`addBeforeAfterObj`](action.md#addBeforeAfterObj), [`afterAction`](action.md#afterAction), [`afterActionMain`](action.md#afterActionMain), [`announceActionObject`](action.md#announceActionObject), [`announceAllDefaultObjects`](action.md#announceAllDefaultObjects), [`announceDefaultObject`](action.md#announceDefaultObject), [`beforeAction`](action.md#beforeAction), [`beforeActionMain`](action.md#beforeActionMain), [`cacheMultiObjectAnnouncements`](action.md#cacheMultiObjectAnnouncements), [`callAfterActionMain`](action.md#callAfterActionMain), [`callCatchAllProp`](action.md#callCatchAllProp), [`callPreConditions`](action.md#callPreConditions), [`callVerifyPreCond`](action.md#callVerifyPreCond), [`callVerifyProp`](action.md#callVerifyProp), [`cancelIteration`](action.md#cancelIteration), [`checkAction`](action.md#checkAction), [`checkPreConditions`](action.md#checkPreConditions), [`checkRemapping`](action.md#checkRemapping), [`combineRemappedVerifyResults`](action.md#combineRemappedVerifyResults), [`createActionFrom`](action.md#createActionFrom), [`createActionInstance`](action.md#createActionInstance), [`createTopicQualifierResolver`](action.md#createTopicQualifierResolver), [`doAction`](action.md#doAction), [`doActionOnce`](action.md#doActionOnce), [`filterAmbiguousWithVerify`](action.md#filterAmbiguousWithVerify), [`filterFacets`](action.md#filterFacets), [`filterPluralWithVerify`](action.md#filterPluralWithVerify), [`finishResolveList`](action.md#finishResolveList), [`getAnaphoricBinding`](action.md#getAnaphoricBinding), [`getCurrentObjects`](action.md#getCurrentObjects), [`getDefaultWithVerify`](action.md#getDefaultWithVerify), [`getEnteredVerbPhrase`](action.md#getEnteredVerbPhrase), [`getImplicitPhrase`](action.md#getImplicitPhrase), [`getInfPhrase`](action.md#getInfPhrase), [`getMatchForRole`](action.md#getMatchForRole), [`getMessageParam`](action.md#getMessageParam), [`getNotifyTable`](action.md#getNotifyTable), [`getObjectForRole`](action.md#getObjectForRole), [`getObjPreCondDescList`](action.md#getObjPreCondDescList), [`getObjPreConditions`](action.md#getObjPreConditions), [`getObjResponseProd`](action.md#getObjResponseProd), [`getOriginalAction`](action.md#getOriginalAction), [`getOrigTokenList`](action.md#getOrigTokenList), [`getOtherObjectRole`](action.md#getOtherObjectRole), [`getParticiplePhrase`](action.md#getParticiplePhrase), [`getPreCondDescList`](action.md#getPreCondDescList), [`getPreCondPropForRole`](action.md#getPreCondPropForRole), [`getPredicate`](action.md#getPredicate), [`getPronounOverride`](action.md#getPronounOverride), [`getQuestionInf`](action.md#getQuestionInf), [`getRemappedFrom`](action.md#getRemappedFrom), [`getRemapPropForRole`](action.md#getRemapPropForRole), [`getResolvedObjList`](action.md#getResolvedObjList), [`getResolveInfo`](action.md#getResolveInfo), [`getRoleFromIndex`](action.md#getRoleFromIndex), [`getSimpleSynonymRemap`](action.md#getSimpleSynonymRemap), [`getSortedVerifyResults`](action.md#getSortedVerifyResults), [`getVerbPhrase`](action.md#getVerbPhrase), [`getVerifyPropForRole`](action.md#getVerifyPropForRole), [`initTentative`](action.md#initTentative), [`isConversational`](action.md#isConversational), [`isNestedIn`](action.md#isNestedIn), [`isPartOf`](action.md#isPartOf), [`isRemapped`](action.md#isRemapped), [`makeResolveInfo`](action.md#makeResolveInfo), [`makeResolveInfoList`](action.md#makeResolveInfoList), [`maybeAnnounceDefaultObject`](action.md#maybeAnnounceDefaultObject), [`maybeAnnounceImplicit`](action.md#maybeAnnounceImplicit), [`maybeAnnounceMultiObject`](action.md#maybeAnnounceMultiObject), [`noMatch`](action.md#noMatch), [`notifyBeforeAfter`](action.md#notifyBeforeAfter), [`objListPronoun`](action.md#objListPronoun), [`preAnnounceActionObject`](action.md#preAnnounceActionObject), [`recalcSenseContext`](action.md#recalcSenseContext), [`repeatAction`](action.md#repeatAction), [`resetAction`](action.md#resetAction), [`resolveAction`](action.md#resolveAction), [`resolvedObjectsInScope`](action.md#resolvedObjectsInScope), [`runBeforeNotifiers`](action.md#runBeforeNotifiers), [`saveActionForAgain`](action.md#saveActionForAgain), [`setCurrentObjects`](action.md#setCurrentObjects), [`setImplicit`](action.md#setImplicit), [`setMessageParam`](action.md#setMessageParam), [`setMessageParams`](action.md#setMessageParams), [`setNested`](action.md#setNested), [`setObjectMatches`](action.md#setObjectMatches), [`setOriginalAction`](action.md#setOriginalAction), [`setPronounOverride`](action.md#setPronounOverride), [`setRemapped`](action.md#setRemapped), [`setResolvedObjects`](action.md#setResolvedObjects), [`spPrefix`](action.md#spPrefix), [`spSuffix`](action.md#spSuffix), [`synthMessageParam`](action.md#synthMessageParam), [`verifyAction`](action.md#verifyAction), [`verifyHandlersExist`](action.md#verifyHandlersExist), [`whatObj`](action.md#whatObj), [`whatTranslate`](action.md#whatTranslate), [`withVerifyResults`](action.md#withVerifyResults), [`zeroActionTime`](action.md#zeroActionTime)

</details>


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
