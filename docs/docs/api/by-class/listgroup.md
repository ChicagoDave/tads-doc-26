# ListGroup

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1877)


List Group Interface. An instance of this object is created for each set of objects that are to be grouped together.


**Superclass chain:** `object` > **ListGroupSubclasses:** [ListGroupCustom](listgroupcustom.md), [ListGroupEquivalent](listgroupequivalent.md), [ListGroupSorted](listgroupsorted.md), [ListGroupParen](listgroupparen.md), [ListGroupPrefixSuffix](listgroupprefixsuffix.md), [SuggestionListGroup](suggestionlistgroup.md), [RoomActorGrouper](roomactorgrouper.md)


## Properties


### `groupDisplaysSublist`

Defined in lister.t, line 1933

Determine if showing the group list will introduce a sublist into an enclosing list. This should return true if we will show a sublist without some kind of grouping, so that the caller knows to introduce some extra grouping into its enclosing list. This should return nil if the sublist we display will be clearly set off in some way (for example, by being enclosed in parentheses).


### `minGroupSize`

Defined in lister.t, line 1945

The minimum number of elements for which we should retain the group in a listing. By default, we need two elements to display a group; any group with only one element is discarded, and the single element is moved into the 'singles' list. This can be overridden to allow single-element groups to be retained. In most cases, it's undesirable to retain single-element groups, but when grouping is used to partition a list into two or more fixed portions, single-element groups become desirable.


## Methods


### `createGroupSublister(parentLister)`

Defined in lister.t, line 1999

Create the group sublister.


### `groupCardinality(lister, lst)`

Defined in lister.t, line 1968

Determine the cardinality of the group listing, grammatically speaking. This is the number of items that the group seems to be for the purposes of grammatical agreement. For example, if the group is displayed as "$1.38 in change", it would be singular for grammatical agreement, hence would return 1 here; if it displays "five coins (two copper, three gold)," it would count as five items for grammatical agreement.


### `groupNounPhraseCount(lister, lst)`

Defined in lister.t, line 1980

Get the number of noun phrases this group will display. This differs from the cardinality in that it doesn't matter how many *objects* the phrases represent; it only matters how many phrases are displayed. For example, "five coins" has cardinality 5 but only displays one noun phrase.


### `showGroupItem(sublister, obj, options, pov, infoTab)`

Defined in lister.t, line 1909

Show an item in the group's sublist. The sublister calls this to display each item in the group when the group calls the sublister to display the group list. By default, we simply let the sublister handle the request, which gives items in our group sublist the same appearance they would have had in the sublist to begin with. We can customize this behavior to give our list items a different appearance special to the group sublist.


### `showGroupItemCounted(sublister, lst, options, pov, infoTab)`

Defined in lister.t, line 1919

Show a counted item in our group list. This is the counted item equivalent of showGroupItem.


### `showGroupList(pov, lister, lst, options, indent, infoTab)`

Defined in lister.t, line 1890

Show a list of items from this group. All of the items in the list will be members of this list group; we are to display a sentence fragment showing the items in the list, suitable for embedding in a larger list.
