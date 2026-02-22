# MultiFaceted

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3264)


A "multi-faceted" object is similar to a MultiInstance object, with the addition that the instance objects are "facets" of one another. This means that they have the same identity, from the perspective of a character in the scenario: all of the instance objects are part of the same conceptual object, not separate objects.


**Superclass chain:** [MultiInstance](multiinstance.md) > [BaseMultiLoc](basemultiloc.md) > `object` > **MultiFaceted**


## Properties


### `instanceMixIn` *(overridden)*

Defined in objects.t, line 3269

the mix-in superclass for our instance objects


## Inherited Properties


*From [MultiInstance](multiinstance.md):* [`instanceList`](multiinstance.md#instanceList), [`instanceObject`](multiinstance.md#instanceObject)


*From [BaseMultiLoc](basemultiloc.md):* [`initialLocationClass`](basemultiloc.md#initialLocationClass), [`locationList`](basemultiloc.md#locationList)


## Methods


### `getFacets`

Defined in objects.t, line 3266

our instance objects represent our facets for parsing purposes


## Inherited Methods


*From [MultiInstance](multiinstance.md):* [`addInstance`](multiinstance.md#addInstance), [`addToContents`](multiinstance.md#addToContents), [`getInstanceIn`](multiinstance.md#getInstanceIn), [`initializeLocation`](multiinstance.md#initializeLocation), [`moveInto`](multiinstance.md#moveInto), [`moveIntoAdd`](multiinstance.md#moveIntoAdd), [`moveOutOf`](multiinstance.md#moveOutOf), [`removeFromContents`](multiinstance.md#removeFromContents)


*From [BaseMultiLoc](basemultiloc.md):* [`buildLocationList`](basemultiloc.md#buildLocationList), [`isDirectlyIn`](basemultiloc.md#isDirectlyIn), [`isIn`](basemultiloc.md#isIn), [`isInitiallyIn`](basemultiloc.md#isInitiallyIn), [`isListedInContents`](basemultiloc.md#isListedInContents), [`isOrIsIn`](basemultiloc.md#isOrIsIn)
