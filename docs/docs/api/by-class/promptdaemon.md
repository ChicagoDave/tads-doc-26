# PromptDaemon

*class* — defined in [events.t](../by-file/events.t.md) (line 813)


Command Prompt Daemon. This is a special type of daemon that executes not according to the game clock, but rather once per command prompt. The system executes all of these daemons just before each time it prompts for a command line.


**Superclass chain:** [Event](event.md) > [BasicEvent](basicevent.md) > `object` > **PromptDaemonSubclasses:** [OneTimePromptDaemon](onetimepromptdaemon.md)


## Properties


### `isPromptDaemon` *(overridden)*

Defined in events.t, line 826

flag: we are a special per-command-prompt daemon


## Inherited Properties


*From [Event](event.md):* [`eventOrder`](event.md#eventOrder), [`nextRunTime`](event.md#nextRunTime)


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `executeEvent` *(overridden)*

Defined in events.t, line 815

execute the daemon


## Inherited Methods


*From [Event](event.md):* [`construct`](event.md#construct), [`delayEvent`](event.md#delayEvent), [`getNextRunTime`](event.md#getNextRunTime), [`removeEvent`](event.md#removeEvent)


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches)
