# LockableWithKey

*class* — defined in [objects.t](../by-file/objects.t.md) (line 4021)


LockableWithKey: a mix-in class that can be combined with an object's other superclasses to make the object respond to the verbs "lock" and "unlock," with a key as an indirect object. A LockableWithKey cannot be locked or unlocked except with the keys listed in the keyList property.


**Superclass chain:** [Lockable](lockable.md) > [Linkable](linkable.md) > `object` > **LockableWithKeySubclasses:** [KeyedContainer](keyedcontainer.md)


## Properties


### `keyList`

Defined in objects.t, line 4070

the list of objects that can serve as keys for this object


### `knownKeyList`

Defined in objects.t, line 4077

The list of keys which the player knows will fit this lock. This is used to make key disambiguation automatic once the player knows the correct key for a lock.


### `lockStatusObvious` *(overridden)*

Defined in objects.t, line 4138

By default, the locked/unlocked status of a keyed lockable is nil. In most cases, an object that's locked and unlocked using a key doesn't have a visible indication of the status; for example, you usually can't tell just by looking at it from the outside whether or not an exterior door to a building is locked. Usually, the only way to tell from the outside that an exterior door is locked is to try opening it and see if it opens.


### `rememberKnownKeys`

Defined in objects.t, line 4120

Flag: remember my keys after they're successfully used. If this is true, whenever a key is successfully used to lock or unlock this object, we'll add the key to our known key list; subsequently, whenever we try to use a key in this lock, we will automatically disambiguate the key based on the keys known to work previously.


## Inherited Properties


*From [Lockable](lockable.md):* [`autoUnlockOnOpen`](lockable.md#autoUnlockOnOpen), [`initiallyLocked`](lockable.md#initiallyLocked), [`isLocked_`](lockable.md#isLocked_), [`lockedDesc`](lockable.md#lockedDesc), [`lockStatusReportable`](lockable.md#lockStatusReportable)


## Methods


### `autoUnlockOnOpen`

Defined in objects.t, line 4148

Should we automatically unlock on OPEN? We will if our inherited handling says so, OR if the current actor is carrying a key that's known to work with this object. We automatically unlock when a known key is present as a convenience: if we have a known key, then there's no mystery in unlocking this object, and thus for playability we want to make its operation fully automatic.


### `dobjFor(Lock)` *(overridden)*

Defined in objects.t, line 4158

Action handling


### `dobjFor(LockWith)` *(overridden)*

Defined in objects.t, line 4265

"lock with"


### `dobjFor(Unlock)` *(overridden)*

Defined in objects.t, line 4184

"unlock"


### `dobjFor(UnlockWith)` *(overridden)*

Defined in objects.t, line 4281

"unlock with"


### `getKnownKeyList`

Defined in objects.t, line 4083

Get my known key list. This simply returns the known key list from the known key owner.


### `getKnownKeyOwner`

Defined in objects.t, line 4091

Get the object that own our known key list. If we explicitly have our own non-empty known key list, we own the key list; otherwise, our master object owns the list, as long as it has a non-nil key list at all.


### `isKeyKnown(key)`

Defined in objects.t, line 4127

Determine if the player knows that the given key operates this lock. Returns true if the key is in our known key list, nil if not.


### `keyFitsLock(key)`

Defined in objects.t, line 4027

Determine if the key fits this lock. Returns true if so, nil if not. By default, we'll return true if the key is in my keyList. This can be overridden to use other key selection criteria.


### `keyIsPlausible(key)`

Defined in objects.t, line 4067

Determine if the key is plausibly of the right type for this lock. This doesn't check to see if the key actually fits the lock - rather, this checks to see if the key is generally the kind of object that might plausibly be used with this lock.


### `lockOrUnlockAction(lock)`

Defined in objects.t, line 4220

perform the action processing for LockWith or UnlockWith - these are highly symmetrical, in that the only thing that varies is the new lock state we establish


## Inherited Methods


*From [Lockable](lockable.md):* [`dobjFor(Open)`](lockable.md#dobjFor(Open)), [`examineStatus`](lockable.md#examineStatus), [`initializeThing`](lockable.md#initializeThing), [`isLocked`](lockable.md#isLocked), [`makeLocked`](lockable.md#makeLocked)


*From [Linkable](linkable.md):* [`masterObject`](linkable.md#masterObject)
