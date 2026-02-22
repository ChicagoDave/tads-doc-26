# SenseFuse

*class* — defined in [events.t](../by-file/events.t.md) (line 727)


Sensory-context-sensitive fuse - this is a fuse with an explicit sensory context. We'll run the fuse in its sense context, so any messages generated will be visible only if the given source object is reachable by the player character in the given sense.


**Superclass chain:** [Fuse](fuse.md) > [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **SenseFuse**


## Inherited Properties


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`isPromptDaemon`](event.md#isPromptDaemon), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, turns, source, sense)` *(overridden)*

Defined in events.t, line 728


## Inherited Methods


*From [Fuse](fuse.md):* [`executeEvent`](fuse.md#executeEvent)


*From [Event](event.md):* [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
