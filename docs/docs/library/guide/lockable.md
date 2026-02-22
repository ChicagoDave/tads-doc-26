# Lockable

Lockable : Linkable

Lockable is a mix-in class that must be used with other classes such as [Door](door.md) or Openable, but even when mixed-in the Lockable class doesn't really do much, as we saw in the case of the [LockableContainer](lockablecontainer.md), since it simply allows something to be locked and unlocked via LOCK and UNLOCK commands, which are carried out implicitly if the player tries to open whatever it is that's locked.

You can verify this by modifying both sides of the door into and out of the lakeRoom:

```tads3
+ lakeDoor : Lockable, Door 'door' 'door';
...
+ lakeDoor2 : Lockable, Door ->lakeDoor 'door' 'door';
```

If you compile and run the game and try to go south through this door from anotherCave you'll find the lock doesn't prove much of a barrier. The only reason to use plain vanilla Lockable with a Door is if the other side of the door is going to be locked by some less plain vanilla means, which is what we'll go on to do. This could represent a situation like a front door, say, which is locked and unlocked by a key on the outside and a simple knob on the inside. Locking the door on the inside would then prevent pursuit by an Actor who did not have the key.

There are a number of properties and methods on the Lockable class, the most useful of which for game authors are:

- **autoUnlockOnOpen**: if true the object is automatically unlocked when someone attempts to open it (or at least, the parser attempts to unlock it, although the attempt may fail if there's some reason why the object can't be unlocked). The library default is to set this to lockStatusObvious (see below).

- **lockedDesc**: the description to display when the object is locked or unlocked. The library default is fine for most situations, but if you want to customize it you need to define the property in the form lockedDesc = (isLocked() ? messageWhenLocked : messageWhenUnlocked), where messageWhenLocked and messageWhenUnlocked are single quoted strings or properties/methods evaluating to single quoted strings.

- **lockStatusObvious**: this should be true or nil depending on whether an actor should be able to tell by simple visual inspection that the object is locked. The library default is true. For a [LockableWithKey](lockablewithkey.md) (e.g. a door with a keyhole) it might not be obvious whether the object is locked until the player tries to open it. In such a case the most desirable behaviour might be for the game to change lockStatusObvious from nil to true once the door has been tried; for example you could override cannotUnlockMsg on the object to include something like '<.reveal door-locked>' and then set lockStatusObvious = gRevealed('door-locked').

- **lockStatusReportable**: this is used to decide whether the parser should report the object as being locked or unlocked. For example, if an object is open, it is obviously unlocked, so it is redundant to report something like "The door is red. It's open. It's unlocked. ", it is sufficient to report "The door is red. It's open. " The library takes care of this particular case by default, but there may be other cases where you want to override the library behaviour.

- **isLocked()**: note this is a *method*, not a property; test this value to determine whether the object is locked, but do *not* overwrite it to lock or unlock an object programmatically. Call makeLocked() instead.

- **makeLocked(stat)**: Call makeLocked(true) or makeLocked(nil) to lock or unlock the object programmatically (e.g. as the result of pushing a button or pulling a lever on an [IndirectLockable](indirectlockable.md)). You can also override this method if you want to produce some additional side-effects of locking or unlocking the object, but make sure you then call inherited(stat) somewhere in your makeLocked(stat) method.

- **initiallyLocked**: if this is true (as it is by default) then the Lockable object starts out locked, so if we don't want it to start out locked we need to change this to nil (note that this was first added to Lockable in TADS 3.0.10)

IMPORTANT NOTE. Since Lockable is a mix-in class (not derived from Thing) (1) it cannot be used on its own (you can't define a physical object as being simply Lockable, it must be a Lockable something, such as a Lockable, Container or a Lockable, Door) and (2) it must be listed *before* any Thing-derived class it is mixed-in with. Thus whereas the following works fine:

```tads3
+ lakeDoor : Lockable, Door 'door' 'door';
```

The following does not:

```tads3
+ lakeDoor : Door, Lockable  'door' 'door';
```

The second of these will compile fine, and the door will appear - but the lock won't work as expected (for example, even if the initiallyLocked property is set to true, the door won't start out locked).
