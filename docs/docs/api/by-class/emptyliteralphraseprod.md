# EmptyLiteralPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4190)


Empty literal phrase - this serves a purpose similar to that of EmptyNounPhraseProd, but can be used where literal phrases are required.


**Superclass chain:** [LiteralProd](literalprod.md) > [BasicProd](basicprod.md) > `object` > **EmptyLiteralPhraseProdSubclasses:** [literalPhrase(empty)](literalphrase%28empty%29.md)


## Properties


### `newText`

Defined in parser.t, line 4268

the response to a previous interactive query


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getLiteralText(results, action, which)`

Defined in parser.t, line 4191


### `getTentativeLiteralText`

Defined in parser.t, line 4255

Tentatively get my literal text. This is used for pre-resolution when we have another phrase we want to resolve first, but we want to provide a tentative form of the text in the meantime. We won't attempt to ask for more information interactively, but we'll return any information we do have.


### `isEmptyPhrase`

Defined in parser.t, line 4265

I'm an empty phrase, unless I already have a text response


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
