# thing.t


## Classes

- [BagAffinityInfo](../by-class/bagaffinityinfo.md)
- [CanTouchInfo](../by-class/cantouchinfo.md)
- [CheckStatus](../by-class/checkstatus.md)
- [CheckStatusFailure](../by-class/checkstatusfailure.md)
- [DropType](../by-class/droptype.md)
- [DropTypeThrow](../by-class/droptypethrow.md)
- [EquivalentStateInfo](../by-class/equivalentstateinfo.md)
- [SenseInfo](../by-class/senseinfo.md)
- [SightTouchInfo](../by-class/sighttouchinfo.md)
- [Thing](../by-class/thing.md)
- [ThingState](../by-class/thingstate.md)
- [VocabObject](../by-class/vocabobject.md)


## Global Objects

- [checkStatusSuccess](../by-class/checkstatussuccess.md)
- [dropTypeDrop](../by-class/droptypedrop.md)
- [senseTmp](../by-class/sensetmp.md)
- findBestFacet
- senseInfoTableSubset


## Functions


### `findBestFacet(actor, lst)`

Defined in thing.t, line 986

Find the best facet from the given list of facets, from the perspective of the given actor. We'll find the facet that has the best visibility, or, visibilities being equal, the best touchability.


### `senseInfoTableSubset(senseTab, func)`

Defined in thing.t, line 124

Given a sense information table (a LookupTable returned from Thing.senseInfoTable()), return a vector of only those objects in the table that match the given criteria.
