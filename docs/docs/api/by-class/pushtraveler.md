# PushTraveler

*class* — defined in [travel.t](../by-file/travel.t.md) (line 3314)


A special Traveler class for travel involving pushing an object from one room to another. This class encapsulates the object being pushed and the actual Traveler performing the travel.


**Superclass chain:** `object` > **PushTraveler**


## Properties


### `obj_`

Defined in travel.t, line 3323

the object being pushed


### `traveler_`

Defined in travel.t, line 3329

the underlying Traveler - this is the real Traveler that will move to a new location


## Methods


### `canTravelVia(connector, dest)`

Defined in travel.t, line 3400

Can we travel via the given connector? We'll ask our underlying traveler first, and if that succeeds, we'll ask the object we're pushing.


### `construct(obj, traveler)`

Defined in travel.t, line 3315


### `explainNoTravelVia(connector, dest)`

Defined in travel.t, line 3412

Explain why the given travel is not possible. If our underlying traveler raised the objection, let it explain; otherwise, let our pushed object explain.


### `propNotDefined(prop, [args])`

Defined in travel.t, line 3421

by default, send everything to the underlying Traveler


### `travelerName(arriving)`

Defined in en_us.t, line 2848

When an actor is pushing an object from one room to another, show its name with an additional clause indicating the object being moved along with us.


### `travelerTravelTo(dest, connector, backConnector)`

Defined in travel.t, line 3337

Travel to a new location. We'll run the normal travel routine for the underlying real traveler; then, if we ended up in a new location, we'll move the object being pushed to the traveler's new location.


### `travelerTravelWithin(actor, dest)`

Defined in travel.t, line 3389

Perform local travel, between nested rooms within a top-level location. By default, we simply don't allow pushing objects between nested rooms.
