# ConvAgendaItem

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5608)


A "conversational" agenda item. This type of item is ready to execute only when the actor hasn't engaged in conversation during the same turn. This type of item is ideal for situations where we want the actor to pursue a conversational topic, because we won't initiate the action until we get a turn where the player didn't directly talk to us.


**Superclass chain:** [AgendaItem](agendaitem.md) > `object` > **ConvAgendaItem**


## Properties


### `isReady` *(overridden)*

Defined in actor.t, line 5609


### `otherActor`

Defined in actor.t, line 5618

The actor we're planning to address - by default, this is the PC. If the conversational overture will be directed to another NPC, you can specify that other actor here.


## Inherited Properties


*From [AgendaItem](agendaitem.md):* [`agendaOrder`](agendaitem.md#agendaOrder), [`initiallyActive`](agendaitem.md#initiallyActive), [`isDone`](agendaitem.md#isDone)


## Inherited Methods


*From [AgendaItem](agendaitem.md):* [`execute`](agendaitem.md#execute), [`getActor`](agendaitem.md#getActor), [`invokeItem`](agendaitem.md#invokeItem), [`resetItem`](agendaitem.md#resetItem)
