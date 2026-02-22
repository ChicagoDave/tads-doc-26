# Direction

*class* — defined in [travel.t](../by-file/travel.t.md) (line 30)


Directions. Each direction is represented by an instance of Direction.


**Superclass chain:** `object` > **DirectionSubclasses:** [CompassDirection](compassdirection.md), [RelativeDirection](relativedirection.md), [ShipboardDirection](shipboarddirection.md), [VerticalDirection](verticaldirection.md)


## Properties


### `allDirections`

Defined in travel.t, line 100

A master list of the defined directions. We build this automatically during initialization to include each Direction instance. Any operation that wants to iterate over all possible directions can run through this list.


### `dirProp`

Defined in travel.t, line 36

The link property for the direction. This is a property pointer that we use to ask an actor's location for a TravelConnector when the actor attempts to travel in this direction.


### `sortingOrder`

Defined in travel.t, line 85

Our sorting order in the master list. We use this to present directions in a consistent, aesthetically pleasing order in listings involving multiple directions. The sorting order is simply an integer that gives the relative position in the list; the list of directions is sorted from lowest sorting order to highest. Sorting order numbers don't have to be contiguous, since we simply put the directions in an order that makes the sortingOrder values ascend through the list.


## Methods


### `defaultConnector(loc)`

Defined in travel.t, line 45

The default TravelConnector when an actor attempts travel in this direction, but the actor's location does not define the dirProp property for this direction. This is almost always a connector that goes nowhere, such as noTravel, since this is used only when a location doesn't have a link for travel in this direction.


### `initializeDirection`

Defined in travel.t, line 52

Initialize. We'll use this routine to add each Direction instance to the master direction list (Direction.allDirections) during pre-initialization.


### `initializeDirectionClass`

Defined in travel.t, line 63

Class initialization - this is called once on the class object. We'll build our master list of all of the Direction objects in the game, and then sort the list using the sorting order.


### `sayArriving(traveler)`

Defined in en_us.t, line 3055

describe a traveler arriving from this direction


### `sayDeparting(traveler)`

Defined in en_us.t, line 3062

describe a traveler departing in this direction
