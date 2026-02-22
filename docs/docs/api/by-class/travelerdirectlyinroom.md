# TravelerDirectlyInRoom

*class* — defined in [precond.t](../by-file/precond.t.md) (line 277)


Pre-condition: the traveler is directly in the given room. This will attempt to remove the traveler from any nested rooms within the given room, but cannot perform travel between rooms not related by containment.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **TravelerDirectlyInRoom**


## Properties


### `actor_`

Defined in precond.t, line 294

the actor doing the travel


### `conn_`

Defined in precond.t, line 297

the connector being traversed


### `loc_`

Defined in precond.t, line 300

the room we need to be directly in


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 286

remember the actor, connector, and room


### `construct(actor, conn, loc)`

Defined in precond.t, line 278


## Inherited Methods


*From [PreCondition](precondition.md):* [`verifyPreCondition`](precondition.md#verifyPreCondition)
