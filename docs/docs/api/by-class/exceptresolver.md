# ExceptResolver

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6778)


Exception list resolver. We use this type of resolution for noun phrases in the "but" list of an "all but" construct.


**Superclass chain:** [ProxyResolver](proxyresolver.md) > `object` > **ExceptResolver**


## Properties


### `isSubResolver`

Defined in parser.t, line 6790

we're a sub-phrase resolver


### `mainList`

Defined in parser.t, line 6855

the main list from which we're excluding things


### `mainListText`

Defined in parser.t, line 6858

the original text for the main list


### `origResolver`

Defined in parser.t, line 6861

the original underlying resolver


## Methods


### `construct(mainList, mainListText, resolver)` *(overridden)*

Defined in parser.t, line 6779


### `filterAmbiguousEquivalents(lst, np)`

Defined in parser.t, line 6826

filter ambiguous equivalents


### `filterAmbiguousNounPhrase(lst, requiredNum, np)`

Defined in parser.t, line 6837

filter an ambiguous noun list


### `filterPluralPhrase(lst, np)`

Defined in parser.t, line 6848

filter a plural noun list


### `getAll(np)`

Defined in parser.t, line 6820

for 'all', simply return the whole original list


### `getQualifierResolver`

Defined in parser.t, line 6808

Resolve qualifiers in the enclosing main scope, since qualifier phrases are not part of the narrowed list - qualifiers apply to the main phrase from which we're excluding, not to the exclusion list itself.


### `matchName(obj, origTokens, adjustedTokens)`

Defined in parser.t, line 6797

match an object's name - we'll use the disambiguation name resolver, so that they can give us partial names just like in answer to a disambiguation question


### `objInScope(obj)`

Defined in parser.t, line 6814

determine if an object is in scope - it's in scope if it's in the original main list


## Inherited Methods


*From [ProxyResolver](proxyresolver.md):* [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
