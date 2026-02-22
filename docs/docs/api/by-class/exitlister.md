# ExitLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5229)


Basic room exit lister. This shows a list of the apparent exits from a location.


**Superclass chain:** [Lister](lister.md) > `object` > **ExitListerGlobal objects:** [explicitExitLister](explicitexitlister.md), [lookAroundExitLister](lookaroundexitlister.md), [lookAroundTerseExitLister](lookaroundterseexitlister.md), [statuslineExitLister](statuslineexitlister.md)


## Properties


### `hasBackNameFlag`

Defined in msg_neu.t, line 5339


### `hasDestNameFlag`

Defined in msg_neu.t, line 5338

My special options flag: at least one object in the list has a destination name. The caller should set this flag in our options if applicable.


### `listerShowsDest`

Defined in msg_neu.t, line 5331

this lister shows destination names


### `nextCustomFlag` *(overridden)*

Defined in msg_neu.t, line 5340


## Methods


### `isListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5239


### `listCardinality(obj)` *(overridden)*

Defined in msg_neu.t, line 5240


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in msg_neu.t, line 5242


### `showListItemDirName(obj, initCap)`

Defined in msg_neu.t, line 5312

show a direction name, hyperlinking it if appropriate


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5230


### `showListSeparator(options, curItemNum, totalItems)` *(overridden)*

Defined in msg_neu.t, line 5282

show the destination


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5237


## Inherited Methods


<details><summary>From [Lister](lister.md) (29)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
