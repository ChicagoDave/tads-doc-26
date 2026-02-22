# ArbitraryNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2539)


Noun phrase explicitly asking us to choose an object arbitrarily (with a word like "any"). This is similar to the indefinite noun phrase, but differs in that this phrase is *explicitly* arbitrary, rather than merely indefinite.


**Superclass chain:** [IndefiniteNounProd](indefinitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ArbitraryNounProdSubclasses:** [qualifiedSingularNounPhrase(anyPlural)](qualifiedsingularnounphrase%28anyplural%29.md), [qualifiedSingularNounPhrase(arbitrary)](qualifiedsingularnounphrase%28arbitrary%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `selectFromList(resolver, results, lst)` *(overridden)*

Defined in parser.t, line 2546

Select an object from a list of potential matches. Since the choice is explicitly arbitrary, we simply choose the first (they're in order from most likely to least likely, so this will choose the most likely).


## Inherited Methods


*From [IndefiniteNounProd](indefinitenounprod.md):* [`areAllEquiv`](indefinitenounprod.md#areAllEquiv), [`resolveMainPhrase`](indefinitenounprod.md#resolveMainPhrase), [`resolveNouns`](indefinitenounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
