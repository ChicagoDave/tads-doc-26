# OneTimePromptDaemon

*class* — defined in [events.t](../by-file/events.t.md) (line 853)


A one-time-only prompt daemon is a regular command prompt daemon, except that it fires only once. After it fires once, the daemon automatically deactivates itself, so that it won't fire again.


**Superclass chain:** [PromptDaemon](promptdaemon.md) > [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **OneTimePromptDaemon**


## Inherited Properties


*From [PromptDaemon](promptdaemon.md):* [`isPromptDaemon`](promptdaemon.md#isPromptDaemon)


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `executeEvent` *(overridden)*

Defined in events.t, line 854


## Inherited Methods


*From [Event](event.md):* [`construct`](event.md#construct), [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
