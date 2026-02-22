# actorReadyToEnterNestedRoom

*object* — defined in [precond.t](../by-file/precond.t.md) (line 324)


Pre-condition: actor is ready to enter a nested location. This is useful for commands that cause travel within a location, such as "sit on chair": this ensures that the actor is either already in the given nested location, or is in the main location; and that the actor is standing. We simply call the actor to do the work.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **actorReadyToEnterNestedRoom**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 325


## Inherited Methods


*From [PreCondition](precondition.md):* [`verifyPreCondition`](precondition.md#verifyPreCondition)
