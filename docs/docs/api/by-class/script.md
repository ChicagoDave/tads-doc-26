# Script

*class* — defined in [misc.t](../by-file/misc.t.md) (line 857)


Generic script object. This class can be used to implement a simple state machine.


**Superclass chain:** `object` > **ScriptSubclasses:** [EventList](eventlist.md), [CyclicEventList](cycliceventlist.md), [ExternalEventList](externaleventlist.md), [RandomEventList](randomeventlist.md), [ShuffledEventList](shuffledeventlist.md), [StopEventList](stopeventlist.md), [SyncEventList](synceventlist.md)


## Properties


### `curScriptState`

Defined in misc.t, line 889

Property giving our current state. This should never be used directly; instead, getScriptState() should always be used, since getScriptState() can be overridden so that the state depends on something other than this internal state property. The meaning of the state identifier is specific to each subclass.


## Methods


### `doScript`

Defined in misc.t, line 877

Process the next step of the script. This routine must be overridden to perform the action of the script. This routine's action should call getScriptState() to get our current state, and should update the internal state appropriately to take us to the next step after the current one.


### `getScriptState`

Defined in misc.t, line 862

Get the current state. This returns a value that gives the current state of the script, which is usually simply an integer.
