# Schedulable

*class* — defined in [events.t](../by-file/events.t.md) (line 223)


An item that can be scheduled for time-based notifications. The main scheduler loop in runScheduler() operates on objects of this class.


**Superclass chain:** `object` > **SchedulableSubclasses:** [Actor](actor.md), [UntakeableActor](untakeableactor.md), [Person](person.md)


**Global objects:** [eventManager](eventmanager.md)


## Properties


### `allSchedulables`

Defined in events.t, line 308

A list of all of the Schedulable objects in the game. We set this up during pre-initialization; if any Schedulable instances are created dynamically, they must be explicitly added to this list after creation.


### `gameClockTime`

Defined in events.t, line 300

A class variable giving the current game clock time. This is a class variable because there's only one global game clock. The game clock starts at zero and increments in game time units; a game time unit is the arbitrary quantum of time for our event scheduling system.


### `nextRunTime`

Defined in events.t, line 291

my next running time, in game clock time


### `scheduleOrder`

Defined in events.t, line 273

Scheduling order. This determines which item goes first when multiple items are schedulable at the same time (i.e., they all have the same getNextRunTime() values). The item with the lowest number here goes first.


## Methods


### `calcScheduleOrder`

Defined in events.t, line 288

Calculate the scheduling order, returning the order value and storing it in our property scheduleOrder. This is used to calculate and cache the value prior to sorting a list of schedulable items. We use this two-step approach (first calculate, then sort) so that we avoid repeatedly evaluating a complex calculation, if indeed there is a complex calculation to perform.


### `construct`

Defined in events.t, line 225

construction - add myself to the Schedulable list


### `execute`

Defined in events.t, line 320

Execute preinitialization. Build a list of all of the schedulable objects in the game, so that we can scan this list quickly during play.


### `executeTurn`

Defined in events.t, line 262

Notify this object that its scheduled run time has arrived. This should perform the scheduled task. If the scheduled task takes any game time, the object's internal next run time should be updated accordingly.


### `getNextRunTime`

Defined in events.t, line 240

Get the next time (on the game clock) at which I'm eligible for execution. We won't receive any scheduling notifications until this time. If this object doesn't want any scheduling notifications, return nil.


### `incNextRunTime(amt)`

Defined in events.t, line 243

advance my next run time by the given number of clock units
