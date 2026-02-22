# DisambigResults

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 534)


A disambiguation results gatherer object. We use this to manage the results of resolution of a disambiguation response.


**Superclass chain:** [BasicResolveResults](basicresolveresults.md) > [ResolveResults](resolveresults.md) > `object` > **DisambigResults**


## Inherited Properties


*From [BasicResolveResults](basicresolveresults.md):* [`allowActionRemapping`](basicresolveresults.md#allowActionRemapping), [`allowEquivalentFiltering`](basicresolveresults.md#allowEquivalentFiltering), [`issuingActor_`](basicresolveresults.md#issuingActor_), [`targetActor_`](basicresolveresults.md#targetActor_)


## Methods


### `ambiguousNounPhrase(keeper, asker, txt, matchList, fullMatchList, scopeList, requiredNum, resolver)` *(overridden)*

Defined in disambig.t, line 541

copy the actor information from the parent resolver


### `construct(parent)`

Defined in disambig.t, line 535


### `noMatch(action, txt)` *(overridden)*

Defined in disambig.t, line 585

show a message on not matching an object - for a disambiguation response, failing to match means that the combination of the disambiguation response plus the original text doesn't name any objects, not that the object in the response itself isn't present


### `noMatchForPossessive(owner, txt)` *(overridden)*

Defined in disambig.t, line 602

throw an error indicating the problem


### `noMatchPoss(action, txt)`

Defined in disambig.t, line 591

throw an error indicating the problem


### `noteOrdinalOutOfRange(ord)`

Defined in disambig.t, line 573

note the an ordinal response is out of range


### `noVocabMatch(action, txt)` *(overridden)*

Defined in disambig.t, line 596


## Inherited Methods


<details><summary>From [BasicResolveResults](basicresolveresults.md) (39)</summary>

[`allNotAllowed`](basicresolveresults.md#allNotAllowed), [`askMissingLiteral`](basicresolveresults.md#askMissingLiteral), [`askMissingObject`](basicresolveresults.md#askMissingObject), [`beginSingleObjSlot`](basicresolveresults.md#beginSingleObjSlot), [`beginTopicSlot`](basicresolveresults.md#beginTopicSlot), [`canResolveInteractively`](basicresolveresults.md#canResolveInteractively), [`emptyNounPhrase`](basicresolveresults.md#emptyNounPhrase), [`endSingleObjSlot`](basicresolveresults.md#endSingleObjSlot), [`endTopicSlot`](basicresolveresults.md#endTopicSlot), [`filterWithDistinguisher`](basicresolveresults.md#filterWithDistinguisher), [`getImpliedObject`](basicresolveresults.md#getImpliedObject), [`incCommandCount`](basicresolveresults.md#incCommandCount), [`insufficientQuantity`](basicresolveresults.md#insufficientQuantity), [`noMatchForAll`](basicresolveresults.md#noMatchForAll), [`noMatchForAllBut`](basicresolveresults.md#noMatchForAllBut), [`noMatchForListBut`](basicresolveresults.md#noMatchForListBut), [`noMatchForLocation`](basicresolveresults.md#noMatchForLocation), [`noMatchForPronoun`](basicresolveresults.md#noMatchForPronoun), [`noMatchPossessive`](basicresolveresults.md#noMatchPossessive), [`noteActorSpecified`](basicresolveresults.md#noteActorSpecified), [`noteAdjEnding`](basicresolveresults.md#noteAdjEnding), [`noteBadPrep`](basicresolveresults.md#noteBadPrep), [`noteEmptyBut`](basicresolveresults.md#noteEmptyBut), [`noteIndefinite`](basicresolveresults.md#noteIndefinite), [`noteLiteral`](basicresolveresults.md#noteLiteral), [`noteMatches`](basicresolveresults.md#noteMatches), [`noteMiscWordList`](basicresolveresults.md#noteMiscWordList), [`noteNounSlots`](basicresolveresults.md#noteNounSlots), [`notePlural`](basicresolveresults.md#notePlural), [`notePronoun`](basicresolveresults.md#notePronoun), [`noteWeakPhrasing`](basicresolveresults.md#noteWeakPhrasing), [`nothingInLocation`](basicresolveresults.md#nothingInLocation), [`reflexiveNotAllowed`](basicresolveresults.md#reflexiveNotAllowed), [`setActors`](basicresolveresults.md#setActors), [`singleObjectRequired`](basicresolveresults.md#singleObjectRequired), [`uniqueObjectRequired`](basicresolveresults.md#uniqueObjectRequired), [`unknownNounPhrase`](basicresolveresults.md#unknownNounPhrase), [`wrongReflexive`](basicresolveresults.md#wrongReflexive), [`zeroQuantity`](basicresolveresults.md#zeroQuantity)

</details>
