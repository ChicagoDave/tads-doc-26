# SensoryEvent

*class* — defined in [objects.t](../by-file/objects.t.md) (line 758)


Sensory Event. This is an object representing a transient event, such as a sound, visual display, or odor, to which some objects observing the event might react.


**Superclass chain:** `object` > **SensoryEventSubclasses:** [SightEvent](sightevent.md), [SmellEvent](smellevent.md), [SoundEvent](soundevent.md)


## Properties


### `notifyProp`

Defined in objects.t, line 830

the notification property - this is the property we'll invoke on each observer to notify it of the event


### `sense`

Defined in objects.t, line 824

the sense in which the event is observable


## Methods


### `triggerEvent(source)`

Defined in objects.t, line 773

Trigger the event. This routine must be called at the time when the event is to occur. We'll notify every interested observer capable of sensing the event that the event is occurring, so observers can take appropriate action in response to the event.
