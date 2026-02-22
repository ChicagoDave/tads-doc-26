# SimpleAttachmentLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5113)


A simple lister to show the objects to which a given Attachable object is attached. This shows the objects which have symmetrical attachment relationships to the given parent object, or which are "major" items to which the parent is attached.


**Superclass chain:** [Lister](lister.md) > `object` > **SimpleAttachmentListerSubclasses:** [MajorAttachmentLister](majorattachmentlister.md)


## Properties


### `parent_`

Defined in msg_neu.t, line 5131

the parent object - this is the object whose attachments are being listed


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `construct(parent)`

Defined in msg_neu.t, line 5114


### `isListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5125

ask the parent if we should list each item


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5116


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5119


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5121


## Inherited Methods


<details><summary>From [Lister](lister.md) (31)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
