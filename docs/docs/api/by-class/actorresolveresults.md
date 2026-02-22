# ActorResolveResults

*class* — defined in [parser.t](../by-file/parser.t.md) (line 5703)


Specialized noun-phrase resolution results gatherer for resolving a command actor (i.e., the target actor of a command).


**Superclass chain:** [BasicResolveResults](basicresolveresults.md) > [ResolveResults](resolveresults.md) > `object` > **ActorResolveResults**


## Properties


### `allowActionRemapping` *(overridden)*

Defined in parser.t, line 5740

don't allow action remapping while resolving the actor


## Inherited Properties


*From [BasicResolveResults](basicresolveresults.md):* [`allowEquivalentFiltering`](basicresolveresults.md#allowEquivalentFiltering), [`issuingActor_`](basicresolveresults.md#issuingActor_), [`targetActor_`](basicresolveresults.md#targetActor_)


## Methods


### `construct`

Defined in parser.t, line 5704


### `getImpliedObject(np, resolver)` *(overridden)*

Defined in parser.t, line 5718

set the initial actor context to the PC - this type of resolver is set up to determine the actor context, so we don't usually know the actual actor context yet when setting up this resolver


### `singleObjectRequired(txt)` *(overridden)*

Defined in parser.t, line 5733

an actor phrase must address a single actor


### `uniqueObjectRequired(txt, matchList)` *(overridden)*

Defined in parser.t, line 5727

there's no default for the actor - it's usually simply a syntax error when the actor is omitted


## Inherited Methods


<details><summary>From [BasicResolveResults](basicresolveresults.md) (40)</summary>

[`allNotAllowed`](basicresolveresults.md#allNotAllowed), [`ambiguousNounPhrase`](basicresolveresults.md#ambiguousNounPhrase), [`askMissingLiteral`](basicresolveresults.md#askMissingLiteral), [`askMissingObject`](basicresolveresults.md#askMissingObject), [`beginSingleObjSlot`](basicresolveresults.md#beginSingleObjSlot), [`beginTopicSlot`](basicresolveresults.md#beginTopicSlot), [`canResolveInteractively`](basicresolveresults.md#canResolveInteractively), [`emptyNounPhrase`](basicresolveresults.md#emptyNounPhrase), [`endSingleObjSlot`](basicresolveresults.md#endSingleObjSlot), [`endTopicSlot`](basicresolveresults.md#endTopicSlot), [`filterWithDistinguisher`](basicresolveresults.md#filterWithDistinguisher), [`incCommandCount`](basicresolveresults.md#incCommandCount), [`insufficientQuantity`](basicresolveresults.md#insufficientQuantity), [`noMatch`](basicresolveresults.md#noMatch), [`noMatchForAll`](basicresolveresults.md#noMatchForAll), [`noMatchForAllBut`](basicresolveresults.md#noMatchForAllBut), [`noMatchForListBut`](basicresolveresults.md#noMatchForListBut), [`noMatchForLocation`](basicresolveresults.md#noMatchForLocation), [`noMatchForPossessive`](basicresolveresults.md#noMatchForPossessive), [`noMatchForPronoun`](basicresolveresults.md#noMatchForPronoun), [`noMatchPossessive`](basicresolveresults.md#noMatchPossessive), [`noteActorSpecified`](basicresolveresults.md#noteActorSpecified), [`noteAdjEnding`](basicresolveresults.md#noteAdjEnding), [`noteBadPrep`](basicresolveresults.md#noteBadPrep), [`noteEmptyBut`](basicresolveresults.md#noteEmptyBut), [`noteIndefinite`](basicresolveresults.md#noteIndefinite), [`noteLiteral`](basicresolveresults.md#noteLiteral), [`noteMatches`](basicresolveresults.md#noteMatches), [`noteMiscWordList`](basicresolveresults.md#noteMiscWordList), [`noteNounSlots`](basicresolveresults.md#noteNounSlots), [`notePlural`](basicresolveresults.md#notePlural), [`notePronoun`](basicresolveresults.md#notePronoun), [`noteWeakPhrasing`](basicresolveresults.md#noteWeakPhrasing), [`nothingInLocation`](basicresolveresults.md#nothingInLocation), [`noVocabMatch`](basicresolveresults.md#noVocabMatch), [`reflexiveNotAllowed`](basicresolveresults.md#reflexiveNotAllowed), [`setActors`](basicresolveresults.md#setActors), [`unknownNounPhrase`](basicresolveresults.md#unknownNounPhrase), [`wrongReflexive`](basicresolveresults.md#wrongReflexive), [`zeroQuantity`](basicresolveresults.md#zeroQuantity)

</details>
