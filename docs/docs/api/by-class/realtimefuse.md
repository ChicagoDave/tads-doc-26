# RealTimeFuse

*class* — defined in [events.t](../by-file/events.t.md) (line 1168)


Real-time fuse. This is an event that fires once at a specified elapsed time into the game.


**Superclass chain:** [RealTimeEvent](realtimeevent.md) > [BasicEvent](basicevent.md) > `object` > **RealTimeFuseSubclasses:** [RealTimeSenseFuse](realtimesensefuse.md)


## Inherited Properties


*From [RealTimeEvent](realtimeevent.md):* [`eventTime`](realtimeevent.md#eventTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, delta)` *(overridden)*

Defined in events.t, line 1174

Creation. 'delta' is the amount of real time (in milliseconds) that should elapse before the fuse is executed. If 'delta' is zero or negative, the fuse will be schedulable immediately.


### `executeEvent` *(overridden)*

Defined in events.t, line 1188

execute the fuse


## Inherited Methods


*From [RealTimeEvent](realtimeevent.md):* [`getEventTime`](realtimeevent.md#getEventTime), [`removeEvent`](realtimeevent.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
