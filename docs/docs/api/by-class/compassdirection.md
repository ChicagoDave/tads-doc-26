# CompassDirection

*class* — defined in [travel.t](../by-file/travel.t.md) (line 110)


The base class for compass directions (north, south, etc). We don't add anything to the basic Direction class, but we use a separate class for compass directions to allow language-specific customizations for all of the directions and to allow travel commands to treat these specially when needed.


**Superclass chain:** [Direction](direction.md) > `object` > **CompassDirectionGlobal objects:** [eastDirection](eastdirection.md), [northDirection](northdirection.md), [northeastDirection](northeastdirection.md), [northwestDirection](northwestdirection.md), [southDirection](southdirection.md), [southeastDirection](southeastdirection.md), [southwestDirection](southwestdirection.md), [westDirection](westdirection.md)


## Inherited Properties


*From [Direction](direction.md):* [`allDirections`](direction.md#allDirections), [`dirProp`](direction.md#dirProp), [`sortingOrder`](direction.md#sortingOrder)


## Methods


### `sayArriving(traveler)` *(overridden)*

Defined in en_us.t, line 3074

describe a traveler arriving from this direction


### `sayDeparting(traveler)` *(overridden)*

Defined in en_us.t, line 3081

describe a traveler departing in this direction


## Inherited Methods


*From [Direction](direction.md):* [`defaultConnector`](direction.md#defaultConnector), [`initializeDirection`](direction.md#initializeDirection), [`initializeDirectionClass`](direction.md#initializeDirectionClass)
