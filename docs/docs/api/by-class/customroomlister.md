# CustomRoomLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4469)


A simple customizable room lister. This can be used to create custom listers for things like remote room contents listings. We act just like any ordinary room lister, but we use custom prefix and suffix strings provided during construction.


**Superclass chain:** [Lister](lister.md) > `object` > **CustomRoomLister**


## Properties


### `prefixStr`

Defined in msg_neu.t, line 4481

our prefix and suffix strings


### `suffixStr`

Defined in msg_neu.t, line 4482


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `construct(prefix, suffix)`

Defined in msg_neu.t, line 4470


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4478


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4476


### `showListSuffixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4477


## Inherited Methods


<details><summary>From [Lister](lister.md) (32)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`isListed`](lister.md#isListed), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
