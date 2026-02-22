# WearingSublister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1727)


Base class for the inventory sub-lister for items being worn. We use a special listing method to show these items, so that items being shown explicitly in a worn list can be shown differently from the way they would in a normal inventory list. (For example, a worn item in a normal inventory list might show a "(worn)" indication, whereas it would not want to show a similar indication in a list of objects explicitly being worn.)


**Superclass chain:** [WearingLister](wearinglister.md) > [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **WearingSublisterGlobal objects:** [actorWearingSublister](actorwearingsublister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListEmpty(pov, parent)` *(overridden)*

Defined in lister.t, line 1731


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in lister.t, line 1729

don't show any prefix, suffix, or 'empty' messages


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in lister.t, line 1730


### `showSeparateContents(pov, lst, options, infoTab)` *(overridden)*

Defined in lister.t, line 1734

don't show out-of-line contents


## Inherited Methods


*From [WearingLister](wearinglister.md):* [`showListItem`](wearinglister.md#showListItem), [`showListItemCounted`](wearinglister.md#showListItemCounted)


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList)


<details><summary>From [Lister](lister.md) (26)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
