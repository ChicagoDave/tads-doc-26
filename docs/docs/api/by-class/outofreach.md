# OutOfReach

*class* — defined in [objects.t](../by-file/objects.t.md) (line 2271)


Out Of Reach - this is a special mix-in that can be used to create an object that places its *contents* out of reach under customizable conditions, and can optionally place itself out of reach as well.


**Superclass chain:** `object` > **OutOfReach**


## Methods


### `cannotReachFromInsideMsg(dest)`

Defined in objects.t, line 2328


### `cannotReachFromOutsideMsg(dest)`

Defined in objects.t, line 2327

The message to use to indicate that we can't reach an object, because the actor is outside me and the target is inside, or vice versa. Each of these can return a property ID giving an actor action message property, or can simply return a string with the message text.


### `canObjReachContents(obj)`

Defined in objects.t, line 2341

Determine if the given object can reach my contents. 'obj' is the object (usually an actor) attempting to reach my contents from outside of me.


### `canObjReachSelf(obj)`

Defined in objects.t, line 2350

Determine if the given object can reach me. 'obj' is the object (usually an actor) attempting to reach this object.


### `canReachFromInside(obj, dest)`

Defined in objects.t, line 2361

Determine if the given object outside of me is reachable from within me. 'obj' (usually an actor) is attempting to reach 'dest'.


### `canReachSelfFromInside(obj)`

Defined in objects.t, line 2371

Determine if we can reach this object itself from within. This is used when 'obj' tries to touch this object when 'obj' is located within this object.


### `checkTouchViaPath(obj, dest, op)`

Defined in objects.t, line 2272


### `tryImplicitRemoveObstructor(sense, obj)`

Defined in objects.t, line 2377

We cannot implicitly remove this obstruction, so simply return nil when asked.
