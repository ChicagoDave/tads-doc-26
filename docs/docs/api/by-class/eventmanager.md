# eventManager

*object* — defined in [events.t](../by-file/events.t.md) (line 425)


Event Manager. This is a schedulable object that keeps track of fuses and daemons, and schedules their execution.


**Superclass chain:** [BasicEventManager](basiceventmanager.md) > `object` > [Schedulable](schedulable.md) > **eventManager**


## Properties


### `curEvent_`

Defined in events.t, line 563

the event currently being executed


### `events_` *(overridden)*

Defined in events.t, line 560

our list of fuses and daemons


### `scheduleOrder` *(overridden)*

Defined in events.t, line 432

Use a scheduling order of 1000 to ensure we go after all actors. By default, actors use scheduling orders in the range 100 to 400, so our order of 1000 ensures that fuses and daemons run after all characters on a given turn.


## Inherited Properties


*From [Schedulable](schedulable.md):* [`allSchedulables`](schedulable.md#allSchedulables), [`gameClockTime`](schedulable.md#gameClockTime), [`nextRunTime`](schedulable.md#nextRunTime)


## Methods


### `executeList(lst)`

Defined in events.t, line 499

internal service routine - execute the fuses and daemons in the given list, in eventOrder priority order


### `executePrompt`

Defined in events.t, line 489

Execute a command prompt turn. We'll execute each per-command-prompt daemon.


### `executeTurn` *(overridden)*

Defined in events.t, line 467

Execute a turn. We'll execute each fuse and each daemon that is currently schedulable.


### `getNextRunTime` *(overridden)*

Defined in events.t, line 438

Get the next run time. We'll find the lowest run time of our fuses and daemons and return that.


## Inherited Methods


*From [BasicEventManager](basiceventmanager.md):* [`addEvent`](basiceventmanager.md#addEvent), [`removeCurrentEvent`](basiceventmanager.md#removeCurrentEvent), [`removeEvent`](basiceventmanager.md#removeEvent), [`removeMatchingEvents`](basiceventmanager.md#removeMatchingEvents)


*From [Schedulable](schedulable.md):* [`calcScheduleOrder`](schedulable.md#calcScheduleOrder), [`construct`](schedulable.md#construct), [`execute`](schedulable.md#execute), [`incNextRunTime`](schedulable.md#incNextRunTime)
