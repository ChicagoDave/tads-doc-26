# BaseInlineContentsLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5027)


Base class for specialized in-line contents listers. This shows the list in the form "(<prep> which is...)", with the preposition obtained from the container's objInPrep property.


**Superclass chain:** [ContentsLister](contentslister.md) > [Lister](lister.md) > `object` > **BaseInlineContentsListerGlobal objects:** [inlineListingContentsLister](inlinelistingcontentslister.md), [rearInlineContentsLister](rearinlinecontentslister.md), [surfaceInlineContentsLister](surfaceinlinecontentslister.md), [undersideInlineContentsLister](undersideinlinecontentslister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5028


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5029


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5034


## Inherited Methods


<details><summary>From [Lister](lister.md) (32)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`isListed`](lister.md#isListed), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
