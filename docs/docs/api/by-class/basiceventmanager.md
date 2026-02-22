# BasicEventManager

*class* — defined in [events.t](../by-file/events.t.md) (line 342)


Basic Event Manager. This is a common base class for the game-time and real-time event managers. This class handles the details of managing the event queue; the subclasses must define the specifics of event timing.


**Superclass chain:** `object` > **BasicEventManagerGlobal objects:** [eventManager](eventmanager.md), [realTimeManager](realtimemanager.md)


## Properties


### `// events_`

Defined in events.t, line 418

event list - each instance must initialize this to a vector


## Methods


### `addEvent(event)`

Defined in events.t, line 344

add an event


### `removeCurrentEvent`

Defined in events.t, line 411

Remove the current event - this is provided for convenience so that an event can cancel itself in the course of its execution.


### `removeEvent(event)`

Defined in events.t, line 351

remove an event


### `removeMatchingEvents(obj, prop)`

Defined in events.t, line 375

Remove events matching the given object and property combination. We remove all events that match both the object and property (events matching only the object or only the property are not affected).
