# literalPhrase(miscList)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7186)


flag the literal text


**Superclass chain:** [LiteralProd](literalprod.md) > [BasicProd](basicprod.md) > `object` > **literalPhrase(miscList)**


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getLiteralText(results, action, which)`

Defined in en_us.t, line 7187


### `getTentativeLiteralText`

Defined in en_us.t, line 7203

return the text


### `resolveLiteral(results)`

Defined in en_us.t, line 7209

our regular text is permanent, so simply use it now


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
