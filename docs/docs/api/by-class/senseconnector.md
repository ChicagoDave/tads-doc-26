# SenseConnector

*class* — defined in [sense.t](../by-file/sense.t.md) (line 431)


SenseConnector: an object that can pass senses across room boundaries. This is a mix-in class: add it to the superclass list of the object before Thing (or a Thing subclass).


**Superclass chain:** [MultiLoc](multiloc.md) > [BaseMultiLoc](basemultiloc.md) > `object` > **SenseConnectorSubclasses:** [DistanceConnector](distanceconnector.md)


## Properties


### `connectorMaterial`

Defined in sense.t, line 436

A SenseConnector's material generally determines how senses pass through the connection.


### `getConnectedContainers` *(overridden)*

Defined in sense.t, line 582

Return a list of my connected containers. We connect to all of our containers, so simply return my location list.


## Inherited Properties


*From [BaseMultiLoc](basemultiloc.md):* [`initialLocationClass`](basemultiloc.md#initialLocationClass), [`locationList`](basemultiloc.md#locationList)


## Methods


### `addDirectConnections(tab)` *(overridden)*

Defined in sense.t, line 451

Add the direct containment connections for this item to a lookup table.


### `checkMoveThrough(obj, dest)`

Defined in sense.t, line 589

Check moving an object through me. This is called when we try to move an object from one of our containers to another of our containers through me. By default, we don't allow it.


### `checkMoveViaPath(obj, dest, op)`

Defined in sense.t, line 617

check for moving via a path


### `checkThrowThrough(obj, dest)`

Defined in sense.t, line 611

Check throwing an object through me. This is called when an actor tries to throw a projectile 'obj' at 'dest' via a path that includes 'self'. By default, we don't allow it.


### `checkThrowViaPath(obj, dest, op)`

Defined in sense.t, line 647

check for throwing via a path


### `checkTouchThrough(obj, dest)`

Defined in sense.t, line 600

Check touching an object through me. This is called when an actor tries to reach from one of my containers through me into another of my containers. By default, we don't allow it.


### `checkTouchViaPath(obj, dest, op)`

Defined in sense.t, line 632

check for touching via a path


### `forEachConnectedContainer(func, [args])` *(overridden)*

Defined in sense.t, line 573

Call a function on each connected container. Since we provide a sense path connection among our containers, we must iterate over each of our containers.


### `sensePathFromWithout(fromParent, sense, trans, obs, fill)`

Defined in sense.t, line 519

Build a sense path from a container to me


### `shineFromWithout(fromParent, sense, ambient, fill)`

Defined in sense.t, line 478

Transmit energy from a container onto me.


### `transSensingThru(sense)`

Defined in sense.t, line 442

Determine how senses pass through this connection. By default, we simply use the material's transparency.


## Inherited Methods


*From [MultiLoc](multiloc.md):* [`baseMoveInto`](multiloc.md#baseMoveInto), [`baseMoveIntoAdd`](multiloc.md#baseMoveIntoAdd), [`baseMoveOutOf`](multiloc.md#baseMoveOutOf), [`cloneForMultiInstanceContents`](multiloc.md#cloneForMultiInstanceContents), [`cloneMultiInstanceContents`](multiloc.md#cloneMultiInstanceContents), [`forEachContainer`](multiloc.md#forEachContainer), [`getDropDestination`](multiloc.md#getDropDestination), [`initializeLocation`](multiloc.md#initializeLocation), [`moveIntoAdd`](multiloc.md#moveIntoAdd), [`moveOutOf`](multiloc.md#moveOutOf), [`reInitializeLocation`](multiloc.md#reInitializeLocation), [`restoreLocation`](multiloc.md#restoreLocation), [`saveLocation`](multiloc.md#saveLocation), [`sensePathToLoc`](multiloc.md#sensePathToLoc), [`shineOnLoc`](multiloc.md#shineOnLoc)


*From [BaseMultiLoc](basemultiloc.md):* [`buildLocationList`](basemultiloc.md#buildLocationList), [`isDirectlyIn`](basemultiloc.md#isDirectlyIn), [`isIn`](basemultiloc.md#isIn), [`isInitiallyIn`](basemultiloc.md#isInitiallyIn), [`isListedInContents`](basemultiloc.md#isListedInContents), [`isOrIsIn`](basemultiloc.md#isOrIsIn)
