# Event

*class* — defined in [events.t](../by-file/events.t.md) (line 637)


Base class for fuses and daemons


**Superclass chain:** [BasicEvent](basicevent.md) > `object` > **EventSubclasses:** [Daemon](daemon.md), [SenseDaemon](sensedaemon.md), [Fuse](fuse.md), [SenseFuse](sensefuse.md), [PromptDaemon](promptdaemon.md), [OneTimePromptDaemon](onetimepromptdaemon.md)


## Properties


### `eventOrder`

Defined in events.t, line 654

Event order - this establishes the order we run relative to other events scheduled to run at the same game clock time. Lowest number goes first. By default, we provide an event order of 100, which should leave plenty of room for custom events before and after default events.


### `isPromptDaemon`

Defined in events.t, line 674

by default, we're not a per-command-prompt daemon


### `nextRunTime`

Defined in events.t, line 671

our next execution time, expressed in game clock time; by default, we'll set this to nil, which means that we are not scheduled to execute at all


## Inherited Properties


*From [BasicEvent](basicevent.md):* [`obj_`](basicevent.md#obj_), [`prop_`](basicevent.md#prop_), [`sense_`](basicevent.md#sense_), [`source_`](basicevent.md#source_)


## Methods


### `construct(obj, prop)` *(overridden)*

Defined in events.t, line 657

creation


### `delayEvent(turns)`

Defined in events.t, line 642

delay our scheduled run time by the given number of turns


### `getNextRunTime`

Defined in events.t, line 639

our next run time, in game clock time


### `removeEvent`

Defined in events.t, line 645

remove this event from the event manager


## Inherited Methods


*From [BasicEvent](basicevent.md):* [`callMethod`](basicevent.md#callMethod), [`eventMatches`](basicevent.md#eventMatches), [`executeEvent`](basicevent.md#executeEvent)
