# TokenListProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1954)


A token list production is an internally generated placeholder when we synthesize a production rather than matching grammar, and we want to keep track of the token list that triggered the node.


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **TokenListProd**


## Properties


### `tokenList`

Defined in parser.t, line 1963

the token list


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `construct(toks)`

Defined in parser.t, line 1955


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
