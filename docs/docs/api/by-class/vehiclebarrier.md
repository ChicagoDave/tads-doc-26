# VehicleBarrier

*class* — defined in [travel.t](../by-file/travel.t.md) (line 7007)


A VehicleBarrier is a TravelConnector that allows actors to travel, but blocks vehicles. By default, we block all vehicles, but subclasses can customize this so that we block only specific vehicles.


**Superclass chain:** [TravelBarrier](travelbarrier.md) > `object` > **VehicleBarrier**


## Methods


### `canTravelerPass(traveler)` *(overridden)*

Defined in travel.t, line 7014

Determine if the given traveler can pass through this connector. By default, we'll return nil for a Vehicle, true for anything else. This can be overridden to allow specific vehicles to pass, or to filter on any other criteria.


### `explainTravelBarrier(traveler)` *(overridden)*

Defined in travel.t, line 7017

explain why we can't pass
