# BaseMultiLoc

*class* — defined in [objects.t](../by-file/objects.t.md) (line 2436)


Base multi-location item with automatic initialization. This is the base class for various multi-located object classes.


**Superclass chain:** `object` > **BaseMultiLocSubclasses:** [MultiInstance](multiinstance.md), [MultiFaceted](multifaceted.md), [MultiLoc](multiloc.md), [SenseConnector](senseconnector.md), [DistanceConnector](distanceconnector.md)


## Properties


### `initialLocationClass`

Defined in objects.t, line 2451

The class of our initial locations. If this is nil, then our default buildLocationList() method will test every object in the entire game with our isInitiallyIn() method; otherwise, we'll test only objects of the given class.


### `locationList`

Defined in objects.t, line 2443

The location list. Instances can override this to manually enumerate our initial locations. By default, we'll call buildLocationList() the first time this is invoked, and store the result.


## Methods


### `buildLocationList`

Defined in objects.t, line 2471

Build my list of locations, and return the list. This default implementation looks for an 'initialLocationClass' property value, and if one is found, looks at every object of that class; otherwise, it looks at every object in the entire game. In either case, each object is then passed to our isInitiallyIn() method, and is included in our result list if isInitiallyIn() returns true.


### `isDirectlyIn(obj)`

Defined in objects.t, line 2533

determine if I'm directly in the given object


### `isIn(obj)`

Defined in objects.t, line 2518

determine if I'm in a given object, directly or indirectly


### `isInitiallyIn(obj)`

Defined in objects.t, line 2460

Test an object for inclusion in our initial location list. By default, we'll simply return true to include every object. We return true by default so that an instance can merely specify a value for initialLocationClass in order to place this object in every instance of the given class.


### `isListedInContents(examinee, :?)`

Defined in objects.t, line 2551

Determine if I'm to be listed within my immediate container. As a multi-location object, we have multiple immediate containers, so we need to know which direct container we're talking about. Thing.examineListContents() passes this down via "cont:", a named parameter. Other callers might not always provide this argument, though, so if it's not present simply base this on whether we have a special description in any context.


### `isOrIsIn(obj)`

Defined in objects.t, line 2559

Am I either inside 'obj', or equal to 'obj'?
