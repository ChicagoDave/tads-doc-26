# Lockable

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3735)


Lockable: a mix-in class that can be combined with an object's other superclasses to make the object respond to the verbs "lock" and "unlock." A Lockable requires no key.


**Superclass chain:** [Linkable](linkable.md) > `object` > **LockableSubclasses:** [IndirectLockable](indirectlockable.md), [LockableContainer](lockablecontainer.md), [LockableWithKey](lockablewithkey.md), [KeyedContainer](keyedcontainer.md)


## Properties


### `autoUnlockOnOpen`

Defined in objects.t, line 3914

Should we automatically unlock this door on OPEN? By default, we do this only if the lock status is obvious.


### `initiallyLocked`

Defined in objects.t, line 3740

Our initial locked state (i.e., at the start of the game). By default, we start out locked.


### `isLocked_`

Defined in objects.t, line 3839

Internal locked state. Do not use this to set the initial state - set initiallyLocked in the master object instead.


### `lockedDesc`

Defined in objects.t, line 3797

Description of the object's current locked state. In English, this simply returns one of 'locked' or 'unlocked'. (Note that this is provided as a convenience to games, for generating messages about the object that include its state. The library doesn't use this message itself, so overriding this won't change any library messages - in particular, it won't change the examineStatus message.)


### `lockStatusObvious`

Defined in objects.t, line 3812

Is our 'locked' status obvious? This should be set to true for an object whose locked/unlocked status can be visually observed, nil for an object whose status is not visuall apparent. For example, you can usually tell from the inside that a door is locked by looking at the position of the lock's paddle, but on the outside of a door there's usually no way to see the status.


### `lockStatusReportable`

Defined in objects.t, line 3833

Is our 'locked' status reportable in our current state? This is similar to lockStatusObvious, but serves a separate purpose: this tells us if we wish to report the lock status for aesthetic reasons.


## Methods


### `dobjFor(Lock)`

Defined in objects.t, line 3857

"lock"


### `dobjFor(LockWith)`

Defined in objects.t, line 3897

"lock with"


### `dobjFor(Open)`

Defined in objects.t, line 3925

A locked object can't be opened - apply a precondition and a check for "open" that ensures that we unlock this object before we can open it.


### `dobjFor(Unlock)`

Defined in objects.t, line 3877

"unlock"


### `dobjFor(UnlockWith)`

Defined in objects.t, line 3904

"unlock with"


### `examineStatus`

Defined in objects.t, line 3773

show our status


### `initializeThing` *(overridden)*

Defined in objects.t, line 3842

initialization


### `isLocked`

Defined in objects.t, line 3746

Current locked state. Use our isLocked_ status if we're the master, otherwise defer to the master.


### `makeLocked(stat)`

Defined in objects.t, line 3760

Make the object locked or unlocked. Objects can override this to apply side effects of locking or unlocking. By default, if we're the master, we'll simply set our isLocked_ property to the new status, and otherwise defer to the master object.


## Inherited Methods


*From [Linkable](linkable.md):* [`masterObject`](linkable.md#masterObject)
