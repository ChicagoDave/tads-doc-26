# Daemon

*class* — defined in [events.t](../by-file/events.t.md) (line 744)


Daemon. A daemon is an event that fires repeatedly at given intervals. When a daemon is executed, it is scheduled again for execution after its interval elapses again.


**Superclass chain:** [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **DaemonSubclasses:** [SenseDaemon](sensedaemon.md)


## Properties


### `interval_`

Defined in events.t, line 788

our execution interval, in turns


## Inherited Properties


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`isPromptDaemon`](event.md#isPromptDaemon), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, interval)` *(overridden)*

Defined in events.t, line 753

Creation. 'interval' is the number of turns between invocations of the daemon; this should be at least 1, which causes the daemon to be invoked on each turn. The first execution will be (interval-1) turns in the future - so if interval is 1, the daemon will first be executed on the current turn, and if interval is 2, the daemon will be executed on the next turn.


### `executeEvent` *(overridden)*

Defined in events.t, line 778

execute the daemon


## Inherited Methods


*From [Event](event.md):* [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
