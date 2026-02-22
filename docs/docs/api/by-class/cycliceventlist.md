# CyclicEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1125)


A cyclical event list - this runs through the event list in order, returning to the first element when we pass the last element.


**Superclass chain:** [EventList](eventlist.md) > [Script](script.md) > `object` > **CyclicEventList**


## Inherited Properties


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `advanceState` *(overridden)*

Defined in misc.t, line 1126


## Inherited Methods


*From [EventList](eventlist.md):* [`construct`](eventlist.md#construct), [`doScript`](eventlist.md#doScript), [`doScriptEvent`](eventlist.md#doScriptEvent), [`scriptDone`](eventlist.md#scriptDone)


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
