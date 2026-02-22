# SuggestedTopicLister

*class* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5593)


Suggested topic lister.


**Superclass chain:** [Lister](lister.md) > `object` > **SuggestedTopicLister**


## Properties


### `askingActor`

Defined in msg_neu.t, line 5678

the actor who's asking for the topic list (usually the PC)


### `isExplicit`

Defined in msg_neu.t, line 5675

flag: this is an explicit listing (i.e., a TOPICS command)


### `scopeList`

Defined in msg_neu.t, line 5684

our cached scope list for the actor


### `targetActor`

Defined in msg_neu.t, line 5681

the actor we're talking to


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `construct(asker, askee, explicit)`

Defined in msg_neu.t, line 5594


### `contentsListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5651

suggestions have no contents


### `isListed(obj)` *(overridden)*

Defined in msg_neu.t, line 5645

list suggestions that are currently active


### `listCardinality(obj)` *(overridden)*

Defined in msg_neu.t, line 5648

each item counts as one item grammatically


### `listWith(obj)` *(overridden)*

Defined in msg_neu.t, line 5654

get the list group


### `longListSepEnd` *(overridden)*

Defined in msg_neu.t, line 5672


### `longListSepMiddle` *(overridden)*

Defined in msg_neu.t, line 5671


### `longListSepTwo` *(overridden)*

Defined in msg_neu.t, line 5670

don't use semicolons, even in long lists


### `markAsSeen(obj, pov)`

Defined in msg_neu.t, line 5657

mark as seen - nothing to do for suggestions


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5620

end the sentence; include a paren if not in explicit mode


### `showListItem(obj, options, pov, infoTab)` *(overridden)*

Defined in msg_neu.t, line 5660

show the item - show the suggestion's theName


### `showListPrefixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5607

cache the actor's scope list


### `showListSeparator(options, curItemNum, totalItems)` *(overridden)*

Defined in msg_neu.t, line 5635

say that the list is empty if it was explicitly requested; say nothing if the list is being added by the library


### `showListSuffixWide(cnt, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 5615

show the prefix; include a paren if not in explicit mode


## Inherited Methods


<details><summary>From [Lister](lister.md) (23)</summary>

[`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListIndent`](lister.md#showListIndent), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSimple`](lister.md#showListSimple), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
