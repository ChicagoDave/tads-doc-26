# BasicPossessiveProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2770)


Basic possessive phrase. The grammar rules for these phrases must map the possessive qualifier phrase to poss_, and the noun phrase being qualified to np_. We are based on DefiniteNounProd because we resolve the possessive qualifier as though it had a definite article.


**Superclass chain:** [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **BasicPossessiveProdSubclasses:** [ButPossessiveProd](butpossessiveprod.md), [exceptNounPhrase(singlePossessive)](exceptnounphrase%28singlepossessive%29.md), [DisambigPossessiveProd](disambigpossessiveprod.md), [disambigListItem(possessive)](disambiglistitem%28possessive%29.md), [PossessiveNounProd](possessivenounprod.md), [qualifiedSingularNounPhrase(possessive)](qualifiedsingularnounphrase%28possessive%29.md), [PossessivePluralProd](possessivepluralprod.md), [explicitDetPluralNounPhrase(possessive)](explicitdetpluralnounphrase%28possessive%29.md), [explicitDetPluralOnlyNounPhrase(possessive)](explicitdetpluralonlynounphrase%28possessive%29.md)


## Properties


### `npKeeper`

Defined in parser.t, line 2979

our ambiguous response keeper


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `construct`

Defined in parser.t, line 2779

To allow this class to be mixed with other classes that have mixed-in ambiguous response keepers, create a separate object to hold our ambiguous response keeper for the possessive phrase. We will never use our own ambiguous response keeper properties, so those are available to any other production class we're mixed into.


### `resolvePossessive(resolver, results, num)`

Defined in parser.t, line 2795

Resolve the possessive, and perform preliminary resolution of the qualified noun phrase. We find the owner object and reduce the resolved objects for the qualified phrase to those owned by the owner.


### `selectWithPossessive(resolver, results, lst, lstOrigText, num)`

Defined in parser.t, line 2830

Resolve the possessive, and reduce the given match list by selecting only those items owned by the resolution of the possessive phrase.


## Inherited Methods


*From [DefiniteNounProd](definitenounprod.md):* [`reduceDefinite`](definitenounprod.md#reduceDefinite), [`resolveDefinite`](definitenounprod.md#resolveDefinite), [`resolveNouns`](definitenounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
