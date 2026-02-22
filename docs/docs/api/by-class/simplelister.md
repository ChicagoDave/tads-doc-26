# SimpleLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1267)


A SimpleLister provides simplified interfaces for creating formatted lists.


**Superclass chain:** [Lister](lister.md) > `object` > **SimpleListerGlobal objects:** [objectLister](objectlister.md), [stringLister](stringlister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)` *(overridden)*

Defined in lister.t, line 1280

by default, everything given to a simple lister is listed


### `makeSimpleList(lst)`

Defined in lister.t, line 1287

Format a simple list, but rather than displaying the result, return it as a string. This simply displays the list as normal, but captures the output as a string and returns it.


### `showSimpleList(lst)`

Defined in lister.t, line 1274

Show a formatted list given a list of items. This lets you create a formatted list from an item list without worrying about visibility or other factors that affect the full Lister interfaces.


## Inherited Methods


<details><summary>From [Lister](lister.md) (34)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
