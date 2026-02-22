# Openable

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3484)


Openable: a mix-in class that can be combined with an object's other superclasses to make the object respond to the verbs "open" and "close." We also add some extra features for other related verbs, such as a must-be-open precondition "look in" and "board".


**Superclass chain:** [BasicOpenable](basicopenable.md) > [Linkable](linkable.md) > `object` > **OpenableSubclasses:** [Door](door.md), [AutoClosingDoor](autoclosingdoor.md), [Matchbook](matchbook.md), [OpenableContainer](openablecontainer.md), [KeyedContainer](keyedcontainer.md), [LockableContainer](lockablecontainer.md)


## Properties


### `descContentsLister`

Defined in objects.t, line 3492

Describe our contents using a special version of the contents lister, so that we add our open/closed status to the listing. The message we add is given by our openStatus method, so if all you want to change is the "it's open" status message, you can just override openStatus rather than providing a whole new lister.


### `lockStatusReportable`

Defined in objects.t, line 3519

By default, an Openable that's also a Lockable must be closed to be locked. This means that when it's open, the object is implicitly unlocked, in which case "It's unlocked" isn't worth mentioning when the description says "It's open."


### `openingLister`

Defined in objects.t, line 3499

Contents lister to use when we're opening the object. This lister shows the items that are newly revealed when the object is opened.


## Inherited Properties


*From [BasicOpenable](basicopenable.md):* [`cannotMoveThroughMsg`](basicopenable.md#cannotMoveThroughMsg), [`cannotTouchThroughMsg`](basicopenable.md#cannotTouchThroughMsg), [`initiallyOpen`](basicopenable.md#initiallyOpen), [`isOpen_`](basicopenable.md#isOpen_), [`openDesc`](basicopenable.md#openDesc)


## Methods


### `addInteriorReachableCond(lst)`

Defined in objects.t, line 3668

Generate a precondition to make sure gActor can reach the interior of the container. We consider the inside reachable if either the actor is located inside the container, or the actor is outside and the container is open.


### `dobjFor(Board)`

Defined in objects.t, line 3716

must be open to get into a nested room


### `dobjFor(Close)`

Defined in objects.t, line 3590

show any special contents as well


### `dobjFor(GetOutOf)`

Defined in objects.t, line 3706

must be open to get out of a nested room


### `dobjFor(Lock)`

Defined in objects.t, line 3696

can't lock an openable that isn't closed


### `dobjFor(LockWith)`

Defined in objects.t, line 3700


### `dobjFor(LookIn)`

Defined in objects.t, line 3608

show the default report


### `dobjFor(Open)`

Defined in objects.t, line 3524

Action handlers


### `dobjFor(Search)`

Defined in objects.t, line 3633

return the result


### `iobjFor(PourInto)`

Defined in objects.t, line 3689

make sure that our interior is reachable


### `iobjFor(PutIn)`

Defined in objects.t, line 3683

return the result


### `openStatus`

Defined in objects.t, line 3511

Get our "open status" message - this is a complete sentence saying that we're open or closed. By default, in English, we just say "it's open" (adjusted for number and gender, of course).


## Inherited Methods


*From [BasicOpenable](basicopenable.md):* [`initializeThing`](basicopenable.md#initializeThing), [`isOpen`](basicopenable.md#isOpen), [`makeOpen`](basicopenable.md#makeOpen), [`tryImplicitRemoveObstructor`](basicopenable.md#tryImplicitRemoveObstructor)


*From [Linkable](linkable.md):* [`masterObject`](linkable.md#masterObject)
