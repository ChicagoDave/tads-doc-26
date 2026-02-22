# DividedInventoryLister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1603)


"Divided" inventory lister. In 'wide' mode, this shows inventory in two parts: the items being carried, and the items being worn. (We use the standard single tree-style listing in 'tall' mode.)


**Superclass chain:** [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **DividedInventoryListerGlobal objects:** [actorInventoryLister](actorinventorylister.md)


## Properties


### `carryingLister`

Defined in lister.t, line 1687

Our associated sub-listers for items begin carried and worn, respectively. We'll use these to list our sublist of items being worn.


### `singleSentenceMaxNouns`

Defined in lister.t, line 1680

The recommended maximum number of number of noun phrases to show in the single-sentence format. This should be used by the showCombinedInventoryList() method to decide whether to display the combined listing as a single sentence or as two separate sentences.


### `wearingLister`

Defined in lister.t, line 1688


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showCombinedInventoryList(parent, carrying, wearing)`

Defined in lister.t, line 1671

Show the combined listing. This must be provided by each language-specific subclass. The inputs are the results (strings) of the captured output of the sublistings of the items being carried and the items being worn. These will be "raw" listings, without any prefix or suffix text. This routine's job is to display the final output, adding the framing text.


### `showList(pov, parent, lst, options, indent, infoTab, parentGroup)` *(overridden)*

Defined in lister.t, line 1608

Show the list. We completely override the main lister method so that we can show our two lists.


## Inherited Methods


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList), [`showListItem`](inventorylister.md#showListItem), [`showListItemCounted`](inventorylister.md#showListItemCounted)


<details><summary>From [Lister](lister.md) (29)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
