# ListGroupParen

*class* — defined in [lister.t](../by-file/lister.t.md) (line 2116)


List Group implementation: parenthesized sublist. Displays the number of items collectively, then displays the list of items in parentheses.


**Superclass chain:** [ListGroupSorted](listgroupsorted.md) > [ListGroup](listgroup.md) > `object` > **ListGroupParen**


## Properties


### `groupDisplaysSublist` *(overridden)*

Defined in lister.t, line 2167

we don't add a sublist, since we enclose our list in parentheses


## Inherited Properties


*From [ListGroup](listgroup.md):* [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `showGroupCountName(lst)`

Defined in lister.t, line 2160

Show the collective count for the list of objects. By default, we'll simply display the countName of the first item in the list, on the assumption that each object has the same plural description. However, in most cases this should be overridden to provide a more general collective name for the group.


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 2120

show the group list


## Inherited Methods


*From [ListGroupSorted](listgroupsorted.md):* [`compareGroupItems`](listgroupsorted.md#compareGroupItems), [`sortListGroup`](listgroupsorted.md#sortListGroup)


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`groupNounPhraseCount`](listgroup.md#groupNounPhraseCount), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
