# PossessiveResolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 1068)


A possessive resolver is a proxy to a main resolver that considers an object in scope if (a) it's in scope in the base resolver, or (b) the object is known to the actor.


**Superclass chain:** [ProxyResolver](proxyresolver.md) > `object` > **PossessiveResolver**


## Properties


### `isSubResolver`

Defined in resolver.t, line 1083

this is a sub-resolver


## Methods


### `objInScope(obj)`

Defined in resolver.t, line 1069


## Inherited Methods


*From [ProxyResolver](proxyresolver.md):* [`construct`](proxyresolver.md#construct), [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
