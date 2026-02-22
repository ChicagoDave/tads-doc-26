# ListGroupEquivalent

*class* — defined in [lister.t](../by-file/lister.t.md) (line 2225)


Equivalent object list group. This is the default listing group for equivalent items. The Thing class creates an instance of this class during initialization for each set of equivalent items.


**Superclass chain:** [ListGroup](listgroup.md) > `object` > **ListGroupEquivalent**


## Properties


### `groupDisplaysSublist` *(overridden)*

Defined in lister.t, line 2239

we display as a single item, so there's no sublist


## Inherited Properties


*From [ListGroup](listgroup.md):* [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `groupNounPhraseCount(lister, lst)` *(overridden)*

Defined in lister.t, line 2236

An equivalence group displays only a single noun phrase to cover the entire group.


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 2226


## Inherited Methods


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
