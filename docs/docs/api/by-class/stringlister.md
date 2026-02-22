# stringLister

*object* — defined in [lister.t](../by-file/lister.t.md) (line 1305)


stringLister is a concrete SimpleLister for formatting lists of strings. To use this lister, pass lists of single-quoted strings (instead of simulation objects) to showSimpleList(), etc.


**Superclass chain:** [SimpleLister](simplelister.md) > [Lister](lister.md) > `object` > **stringLister**


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `getArrangedListCardinality(singles, groups, groupTab)` *(overridden)*

Defined in lister.t, line 1314

get the cardinality of an arranged list (we need to override this because our items are strings, which don't have the normal object properties that would let us count cardinality the usual way)


### `showListItem(str, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1307

show a list item - list items are strings, so simply 'say' them


## Inherited Methods


*From [SimpleLister](simplelister.md):* [`isListed`](simplelister.md#isListed), [`makeSimpleList`](simplelister.md#makeSimpleList), [`showSimpleList`](simplelister.md#showSimpleList)


<details><summary>From [Lister](lister.md) (32)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
