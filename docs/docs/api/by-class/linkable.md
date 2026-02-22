# Linkable

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3309)


A "linkable" object is one that can participate in a master/slave relationship. This kind of relationship means that the state of both objects in the pair is controlled by one of the objects, called the master; the other object defers to the other to get and set all of its linkable state.


**Superclass chain:** `object` > **Linkable**


<details><summary>Subclasses (21)</summary>

- [BasicOpenable](basicopenable.md)
- [BasicDoor](basicdoor.md)
- [Door](door.md)
- [AutoClosingDoor](autoclosingdoor.md)
- [SecretDoor](secretdoor.md)
- [HiddenDoor](hiddendoor.md)
- [Openable](openable.md)
- [Matchbook](matchbook.md)
- [OpenableContainer](openablecontainer.md)
- [KeyedContainer](keyedcontainer.md)
- [LockableContainer](lockablecontainer.md)
- [Lockable](lockable.md)
- [IndirectLockable](indirectlockable.md)
- [LockableWithKey](lockablewithkey.md)
- [Passage](passage.md)
- [Stairway](stairway.md)
- [StairwayDown](stairwaydown.md)
- [StairwayUp](stairwayup.md)
- [ThroughPassage](throughpassage.md)
- [ExitOnlyPassage](exitonlypassage.md)
- [PathPassage](pathpassage.md)

</details>


## Methods


### `initializeThing`

Defined in objects.t, line 3340

We're normally mixed into a Thing; do some extra work in initialization.


### `masterObject`

Defined in objects.t, line 3324

Get the master object, which holds our state. By default, this is simply 'self', but some objects might want to override this. For example, doors are usually implemented with two separate objects, representing the two sides of the door, which share common state; in such cases, one of the pair can be designated as the master, which holds the common state of the door, and this method can be overridden so that all state operations on the lock are performed on the master side of the door.
