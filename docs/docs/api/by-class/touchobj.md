# touchObj

*object* — defined in [precond.t](../by-file/precond.t.md) (line 690)


Pre-condition: actor must be able to touch the object. This doesn't require that the actor is actually holding the object, but the actor must be able to physically touch the object. This ensures that the actor and object are not, for example, separated by a transparent barrier.


**Superclass chain:** [TouchObjCondition](touchobjcondition.md) > [PreCondition](precondition.md) > `object` > **touchObj**


## Properties


### `sourceObj` *(overridden)*

Defined in precond.t, line 692

we want to test reaching from the current actor to the target object


## Inherited Properties


*From [TouchObjCondition](touchobjcondition.md):* [`preCondOrder`](touchobjcondition.md#preCondOrder)


## Inherited Methods


*From [TouchObjCondition](touchobjcondition.md):* [`checkPreCondition`](touchobjcondition.md#checkPreCondition), [`construct`](touchobjcondition.md#construct), [`verifyPreCondition`](touchobjcondition.md#verifyPreCondition)
