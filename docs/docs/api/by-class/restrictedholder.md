# RestrictedHolder

*class* — defined in [objects.t](../by-file/objects.t.md) (line 5018)


A "restricted holder" is a generic mix-in class for various container types (Containers, Surfaces, Undersides, RearContainers, RearSurfaces) that adds a restriction to what can be contained.


**Superclass chain:** `object` > **RestrictedHolderSubclasses:** [RestrictedContainer](restrictedcontainer.md), [RestrictedRearContainer](restrictedrearcontainer.md), [RestrictedRearSurface](restrictedrearsurface.md), [RestrictedSurface](restrictedsurface.md), [RestrictedUnderside](restrictedunderside.md)


## Properties


### `validContents`

Defined in objects.t, line 5025

A list of acceptable items for the container. This list can be used to identify the objects that can be put in the container (or on the surface, under the underside, or behind the rear container or surface).


## Methods


### `canPutIn(obj)`

Defined in objects.t, line 5037

Is the given object allowed to go in this container (or on/under/behind it, as appropriate for the type)? Returns true if so, nil if not. By default, we'll return true if the object is found in our validContents list, nil if not. This can be overridden if a subclass wants to determine which objects are acceptable with some other kind of per-object test; for example, a subclass might accept only objects of a given class as contents, or might accept only contents with some particular attribute.


### `checkPutDobj(msgProp)`

Defined in objects.t, line 5043

Check a PUT IN/ON/UNDER/BEHIND action to ensure that the direct object is in our approved-contents list.
