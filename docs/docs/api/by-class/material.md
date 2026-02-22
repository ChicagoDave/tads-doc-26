# Material

*class* — defined in [sense.t](../by-file/sense.t.md) (line 21)


Material: the base class for library objects that specify the way senses pass through objects.


**Superclass chain:** `object` > **MaterialGlobal objects:** [adventium](adventium.md), [coarseMesh](coarsemesh.md), [fineMesh](finemesh.md), [glass](glass.md), [paper](paper.md)


## Properties


### `hearThru`

Defined in sense.t, line 41


### `seeThru`

Defined in sense.t, line 40

For each sense, each material must define an appropriate xxxThru property that returns the transparency level for that sense through the material. Any xxxThru property not defined in an individual material defaults to opaque.


### `smellThru`

Defined in sense.t, line 42


### `touchThru`

Defined in sense.t, line 43


## Methods


### `senseThru(sense)`

Defined in sense.t, line 28

Determine how a sense passes through the material. We'll return a transparency level. (Individual materials should not need to override this method, since it simply dispatches to the various xxxThru methods.)
