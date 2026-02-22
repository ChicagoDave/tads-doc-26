# actorSingleInventoryLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4490)


Single-list inventory lister. This shows the inventory listing as a single list, with worn items mixed in among the other inventory items and labeled "(being worn)".


**Superclass chain:** [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **actorSingleInventoryLister**


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListContentsPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4498


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4501


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4496


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4491


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4493


## Inherited Methods


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList), [`showListItem`](inventorylister.md#showListItem), [`showListItemCounted`](inventorylister.md#showListItemCounted)


<details><summary>From [Lister](lister.md) (25)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListIndent`](lister.md#showListIndent), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
