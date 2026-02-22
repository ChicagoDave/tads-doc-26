# MultiInstanceInstance

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3173)


An instance of a MultiInstance object. This is a mix-in class that we add (using mutiple inheritance) to each instance. This overrides the location manipulation methods, to ensure that we keep the MultiInstance parent object in sync with any changes made directly to the instance objects.


**Superclass chain:** `object` > **MultiInstanceInstanceSubclasses:** [MultiFacetedFacet](multifacetedfacet.md)


## Properties


### `isEquivalent`

Defined in objects.t, line 3227

All instances of a given MultiInstance are equivalent to one another, for parsing purposes.


### `miParent`

Defined in objects.t, line 3230

our MultiInstance parent


## Methods


### `baseMoveInto(newCont)`

Defined in objects.t, line 3187

move to a new location


### `construct(parent)`

Defined in objects.t, line 3174
