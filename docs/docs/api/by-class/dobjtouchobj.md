# dobjTouchObj

*object* — defined in [precond.t](../by-file/precond.t.md) (line 722)


Pre-condition: the direct object can touch the target object. This is useful for situations where the direct object is being manipulated directly and the indirect object is more of a passive participant in the action, such as PLUG CORD INTO OUTLET.


**Superclass chain:** [TouchObjCondition](touchobjcondition.md) > [PreCondition](precondition.md) > `object` > **dobjTouchObj**


## Properties


### `sourceObj` *(overridden)*

Defined in precond.t, line 724

the direct object has to be able to touch the target object


## Inherited Properties


*From [TouchObjCondition](touchobjcondition.md):* [`preCondOrder`](touchobjcondition.md#preCondOrder)


## Inherited Methods


*From [TouchObjCondition](touchobjcondition.md):* [`checkPreCondition`](touchobjcondition.md#checkPreCondition), [`construct`](touchobjcondition.md#construct), [`verifyPreCondition`](touchobjcondition.md#verifyPreCondition)
