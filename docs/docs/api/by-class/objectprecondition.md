# ObjectPreCondition

*class* — defined in [precond.t](../by-file/precond.t.md) (line 75)


A pre-condition that applies to a specific, pre-determined object, rather than the direct/indirect object of the command.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **ObjectPreCondition**


## Properties


### `cond_`

Defined in precond.t, line 106

the pre-condition we check


### `obj_`

Defined in precond.t, line 103

the object we check with the condition


### `preCondOrder` *(overridden)*

Defined in precond.t, line 100

use the same order as our underlying condition


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 87

route our check to the pre-condition using our specific object


### `construct(obj, cond)`

Defined in precond.t, line 76


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 94

route our verification check to the pre-condition
