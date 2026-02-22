# AllPluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2173)


A plural phrase that explicitly selects all of matching objects. For English, this would be a phrase like "all of the marbles". This type of phrase matches all of the objects that match the name in the plural, except that if we have a collective object and we also have objects that are part of the collective (such as a bag of marbles and some individual marbles), we'll omit the collective, and match only the individual items.


**Superclass chain:** [PluralProd](pluralprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **AllPluralProdSubclasses:** [explicitDetPluralOnlyNounPhrase(definite)](explicitdetpluralonlynounphrase%28definite%29.md), [qualifiedPluralNounPhrase(all)](qualifiedpluralnounphrase%28all%29.md)


## Properties


### `filterForCollectives` *(overridden)*

Defined in parser.t, line 2187

prefer to keep individuals over collectives


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getVerifyKeepers(results)` *(overridden)*

Defined in parser.t, line 2184

since the player explicitly told us to use ALL of the matching objects, keep everything in the verify list, logical or not


### `resolveNouns(resolver, results)`

Defined in parser.t, line 2174


## Inherited Methods


*From [PluralProd](pluralprod.md):* [`basicPluralResolveNouns`](pluralprod.md#basicPluralResolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
