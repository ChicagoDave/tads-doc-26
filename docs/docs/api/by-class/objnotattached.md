# objNotAttached

*object* — defined in [extras.t](../by-file/extras.t.md) (line 3261)


An Attachable-specific precondition: the Attachable isn't already attached to something else. This can be added to the preCond list for an Attachable (for iobjFor(AttachTo) and dobjFor(AttachTo)) to ensure that any existing attachment is removed before a new attachment is formed. This is useful when the Attachable can connect to only one thing at a time.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **objNotAttached**


## Inherited Properties


*From [PreCondition](precondition.md):* [`preCondOrder`](precondition.md#preCondOrder)


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in extras.t, line 3262


## Inherited Methods


*From [PreCondition](precondition.md):* [`verifyPreCondition`](precondition.md#verifyPreCondition)
