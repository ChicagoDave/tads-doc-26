# RealTimeDaemon

*class* — defined in [events.t](../by-file/events.t.md) (line 1233)


Real-time daemon. This is an event that occurs repeatedly at given real-time intervals. When a daemon is executed, it is scheduled again for execution after its real-time interval elapses again. The daemon's first execution will occur one interval from the time at which the daemon is created.


**Superclass chain:** [RealTimeEvent](realtimeevent.md) > [BasicEvent](basicevent.md) > `object` > **RealTimeDaemonSubclasses:** [RealTimeSenseDaemon](realtimesensedaemon.md)


## Properties


### `interval_`

Defined in events.t, line 1275

my execution interval, in milliseconds


## Inherited Properties


*From [RealTimeEvent](realtimeevent.md):* [`eventTime`](realtimeevent.md#eventTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, interval)` *(overridden)*

Defined in events.t, line 1238

Creation. 'interval' is the number of milliseconds between invocations.


### `executeEvent` *(overridden)*

Defined in events.t, line 1254

execute the daemon


## Inherited Methods


*From [RealTimeEvent](realtimeevent.md):* [`getEventTime`](realtimeevent.md#getEventTime), [`removeEvent`](realtimeevent.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
