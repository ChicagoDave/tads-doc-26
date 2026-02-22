# CommandRanking

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6099)


Production match ranking object. We create one of these objects for each match tree that we wish to rank.


**Superclass chain:** [ResolveResults](resolveresults.md) > `object` > **CommandRankingSubclasses:** [DisambigRanking](disambigranking.md), [MissingObjectRanking](missingobjectranking.md), [OopsResults](oopsresults.md)


## Properties


### `actorSpecifiedCount`

Defined in parser.t, line 6384

an actor is specified


### `allExcludedCount`

Defined in parser.t, line 6357

number of "all" or "any" lists totally excluded by "but"


### `allowActionRemapping`

Defined in parser.t, line 6714

don't allow action remapping while ranking


### `ambigCount`

Defined in parser.t, line 6378

number of ambiguous noun phrases


### `commandCount`

Defined in parser.t, line 6381

number of subcommands in the command


### `emptyButCount`

Defined in parser.t, line 6354

number of empty "but" lists


### `endAdjCount`

Defined in parser.t, line 6366

number of phrases ending in adjectives


### `indefiniteCount`

Defined in parser.t, line 6369

number of phrases with indefinite noun phrase structure


### `inSingleObjSlot`

Defined in parser.t, line 6663


### `insufficientCount`

Defined in parser.t, line 6348

number of phrases requiring quantity higher than can be fulfilled


### `inTopicSlot`

Defined in parser.t, line 6667


### `listForSingle`

Defined in parser.t, line 6351

number of noun lists in single-noun slots


### `literalLength`

Defined in parser.t, line 6390

total character length of literal text phrases


### `match`

Defined in parser.t, line 6316

the match tree I'm ranking


### `miscWordListCount`

Defined in parser.t, line 6372

number of miscellaneous word lists as noun phrases


### `missingCount`

Defined in parser.t, line 6360

missing phrases (structurally omitted, as in "put book")


### `nonMatchCount`

Defined in parser.t, line 6338

number of noun phrases matching nothing in scope


### `nonMatchPossCount`

Defined in parser.t, line 6345

Number of possessive-qualified noun phrases matching nothing in scope. For example, "bob's desk" when there's no desk in scope (Bob's or otherwise).


### `nounSlotCount`

Defined in parser.t, line 6332

The number of structural "noun phrase slots" in the verb. An intransitive verb has no noun phrase slots; a transitive verb with a direct object has one; a verb with a direct and indirect object has two slots.


### `pluralTruncCount`

Defined in parser.t, line 6363

number of truncated plurals


### `pronounCount`

Defined in parser.t, line 6393

number of pronoun phrases


### `rankingCriteria`

Defined in parser.t, line 6292

Our list of ranking criteria. This is a list of CommandRankingCriterion objects. The list is given in order of importance: the first criterion is the most important, so if it can discriminate the two match trees, we use its result; if the first criterion can't tell any difference, then we move on to the second criterion; and so on through the list.


### `tokCount`

Defined in parser.t, line 6319

the number of tokens my match tree consumes


### `truncCount`

Defined in parser.t, line 6375

number of truncated words overall


### `unknownWordCount`

Defined in parser.t, line 6387

unknown words


### `unwantedPluralCount`

Defined in parser.t, line 6399

number of plural phrases encountered in single-object slots


### `vocabNonMatchCount`

Defined in parser.t, line 6335

number of noun phrases matching nothing anywhere in the game


### `weaknessLevel`

Defined in parser.t, line 6396

weakness level (for noteWeakPhrasing)


## Methods


### `allNotAllowed`

Defined in parser.t, line 6432

note that we have an unmatched possessive-qualified noun phrase


### `ambiguousNounPhrase(keeper, asker, txt, matchList, fullMatchList, scopeList, requiredNum, resolver)`

Defined in parser.t, line 6503

treat this as any other noun phrase that matches nothing


### `askMissingObject(asker, resolver, responseProd)`

Defined in parser.t, line 6566

count the missing object phrase


### `beginSingleObjSlot`

Defined in parser.t, line 6661

if this object was matched with a truncated plural, note it


### `beginTopicSlot`

Defined in parser.t, line 6665


### `calcRanking(resolveArguments)`

Defined in parser.t, line 6146

calculate my ranking


### `compareRanking(other)`

Defined in parser.t, line 6173

Compare two production list entries for ranking purposes. Returns a negative number if this one ranks worse than the other, 0 if they have the same ranking, or a positive number if this one ranks better than the other one.


### `construct(match)`

Defined in parser.t, line 6136

create a new entry


### `emptyNounPhrase(resolver)`

Defined in parser.t, line 6582

add the length of this literal to the total literal length


### `endSingleObjSlot`

Defined in parser.t, line 6662


### `endTopicSlot`

Defined in parser.t, line 6666


### `getImpliedObject(np, resolver)`

Defined in parser.t, line 6559

return the results


### `incCommandCount`

Defined in parser.t, line 6682

If we're resolving a single-object slot, we want to avoid plurals, since they could resolve to multiple objects as though we'd typed a list of objects here. This isn't a problem for topics, though, since a topic slot isn't iterated for execution.


### `insufficientQuantity(txt, matchList, requiredNum)`

Defined in parser.t, line 6595

treat this as a non-matching noun phrase


### `noMatch(action, txt)`

Defined in parser.t, line 6419

note the unknown phrase


### `noMatchForAll`

Defined in parser.t, line 6438

treat this as a non-matching noun phrase


### `noMatchForAllBut`

Defined in parser.t, line 6450

note it


### `noMatchForListBut`

Defined in parser.t, line 6456

count the total exclusion


### `noMatchForLocation(loc, txt)`

Defined in parser.t, line 6486

treat this as any other noun phrase that matches nothing


### `noMatchForPossessive(owner, txt)`

Defined in parser.t, line 6480

treat this as any other noun phrase that matches nothing


### `noMatchForPronoun(typ, txt)`

Defined in parser.t, line 6462

treat this as any other noun phrase that matches nothing


### `noMatchPossessive(action, txt)`

Defined in parser.t, line 6425

note that we have a noun phrase that matches nothing


### `noteActorSpecified`

Defined in parser.t, line 6688

increase our subcommand counter


### `noteAdjEnding`

Defined in parser.t, line 6615

ignore this for now - we might get a unique object via disambiguation during the execution phase


### `noteBadPrep`

Defined in parser.t, line 6492

treat this as any other noun phrase that matches nothing


### `noteEmptyBut`

Defined in parser.t, line 6444

treat this as any other noun phrase that matches nothing


### `noteIndefinite`

Defined in parser.t, line 6621

count it


### `noteLiteral(txt)`

Defined in parser.t, line 6576

no need to do anything here - we'll count the missing object in getImpliedObject, and we don't want to ask for anything interactively at this point


### `noteMatches(matchList)`

Defined in parser.t, line 6642

note the presence of a pronoun


### `noteMiscWordList(txt)`

Defined in parser.t, line 6627

count it


### `noteNounSlots(cnt)`

Defined in parser.t, line 6694

note it


### `notePlural`

Defined in parser.t, line 6669


### `notePronoun`

Defined in parser.t, line 6636

count this as a literal as well


### `noteWeakPhrasing(level)`

Defined in parser.t, line 6707

If this is the first noun slot count we've received, remember it. If we already have a count, ignore the new one - we only want to consider the first verb phrase if there are multiple verb phrases, since we'll reconsider the next verb phrase when we're ready to execute it.


### `nothingInLocation(txt)`

Defined in parser.t, line 6497

don't do anything at this point


### `noVocabMatch(action, txt)`

Defined in parser.t, line 6413

ResolveResults implementation. We use this results receiver when we're comparing the semantic strengths of multiple structural matches, so we merely note each error condition without showing any message to the user or asking the user for any input. Once we've ranked all of the matches, we'll choose the one with the best attributes and then resolve it for real, at which point if we chose one with any errors, we'll finally get around to showing the errors to the user.


### `reflexiveNotAllowed(typ, txt)`

Defined in parser.t, line 6468

treat this as any other noun phrase that matches nothing


### `singleObjectRequired(txt)`

Defined in parser.t, line 6601

treat this as a non-matching noun phrase


### `sortByRanking(lst, [resolveArguments])`

Defined in parser.t, line 6108

Sort a list of productions, as returned from GrammarProd.parseTokens(), in descending order of command strength. We return a list of CommandRanking objects whose first element is the best command interpretation.


### `uniqueObjectRequired(txt, matchList)`

Defined in parser.t, line 6607

treat this as a non-matching noun phrase


### `unknownNounPhrase(match, resolver)`

Defined in parser.t, line 6529

return the abbreviated list


### `wrongReflexive(typ, txt)`

Defined in parser.t, line 6474

treat this as any other noun phrase that matches nothing


### `zeroQuantity(txt)`

Defined in parser.t, line 6589

treat this as a non-matching noun phrase
