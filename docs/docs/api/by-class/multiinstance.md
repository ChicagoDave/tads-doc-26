# MultiInstance

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3049)


A "multi-instance" object is a simple way of creating copies of an object in several places. This is often useful for decorations and other features that recur in a whole group of rooms.


**Superclass chain:** [BaseMultiLoc](basemultiloc.md) > `object` > **MultiInstanceSubclasses:** [MultiFaceted](multifaceted.md)


## Properties


### `instanceList`

Defined in objects.t, line 3159

our vector of active instance objects


### `instanceMixIn`

Defined in objects.t, line 3156

the mix-in superclass for our instance objects


### `instanceObject`

Defined in objects.t, line 3051

the template object


## Inherited Properties


*From [BaseMultiLoc](basemultiloc.md):* [`initialLocationClass`](basemultiloc.md#initialLocationClass), [`locationList`](basemultiloc.md#locationList)


## Methods


### `addInstance(loc)`

Defined in objects.t, line 3119

internal service routine - add an instance for a given location


### `addToContents(obj)`

Defined in objects.t, line 3147

If any contents are added to the MultiInstance object, they must be contents of the template object, so add them to the template object instead of the MultiInstance parent.


### `getInstanceIn(loc)`

Defined in objects.t, line 3115

get our instance object (if any) that's in the given location


### `initializeLocation`

Defined in objects.t, line 3054

initialize my locations


### `moveInto(loc)`

Defined in objects.t, line 3065

Move the MultiInstance into the given location. This removes us from any other existing locations and adds us (if we're not already there) to the given location.


### `moveIntoAdd(loc)`

Defined in objects.t, line 3091

Add the new location to our set of locations. Any existing locations are unaffected.


### `moveOutOf(loc)`

Defined in objects.t, line 3102

Remove me from the given location. Other locations are unaffected.


### `removeFromContents(obj)`

Defined in objects.t, line 3153

remove an object from our contents - we'll delegate this to our template object just like we delegate addToContents


## Inherited Methods


*From [BaseMultiLoc](basemultiloc.md):* [`buildLocationList`](basemultiloc.md#buildLocationList), [`isDirectlyIn`](basemultiloc.md#isDirectlyIn), [`isIn`](basemultiloc.md#isIn), [`isInitiallyIn`](basemultiloc.md#isInitiallyIn), [`isListedInContents`](basemultiloc.md#isListedInContents), [`isOrIsIn`](basemultiloc.md#isOrIsIn)
