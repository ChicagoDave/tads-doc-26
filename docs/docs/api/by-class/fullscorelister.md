# fullScoreLister

*object* — defined in [score.t](../by-file/score.t.md) (line 194)


List interface for showing the full score list


**Superclass chain:** [Lister](lister.md) > `object` > **fullScoreLister**


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `getContents(obj)` *(overridden)*

Defined in score.t, line 208

achievements have no containment hierarchy


### `getListedContents(obj, infoTab)` *(overridden)*

Defined in score.t, line 209


### `isListed(obj)` *(overridden)*

Defined in score.t, line 202

every achievement is listed


### `listCardinality(obj)` *(overridden)*

Defined in score.t, line 205

each item counts as a singular object grammatically


### `showContentsList(pov, obj, options, indent, infoTab)` *(overridden)*

Defined in score.t, line 210


### `showInlineContentsList(pov, obj, options, indent, infoTab)` *(overridden)*

Defined in score.t, line 211


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in score.t, line 214

show an item


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in score.t, line 195


## Inherited Methods


<details><summary>From [Lister](lister.md) (27)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getFilteredList`](lister.md#getFilteredList), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
