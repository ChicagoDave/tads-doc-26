# SenseDaemon

*class* — defined in [events.t](../by-file/events.t.md) (line 795)


Sensory-context-sensitive daemon - this is a daemon with an explicit sensory context. This is the daemon counterpart of SenseFuse.


**Superclass chain:** [Daemon](daemon.md) > [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **SenseDaemon**


## Inherited Properties


*From [Daemon](daemon.md):* [`interval_`](daemon.md#interval_)


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`isPromptDaemon`](event.md#isPromptDaemon), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, interval, source, sense)` *(overridden)*

Defined in events.t, line 796


## Inherited Methods


*From [Daemon](daemon.md):* [`executeEvent`](daemon.md#executeEvent)


*From [Event](event.md):* [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
