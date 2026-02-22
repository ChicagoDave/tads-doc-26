# StopEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1167)


A stopping event list - this runs through the event list in order, then stops at the last item and repeats it each time the script is subsequently invoked.


**Superclass chain:** [EventList](eventlist.md) > [Script](script.md) > `object` > **StopEventList**


## Inherited Properties


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `advanceState` *(overridden)*

Defined in misc.t, line 1168


## Inherited Methods


*From [EventList](eventlist.md):* [`construct`](eventlist.md#construct), [`doScript`](eventlist.md#doScript), [`doScriptEvent`](eventlist.md#doScriptEvent), [`scriptDone`](eventlist.md#scriptDone)


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
