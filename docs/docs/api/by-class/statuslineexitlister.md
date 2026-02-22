# statuslineExitLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5431)


Show room exits in the status line (used in HTML mode only)


**Superclass chain:** [ExitLister](exitlister.md) > [Lister](lister.md) > `object` > **statuslineExitLister**


## Properties


### `listerShowsDest` *(overridden)*

Defined in msg_neu.t, line 5457

this lister does not show destination names


## Inherited Properties


*From [ExitLister](exitlister.md):* [`hasBackNameFlag`](exitlister.md#hasBackNameFlag), [`hasDestNameFlag`](exitlister.md#hasDestNameFlag), [`nextCustomFlag`](exitlister.md#nextCustomFlag)


## Methods


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5432


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in msg_neu.t, line 5444


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5436


### `showListSeparator(options, curItemNum, totalItems)` *(overridden)*

Defined in msg_neu.t, line 5449


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5440


## Inherited Methods


*From [ExitLister](exitlister.md):* [`isListed`](exitlister.md#isListed), [`listCardinality`](exitlister.md#listCardinality), [`showListItemDirName`](exitlister.md#showListItemDirName)


<details><summary>From [Lister](lister.md) (28)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
