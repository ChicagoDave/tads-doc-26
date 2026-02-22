# BoredomAgendaItem

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5180)


A special kind of agenda item for monitoring "boredom" during a conversation. We check to see if our actor is in a conversation, and the PC has been ignoring the conversation for too long; if so, our actor initiates the end of the conversation, since the PC apparently isn't paying any attention to us.


**Superclass chain:** [AgendaItem](agendaitem.md) > `object` > **BoredomAgendaItem**


## Properties


### `agendaOrder` *(overridden)*

Defined in actor.t, line 5218

by default, handle boredom before other agenda items - we do this because an ongoing conversation will be the first thing on the NPC's mind


## Inherited Properties


*From [AgendaItem](agendaitem.md):* [`initiallyActive`](agendaitem.md#initiallyActive), [`isDone`](agendaitem.md#isDone), [`isReady`](agendaitem.md#isReady)


## Methods


### `construct(actor)`

Defined in actor.t, line 5182

we construct these dynamically during actor initialization


### `invokeItem` *(overridden)*

Defined in actor.t, line 5204

on invocation, end the conversation


### `isReady`

Defined in actor.t, line 5192

we're ready to run if our actor is in an InConversationState and its boredom count has reached the limit for the state


## Inherited Methods


*From [AgendaItem](agendaitem.md):* [`execute`](agendaitem.md#execute), [`getActor`](agendaitem.md#getActor), [`resetItem`](agendaitem.md#resetItem)
