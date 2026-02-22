# SyncEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1189)


A synchronized event list. This is an event list that takes its actions from a separate event list object. We get our current state from the other list, and advancing our state advances the other list's state in lock step. Set 'masterObject' to refer to the master list whose state we synchronize with.


**Superclass chain:** [EventList](eventlist.md) > [Script](script.md) > `object` > **SyncEventList**


## Properties


### `masterObject`

Defined in misc.t, line 1191

my master event list object


## Inherited Properties


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `advanceState` *(overridden)*

Defined in misc.t, line 1197

to advance my state, advance the master list's state


### `getScriptState` *(overridden)*

Defined in misc.t, line 1194

my state is simply the master list's state


### `scriptDone` *(overridden)*

Defined in misc.t, line 1200

let the master list take care of finishing a script step


## Inherited Methods


*From [EventList](eventlist.md):* [`construct`](eventlist.md#construct), [`doScript`](eventlist.md#doScript), [`doScriptEvent`](eventlist.md#doScriptEvent)
