# literalPhrase(string)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 7163)


A "literal" is essentially any phrase. This can include a quoted string, a number, or any set of word tokens.


**Superclass chain:** [LiteralProd](literalprod.md) > [BasicProd](basicprod.md) > `object` > **literalPhrase(string)**


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getLiteralText(results, action, which)`

Defined in en_us.t, line 7164


### `getTentativeLiteralText`

Defined in en_us.t, line 7170

get the text from our underlying quoted string


### `resolveLiteral(results)`

Defined in en_us.t, line 7179

our result will never change, so our tentative text is the same as our regular literal text


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
