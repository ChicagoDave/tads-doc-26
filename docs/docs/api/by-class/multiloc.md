# MultiLoc

*class* — defined in [objects.t](../by-file/objects.t.md) (line 2604)


MultiLoc: this class can be multiply inherited by any object that must exist in more than one place at a time. To use this class, put it BEFORE Thing (or any subclass of Thing) in the object's superclass list, to ensure that we override the default containment implementation for the object.


**Superclass chain:** [BaseMultiLoc](basemultiloc.md) > `object` > **MultiLocSubclasses:** [SenseConnector](senseconnector.md), [DistanceConnector](distanceconnector.md)


## Properties


### `getConnectedContainers`

Defined in objects.t, line 2832

get a list of my connected containers; by default, we don't connect our containers, so this is an empty list


## Inherited Properties


*From [BaseMultiLoc](basemultiloc.md):* [`initialLocationClass`](basemultiloc.md#initialLocationClass), [`locationList`](basemultiloc.md#locationList)


## Methods


### `addDirectConnections(tab)`

Defined in objects.t, line 2866

Add the direct containment connections for this item to a lookup table.


### `baseMoveInto(newContainer)`

Defined in objects.t, line 2722

Basic routine to move this object into a given single container. Removes the object from all of its other containers. Performs no notifications.


### `baseMoveIntoAdd(newContainer)`

Defined in objects.t, line 2747

Add this object to a new location - base version that performs no notifications.


### `baseMoveOutOf(cont)`

Defined in objects.t, line 2776

Base routine to move myself out of a given container. Performs no notifications.


### `cloneForMultiInstanceContents(loc)`

Defined in objects.t, line 2848

Create a clone of this object for inclusion in a MultiInstance's contents tree. We don't actually need to make a copy of the object, because a MultiLoc can be in several locations simultaneously; all we need to do is add ourselves to the new location.


### `cloneMultiInstanceContents(loc)`

Defined in objects.t, line 2839

Clone this object's contents for inclusion in a MultiInstance's contents tree. A MultiLoc is capable of being in multiple places at once, so we can just use our original contents tree as is.


### `forEachConnectedContainer(func, ...)`

Defined in objects.t, line 2826

Call a function on each connected container. By default, we don't connect our containers for sense purposes, so we do nothing here.


### `forEachContainer(func, [args])`

Defined in objects.t, line 2814

Call a function on each container. We'll invoke the function as follows for each container 'cont':


### `getDropDestination(obj, path)`

Defined in objects.t, line 2950

Get the drop destination. The default implementation in Thing won't work for us, because it delegates to its location to find the drop destination; we can't do that because we could have several locations. To figure out which of our multiple locations to delegate to, we'll look for 'self' in the supplied sense path; if we can find it, and the previous path element is a container or peer of ours, then we'll delegate to that container, because it's the "side" we approached from. If there's no path, or if we're not preceded in the path by a container of ours, we'll arbitrarily delegate to our first container.


### `initializeLocation`

Defined in objects.t, line 2609

Initialize my location's contents list - add myself to my container during initialization


### `moveIntoAdd(newContainer)`

Defined in objects.t, line 2759

Add this object to a new location.


### `moveOutOf(cont)`

Defined in objects.t, line 2789

Remove myself from a given container, leaving myself in any other containers.


### `reInitializeLocation`

Defined in objects.t, line 2634

Re-initialize the location list. This calls buildLocationList() to re-evaluate the location rules, then updates the locationList to match the new results. We'll remove the MultiLoc from any old locations that are no longer part of the location list, and we'll add it to any new locations that weren't previously in the location list. You can call this at any time to update the MutliLoc's presence to reflect applying our location rules to the current game state.


### `restoreLocation(oldLoc)`

Defined in objects.t, line 2692

restore a previously saved location


### `saveLocation`

Defined in objects.t, line 2685

save my location for later restoration


### `sensePathToLoc(sense, trans, obs, fill)`

Defined in objects.t, line 2919

Build a sense path to my location or locations. Note that even though we don't by default connect our different containers together, we still build a sense path from within to outside, because we can see from within out to all of our containers.


### `shineOnLoc(sense, ambient, fill)`

Defined in objects.t, line 2905

Transmit ambient energy to my location or locations. Note that even though we don't by default shine light from one of our containers to another, we still shine light from within me to each of our containers.


## Inherited Methods


*From [BaseMultiLoc](basemultiloc.md):* [`buildLocationList`](basemultiloc.md#buildLocationList), [`isDirectlyIn`](basemultiloc.md#isDirectlyIn), [`isIn`](basemultiloc.md#isIn), [`isInitiallyIn`](basemultiloc.md#isInitiallyIn), [`isListedInContents`](basemultiloc.md#isListedInContents), [`isOrIsIn`](basemultiloc.md#isOrIsIn)
