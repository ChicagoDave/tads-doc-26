# qualifiedSingularNounPhrase(anyPlural)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5772)


A singular qualified noun phrase that arbitrarily selects from a plural set. This is singular, even though the underlying noun phrase is plural, because we're explicitly selecting one item.


**Superclass chain:** [ArbitraryNounProd](arbitrarynounprod.md) > [IndefiniteNounProd](indefinitenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **qualifiedSingularNounPhrase(anyPlural)**


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [ArbitraryNounProd](arbitrarynounprod.md):* [`selectFromList`](arbitrarynounprod.md#selectFromList)


*From [IndefiniteNounProd](indefinitenounprod.md):* [`areAllEquiv`](indefinitenounprod.md#areAllEquiv), [`resolveMainPhrase`](indefinitenounprod.md#resolveMainPhrase), [`resolveNouns`](indefinitenounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
