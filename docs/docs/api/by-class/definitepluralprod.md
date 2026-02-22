# DefinitePluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2207)


A plural phrase qualified by a definite article ("the books"). This type of phrasing doesn't specify anything about the specific number of items involved, except that they number more than one.


**Superclass chain:** [PluralProd](pluralprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **DefinitePluralProdSubclasses:** [explicitDetPluralNounPhrase(definite)](explicitdetpluralnounphrase%28definite%29.md), [implicitDetPluralOnlyNounPhrase(main)](implicitdetpluralonlynounphrase%28main%29.md)


## Properties


### `filterForCollectives` *(overridden)*

Defined in parser.t, line 2215

prefer to keep collectives instead of their individuals


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)`

Defined in parser.t, line 2208


## Inherited Methods


*From [PluralProd](pluralprod.md):* [`basicPluralResolveNouns`](pluralprod.md#basicPluralResolveNouns), [`getVerifyKeepers`](pluralprod.md#getVerifyKeepers)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
