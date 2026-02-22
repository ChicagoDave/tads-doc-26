# LookWhereContentsLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4794)


Base contents lister for "LOOK <PREP>" commands (LOOK IN, LOOK UNDER, LOOK BEHIND, etc). This can be subclasses for the appropriate LOOK <PREP> command matching the container type - LOOK UNDER for undersides, LOOK BEHIND for rear containers, etc. To use this class, combine it via multiple inheritance with the appropriate Base<Prep>ContentsLister for the preposition type.


**Superclass chain:** [DescContentsLister](desccontentslister.md) > [Lister](lister.md) > `object` > **LookWhereContentsListerGlobal objects:** [rearLookBehindLister](rearlookbehindlister.md), [surfaceLookInLister](surfacelookinlister.md), [thingLookInLister](thinglookinlister.md), [undersideLookUnderLister](undersidelookunderlister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4795


## Inherited Methods


*From [DescContentsLister](desccontentslister.md):* [`isListed`](desccontentslister.md#isListed)


<details><summary>From [Lister](lister.md) (33)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
