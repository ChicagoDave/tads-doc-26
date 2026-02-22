# SenseLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1772)


Base class for sense listers, which list the items that can be sensed for a command like "listen" or "smell".


**Superclass chain:** [ParagraphLister](paragraphlister.md) > [Lister](lister.md) > `object` > **SenseListerGlobal objects:** [inventoryListenLister](inventorylistenlister.md), [inventorySmellLister](inventorysmelllister.md), [roomListenLister](roomlistenlister.md), [roomSmellLister](roomsmelllister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)` *(overridden)*

Defined in lister.t, line 1774

show everything we're asked to list


### `showListItemCounted(lst, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1777

show a counted list item


## Inherited Methods


*From [ParagraphLister](paragraphlister.md):* [`showListPrefixWide`](paragraphlister.md#showListPrefixWide), [`showListSeparator`](paragraphlister.md#showListSeparator)


<details><summary>From [Lister](lister.md) (31)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
