# ExactQuantifiedPluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2382)


Exact quantified plural phrase. This is similar to the normal quantified plural, but has the additional requirement of matching an unambiguous set of the exact given number ("the five books" means that we expect to find exactly five books matching the phrase - no fewer, and no more).


**Superclass chain:** [QuantifiedPluralProd](quantifiedpluralprod.md) > [PluralProd](pluralprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **ExactQuantifiedPluralProdSubclasses:** [BothPluralProd](bothpluralprod.md), [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md), [explicitDetPluralNounPhrase(definiteNumber)](explicitdetpluralnounphrase%28definitenumber%29.md), [explicitDetPluralOnlyNounPhrase(definiteNumber)](explicitdetpluralonlynounphrase%28definitenumber%29.md), [qualifiedPluralNounPhrase(allNum)](qualifiedpluralnounphrase%28allnum%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `getVerifyKeepers(results)` *(overridden)*

Defined in parser.t, line 2413

get the keepers in the verify stage


### `selectExactCount(lst, num, scopeList, resolver, results)` *(overridden)*

Defined in parser.t, line 2387

Select the desired number of matches. Since we want an exact set of matches, we'll run disambiguation on the set.


## Inherited Methods


*From [QuantifiedPluralProd](quantifiedpluralprod.md):* [`getQuantity`](quantifiedpluralprod.md#getQuantity), [`resolveMainPhrase`](quantifiedpluralprod.md#resolveMainPhrase), [`resolveNouns`](quantifiedpluralprod.md#resolveNouns)


*From [PluralProd](pluralprod.md):* [`basicPluralResolveNouns`](pluralprod.md#basicPluralResolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
