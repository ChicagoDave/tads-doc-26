# PushTravelBarrier

*class* — defined in [travel.t](../by-file/travel.t.md) (line 3430)


A PushTravelBarrier is a TravelConnector that allows regular travel, but not travel that involves pushing something. By default, we block all push travel, but subclasses can customize this so that we block only specific objects.


**Superclass chain:** [TravelBarrier](travelbarrier.md) > `object` > **PushTravelBarrier**


## Methods


### `canPushedObjectPass(obj)`

Defined in travel.t, line 3437

Determine if the given pushed object is allowed to pass. Returns true if so, nil if not. By default, we'll return nil for every object; subclasses can override this to allow some objects to be pushed through the barrier but not others.


### `canTravelerPass(traveler)` *(overridden)*

Defined in travel.t, line 3451

Determine if the given traveler can pass through this connector. If the traveler isn't a push traveler, we'll allow the travel; otherwise, we'll block the travel if our canPushedObjectPass routine says the object being pushed can pass.


### `explainTravelBarrier(traveler)` *(overridden)*

Defined in travel.t, line 3440

explain why an object can't pass
