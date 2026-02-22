# objBurning

*object* — defined in [precond.t](../by-file/precond.t.md) (line 1084)


Pre-condition: object is burning. This can be used for matches, candles, and the like. If the object's isLit is nil, we'll attempt a "burn" command on the object.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **objBurning**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 1085


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 1112

abort the command
