# ContainerResolver

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3288)


Container Resolver. This is a proxy for the main qualifier resolver that prefers to match objects that are plausible in the sense that they contain something in the tentative resolution of the main list.


**Superclass chain:** [BasicContainerResolver](basiccontainerresolver.md) > [ProxyResolver](proxyresolver.md) > `object` > **ContainerResolver**


## Properties


### `mainList`

Defined in parser.t, line 3330

the tentative match list for the main phrase we're qualifying


### `mainListText`

Defined in parser.t, line 3333

the text of the main phrase we're qualifying


## Inherited Properties


*From [BasicContainerResolver](basiccontainerresolver.md):* [`isSubResolver`](basiccontainerresolver.md#isSubResolver)


## Methods


### `construct(mainList, mainText, origResolver)` *(overridden)*

Defined in parser.t, line 3289


### `filterAmbiguousEquivalents(lst, np)`

Defined in parser.t, line 3300

filter ambiguous equivalents


## Inherited Methods


*From [BasicContainerResolver](basiccontainerresolver.md):* [`filterAmbiguousNounPhrase`](basiccontainerresolver.md#filterAmbiguousNounPhrase), [`getQualifierResolver`](basiccontainerresolver.md#getQualifierResolver)


*From [ProxyResolver](proxyresolver.md):* [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
