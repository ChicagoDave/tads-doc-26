# BasicResolveResults

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4756)


An implementation of ResolveResults for normal noun resolution.


**Superclass chain:** [ResolveResults](resolveresults.md) > `object` > **BasicResolveResultsSubclasses:** [ActorResolveResults](actorresolveresults.md), [DisambigResults](disambigresults.md)


## Properties


### `allowActionRemapping`

Defined in parser.t, line 5667

allow remapping the action


### `allowEquivalentFiltering`

Defined in parser.t, line 5670

allow making an arbitrary choice among equivalents


### `issuingActor_`

Defined in parser.t, line 4761


### `targetActor_`

Defined in parser.t, line 4760

The target and issuing actors for the command being resolved.


## Methods


### `allNotAllowed`

Defined in parser.t, line 4794

use the basic noMatch handling


### `ambiguousNounPhrase(keeper, asker, txt, matchList, fullMatchList, scopeList, requiredNum, resolver)`

Defined in parser.t, line 4927

Handle an ambiguous noun phrase. We'll first check to see if we can find a Distinguisher that can tell at least some of the matches apart; if we fail to do that, we'll just pick the required number of objects arbitrarily, since we have no way to distinguish any of them. Once we've chosen a Distinguisher, we'll ask the user for help interactively if possible.


### `askMissingLiteral(action, which)`

Defined in parser.t, line 5542

there's nothing to do with a literal at this point, since we're not ranking anything


### `askMissingObject(asker, resolver, responseProd)`

Defined in parser.t, line 5511

ask the resolver to supply an implied default object


### `beginSingleObjSlot`

Defined in parser.t, line 5633

we don't care about these right now


### `beginTopicSlot`

Defined in parser.t, line 5636


### `canResolveInteractively(action)`

Defined in parser.t, line 4895

Service routine - determine if we can interactively resolve a need for more information. If the issuer is the player, and the target actor can talk to the player, then we can resolve a question interactively; otherwise, we cannot.


### `emptyNounPhrase(resolver)`

Defined in parser.t, line 5568

return the response


### `endSingleObjSlot`

Defined in parser.t, line 5634


### `endTopicSlot`

Defined in parser.t, line 5637


### `filterWithDistinguisher(lst, dist)`

Defined in parser.t, line 5448

filter a match list with a specific Distinguisher


### `getImpliedObject(np, resolver)`

Defined in parser.t, line 5505

If we didn't find any unknown words, it means that they used a word that's in the dictionary in a way that makes no sense to us. Simply return an empty list and let the resolver proceed with its normal handling for unmatched noun phrases.


### `incCommandCount`

Defined in parser.t, line 5639


### `insufficientQuantity(txt, matchList, requiredNum)`

Defined in parser.t, line 5581

abort with an error


### `noMatch(action, txt)`

Defined in parser.t, line 4781

indicate that we couldn't match the phrase


### `noMatchForAll`

Defined in parser.t, line 4800

show an error


### `noMatchForAllBut`

Defined in parser.t, line 4811

this isn't an error - ignore it


### `noMatchForListBut`

Defined in parser.t, line 4817

show an error


### `noMatchForLocation(loc, txt)`

Defined in parser.t, line 4859

let the (singular) owner object generate the error


### `noMatchForPossessive(owner, txt)`

Defined in parser.t, line 4844

show an error


### `noMatchForPronoun(typ, txt)`

Defined in parser.t, line 4823

show an error


### `noMatchPossessive(action, txt)`

Defined in parser.t, line 4788

show an error


### `noteActorSpecified`

Defined in parser.t, line 5644

we don't care about how many subcommands there are


### `noteAdjEnding`

Defined in parser.t, line 5603

abort with an error


### `noteBadPrep`

Defined in parser.t, line 4871

let the location object generate the error


### `noteEmptyBut`

Defined in parser.t, line 4806

show an error


### `noteIndefinite`

Defined in parser.t, line 5608

we don't care about adjective-ending noun phrases at this point


### `noteLiteral(txt)`

Defined in parser.t, line 5534

try reading an object response


### `noteMatches(matchList)`

Defined in parser.t, line 5623

we don't care about pronouns right now


### `noteMiscWordList(txt)`

Defined in parser.t, line 5613

we don't care about indefinites at this point


### `noteNounSlots(cnt)`

Defined in parser.t, line 5653

we don't care about this during execution - it only matters for determining the strength of the command during the ranking process


### `notePlural`

Defined in parser.t, line 5628

we don't care about the matches just now


### `notePronoun`

Defined in parser.t, line 5618

we don't care about unstructured noun phrases at this point


### `noteWeakPhrasing(level)`

Defined in parser.t, line 5661

we don't care about this during execution; it only matters for the ranking process


### `nothingInLocation(loc)`

Defined in parser.t, line 4865

let the location object generate the error


### `noVocabMatch(action, txt)`

Defined in parser.t, line 4774

Results gatherer methods


### `reflexiveNotAllowed(typ, txt)`

Defined in parser.t, line 4830

show an error


### `setActors(target, issuer)`

Defined in parser.t, line 4764

set up the actor parameters


### `singleObjectRequired(txt)`

Defined in parser.t, line 5596

abort with an error


### `uniqueObjectRequired(txt, matchList)`

Defined in parser.t, line 5589

abort with an error


### `unknownNounPhrase(match, resolver)`

Defined in parser.t, line 5475

handle a noun phrase that doesn't match any legal grammar rules for noun phrases


### `wrongReflexive(typ, txt)`

Defined in parser.t, line 4837

show an error


### `zeroQuantity(txt)`

Defined in parser.t, line 5574

abort with an error
