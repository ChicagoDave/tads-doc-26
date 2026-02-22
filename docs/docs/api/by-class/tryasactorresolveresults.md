# TryAsActorResolveResults

*class* — defined in [parser.t](../by-file/parser.t.md) (line 5753)


A results object for resolving an actor in a command with an unknown word or invalid phrasing in the predicate. For this type of resolution, we're trying to interpret the actor portion of the command as a noun phrase referring to an actor, but it could also just be another command. E.g., we could have "bob, asdf" or "east, asdf". Since we're only tentatively interpreting the phrase as a noun phrase, to see if that interpretation goes anywhere, we don't want to throw any errors on failures; instead we simply allow empty match lists.


**Superclass chain:** [ResolveResults](resolveresults.md) > `object` > **TryAsActorResolveResults**


## Properties


### `allowActionRemapping`

Defined in parser.t, line 5795


### `allowEquivalentFiltering`

Defined in parser.t, line 5796


## Methods


### `allNotAllowed`

Defined in parser.t, line 5762


### `ambiguousNounPhrase(keeper, askwer, txt, matchLst, fullMatchLst, scopeList, requiredNum, resolver)`

Defined in parser.t, line 5769


### `askMissingLiteral(action, which)`

Defined in parser.t, line 5775


### `askMissingObject(asker, resolver, responseProd)`

Defined in parser.t, line 5773


### `beginSingleObjSlot`

Defined in parser.t, line 5787


### `beginTopicSlot`

Defined in parser.t, line 5789


### `emptyNounPhrase(resolver)`

Defined in parser.t, line 5776


### `endSingleObjSlot`

Defined in parser.t, line 5788


### `endTopicSlot`

Defined in parser.t, line 5790


### `getImpliedObject(np, resolver)`

Defined in parser.t, line 5772


### `incCommandCount`

Defined in parser.t, line 5791


### `insufficientQuantity(txt, matchList, requiredNum)`

Defined in parser.t, line 5778


### `noMatch(action, txt)`

Defined in parser.t, line 5755


### `noMatchForAll`

Defined in parser.t, line 5757


### `noMatchForAllBut`

Defined in parser.t, line 5758


### `noMatchForListBut`

Defined in parser.t, line 5759


### `noMatchForLocation(loc, txt)`

Defined in parser.t, line 5766


### `noMatchForPossessive(owner, txt)`

Defined in parser.t, line 5765


### `noMatchForPronoun`

Defined in parser.t, line 5761


### `noMatchPossessive(action, txt)`

Defined in parser.t, line 5756


### `noteActorSpecified`

Defined in parser.t, line 5792


### `noteAdjEnding`

Defined in parser.t, line 5781


### `noteBadPrep`

Defined in parser.t, line 5767


### `noteEmptyBut`

Defined in parser.t, line 5760


### `noteIndefinite`

Defined in parser.t, line 5782


### `noteLiteral(txt)`

Defined in parser.t, line 5774


### `noteMatches(matchList)`

Defined in parser.t, line 5783


### `noteMiscWord(txt)`

Defined in parser.t, line 5784


### `noteNounSlots(cnt)`

Defined in parser.t, line 5793


### `notePlural`

Defined in parser.t, line 5786


### `notePronoun`

Defined in parser.t, line 5785


### `noteWeakPhrasing`

Defined in parser.t, line 5794


### `nothingInLocation(loc)`

Defined in parser.t, line 5768


### `noVocabMatch(action, txt)`

Defined in parser.t, line 5754


### `reflexiveNotAllowed`

Defined in parser.t, line 5763


### `singleObjectRequired(txt)`

Defined in parser.t, line 5780


### `uniqueObjectRequired(txt, matchList)`

Defined in parser.t, line 5779


### `unknownNounPhrase(match, resolver)`

Defined in parser.t, line 5771


### `wrongReflexive(typ, txt)`

Defined in parser.t, line 5764


### `zeroQuantity(txt)`

Defined in parser.t, line 5777
