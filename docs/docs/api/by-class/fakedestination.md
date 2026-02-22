# FakeDestination

*class* — defined in [travel.t](../by-file/travel.t.md) (line 2266)


A fake apparent destination, for dead-end connectors. The dead-end connector will create an object of this class to represent its apparent but actually unreachable destination, if it has an apparent destination name.


**Superclass chain:** `object` > **FakeDestination**


## Properties


### `connector`

Defined in travel.t, line 2274

our underlying connector (usually a DeadEndConnector)


## Methods


### `construct(conn)`

Defined in travel.t, line 2268

construct - remember our associated connector


### `getDestName(actor, origin)`

Defined in travel.t, line 2271

get our destination name - this is the name from our connector
