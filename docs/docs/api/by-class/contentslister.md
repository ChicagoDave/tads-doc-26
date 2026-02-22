# ContentsLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1750)


Base class for contents listers. This is used to list the contents of the objects that appear in top-level lists (a top-level list is the list of objects directly in a room that appears in a room description, or the list of items being carried in an INVENTORY command, or the direct contents of an object being examined).


**Superclass chain:** [Lister](lister.md) > `object` > **ContentsListerSubclasses:** [BaseInlineContentsLister](baseinlinecontentslister.md)


**Global objects:** [rearContentsLister](rearcontentslister.md), [surfaceContentsLister](surfacecontentslister.md), [thingContentsLister](thingcontentslister.md), [undersideContentsLister](undersidecontentslister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Inherited Methods


<details><summary>From [Lister](lister.md) (35)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`isListed`](lister.md#isListed), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
