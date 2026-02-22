# ObjOpenCondition

*class* — defined in [precond.t](../by-file/precond.t.md) (line 870)


Pre-condition: the object is open.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **ObjOpenConditionGlobal objects:** [doorOpen](dooropen.md), [objOpen](objopen.md)


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 871


### `conditionFailed(obj)`

Defined in precond.t, line 901

The condition failed - report the failure and give up. We separate this to allow subclasses to report failure differently for specialized types of opening.


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 911

reduce the likelihood rating for anything that isn't already open
