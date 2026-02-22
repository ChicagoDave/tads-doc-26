# thingDescContentsLister

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 4767)


Contents lister for descriptions of things - this is used to display the contents of a thing as part of the long description of the thing (in response to an "examine" command); it differs from a regular thing contents lister in that we use a pronoun to refer to the thing, rather than its full name, since the full name was probably just used in the basic long description.


**Superclass chain:** [DescContentsLister](desccontentslister.md) > [Lister](lister.md) > `object` > [BaseThingContentsLister](basethingcontentslister.md) > **thingDescContentsLister**


## Inherited Properties


*From [Lister](lister.md):* [`nextCustomFlag`](lister.md#nextCustomFlag)


## Methods


### `showListPrefixWide(itemCount, pov, parent)` *(overridden)*

Defined in msg_neu.t, line 4768


## Inherited Methods


*From [DescContentsLister](desccontentslister.md):* [`isListed`](desccontentslister.md#isListed)


<details><summary>From [Lister](lister.md) (33)</summary>

[`contentsListed`](lister.md#contentsListed), [`contentsListedSeparately`](lister.md#contentsListedSeparately), [`getArrangedListCardinality`](lister.md#getArrangedListCardinality), [`getArrangedListNounPhraseCount`](lister.md#getArrangedListNounPhraseCount), [`getContents`](lister.md#getContents), [`getFilteredList`](lister.md#getFilteredList), [`getListedContents`](lister.md#getListedContents), [`getListGrouping`](lister.md#getListGrouping), [`getTopLister`](lister.md#getTopLister), [`listCardinality`](lister.md#listCardinality), [`listSepEnd`](lister.md#listSepEnd), [`listSepMiddle`](lister.md#listSepMiddle), [`listSepTwo`](lister.md#listSepTwo), [`listWith`](lister.md#listWith), [`longListSepEnd`](lister.md#longListSepEnd), [`longListSepMiddle`](lister.md#longListSepMiddle), [`longListSepTwo`](lister.md#longListSepTwo), [`showArrangedList`](lister.md#showArrangedList), [`showContentsList`](lister.md#showContentsList), [`showInlineContentsList`](lister.md#showInlineContentsList), [`showList`](lister.md#showList), [`showListAll`](lister.md#showListAll), [`showListContentsPrefixTall`](lister.md#showListContentsPrefixTall), [`showListEmpty`](lister.md#showListEmpty), [`showListIndent`](lister.md#showListIndent), [`showListItem`](lister.md#showListItem), [`showListItemCounted`](lister.md#showListItemCounted), [`showListPrefixTall`](lister.md#showListPrefixTall), [`showListSeparator`](lister.md#showListSeparator), [`showListSimple`](lister.md#showListSimple), [`showListSuffixWide`](lister.md#showListSuffixWide), [`showSeparateContents`](lister.md#showSeparateContents), [`showTallListNewline`](lister.md#showTallListNewline)

</details>
