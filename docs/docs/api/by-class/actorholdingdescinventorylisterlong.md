# actorHoldingDescInventoryListerLong

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4666)


Special inventory lister for non-player character descriptions - long form lister. This is used to display the inventory of an NPC as part of the full description of the NPC.


**Superclass chain:** [actorInventoryLister](actorinventorylister.md) > [DividedInventoryLister](dividedinventorylister.md) > [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **actorHoldingDescInventoryListerLong**


## Inherited Properties


*From [actorInventoryLister](actorinventorylister.md):* [`phraseSepPat`](actorinventorylister.md#phraseSepPat)


*From [DividedInventoryLister](dividedinventorylister.md):* [`carryingLister`](dividedinventorylister.md#carryingLister), [`singleSentenceMaxNouns`](dividedinventorylister.md#singleSentenceMaxNouns), [`wearingLister`](dividedinventorylister.md#wearingLister)


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showInventoryCarryingOnly(parent, carrying)`

Defined in msg_neu.t, line 4677

we're carrying nothing but wearing some items


### `showInventoryEmpty(parent)`

Defined in msg_neu.t, line 4667


### `showInventoryLongLists(parent, carrying, wearing)`

Defined in msg_neu.t, line 4691

short lists - combine carried and worn in a single sentence


### `showInventoryShortLists(parent, carrying, wearing)`

Defined in msg_neu.t, line 4683

we have only carried items to report


### `showInventoryWearingOnly(parent, wearing)`

Defined in msg_neu.t, line 4671

empty inventory - saying nothing in an actor description


## Inherited Methods


*From [actorInventoryLister](actorinventorylister.md):* [`countPhrases`](actorinventorylister.md#countPhrases), [`showCombinedInventoryList`](actorinventorylister.md#showCombinedInventoryList), [`showListContentsPrefixTall`](actorinventorylister.md#showListContentsPrefixTall), [`showListEmpty`](actorinventorylister.md#showListEmpty), [`showListPrefixTall`](actorinventorylister.md#showListPrefixTall)


*From [DividedInventoryLister](dividedinventorylister.md):* [`showList`](dividedinventorylister.md#showList)


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList), [`showListItem`](inventorylister.md#showListItem), [`showListItemCounted`](inventorylister.md#showListItemCounted)


<details><summary>From [Lister](lister.md) (26)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showListAll`](lister.md#showListAll), [`showListIndent`](lister.md#showListIndent), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
