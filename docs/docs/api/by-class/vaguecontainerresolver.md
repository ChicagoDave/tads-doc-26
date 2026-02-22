# VagueContainerResolver

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3533)


Container Resolver for vaguely-specified containment phrases. We'll select for objects that have contents, but that's about as much as we can do, since the main phrase is bounded only by the container in vague containment phrases (and thus provides no information that would help us narrow down the container itself).


**Superclass chain:** [BasicContainerResolver](basiccontainerresolver.md) > [ProxyResolver](proxyresolver.md) > `object` > **VagueContainerResolver**


## Inherited Properties


*From [BasicContainerResolver](basiccontainerresolver.md):* [`isSubResolver`](basiccontainerresolver.md#isSubResolver)


## Methods


### `filterAmbiguousEquivalents(lst, np)`

Defined in parser.t, line 3535

filter ambiguous equivalents


## Inherited Methods


*From [BasicContainerResolver](basiccontainerresolver.md):* [`filterAmbiguousNounPhrase`](basiccontainerresolver.md#filterAmbiguousNounPhrase), [`getQualifierResolver`](basiccontainerresolver.md#getQualifierResolver)


*From [ProxyResolver](proxyresolver.md):* [`construct`](proxyresolver.md#construct), [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
