# WearingLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1590)


Base class for worn-inventory listers. This lister uses a special listing method to show the items, so that items being worn are shown *without* the special '(being worn)' notation that might otherwise appear in inventory listings.


**Superclass chain:** [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **WearingListerSubclasses:** [WearingSublister](wearingsublister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1592

show the list item using the "worn listing" name


### `showListItemCounted(lst, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1594


## Inherited Methods


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList)


<details><summary>From [Lister](lister.md) (30)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
