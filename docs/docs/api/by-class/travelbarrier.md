# TravelBarrier

*class* — defined in [travel.t](../by-file/travel.t.md) (line 1658)


A TravelBarrier can be attached to a TravelConnector, via the travelBarrier property, to form a conditional barrier to travel.


**Superclass chain:** `object` > **TravelBarrierSubclasses:** [PushTravelBarrier](pushtravelbarrier.md), [VehicleBarrier](vehiclebarrier.md)


## Methods


### `canTravelerPass(traveler)`

Defined in travel.t, line 1664

Determine if this barrier blocks the given traveler. By default, we don't block anyone. This doesn't make us much of a barrier, so subclasses should override this with a more specific condition.


### `explainTravelBarrier(traveler)`

Defined in travel.t, line 1672

Explain why travel isn't allowed. This should generate an appropriate failure report explaining the problem. This is invoked when travel is attempted and canTravelerPass returns nil. Subclasses must override this.
