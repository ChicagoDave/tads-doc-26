# UnlistedProxyConnector

*class* — defined in [travel.t](../by-file/travel.t.md) (line 1688)


An "unlisted proxy" connector acts as a proxy for another connector. We act exactly like the underlying connector, except that we suppress the connector from automatic exit lists. This can be used for cases where an otherwise normal connector is needed but the connector is not to appear in automatic exit lists (such as the status line).


**Superclass chain:** `object` > **UnlistedProxyConnector**


## Properties


### `isConnectorListed`

Defined in travel.t, line 1705

we're not listed


### `primaryConn`

Defined in travel.t, line 1702

Our underlying connector. Start out with a default TadsObject rather than nil in case anyone wants to call a property or test inheritance before we're finished with our constructor - this will produce reasonable default behavior without having to test for nil everywhere.


## Methods


### `construct(pri)`

Defined in travel.t, line 1689


### `dobjFor(TravelVia)`

Defined in travel.t, line 1708

map any TravelVia action to our underlying connector


### `ofKind(cls)`

Defined in travel.t, line 1721

As a proxy, we don't want to disguise the fact that we're a proxy, if someone specifically asks, so admist to being of our own true kind; but we also act mostly like our underlying connector, so if someone wants to know if we're one of those, say yes to that as well. So, return true if the inherited version returns true, and also return true if our primary connector would return true.


### `propNotDefined(prop, [args])`

Defined in travel.t, line 1711

redirect everything we don't handle to the underlying connector
