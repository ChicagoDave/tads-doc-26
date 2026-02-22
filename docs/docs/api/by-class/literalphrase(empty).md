# literalPhrase(empty)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7228)


In case we have a verb grammar rule that calls for a literal phrase, but the player enters a command with nothing in that slot, match an empty token list as a last resort. Since this phrasing has a badness, we won't match it unless we don't have any better structural match.


**Superclass chain:** [EmptyLiteralPhraseProd](emptyliteralphraseprod.md) > [LiteralProd](literalprod.md) > [BasicProd](basicprod.md) > `object` > **literalPhrase(empty)**


## Inherited Properties


*From [EmptyLiteralPhraseProd](emptyliteralphraseprod.md):* [`newText`](emptyliteralphraseprod.md#newText)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveLiteral(results)`

Defined in en_us.t, line 7229


## Inherited Methods


*From [EmptyLiteralPhraseProd](emptyliteralphraseprod.md):* [`getLiteralText`](emptyliteralphraseprod.md#getLiteralText), [`getTentativeLiteralText`](emptyliteralphraseprod.md#getTentativeLiteralText), [`isEmptyPhrase`](emptyliteralphraseprod.md#isEmptyPhrase)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
