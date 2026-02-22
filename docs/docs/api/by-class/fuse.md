# Fuse

*class* — defined in [events.t](../by-file/events.t.md) (line 682)


Fuse. A fuse is an event that fires once at a given time in the future. Once a fuse is executed, it is removed from further scheduling.


**Superclass chain:** [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **FuseSubclasses:** [SenseFuse](sensefuse.md)


## Inherited Properties


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`isPromptDaemon`](event.md#isPromptDaemon), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop, turns)` *(overridden)*

Defined in events.t, line 688

Creation. 'turns' is the number of turns in the future at which the fuse is executed; if turns is 0, the fuse will be executed on the current turn.


### `executeEvent` *(overridden)*

Defined in events.t, line 701

execute the fuse


## Inherited Methods


*From [Event](event.md):* [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
