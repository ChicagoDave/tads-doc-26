# RealTimeSenseDaemon

*class* — defined in [events.t](../by-file/events.t.md) (line 1283)


Sensory-context-sensitive real-time daemon - this is a real-time daemon with an explicit sensory context. This is the daemon counterpart of RealTimeSenseFuse.


**Superclass chain:** [RealTimeDaemon](realtimedaemon.md) > [RealTimeEvent](realtimeevent.md) > [BasicEvent](basicevent.md) > `object` > **RealTimeSenseDaemon**


## Inherited Properties


*From [RealTimeDaemon](realtimedaemon.md):* [`interval_`](realtimedaemon.md#interval_)


*From [RealTimeEvent](realtimeevent.md):* [`eventTime`](realtimeevent.md#eventTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, interval, source, sense)` *(overridden)*

Defined in events.t, line 1284


## Inherited Methods


*From [RealTimeDaemon](realtimedaemon.md):* [`executeEvent`](realtimedaemon.md#executeEvent)


*From [RealTimeEvent](realtimeevent.md):* [`getEventTime`](realtimeevent.md#getEventTime), [`removeEvent`](realtimeevent.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
