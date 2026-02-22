# PreResolvedProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1856)


Pre-resolved phrase production. This isn't normally used in any actual grammar; instead, this is for use when building actions programmatically. This allows us to fill in an action tree when we already know the object we want to resolve.


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **PreResolvedProd**


## Properties


### `obj_`

Defined in parser.t, line 1886

Our pre-resolved object result. This is a list containing a single ResolveInfo representing our resolved object, since this is the form required by callers of resolveNouns.


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `construct(obj)`

Defined in parser.t, line 1857


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1875

resolve the nouns: this is easy, since we started out resolved


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
