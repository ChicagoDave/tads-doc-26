# iobjTouchObj

*object* — defined in [precond.t](../by-file/precond.t.md) (line 711)


Pre-condition: the indirect object must be able to touch the target object. This can be used for actions where the direct object is going to be manipulated by an "agent" of the action (i.e., the indirect object), rather than directly by the actor: MOVE X WITH Y, for example.


**Superclass chain:** [TouchObjCondition](touchobjcondition.md) > [PreCondition](precondition.md) > `object` > **iobjTouchObj**


## Properties


### `sourceObj` *(overridden)*

Defined in precond.t, line 713

the indirect object has to be able to touch the target object


## Inherited Properties


*From [TouchObjCondition](touchobjcondition.md):* [`preCondOrder`](touchobjcondition.md#preCondOrder)


## Inherited Methods


*From [TouchObjCondition](touchobjcondition.md):* [`checkPreCondition`](touchobjcondition.md#checkPreCondition), [`construct`](touchobjcondition.md#construct), [`verifyPreCondition`](touchobjcondition.md#verifyPreCondition)
