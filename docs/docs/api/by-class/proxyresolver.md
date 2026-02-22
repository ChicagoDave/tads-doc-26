# ProxyResolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 761)


Proxy Resolver - this is used to create resolvers that refer methods not otherwise overridden back to an underlying resolver


**Superclass chain:** `object` > **ProxyResolverSubclasses:** [BasicContainerResolver](basiccontainerresolver.md), [ContainerResolver](containerresolver.md), [VagueContainerResolver](vaguecontainerresolver.md), [ExceptResolver](exceptresolver.md), [InteractiveResolver](interactiveresolver.md), [DisambigResolver](disambigresolver.md), [PossessiveResolver](possessiveresolver.md)


## Methods


### `construct(origResolver)`

Defined in resolver.t, line 762


### `getPossessiveResolver`

Defined in resolver.t, line 776

base our possessive resolver on the proxy


### `propNotDefined(prop, [args])`

Defined in resolver.t, line 769

delegate methods we don't override to the underlying resolver
