# DisambigResolver

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 343)


Disambiguation Resolver. This is a special resolver that we use for resolving disambiguation responses.


**Superclass chain:** [InteractiveResolver](interactiveresolver.md) > [ProxyResolver](proxyresolver.md) > `object` > **DisambigResolver**


## Properties


### `allowAll`

Defined in disambig.t, line 389

we allow ALL in interactive disambiguation responses, regardless of the verb, because we're just selecting from the list presented in the prompt in these cases


### `distinguisher`

Defined in disambig.t, line 464

The distinguisher that was used to generate the prompt. Some distinguishers can tell objects apart by other characteristics than just their names, so when parsing we want to be able to give the distinguisher a look at the input to see if the player is referring to one of the distinguishing characteristics rather than the object's own name.


### `fullMatchList`

Defined in disambig.t, line 454

the full original match list, which might include items in scope beyond those offered as interactive choices


### `matchList`

Defined in disambig.t, line 448

the original match list we are disambiguating, which includes all of the objects offered as interactive choices, and might include indistinguishable equivalents of offered items


### `matchText`

Defined in disambig.t, line 431

the text of the phrase we're disambiguating


### `ordinalMatchList`

Defined in disambig.t, line 441

The "ordinal" match list: this includes the exact list offered as interactive choices in the same order as they were shown in the prompt. This list can be used to correlate ordinal responses to the prompt list, since it contains exactly the items listed in the prompt. Note that this list will only contain one of each indistinguishable object.


## Methods


### `construct(matchText, ordinalMatchList, matchList, fullMatchList, resolver, dist)` *(overridden)*

Defined in disambig.t, line 344


### `filterAmbiguousNounPhrase(lst, requiredNum, np)`

Defined in disambig.t, line 395

filter an ambiguous noun list


### `filterPluralPhrase(lst, np)`

Defined in disambig.t, line 406

filter a plural noun list


### `getAll(np)`

Defined in disambig.t, line 392

for 'all', use the full current full match list


### `getQualifierResolver`

Defined in disambig.t, line 373

Resolve qualifiers in the enclosing main scope, since qualifier phrases in responses are not part of the narrowed list being disambiguated.


### `matchName(obj, origTokens, adjustedTokens)`

Defined in disambig.t, line 362

Match an object's name. We'll send this to the distinguisher for handling.


### `objInScope(obj)`

Defined in disambig.t, line 379

Determine if an object is in scope. We pass this to the distinguisher to decide.


### `resolvePronounAntecedent(typ, np, results, poss)` *(overridden)*

Defined in en_us.t, line 3444

Perform special resolution on pronouns used in interactive responses. If the pronoun is HIM or HER, then look through the list of possible matches for a matching gendered object, and use it as the result if we find one. If we find more than one, then use the default handling instead, treating the pronoun as referring back to the simple antecedent previously set.


### `selectIndefinite(results, lst, requiredNumber)`

Defined in disambig.t, line 422

Select the match for an indefinite noun phrase. In interactive disambiguation, an indefinite noun phrase simply narrows the list, rather than selecting any match, so treat this as still ambiguous.


## Inherited Methods


*From [InteractiveResolver](interactiveresolver.md):* [`getReflexiveBinding`](interactiveresolver.md#getReflexiveBinding), [`resolvePronounAsTargetActor`](interactiveresolver.md#resolvePronounAsTargetActor)


*From [ProxyResolver](proxyresolver.md):* [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
