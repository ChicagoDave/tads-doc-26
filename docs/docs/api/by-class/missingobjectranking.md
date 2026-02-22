# MissingObjectRanking

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4743)


Missing-object response ranker.


**Superclass chain:** [CommandRanking](commandranking.md) > [ResolveResults](resolveresults.md) > `object` > **MissingObjectRanking**


## Properties


### `nounSlotCount` *(overridden)*

Defined in parser.t, line 4749

missing-object responses have no verb, so they won't count any noun slots; we just need to give these an arbitrary value so that we can compare them (and find them equal)


## Inherited Properties


*From [CommandRanking](commandranking.md):* [`actorSpecifiedCount`](commandranking.md#actorSpecifiedCount), [`allExcludedCount`](commandranking.md#allExcludedCount), [`allowActionRemapping`](commandranking.md#allowActionRemapping), [`ambigCount`](commandranking.md#ambigCount), [`commandCount`](commandranking.md#commandCount), [`emptyButCount`](commandranking.md#emptyButCount), [`endAdjCount`](commandranking.md#endAdjCount), [`indefiniteCount`](commandranking.md#indefiniteCount), [`inSingleObjSlot`](commandranking.md#inSingleObjSlot), [`insufficientCount`](commandranking.md#insufficientCount), [`inTopicSlot`](commandranking.md#inTopicSlot), [`listForSingle`](commandranking.md#listForSingle), [`literalLength`](commandranking.md#literalLength), [`match`](commandranking.md#match), [`miscWordListCount`](commandranking.md#miscWordListCount), [`missingCount`](commandranking.md#missingCount), [`nonMatchCount`](commandranking.md#nonMatchCount), [`nonMatchPossCount`](commandranking.md#nonMatchPossCount), [`pluralTruncCount`](commandranking.md#pluralTruncCount), [`pronounCount`](commandranking.md#pronounCount), [`rankingCriteria`](commandranking.md#rankingCriteria), [`tokCount`](commandranking.md#tokCount), [`truncCount`](commandranking.md#truncCount), [`unknownWordCount`](commandranking.md#unknownWordCount), [`unwantedPluralCount`](commandranking.md#unwantedPluralCount), [`vocabNonMatchCount`](commandranking.md#vocabNonMatchCount), [`weaknessLevel`](commandranking.md#weaknessLevel)


## Inherited Methods


<details><summary>From [CommandRanking](commandranking.md) (43)</summary>

[`allNotAllowed`](commandranking.md#allNotAllowed), [`ambiguousNounPhrase`](commandranking.md#ambiguousNounPhrase), [`askMissingObject`](commandranking.md#askMissingObject), [`beginSingleObjSlot`](commandranking.md#beginSingleObjSlot), [`beginTopicSlot`](commandranking.md#beginTopicSlot), [`calcRanking`](commandranking.md#calcRanking), [`compareRanking`](commandranking.md#compareRanking), [`construct`](commandranking.md#construct), [`emptyNounPhrase`](commandranking.md#emptyNounPhrase), [`endSingleObjSlot`](commandranking.md#endSingleObjSlot), [`endTopicSlot`](commandranking.md#endTopicSlot), [`getImpliedObject`](commandranking.md#getImpliedObject), [`incCommandCount`](commandranking.md#incCommandCount), [`insufficientQuantity`](commandranking.md#insufficientQuantity), [`noMatch`](commandranking.md#noMatch), [`noMatchForAll`](commandranking.md#noMatchForAll), [`noMatchForAllBut`](commandranking.md#noMatchForAllBut), [`noMatchForListBut`](commandranking.md#noMatchForListBut), [`noMatchForLocation`](commandranking.md#noMatchForLocation), [`noMatchForPossessive`](commandranking.md#noMatchForPossessive), [`noMatchForPronoun`](commandranking.md#noMatchForPronoun), [`noMatchPossessive`](commandranking.md#noMatchPossessive), [`noteActorSpecified`](commandranking.md#noteActorSpecified), [`noteAdjEnding`](commandranking.md#noteAdjEnding), [`noteBadPrep`](commandranking.md#noteBadPrep), [`noteEmptyBut`](commandranking.md#noteEmptyBut), [`noteIndefinite`](commandranking.md#noteIndefinite), [`noteLiteral`](commandranking.md#noteLiteral), [`noteMatches`](commandranking.md#noteMatches), [`noteMiscWordList`](commandranking.md#noteMiscWordList), [`noteNounSlots`](commandranking.md#noteNounSlots), [`notePlural`](commandranking.md#notePlural), [`notePronoun`](commandranking.md#notePronoun), [`noteWeakPhrasing`](commandranking.md#noteWeakPhrasing), [`nothingInLocation`](commandranking.md#nothingInLocation), [`noVocabMatch`](commandranking.md#noVocabMatch), [`reflexiveNotAllowed`](commandranking.md#reflexiveNotAllowed), [`singleObjectRequired`](commandranking.md#singleObjectRequired), [`sortByRanking`](commandranking.md#sortByRanking), [`uniqueObjectRequired`](commandranking.md#uniqueObjectRequired), [`unknownNounPhrase`](commandranking.md#unknownNounPhrase), [`wrongReflexive`](commandranking.md#wrongReflexive), [`zeroQuantity`](commandranking.md#zeroQuantity)

</details>
