# actorInventoryLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4513)


Standard inventory lister for actors - this will work for the player character and NPC's as well. This lister uses a "divided" format, which segregates the listing into items being carried and items being worn. We'll combine the two lists into a single sentence if the overall list is short, otherwise we'll show two separate sentences for readability.


**Superclass chain:** [DividedInventoryLister](dividedinventorylister.md) > [InventoryLister](inventorylister.md) > [Lister](lister.md) > `object` > **actorInventoryLister**


## Properties


### `phraseSepPat`

Defined in msg_neu.t, line 4604

return the count


## Inherited Properties


*From [DividedInventoryLister](dividedinventorylister.md):* [`carryingLister`](dividedinventorylister.md#carryingLister), [`singleSentenceMaxNouns`](dividedinventorylister.md#singleSentenceMaxNouns), [`wearingLister`](dividedinventorylister.md#wearingLister)


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `countPhrases(txt)`

Defined in msg_neu.t, line 4570

Count the noun phrases in a string. We'll count the number of elements in the list as indicated by commas and semicolons. This might not be a perfect count of the actual number of noun phrases, since we could have commas setting off some other kind of clauses, but it nonetheless will give us a good estimate of the overall complexity of the text, which is what we're really after. The point is that we want to break up the listings if they're long, but combine them into a single sentence if they're short.


### `showCombinedInventoryList(parent, carrying, wearing)` *(overridden)*

Defined in msg_neu.t, line 4518

Show the combined inventory listing, putting together the raw lists of the items being carried and the items being worn.


### `showInventoryCarryingOnly(parent, carrying)`

Defined in msg_neu.t, line 4623

we're carrying nothing but wearing some items


### `showInventoryEmpty(parent)`

Defined in msg_neu.t, line 4612

Once we've made up our mind about the format, we'll call one of these methods to show the final sentence. These are all separate methods so that the individual formats can be easily tweaked without overriding the whole combined-inventory-listing method.


### `showInventoryLongLists(parent, carrying, wearing)`

Defined in msg_neu.t, line 4636

short lists - combine carried and worn in a single sentence


### `showInventoryShortLists(parent, carrying, wearing)`

Defined in msg_neu.t, line 4628

we have only carried items to report


### `showInventoryWearingOnly(parent, wearing)`

Defined in msg_neu.t, line 4617

empty inventory


### `showListContentsPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4651


### `showListEmpty(pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4653


### `showListPrefixTall(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4649

For 'tall' listings, we'll use the standard listing style, so we need to provide the framing messages for the tall-mode listing.


## Inherited Methods


*From [DividedInventoryLister](dividedinventorylister.md):* [`showList`](dividedinventorylister.md#showList)


*From [InventoryLister](inventorylister.md):* [`isListed`](inventorylister.md#isListed), [`showContentsList`](inventorylister.md#showContentsList), [`showInlineContentsList`](inventorylister.md#showInlineContentsList), [`showListItem`](inventorylister.md#showListItem), [`showListItemCounted`](inventorylister.md#showListItemCounted)


<details><summary>From [Lister](lister.md) (26)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showListAll`](lister.md#showListAll), [`showListIndent`](lister.md#showListIndent), [`showListPrefixWide`](lister.md#showListPrefixWide), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
