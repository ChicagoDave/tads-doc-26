# DisambigRanking

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 282)


Disambiguation Ranking. This is a special version of the command ranker that we use to rank the intepretations of a disambiguation response.


**Superclass chain:** [CommandRanking](commandranking.md) > [ResolveResults](resolveresults.md) > `object` > **DisambigRanking**


## Properties


### `disambigOrdinalCount`

Defined in disambig.t, line 319

number of list ordinals in the match


### `nounSlotCount` *(overridden)*

Defined in disambig.t, line 325

disambiguation commands have no verbs, so there's no verb structure to rank; so just use an arbitrary noun slot count


### `rankingCriteria` *(overridden)*

Defined in disambig.t, line 295

Add the ordinal count ranking criterion at the end of the inherited list of ranking criteria. If we can't find any differences on the basis of the other criteria, choose the interpretation that uses fewer ordinal phrases. (We prefer an non-ordinal interpretation, because this will prefer matches to explicit vocabulary for objects over matches for generic ordinals.)


## Inherited Properties


*From [CommandRanking](commandranking.md):* [`actorSpecifiedCount`](commandranking.md#actorSpecifiedCount), [`allExcludedCount`](commandranking.md#allExcludedCount), [`allowActionRemapping`](commandranking.md#allowActionRemapping), [`ambigCount`](commandranking.md#ambigCount), [`commandCount`](commandranking.md#commandCount), [`emptyButCount`](commandranking.md#emptyButCount), [`endAdjCount`](commandranking.md#endAdjCount), [`indefiniteCount`](commandranking.md#indefiniteCount), [`inSingleObjSlot`](commandranking.md#inSingleObjSlot), [`insufficientCount`](commandranking.md#insufficientCount), [`inTopicSlot`](commandranking.md#inTopicSlot), [`listForSingle`](commandranking.md#listForSingle), [`literalLength`](commandranking.md#literalLength), [`match`](commandranking.md#match), [`miscWordListCount`](commandranking.md#miscWordListCount), [`missingCount`](commandranking.md#missingCount), [`nonMatchCount`](commandranking.md#nonMatchCount), [`nonMatchPossCount`](commandranking.md#nonMatchPossCount), [`pluralTruncCount`](commandranking.md#pluralTruncCount), [`pronounCount`](commandranking.md#pronounCount), [`tokCount`](commandranking.md#tokCount), [`truncCount`](commandranking.md#truncCount), [`unknownWordCount`](commandranking.md#unknownWordCount), [`unwantedPluralCount`](commandranking.md#unwantedPluralCount), [`vocabNonMatchCount`](commandranking.md#vocabNonMatchCount), [`weaknessLevel`](commandranking.md#weaknessLevel)


## Methods


### `noteDisambigOrdinal`

Defined in disambig.t, line 312

note a list ordinal (i.e., "the first one" to refer to the first item in the ambiguous list) - we take list ordinals as less desirable than treating ordinal words as adjectives or nouns


### `noteOrdinalOutOfRange(ord)`

Defined in disambig.t, line 301

note the an ordinal response is out of range


## Inherited Methods


<details><summary>From [CommandRanking](commandranking.md) (43)</summary>

[`allNotAllowed`](commandranking.md#allNotAllowed), [`ambiguousNounPhrase`](commandranking.md#ambiguousNounPhrase), [`askMissingObject`](commandranking.md#askMissingObject), [`beginSingleObjSlot`](commandranking.md#beginSingleObjSlot), [`beginTopicSlot`](commandranking.md#beginTopicSlot), [`calcRanking`](commandranking.md#calcRanking), [`compareRanking`](commandranking.md#compareRanking), [`construct`](commandranking.md#construct), [`emptyNounPhrase`](commandranking.md#emptyNounPhrase), [`endSingleObjSlot`](commandranking.md#endSingleObjSlot), [`endTopicSlot`](commandranking.md#endTopicSlot), [`getImpliedObject`](commandranking.md#getImpliedObject), [`incCommandCount`](commandranking.md#incCommandCount), [`insufficientQuantity`](commandranking.md#insufficientQuantity), [`noMatch`](commandranking.md#noMatch), [`noMatchForAll`](commandranking.md#noMatchForAll), [`noMatchForAllBut`](commandranking.md#noMatchForAllBut), [`noMatchForListBut`](commandranking.md#noMatchForListBut), [`noMatchForLocation`](commandranking.md#noMatchForLocation), [`noMatchForPossessive`](commandranking.md#noMatchForPossessive), [`noMatchForPronoun`](commandranking.md#noMatchForPronoun), [`noMatchPossessive`](commandranking.md#noMatchPossessive), [`noteActorSpecified`](commandranking.md#noteActorSpecified), [`noteAdjEnding`](commandranking.md#noteAdjEnding), [`noteBadPrep`](commandranking.md#noteBadPrep), [`noteEmptyBut`](commandranking.md#noteEmptyBut), [`noteIndefinite`](commandranking.md#noteIndefinite), [`noteLiteral`](commandranking.md#noteLiteral), [`noteMatches`](commandranking.md#noteMatches), [`noteMiscWordList`](commandranking.md#noteMiscWordList), [`noteNounSlots`](commandranking.md#noteNounSlots), [`notePlural`](commandranking.md#notePlural), [`notePronoun`](commandranking.md#notePronoun), [`noteWeakPhrasing`](commandranking.md#noteWeakPhrasing), [`nothingInLocation`](commandranking.md#nothingInLocation), [`noVocabMatch`](commandranking.md#noVocabMatch), [`reflexiveNotAllowed`](commandranking.md#reflexiveNotAllowed), [`singleObjectRequired`](commandranking.md#singleObjectRequired), [`sortByRanking`](commandranking.md#sortByRanking), [`uniqueObjectRequired`](commandranking.md#uniqueObjectRequired), [`unknownNounPhrase`](commandranking.md#unknownNounPhrase), [`wrongReflexive`](commandranking.md#wrongReflexive), [`zeroQuantity`](commandranking.md#zeroQuantity)

</details>
