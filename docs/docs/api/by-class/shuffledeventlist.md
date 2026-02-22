# ShuffledEventList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1268)


Shuffled event list. This is similar to a random event list, except that we fire our events in a "shuffled" order rather than an independently random order. "Shuffled order" means that we fire the events in random order, but we don't re-fire an event until we've run through all of the other events. The effect is as though we were dealing from a deck of cards.


**Superclass chain:** [RandomFiringScript](randomfiringscript.md) > `object` > [EventList](eventlist.md) > [Script](script.md) > **ShuffledEventList**


## Properties


### `firstEvents`

Defined in misc.t, line 1273

a list of events to go through sequentially, in the exact order specified, before firing any events from the main list


### `shuffledList_`

Defined in misc.t, line 1378

our ShuffledList - we'll initialize this on demand


### `shuffleFirst`

Defined in misc.t, line 1283

Flag: shuffle the eventList list before we show it for the first time. By default, this is set to true, so that the behavior is random on each independent run of the game. However, it might be desirable in some cases to always use the original ordering of the eventList list the first time through the list. If this is set to nil, we won't shuffle the list the first time through.


### `suppressRepeats`

Defined in misc.t, line 1298

Flag: suppress repeats in the shuffle. If this is true, it prevents a given event from showing up twice in a row, which could otherwise happen right after a shuffle. This is ignored for lists with one or two events: it's impossible to prevent repeats in a one-element list, and doing so in a two-element list would produce a predictable A-B-A-B... pattern.


## Inherited Properties


*From [RandomFiringScript](randomfiringscript.md):* [`eventPercent`](randomfiringscript.md#eventPercent), [`eventReduceAfter`](randomfiringscript.md#eventReduceAfter), [`eventReduceTo`](randomfiringscript.md#eventReduceTo)


*From [EventList](eventlist.md):* [`curScriptState`](eventlist.md#curScriptState), [`eventList`](eventlist.md#eventList), [`eventListLen`](eventlist.md#eventListLen)


## Methods


### `doScript` *(overridden)*

Defined in misc.t, line 1301

process the next step of the script


### `getNextRandom`

Defined in misc.t, line 1358

Get the next random event. We'll pick an event from our list of events using a ShuffledIntegerList to ensure we pick each value once before re-using any values.


## Inherited Methods


*From [RandomFiringScript](randomfiringscript.md):* [`checkEventOdds`](randomfiringscript.md#checkEventOdds)


*From [EventList](eventlist.md):* [`advanceState`](eventlist.md#advanceState), [`construct`](eventlist.md#construct), [`doScriptEvent`](eventlist.md#doScriptEvent), [`scriptDone`](eventlist.md#scriptDone)


*From [Script](script.md):* [`getScriptState`](script.md#getScriptState)
