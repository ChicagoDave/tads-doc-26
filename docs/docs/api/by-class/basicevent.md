# BasicEvent

*class* — defined in [events.t](../by-file/events.t.md) (line 581)


A basic event, for game-time and real-time events.


**Superclass chain:** `object` > **BasicEvent**


<details><summary>Subclasses (12)</summary>

- [Event](event.md)
- [Daemon](daemon.md)
- [SenseDaemon](sensedaemon.md)
- [Fuse](fuse.md)
- [SenseFuse](sensefuse.md)
- [PromptDaemon](promptdaemon.md)
- [OneTimePromptDaemon](onetimepromptdaemon.md)
- [RealTimeEvent](realtimeevent.md)
- [RealTimeDaemon](realtimedaemon.md)
- [RealTimeSenseDaemon](realtimesensedaemon.md)
- [RealTimeFuse](realtimefuse.md)
- [RealTimeSenseFuse](realtimesensefuse.md)

</details>


## Properties


### `obj_`

Defined in events.t, line 617

the object and property we invoke


### `prop_`

Defined in events.t, line 618


### `sense_`

Defined in events.t, line 631


### `source_`

Defined in events.t, line 630

The sensory context of the event. When the event fires, we'll execute its method in this sensory context, so that any messages generated will be displayed only if the player character can sense the source object in the given sense.


## Methods


### `callMethod`

Defined in events.t, line 605

Call our underlying method. This is an internal routine intended for use by the executeEvent() implementations.


### `construct(obj, prop)`

Defined in events.t, line 583

construction


### `eventMatches(obj, prop)`

Defined in events.t, line 599

does this event match the given object/property combination?


### `executeEvent`

Defined in events.t, line 596

Execute the event. This must be overridden by the subclass to perform the appropriate operation when executed. In particular, the subclass must reschedule or unschedule the event, as appropriate.
