# dropDestinationIsOuterRoom

*object* — defined in [precond.t](../by-file/precond.t.md) (line 1056)


Pre-condition: destination for "drop" is an outermost room. If the drop destination is a nested room, we'll try returning the actor to the outermost room via an implicit command.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **dropDestinationIsOuterRoom**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 1057


## Inherited Methods


*From [PreCondition](precondition.md):* [`verifyPreCondition`](precondition.md#verifyPreCondition)
