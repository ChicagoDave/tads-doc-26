# InventorySublister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1703)


Base class for the inventory sub-lister for items being carried. This is a minor specialization of the basic inventory lister; in this version, we omit any prefix, suffix, or empty messages, since we'll rely on the caller to combine our raw listing with the raw 'wearing' listing to form the full results.


**Superclass chain:** [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **InventorySublisterGlobal objects:** [actorCarryingSublister](actorcarryingsublister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListEmpty(pov, parent)` *(overridden)*

Defined in lister.t, line 1707


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in lister.t, line 1705

don't show any prefix, suffix, or 'empty' messages


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in lister.t, line 1706


### `showSeparateContents(pov, lst, options, infoTab)` *(overridden)*

Defined in lister.t, line 1710

don't show out-of-line contents


## Inherited Methods


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList), [`showListItem`](inventorylister.md#showListItem), [`showListItemCounted`](inventorylister.md#showListItemCounted)


<details><summary>From [Lister](lister.md) (26)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
