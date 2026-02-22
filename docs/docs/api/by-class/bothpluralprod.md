# BothPluralProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2611)


A qualified plural phrase explicitly including two objects (such as, in English, "both books").


**Superclass chain:** [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md) > [QuantifiedPluralProd](quantifiedpluralprod.md) > [PluralProd](pluralprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **BothPluralProdSubclasses:** [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `getQuantity` *(overridden)*

Defined in parser.t, line 2613

the quantity specified by a "both" phrase is 2


## Inherited Methods


*From [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md):* [`getVerifyKeepers`](exactquantifiedpluralprod.md#getVerifyKeepers), [`selectExactCount`](exactquantifiedpluralprod.md#selectExactCount)


*From [QuantifiedPluralProd](quantifiedpluralprod.md):* [`resolveMainPhrase`](quantifiedpluralprod.md#resolveMainPhrase), [`resolveNouns`](quantifiedpluralprod.md#resolveNouns)


*From [PluralProd](pluralprod.md):* [`basicPluralResolveNouns`](pluralprod.md#basicPluralResolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
