# BagOfHolding

*class* — defined in [extras.t](../by-file/extras.t.md) (line 1184)


"Bag of Holding." This is a mix-in that actively moves items from the holding actor's direct inventory into itself when the actor's hands are too full.


**Superclass chain:** `object` > **BagOfHoldingSubclasses:** [Keyring](keyring.md)


## Methods


### `affinityFor(obj)`

Defined in extras.t, line 1244

Get my "affinity" for the given object. This is an indication of how strongly this bag wants to contain the object. The affinity is a number in arbitrary units; higher numbers indicate stronger affinities. An affinity of zero means that the bag does not want to contain the object at all.


### `getBagsOfHolding(vec)`

Defined in extras.t, line 1190

Get my bags of holding. Since we are a bag of holding, we'll add ourselves to the vector, then we'll inherit the normal handling to pick up our contents.
