# IndirectLockable

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3975)


A lockable that can't be locked and unlocked by direct action. The LOCK and UNLOCK commands cannot be used with this kind of lockable.


**Superclass chain:** [Lockable](lockable.md) > [Linkable](linkable.md) > `object` > **IndirectLockable**


## Properties


### `cannotLockMsg`

Defined in objects.t, line 4005

the message we display in response to LOCK/UNLOCK


### `cannotUnlockMsg`

Defined in objects.t, line 4006


### `lockStatusObvious` *(overridden)*

Defined in objects.t, line 4002

Since we can't be locked and unlocked with simple LOCK and UNLOCK commands, presume that the lock status isn't obvious. If the alternative mechanism that locks and unlocks the object makes the current status readily apparent, this should be overridden and set to true.


## Inherited Properties


*From [Lockable](lockable.md):* [`autoUnlockOnOpen`](lockable.md#autoUnlockOnOpen), [`initiallyLocked`](lockable.md#initiallyLocked), [`isLocked_`](lockable.md#isLocked_), [`lockedDesc`](lockable.md#lockedDesc), [`lockStatusReportable`](lockable.md#lockStatusReportable)


## Methods


### `dobjFor(Lock)` *(overridden)*

Defined in objects.t, line 3976


### `dobjFor(LockWith)` *(overridden)*

Defined in objects.t, line 3984


### `dobjFor(Unlock)` *(overridden)*

Defined in objects.t, line 3985


### `dobjFor(UnlockWith)` *(overridden)*

Defined in objects.t, line 3993


## Inherited Methods


*From [Lockable](lockable.md):* [`dobjFor(Open)`](lockable.md#dobjFor(Open)), [`examineStatus`](lockable.md#examineStatus), [`initializeThing`](lockable.md#initializeThing), [`isLocked`](lockable.md#isLocked), [`makeLocked`](lockable.md#makeLocked)


*From [Linkable](linkable.md):* [`masterObject`](linkable.md#masterObject)
