# QuantifiedPluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2221)


Quantified plural phrase.


**Superclass chain:** [PluralProd](pluralprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **QuantifiedPluralProdSubclasses:** [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md), [BothPluralProd](bothpluralprod.md), [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md), [explicitDetPluralNounPhrase(definiteNumber)](explicitdetpluralnounphrase%28definitenumber%29.md), [explicitDetPluralOnlyNounPhrase(definiteNumber)](explicitdetpluralonlynounphrase%28definitenumber%29.md), [qualifiedPluralNounPhrase(allNum)](qualifiedpluralnounphrase%28allnum%29.md), [qualifiedPluralNounPhrase(anyNum)](qualifiedpluralnounphrase%28anynum%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getQuantity`

Defined in parser.t, line 2242

get the quantity specified - by default, this comes from the quantifier phrase in "quant_"


### `getVerifyKeepers(results)` *(overridden)*

Defined in parser.t, line 2358

Since the player explicitly told us to use a given number of matching objects, keep the required number, logical or not.


### `resolveMainPhrase(resolver, results)`

Defined in parser.t, line 2232

Resolve the main noun phrase. By default, we simply resolve np_, but we make this separately overridable to allow this class to be subclassed for quantifying other types of plural phrases.


### `resolveNouns(resolver, results)`

Defined in parser.t, line 2245

resolve the noun phrase


### `selectExactCount(lst, num, scopeList, resolver, results)`

Defined in parser.t, line 2342

Select the desired number of matches from what the normal disambiguation filtering leaves us with.


## Inherited Methods


*From [PluralProd](pluralprod.md):* [`basicPluralResolveNouns`](pluralprod.md#basicPluralResolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
