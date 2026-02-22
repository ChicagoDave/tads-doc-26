# BasicOpenable

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3379)


A "basic openable" is an object that keeps open/closed status, and which can be linked to another object to maintain that status. This basic class doesn't handle any special commands; it's purely for keeping track of internal open/closed state.


**Superclass chain:** [Linkable](linkable.md) > `object` > **BasicOpenableSubclasses:** [BasicDoor](basicdoor.md), [Door](door.md), [AutoClosingDoor](autoclosingdoor.md), [SecretDoor](secretdoor.md), [HiddenDoor](hiddendoor.md), [Openable](openable.md), [Matchbook](matchbook.md), [OpenableContainer](openablecontainer.md), [KeyedContainer](keyedcontainer.md), [LockableContainer](lockablecontainer.md)


## Properties


### `cannotMoveThroughMsg`

Defined in objects.t, line 3468


### `cannotTouchThroughMsg`

Defined in objects.t, line 3467

if we can't reach or move something through the container, it must be because we're closed


### `initiallyOpen`

Defined in objects.t, line 3387

Initial open/closed setting. Set this to true to make the object open initially. If this object is linked to another object (as in the two sides of a door), you only need to set this property in the *master* object - the other side will automatically link up to the master object during initialization.


### `isOpen_`

Defined in objects.t, line 3474

Internal open/closed status. Do not use this for initialization - set initiallyOpen in the master object instead.


### `openDesc`

Defined in objects.t, line 3432

Open status name. This is an adjective describing whether the object is opened or closed. In English, this will return "open" or "closed."


## Methods


### `initializeThing` *(overridden)*

Defined in objects.t, line 3436

initialization


### `isOpen`

Defined in objects.t, line 3393

Flag: door is open. Travel is only possible when the door is open. Return the master's status.


### `makeOpen(stat)`

Defined in objects.t, line 3412

Make the object open or closed. By default, we'll simply set the isOpen flag to the new status. Objects can override this to apply side effects of opening or closing the object.


### `tryImplicitRemoveObstructor(sense, obj)`

Defined in objects.t, line 3450

If we're obstructing a sense path, it must be because we're closed. Try implicitly opening.


## Inherited Methods


*From [Linkable](linkable.md):* [`masterObject`](linkable.md#masterObject)
