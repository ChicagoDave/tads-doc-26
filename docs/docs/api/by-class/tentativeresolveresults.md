# TentativeResolveResults

*class* — defined in [action.t](../by-file/action.t.md) (line 3828)


"Tentative" noun resolver results gather. This type of results gatherer is used to perform a tentative pre-resolution of an object of a multi-object action.


**Superclass chain:** [ResolveResults](resolveresults.md) > `object` > **TentativeResolveResults**


## Properties


### `allowActionRemapping`

Defined in action.t, line 3864


### `allowEquivalentFiltering`

Defined in action.t, line 3872

during the tentative phase, keep all equivalents - we don't want to make any arbitrary choices among equivalents during this phase, because doing so could improperly force a choice among otherwise ambiguous resolutions to the other phrase


### `npMissing`

Defined in action.t, line 3912

flag: the noun phrase we're resolving is a missing noun phrase, which means that we'll ask for it to be filled in when we get around to resolving it for real


## Methods


### `ambiguousNounPhrase(keeper, asker, txt, matchList, fullMatchList, scopeList, requiredNum, resolver)`

Defined in action.t, line 3878

for ambiguous results, don't attempt to narrow things down - just keep the entire list


### `askMissingLiteral(action, which)`

Defined in action.t, line 3902

no interaction is allowed, so return no tokens if we need to ask for a literal


### `askMissingObject(asker, resolver, responseProd)`

Defined in action.t, line 3889

no interaction is allowed, so return nothing if we need to ask for a missing object


### `canResolveInteractively`

Defined in action.t, line 3905

no interaction is allowed during tentative resolution


### `construct(target, issuer)`

Defined in action.t, line 3829


### `emptyNounPhrase(resolver)`

Defined in action.t, line 3851


### `incCommandCount`

Defined in action.t, line 3860


### `insufficientQuantity(txt, matchList, requiredNum)`

Defined in action.t, line 3853


### `noMatch(action, txt)`

Defined in action.t, line 3835

ignore most resolution problems, since this is only a tentative resolution pass


### `noMatchForAll`

Defined in action.t, line 3838


### `noMatchForAllBut`

Defined in action.t, line 3840


### `noMatchForListBut`

Defined in action.t, line 3841


### `noMatchForLocation(loc, txt)`

Defined in action.t, line 3846


### `noMatchForPossessive(owner, txt)`

Defined in action.t, line 3845


### `noMatchForPronoun(typ, txt)`

Defined in action.t, line 3842


### `noMatchPoss(action, txt)`

Defined in action.t, line 3836


### `noteActorSpecified`

Defined in action.t, line 3861


### `noteAdjEnding`

Defined in action.t, line 3855


### `noteBadPrep`

Defined in action.t, line 3847


### `noteEmptyBut`

Defined in action.t, line 3839


### `noteIndefinite`

Defined in action.t, line 3856


### `noteLiteral(txt)`

Defined in action.t, line 3850


### `noteMatches(matchList)`

Defined in action.t, line 3859


### `noteMiscWordList(txt)`

Defined in action.t, line 3857


### `noteNounSlots(cnt)`

Defined in action.t, line 3862


### `notePronoun`

Defined in action.t, line 3858


### `noteWeakPhrasing(level)`

Defined in action.t, line 3863


### `nothingInLocation(loc)`

Defined in action.t, line 3848


### `noVocabMatch(action, txt)`

Defined in action.t, line 3837


### `reflexiveNotAllowed(typ, txt)`

Defined in action.t, line 3843


### `uniqueObjectRequired(txt, matchList)`

Defined in action.t, line 3854


### `unknownNounPhrase(match, resolver)`

Defined in action.t, line 3849


### `wrongReflexive(typ, txt)`

Defined in action.t, line 3844


### `zeroQuantity(txt)`

Defined in action.t, line 3852
