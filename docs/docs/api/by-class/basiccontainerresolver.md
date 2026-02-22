# BasicContainerResolver

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3251)


Basic container resolver. This is a common subclass for the standard container resolver and the "vague" container resolver.


**Superclass chain:** [ProxyResolver](proxyresolver.md) > `object` > **BasicContainerResolverSubclasses:** [ContainerResolver](containerresolver.md), [VagueContainerResolver](vaguecontainerresolver.md)


## Properties


### `isSubResolver`

Defined in parser.t, line 3253

we're a sub-phrase resolver


## Methods


### `filterAmbiguousNounPhrase(lst, requiredNum, np)`

Defined in parser.t, line 3259

filter an ambiguous noun phrase


### `getQualifierResolver`

Defined in parser.t, line 3256

resolve any qualifiers in the main scope


## Inherited Methods


*From [ProxyResolver](proxyresolver.md):* [`construct`](proxyresolver.md#construct), [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
