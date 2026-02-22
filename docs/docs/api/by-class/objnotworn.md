# objNotWorn

*object* — defined in [precond.t](../by-file/precond.t.md) (line 826)


Pre-condition: the actor must not be wearing the object. If the actor is currently wearing the object, we'll try asking the actor to doff the object.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **objNotWorn**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 827


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 858

lower the likelihood rating for anything being worn
