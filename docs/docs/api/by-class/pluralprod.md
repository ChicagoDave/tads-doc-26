# PluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2092)


Base class for a plural production


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **PluralProd**


<details><summary>Subclasses (14)</summary>

- [AllPluralProd](allpluralprod.md)
- [explicitDetPluralOnlyNounPhrase(definite)](explicitdetpluralonlynounphrase%28definite%29.md)
- [qualifiedPluralNounPhrase(all)](qualifiedpluralnounphrase%28all%29.md)
- [DefinitePluralProd](definitepluralprod.md)
- [explicitDetPluralNounPhrase(definite)](explicitdetpluralnounphrase%28definite%29.md)
- [implicitDetPluralOnlyNounPhrase(main)](implicitdetpluralonlynounphrase%28main%29.md)
- [QuantifiedPluralProd](quantifiedpluralprod.md)
- [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md)
- [BothPluralProd](bothpluralprod.md)
- [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md)
- [explicitDetPluralNounPhrase(definiteNumber)](explicitdetpluralnounphrase%28definitenumber%29.md)
- [explicitDetPluralOnlyNounPhrase(definiteNumber)](explicitdetpluralonlynounphrase%28definitenumber%29.md)
- [qualifiedPluralNounPhrase(allNum)](qualifiedpluralnounphrase%28allnum%29.md)
- [qualifiedPluralNounPhrase(anyNum)](qualifiedpluralnounphrase%28anynum%29.md)

</details>


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `basicPluralResolveNouns(resolver, results)`

Defined in parser.t, line 2097

Basic plural noun resolution. We'll retrieve the matching objects and filter them using filterPluralPhrase.


### `getVerifyKeepers(results)` *(overridden)*

Defined in parser.t, line 2137

Get the verify "keepers" for a plural phrase.


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
