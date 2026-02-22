# ExternalEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1117)


An "external" event list is one whose state is driven externally to the script. Specifically, the state is *not* advanced by invoking the script; the state is advanced exclusively by some external process (for example, by a daemon that invokes the event list's advanceState() method).


**Superclass chain:** [EventList](eventlist.md) > [Script](script.md) > `object` > **ExternalEventList**


## Inherited Properties


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `scriptDone` *(overridden)*

Defined in misc.t, line 1118


## Inherited Methods


*From [EventList](eventlist.md):* [`advanceState`](eventlist.md#advanceState), [`construct`](eventlist.md#construct), [`doScript`](eventlist.md#doScript), [`doScriptEvent`](eventlist.md#doScriptEvent)


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
