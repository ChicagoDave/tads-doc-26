# InventoryLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1547)


Base class for inventory listers. This lister uses a special listing method to show the items, so that items can be shown with special notations in an inventory list that might not appear in other types of listings.


**Superclass chain:** [Lister](lister.md) > `object` > **InventoryListerSubclasses:** [DividedInventoryLister](dividedinventorylister.md), [InventorySublister](inventorysublister.md), [WearingLister](wearinglister.md), [WearingSublister](wearingsublister.md)


**Global objects:** [actorSingleInventoryLister](actorsingleinventorylister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)` *(overridden)*

Defined in lister.t, line 1549

list items in inventory according to their isListedInInventory


### `showContentsList(pov, obj, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 1566

Show contents of the items in the inventory. We customize this so that we can differentiate inventory contents lists from other contents lists.


### `showInlineContentsList(pov, obj, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 1576

Show the contents in-line, for an inventory listing.


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1555

Show list items using the inventory name, which might differ from the regular nmae of the object.


### `showListItemCounted(lst, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1558


## Inherited Methods


<details><summary>From [Lister](lister.md) (30)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
