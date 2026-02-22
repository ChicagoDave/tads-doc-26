# GroupSublister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1340)


Sub-lister for listing the contents of a group. This lister shows a simple list with no prefix or suffix, and otherwise uses the characteristics of the parent lister.


**Superclass chain:** `object` > **GroupSublister**


## Properties


### `parentGroup`

Defined in lister.t, line 1392

my parent list group


### `parentLister`

Defined in lister.t, line 1389

my parent lister


## Methods


### `construct(parentLister, parentGroup)`

Defined in lister.t, line 1341


### `getTopLister`

Defined in lister.t, line 1386

get the top-level lister - returns my parent's top-level lister


### `propNotDefined(prop, [args])`

Defined in lister.t, line 1380

delegate everything we don't explicitly handle to our parent lister


### `showListEmpty(pov, parent)`

Defined in lister.t, line 1354

show nothing when empty


### `showListItem(obj, options, pov, infoTab)`

Defined in lister.t, line 1361

Show an item in the list. Rather than going through the parent lister directly, we go through the parent group, so that it can customize the display of items in the group.


### `showListItemCounted(lst, options, pov, infoTab)`

Defined in lister.t, line 1372

Show a counted item in the group. As with showListItem, we ask the parent group to do the work, so that it can customize the display if desired.


### `showListPrefixTall(itemCount, pov, parent)`

Defined in lister.t, line 1351


### `showListPrefixWide(itemCount, pov, parent)`

Defined in lister.t, line 1349

no prefix or suffix


### `showListSuffixWide(itemCount, pov, parent)`

Defined in lister.t, line 1350
