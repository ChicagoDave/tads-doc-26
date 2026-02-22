# TouchObjCondition

*class* — defined in [precond.t](../by-file/precond.t.md) (line 419)


Pre-condition: a given source object must be able to touch the object. This requires that the source object (given by our property 'sourceObj') has a clear 'touch' path to the target object.


**Superclass chain:** [PreCondition](precondition.md) > `object` > **TouchObjConditionGlobal objects:** [dobjTouchObj](dobjtouchobj.md), [iobjTouchObj](iobjtouchobj.md), [touchObj](touchobj.md)


## Properties


### `preCondOrder` *(overridden)*

Defined in precond.t, line 673

This condition tends to be fragile, in the sense that other preconditions for the same action have the potential to undo any implicit action that we perform to make an object touchable. This is most likely to happen when we implicitly move the actor (moving in or out of a nested room, for example) to put the actor within reach of the target object. To reduce the likelihood that this fragility will be visible to a player, try to execute this condition after other conditions. Most other preconditions tend to be "stickier" - less likely to be undone by subsequent preconditions.


### `sourceObj`

Defined in precond.t, line 427

the source object - this is the object that is attempting to touch the target object


## Methods


### `checkPreCondition(obj, allowImplicit)` *(overridden)*

Defined in precond.t, line 430

check the condition


### `construct(src)`

Defined in precond.t, line 421

construct with a given source object


### `verifyPreCondition(obj)` *(overridden)*

Defined in precond.t, line 565

We've tried an implied command to remove this obstructor, but that isn't guaranteed to make the target touchable, as there could be further obstrutions, or the implied command could have failed to actually remove the obstruction. Keep iterating. To avoid looping forever in the event the implicit command we just tried isn't good enough to remove this obstruction, make a note of the obstruction we just tried to remove; if we find it again on a subsequent iteration, we'll know that we've tried before to remove it and failed, and thus we'll know to give up without making the same doomed attempt again.
