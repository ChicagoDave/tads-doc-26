# MultiFacetedFacet

*class* — defined in [objects.t](../by-file/objects.t.md) (line 3279)


The mix-in superclass for MultiFaceted facet instances.


**Superclass chain:** [MultiInstanceInstance](multiinstanceinstance.md) > `object` > **MultiFacetedFacet**


## Inherited Properties


*From [MultiInstanceInstance](multiinstanceinstance.md):* [`isEquivalent`](multiinstanceinstance.md#isEquivalent), [`miParent`](multiinstanceinstance.md#miParent)


## Methods


### `getFacets`

Defined in objects.t, line 3286

Get our other facets for parsing purposes - our parent maintains the list of all of its facets, so simply return that list. (Note that we'll be in the list as well, but that's harmless, so don't bother removing us.)


## Inherited Methods


*From [MultiInstanceInstance](multiinstanceinstance.md):* [`baseMoveInto`](multiinstanceinstance.md#baseMoveInto), [`construct`](multiinstanceinstance.md#construct)
