# SpecialDescContentsLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1438)


Special description lister for the contents of an item being examined. This is similar to the regular specialDescLister, but shows the special descriptions of the contents of an object being described with "examine" or "look in," rather than of the entire location.


**Superclass chain:** [ParagraphLister](paragraphlister.md) > [Lister](lister.md) > `object` > **SpecialDescContentsLister**


## Properties


### `cont_`

Defined in lister.t, line 1459

the containing object we're examining


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `construct(cont)`

Defined in lister.t, line 1439


### `isListed(obj)` *(overridden)*

Defined in lister.t, line 1446

list everything


### `listWith(obj)` *(overridden)*

Defined in lister.t, line 1456

use the object's special description grouper


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in lister.t, line 1449

show a list item


## Inherited Methods


*From [ParagraphLister](paragraphlister.md):* [`showListPrefixWide`](paragraphlister.md#showListPrefixWide), [`showListSeparator`](paragraphlister.md#showListSeparator)


<details><summary>From [Lister](lister.md) (30)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
