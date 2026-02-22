# AgendaItem

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5511)


An "agenda item." Each actor can have its own "agenda," which is a list of these items. Each item represents an action that the actor wants to perform - this is usually a goal the actor wants to achieve, or a conversational topic the actor wants to pursue.


**Superclass chain:** `object` > **AgendaItemSubclasses:** [BoredomAgendaItem](boredomagendaitem.md), [ConvAgendaItem](convagendaitem.md), [DelayedAgendaItem](delayedagendaitem.md)


## Properties


### `agendaOrder`

Defined in actor.t, line 5558

The ordering of the item relative to other agenda items. When we choose an agenda item to execute, we always choose the lowest numbered item that's ready to run. You can leave this with the default value if you don't care about the order.


### `initiallyActive`

Defined in actor.t, line 5525

Is this item active at the start of the game? Override this to true to make the item initially active; we'll add it to the actor's agenda during the game's initialization.


### `isDone`

Defined in actor.t, line 5550

Is this item done? On each turn, we'll remove any items marked as done from the actor's agenda list. We remove items marked as done before executing any items, so done-ness overrides readiness; in other words, if an item is both 'done' and 'ready', it'll simply be removed from the list and will not be executed.


### `isReady`

Defined in actor.t, line 5533

Is this item ready to execute? The actor will only execute an agenda item when this condition is met. By default, we're ready to execute. Items can override this to provide a declarative condition of readiness if desired.


## Methods


### `execute`

Defined in actor.t, line 5587

An AgendaItem initializer. For each agenda item that's initially active, we'll add the item to its actor's agenda.


### `getActor`

Defined in actor.t, line 5518

My actor - agenda items should be nested within the actor using '+' so that we can find our actor. Note that this doesn't add the item to the actor's agenda - that has to be done explicitly with actor.addToAgenda().


### `invokeItem`

Defined in actor.t, line 5565

Execute this item. This is invoked during the actor's turn when the item is the first item that's ready to execute in the actor's agenda list. We do nothing by default.


### `resetItem`

Defined in actor.t, line 5574

Reset the item. This is invoked whenever the item is added to an actor's agenda. By default, we'll set isDone to nil as long as isDone isn't a method; this makes it easier to reuse agenda items, since we don't have to worry about clearing out the isDone flag when reusing an item.
