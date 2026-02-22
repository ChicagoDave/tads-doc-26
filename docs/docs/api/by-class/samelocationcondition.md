# SameLocationCondition

*class* — defined in [precond.t](../by-file/precond.t.md) (line 732)


A precondition ensuring that the target object is in the same immediate location as a given object.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **SameLocationConditionGlobal objects:** [sameLocationAsDobj](samelocationasdobj.md), [sameLocationAsIobj](samelocationasiobj.md)


## Properties


### `sourceObj`

Defined in precond.t, line 740

the object whose location we must match


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 743

check the condition


### `construct(obj)`

Defined in precond.t, line 737

construct dynamically, setting the other object whose location we must match


## Inherited Methods


*From [PreCondition](precondition.md):* [`verifyPreCondition`](precondition.md#verifyPreCondition)
