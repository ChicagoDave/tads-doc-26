# finishOptionsLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5157)


Finish Options lister. This lister is used to offer the player options in finishGame().


**Superclass chain:** [Lister](lister.md) > `object` > **finishOptionsLister**


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `isListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5168

end the question, add a blank line, and show the ">" prompt


### `listCardinality(obj)` *(overridden)*

Defined in msg_neu.t, line 5169


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in msg_neu.t, line 5171


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5158


### `showListSeparator(options, curItemNum, totalItems)` *(overridden)*

Defined in msg_neu.t, line 5177

obj is a FinishOption object; show its description


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5162


## Inherited Methods


<details><summary>From [Lister](lister.md) (29)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
