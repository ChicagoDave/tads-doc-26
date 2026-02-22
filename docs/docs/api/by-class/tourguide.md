# TourGuide

*class* — defined in [extras.t](../by-file/extras.t.md) (line 2319)


"Tour Guide" is a mix-in class for Actors. This class can be multiply inherited by objects along with Actor or a subclass of Actor. This mix-in makes the Follow action, when applied to the tour guide, initiate travel according to where the tour guide wants to go next. So, if the tour guide is here and is waving us through the door, FOLLOW GUIDE will initiate travel through the door.


**Superclass chain:** `object` > **TourGuide**


## Methods


### `dobjFor(Follow)`

Defined in extras.t, line 2320


### `getTourDest`

Defined in extras.t, line 2376

Get the travel connector that takes us to our next guided tour destination. By default, this returns the escortDest from our current actor state if our state is a guided tour state, or nil if our state is any other kind of state. Subclasses must override this if they use other kinds of states to represent guided tours, since we'll only detect that we're in a guided tour state if our current actor state object is of class GuidedTourState (or any subclass).
