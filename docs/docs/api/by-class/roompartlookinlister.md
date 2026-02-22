# roomPartLookInLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4941)


Look-in lister for room parts. Most room parts act like surfaces rather than containers, so base this lister on the surface lister.


**Superclass chain:** [surfaceLookInLister](surfacelookinlister.md) > [LookWhereContentsLister](lookwherecontentslister.md) > [DescContentsLister](desccontentslister.md) > [Lister](lister.md) > `object` > [BaseSurfaceContentsLister](basesurfacecontentslister.md) > [BaseContentsLister](basecontentslister.md) > **roomPartLookInLister**


## Properties


### `part_`

Defined in msg_neu.t, line 4948

list the object if it's listed in the room part


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)`

Defined in msg_neu.t, line 4942


## Inherited Methods


*From [LookWhereContentsLister](lookwherecontentslister.md):* [`showListEmpty`](lookwherecontentslister.md#showListEmpty)


<details><summary>From [Lister](lister.md) (33)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
