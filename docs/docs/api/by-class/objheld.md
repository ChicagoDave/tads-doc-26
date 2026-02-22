# objHeld

*object* — defined in [precond.t](../by-file/precond.t.md) (line 367)


Pre-condition: object must be held. This condition requires that an object of a command must be held by the actor. If it is not, we will attempt a recursive "take" command on the object.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **objHeld**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 368


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 401

lower the likelihood rating for anything not being held
