# ListGroupSorted

*class* — defined in [lister.t](../by-file/lister.t.md) (line 2047)


Sorted group list. This is a list that simply displays its members in a specific sorting order.


**Superclass chain:** [ListGroup](listgroup.md) > `object` > **ListGroupSortedSubclasses:** [ListGroupParen](listgroupparen.md), [ListGroupPrefixSuffix](listgroupprefixsuffix.md), [SuggestionListGroup](suggestionlistgroup.md)


## Inherited Properties


*From [ListGroup](listgroup.md):* [`groupDisplaysSublist`](listgroup.md#groupDisplaysSublist), [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `// compareGroupItems (a, b)`

Defined in lister.t, line 2104

Compare a pair of items from the group to determine their relative sorting order. This should return 0 if the two items are at the same sorting order, a positive integer if the first item sorts after the second item, or a negative integer if the first item sorts before the second item.


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 2051

Show the group list


### `sortListGroup(lst)`

Defined in lister.t, line 2069

Sort the group list. By default, if we have a compareGroupItems() method defined, we'll sort the list using that method; otherwise, we'll just return the list unchanged.


## Inherited Methods


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`groupNounPhraseCount`](listgroup.md#groupNounPhraseCount), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
