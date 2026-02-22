# MajorAttachmentLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5140)


The "major" attachment lister. This lists the objects which are attached to a given parent Attachable, and for which the parent is the "major" item in the relationship. The items in the list are described as being attached to the parent.


**Superclass chain:** [SimpleAttachmentLister](simpleattachmentlister.md) > [Lister](lister.md) > `object` > **MajorAttachmentLister**


## Inherited Properties


*From [SimpleAttachmentLister](simpleattachmentlister.md):* [`parent_`](simpleattachmentlister.md#parent_)


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5150

ask the parent if we should list each item


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5141


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5142


## Inherited Methods


*From [SimpleAttachmentLister](simpleattachmentlister.md):* [`construct`](simpleattachmentlister.md#construct), [`showListEmpty`](simpleattachmentlister.md#showListEmpty)


<details><summary>From [Lister](lister.md) (31)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
