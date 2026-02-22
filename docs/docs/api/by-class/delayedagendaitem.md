# DelayedAgendaItem

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5625)


A delayed agenda item. This type of item becomes ready to execute when the game clock reaches a given turn counter.


**Superclass chain:** [AgendaItem](agendaitem.md) > `object` > **DelayedAgendaItem**


## Properties


### `isReady` *(overridden)*

Defined in actor.t, line 5627

we're ready if the game clock time has reached our ready time


### `readyTime`

Defined in actor.t, line 5630

the turn counter on the game clock when we become ready


## Inherited Properties


*From [AgendaItem](agendaitem.md):* [`agendaOrder`](agendaitem.md#agendaOrder), [`initiallyActive`](agendaitem.md#initiallyActive), [`isDone`](agendaitem.md#isDone)


## Methods


### `setDelay(turns)`

Defined in actor.t, line 5641

Set our ready time based on a delay from the current time. We'll become ready after the given number of turns elapses. For convenience, we return 'self', so a delayed agenda item can be initialized and added to an actor's agenda in one simple operation, like so:


## Inherited Methods


*From [AgendaItem](agendaitem.md):* [`execute`](agendaitem.md#execute), [`getActor`](agendaitem.md#getActor), [`invokeItem`](agendaitem.md#invokeItem), [`resetItem`](agendaitem.md#resetItem)
