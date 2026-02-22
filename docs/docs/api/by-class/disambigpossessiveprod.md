# DisambigPossessiveProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3079)


Possessive phrase production for disambiguation. This base class can be used for grammar productions that match possessive phrases in disambiguation prompt ("which book do you mean...?") responses.


**Superclass chain:** [BasicPossessiveProd](basicpossessiveprod.md) > [DefiniteNounProd](definitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > [DisambigProd](disambigprod.md) > **DisambigPossessiveProdSubclasses:** [disambigListItem(possessive)](disambiglistitem%28possessive%29.md)


## Properties


### `qualifiedList_`

Defined in parser.t, line 3145

the list of objects being qualified - this is the list of books, for example, in "bob's books"


## Inherited Properties


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`npKeeper`](basicpossessiveprod.md#npKeeper)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `reduceDefinite(lst, resolver, results)` *(overridden)*

Defined in parser.t, line 3122

Do extra filter during disambiguation. Since we have a list of objects we're trying to qualify, we can look at that list to see if some of the possible matches for the qualifier phrase are owners of things in the qualified list.


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 3080


## Inherited Methods


*From [BasicPossessiveProd](basicpossessiveprod.md):* [`construct`](basicpossessiveprod.md#construct), [`resolvePossessive`](basicpossessiveprod.md#resolvePossessive), [`selectWithPossessive`](basicpossessiveprod.md#selectWithPossessive)


*From [DefiniteNounProd](definitenounprod.md):* [`resolveDefinite`](definitenounprod.md#resolveDefinite)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)


*From [DisambigProd](disambigprod.md):* [`removeAmbigFlags`](disambigprod.md#removeAmbigFlags)
