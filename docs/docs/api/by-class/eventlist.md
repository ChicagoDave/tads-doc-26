# EventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1017)


An "event list." This is a general-purpose type of script that lets you define the scripted events separately from the Script object.


**Superclass chain:** [Script](script.md) > `object` > **EventListSubclasses:** [CyclicEventList](cycliceventlist.md), [ExternalEventList](externaleventlist.md), [RandomEventList](randomeventlist.md), [ShuffledEventList](shuffledeventlist.md), [StopEventList](stopeventlist.md), [SyncEventList](synceventlist.md)


## Properties


### `curScriptState` *(overridden)*

Defined in misc.t, line 1034

by default, start at the first list element


### `eventList`

Defined in misc.t, line 1021

the list of events


### `eventListLen`

Defined in misc.t, line 1024

cached length of the event list


## Methods


### `advanceState`

Defined in misc.t, line 1027

advance to the next state


### `construct(lst)`

Defined in misc.t, line 1018


### `doScript` *(overridden)*

Defined in misc.t, line 1037

process the next step of the script


### `doScriptEvent(evt)`

Defined in misc.t, line 1060

carry out one script event


### `scriptDone`

Defined in misc.t, line 1103

Perform any end-of-script processing. By default, we advance the script to the next state.


## Inherited Methods


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
