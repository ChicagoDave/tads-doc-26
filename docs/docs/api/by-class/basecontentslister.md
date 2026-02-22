# BaseContentsLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4863)


Base contents lister. This class handles contents listings for most kinds of specialized containers - Surfaces, RearConainers, RearSurfaces, and Undersides. The main variation in the contents listings for these various types of containers is simply the preposition that's used to describe the relationship between the container and the contents, and for this we can look to the objInPrep property of the container.


**Superclass chain:** [Lister](lister.md) > `object` > **BaseContentsListerSubclasses:** [BaseRearContentsLister](baserearcontentslister.md), [BaseSurfaceContentsLister](basesurfacecontentslister.md), [BaseUndersideContentsLister](baseundersidecontentslister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListContentsPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4878


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4873


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4864


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4869


## Inherited Methods


<details><summary>From [Lister](lister.md) (31)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`isListed`](lister.md#isListed), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
