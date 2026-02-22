# BaseThingContentsLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4740)


Base contents lister for things. This is used to display the contents of things shown in room and inventory listings; we subclass this for various purposes


**Superclass chain:** [Lister](lister.md) > `object` > **BaseThingContentsListerGlobal objects:** [openableOpeningLister](openableopeninglister.md), [thingContentsLister](thingcontentslister.md), [thingDescContentsLister](thingdesccontentslister.md), [thingLookInLister](thinglookinlister.md)


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListContentsPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4747


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4745


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4741


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4743


## Inherited Methods


<details><summary>From [Lister](lister.md) (31)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`isListed`](lister.md#isListed), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
