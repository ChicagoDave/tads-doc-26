# lookAroundTerseExitLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5392)


Show room exits as part of a room description, using the "terse" notation.


**Superclass chain:** [ExitLister](exitlister.md) > [Lister](lister.md) > `object` > **lookAroundTerseExitLister**


## Properties


### `listerShowsDest` *(overridden)*

Defined in msg_neu.t, line 5414

this lister does not show destination names


## Inherited Properties


*From [ExitLister](exitlister.md):* [`hasBackNameFlag`](exitlister.md#hasBackNameFlag), [`hasDestNameFlag`](exitlister.md#hasDestNameFlag), [`nextCustomFlag`](exitlister.md#nextCustomFlag)


## Methods


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in msg_neu.t, line 5397


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5393


### `showListSeparator(options, curItemNum, totalItems)` *(overridden)*

Defined in msg_neu.t, line 5406


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5402

show the direction name


## Inherited Methods


*From [ExitLister](exitlister.md):* [`isListed`](exitlister.md#isListed), [`listCardinality`](exitlister.md#listCardinality), [`showListItemDirName`](exitlister.md#showListItemDirName)


<details><summary>From [Lister](lister.md) (29)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
