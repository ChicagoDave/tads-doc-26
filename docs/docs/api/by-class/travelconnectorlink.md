# TravelConnectorLink

*class* — defined in [travel.t](../by-file/travel.t.md) (line 3072)


The base class for Enterables and Exitables. These are physical objects associated with travel connectors. For example, the object representing the exterior of a building in the location containing the building could be an Enterable, so that typing ENTER BUILDING takes us into the building via the travel connector that leads inside.


**Superclass chain:** `object` > **TravelConnectorLinkSubclasses:** [Enterable](enterable.md), [EntryPortal](entryportal.md), [Exitable](exitable.md), [ExitPortal](exitportal.md)


## Properties


### `connector`

Defined in travel.t, line 3074

the underlying travel connector


### `sightSize`

Defined in travel.t, line 3102

These objects are generally things like buildings (exterior or interior), which tend to be large enough that their details can be seen at a distance.


## Methods


### `dobjFor(TravelVia)`

Defined in travel.t, line 3084

The internal "TravelVia" action just maps to travel via the underlying connector. However, we want to apply our own preconditions, so we don't directly remap to the underlying connector. Instead, we provide our own full TravelVia implementation, and then we perform the travel on the underlying connector via a replacement action in our own action() handler.
