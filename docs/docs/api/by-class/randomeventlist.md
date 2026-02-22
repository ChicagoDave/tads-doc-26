# RandomEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1207)


Randomized event list. This is similar to a regular event list, but chooses an event at random each time it's invoked.


**Superclass chain:** [RandomFiringScript](randomfiringscript.md) > `object` > [EventList](eventlist.md) > [Script](script.md) > **RandomEventList**


## Inherited Properties


*From [RandomFiringScript](randomfiringscript.md):* [`eventPercent`](randomfiringscript.md#eventPercent), [`eventReduceAfter`](randomfiringscript.md#eventReduceAfter), [`eventReduceTo`](randomfiringscript.md#eventReduceTo)


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `doScript` *(overridden)*

Defined in misc.t, line 1209

process the next step of the script


### `getNextRandom`

Defined in misc.t, line 1233

Get the next random state. By default, we simply return a number from 1 to the number of entries in our event list. This is a separate method to allow subclasses to customize the way the random number is selected.


## Inherited Methods


*From [RandomFiringScript](randomfiringscript.md):* [`checkEventOdds`](randomfiringscript.md#checkEventOdds)


*From [EventList](eventlist.md):* [`advanceState`](eventlist.md#advanceState), [`construct`](eventlist.md#construct), [`doScriptEvent`](eventlist.md#doScriptEvent), [`scriptDone`](eventlist.md#scriptDone)


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
