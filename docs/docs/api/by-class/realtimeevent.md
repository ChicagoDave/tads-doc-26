# RealTimeEvent

*class* — defined in [events.t](../by-file/events.t.md) (line 1136)


Real-Time Event. This is an event that occurs according to elapsed wall-clock time in the real world.


**Superclass chain:** [BasicEvent](basicevent.md) > `object` > **RealTimeEventSubclasses:** [RealTimeDaemon](realtimedaemon.md), [RealTimeSenseDaemon](realtimesensedaemon.md), [RealTimeFuse](realtimefuse.md), [RealTimeSenseFuse](realtimesensefuse.md)


## Properties


### `eventTime`

Defined in events.t, line 1161

our scheduled event time


## Inherited Properties


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop)` *(overridden)*

Defined in events.t, line 1148

construction


### `getEventTime`

Defined in events.t, line 1141

Get the elapsed real time at which this event is triggered. This is a time value in terms of realTimeManager.getElapsedTime().


### `removeEvent`

Defined in events.t, line 1158

remove this event from the real-time event manager


## Inherited Methods


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches), [`executeEvent`](basicevent.md#executeEvent)
