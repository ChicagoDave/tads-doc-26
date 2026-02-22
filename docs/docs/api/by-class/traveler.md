# Traveler

*class* — defined in [travel.t](../by-file/travel.t.md) (line 273)


A Traveler is an object that can travel. The two main kinds of travelers are Actors and Vehicles. A vehicle can contain multiple actors, so a single vehicle travel operation could move several actors.


**Superclass chain:** [TravelMessageHandler](travelmessagehandler.md) > `object` > **TravelerSubclasses:** [Actor](actor.md), [UntakeableActor](untakeableactor.md), [Person](person.md), [Vehicle](vehicle.md)


## Properties


### `getTravelerActors`

Defined in travel.t, line 723

Get the list of actors taking part in the travel. When an actor is the traveler, this list simply contains the actor itself; for a vehicle or other composite traveler that moves more than one actor at a time, this should return the list of all of the actors involved in the travel.


### `getTravelerMotiveActors`

Defined in travel.t, line 734

Get the list of actors traveling undo their own power. In the case of an actor traveling directly, this is just the actor; in the case of an actor pushing something, this is likewise the actor; in the case of a group of actors traveling together, this is the list of traveling actors; in the case of a vehicle, this is an empty list, since anyone traveling with the vehicle is traveling under the vehicle's power.


## Methods


### `canTravelVia(connector, dest)`

Defined in travel.t, line 308

Can the traveler travel via the given connector to the given destination? Returns true if the travel is permitted, nil if not.


### `checkDirectlyInRoom(dest, allowImplicit)`

Defined in travel.t, line 279

Check, using pre-condition rules, that the traveler is directly in the given room. We'll attempt to implicitly remove the actor from any nested rooms within the given room.


### `checkMovingTravelerInto(room, allowImplicit)`

Defined in travel.t, line 289

Check, using pre-condition rules, that the traveler is in the given room, moving the traveler to the room if possible.


### `describeArrival(origin, backConnector)`

Defined in travel.t, line 415

Show my arrival message - this is shown when I'm entering a room in view of the player character from a location where the player character could not see me. 'backConnector' is the connector in the destination location from which we appear to be emerging.


### `describeDeparture(dest, connector)`

Defined in travel.t, line 327

Show my departure message - this is shown when I'm leaving a room where the player character can see me for another room where the player character cannot see me.


### `describeNpcArrival(origin, backConnector)`

Defined in travel.t, line 462

Describe the arrival of a non-player character or any other traveler that doesn't involve the player character.


### `describeNpcDeparture(dest, connector)`

Defined in travel.t, line 355

Describe the departure of a non-player character, or any traveler not involving the player character.


### `explainNoTravelVia(connector, dest)`

Defined in travel.t, line 320

Explain why the given travel is not possible. This is called when canTravelVia() returns nil, to display a report to the player explaining why the travel was disallowed.


### `forEachTravelingActor(func)`

Defined in travel.t, line 710

invoke a callback function for each traveling actor


### `getNotifyTable`

Defined in travel.t, line 665

Get a lookup table giving the set of objects to be notified of a beforeTravel/afterTravel event. By default, we return a table including every object connected to the traveler by containment.


### `isActorTraveling(actor)`

Defined in travel.t, line 681

Is the given actor traveling with this traveler? Returns true if the actor is in my getTravelerActors list.


### `isTravelerCarrying(obj)`

Defined in travel.t, line 692

Is the given object being carried by the traveler? Returns true if the object is inside the traveler itself, or is inside any of the actors traveling.


### `travelerLocName`

Defined in en_us.t, line 2776

Get my location's name, from the PC's perspective, for describing my arrival to or departure from my current location. We'll simply return our location's destName, or "the area" if it doesn't have one.


### `travelerPreCond(conn)`

Defined in travel.t, line 298

Get the travel preconditions specific to the traveler, for the given connector. By default, we return no extra conditions.


### `travelerRemoteLocName`

Defined in en_us.t, line 2792

Get my "remote" location name, from the PC's perspective. This returns my location name, but only if my location is remote from the PC's perspective - that is, my location has to be outside of the PC's top-level room. If we're within the PC's top-level room, we'll simply return an empty string.


### `travelerSeenBy(actor)`

Defined in travel.t, line 675

Determine if the given actor can see this traveler. By default, we'll simply check to see if the actor can see 'self'.


### `travelerTravelTo(dest, connector, backConnector)`

Defined in travel.t, line 555

Travel to a new location. Moves the traveler to a new location via the given connector, triggering any side effects of the travel.


### `travelerTravelWithin(actor, dest)`

Defined in travel.t, line 655

Perform "local" travel - that is, travel between nested rooms within a single top-level location. By default, we simply defer to the actor to let it perform the local travel.


## Inherited Methods


*From [TravelMessageHandler](travelmessagehandler.md):* [`getNominalTraveler`](travelmessagehandler.md#getNominalTraveler), [`sayArriving`](travelmessagehandler.md#sayArriving), [`sayArrivingDir`](travelmessagehandler.md#sayArrivingDir), [`sayArrivingDownStairs`](travelmessagehandler.md#sayArrivingDownStairs), [`sayArrivingLocally`](travelmessagehandler.md#sayArrivingLocally), [`sayArrivingThroughPassage`](travelmessagehandler.md#sayArrivingThroughPassage), [`sayArrivingUpStairs`](travelmessagehandler.md#sayArrivingUpStairs), [`sayArrivingViaPath`](travelmessagehandler.md#sayArrivingViaPath), [`sayDeparting`](travelmessagehandler.md#sayDeparting), [`sayDepartingDir`](travelmessagehandler.md#sayDepartingDir), [`sayDepartingDownStairs`](travelmessagehandler.md#sayDepartingDownStairs), [`sayDepartingLocally`](travelmessagehandler.md#sayDepartingLocally), [`sayDepartingThroughPassage`](travelmessagehandler.md#sayDepartingThroughPassage), [`sayDepartingUpStairs`](travelmessagehandler.md#sayDepartingUpStairs), [`sayDepartingViaPath`](travelmessagehandler.md#sayDepartingViaPath), [`sayTravelingRemotely`](travelmessagehandler.md#sayTravelingRemotely)
