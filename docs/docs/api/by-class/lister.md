# Lister

*class* — defined in [lister.t](../by-file/lister.t.md) (line 33)


Lister. This is the base class for formatting of lists of objects.


**Superclass chain:** `object` > **Lister**


<details><summary>Subclasses (24)</summary>

- [BaseContentsLister](basecontentslister.md)
- [BaseRearContentsLister](baserearcontentslister.md)
- [BaseSurfaceContentsLister](basesurfacecontentslister.md)
- [BaseUndersideContentsLister](baseundersidecontentslister.md)
- [BaseThingContentsLister](basethingcontentslister.md)
- [ContentsLister](contentslister.md)
- [BaseInlineContentsLister](baseinlinecontentslister.md)
- [CustomRoomLister](customroomlister.md)
- [DescContentsLister](desccontentslister.md)
- [LookWhereContentsLister](lookwherecontentslister.md)
- [ExitLister](exitlister.md)
- [InventoryLister](inventorylister.md)
- [DividedInventoryLister](dividedinventorylister.md)
- [InventorySublister](inventorysublister.md)
- [WearingLister](wearinglister.md)
- [WearingSublister](wearingsublister.md)
- [ParagraphLister](paragraphlister.md)
- [SenseLister](senselister.md)
- [SpecialDescContentsLister](specialdesccontentslister.md)
- [RemoteRoomLister](remoteroomlister.md)
- [SimpleAttachmentLister](simpleattachmentlister.md)
- [MajorAttachmentLister](majorattachmentlister.md)
- [SimpleLister](simplelister.md)
- [SuggestedTopicLister](suggestedtopiclister.md)

</details>


**Global objects:** [aboardVehicleLister](aboardvehiclelister.md), [darkRoomLister](darkroomlister.md), [equivalentStateLister](equivalentstatelister.md), [finishOptionsLister](finishoptionslister.md), [fullScoreLister](fullscorelister.md), [otherExitLister](otherexitlister.md), [plainLister](plainlister.md), [roomLister](roomlister.md)


## Properties


### `nextCustomFlag`

Defined in lister.t, line 1258

The last custom flag defined by this class. Lister and each subclass are required to define this so that each subclass can allocate its own custom flags in a manner that adapts automatically to future additions of flags to base classes. As the base class, we allocate our flags statically with #define's, so we simply use the fixed #define'd last flag value here.


## Methods


### `contentsListed(obj)`

Defined in lister.t, line 1088

Are this item's contents listable?


### `contentsListedSeparately(obj)`

Defined in lister.t, line 1008

Determine if an object's contents are listed separately from its own list entry for the purposes of our type of listing. If this returns true, then we'll list the object's contents in a separate listing (a separate sentence following the main listing sentence, or a separate tree when in 'tall' mode).


### `getArrangedListCardinality(singles, groups, groupTab)`

Defined in lister.t, line 769

Get the cardinality of an arranged list. Returns the number of items that will appear in the list, for grammatical agreement.


### `getArrangedListNounPhraseCount(singles, groups, groupTab)`

Defined in lister.t, line 805

Get the number of noun phrase elements in a list. This differs from the cardinality in that we only count noun phrases, not the cardinality of each noun phrase. So, for example, "five coins" has cardinality five, but has only one noun phrase.


### `getContents(obj)`

Defined in lister.t, line 1093

Get all contents of this item.


### `getFilteredList(lst, infoTab)`

Defined in lister.t, line 148

Filter a list to get only the elements we actually want to show. Returns a new list consisting only of the items that (1) pass the isListed() test, and (2) are represented in the sense information table (infoTab). If infoTab is nil, no sense filtering is applied.


### `getListedContents(obj, infoTab)`

Defined in lister.t, line 1102

Get the listed contents of an object. 'infoTab' is the sense information table for the enclosing listing. By default, we call the object's getListedContents() method, but this is virtualized in the lister interface to allow for listing other hierarchies besides ordinary contents.


### `getListGrouping(groupTab, groups, singles, lst, parentGroup)`

Defined in lister.t, line 194

Get the groupings for a given listing.


### `getTopLister`

Defined in lister.t, line 1248

Get my "top-level" lister. For a sub-lister, this will return the parent lister's top-level lister. The default lister is a top-level lister, so we just return ourself.


### `isListed(obj)`

Defined in lister.t, line 1076

Is this item to be listed in room descriptions? Returns true if so, nil if not. By default, we'll use the object's isListed method to make this determination. We virtualize this into the lister interface to allow for different inclusion rules for the same object depending on the type of list we're generating.


### `listCardinality(obj)`

Defined in lister.t, line 1083

Get the grammatical cardinality of this listing item. This should return the number of items that this item appears to be grammatically, for noun-verb agreement purposes.


### `listSepEnd`

Defined in lister.t, line 1240

normal and long list separator between second-to-last and last items in a list with more than two items


### `listSepMiddle`

Defined in lister.t, line 1233

normal and long list separator between items in list with more than two items


### `listSepTwo`

Defined in lister.t, line 1226

normal and "long list" separator between the two items in a list with exactly two items


### `listWith(obj)`

Defined in lister.t, line 1119

Get the list of grouping objects for listing the item. By default, we return the object's listWith result. Subclasses can override this to specify different groupings for the same object depending on the type of list we're generating.


### `longListSepEnd`

Defined in lister.t, line 1241


### `longListSepMiddle`

Defined in lister.t, line 1234


### `longListSepTwo`

Defined in lister.t, line 1227


### `showArrangedList(pov, parent, lst, options, indent, infoTab, itemCount, singles, groups, groupTab, origLst)`

Defined in lister.t, line 533

Show the list. This is called after we've figured out which items we intend to display, and after we've arranged the items into groups. In rare cases, listers might want to override this, to customize the way the way the list is displayed based on the internal arrangement of the list.


### `showContentsList(pov, obj, options, indent, infoTab)`

Defined in lister.t, line 985

List the contents of an item.


### `showInlineContentsList(pov, obj, options, indent, infoTab)`

Defined in lister.t, line 1016

Show an "in-line" contents list. This shows the item's contents list as a parenthetical, as part of a recursive listing. This is pretty much the same as showContentsList(), but uses the object's in-line contents lister instead of its regular contents lister.


### `showList(pov, parent, lst, options, indent, infoTab, parentGroup)`

Defined in lister.t, line 95

Display a list of items, grouping according to the 'listWith' associations of the items. We will only list items for which isListed() returns true.


### `showListAll(lst, options, indent)`

Defined in lister.t, line 38

Show a list, showing all items in the list as though they were fully visible, regardless of their actual sense status.


### `showListContentsPrefixTall(itemCount, pov, parent)`

Defined in lister.t, line 1057

Show the list prefix for the contents of an object in a 'tall' listing. By default, we just show our usual tall list prefix.


### `showListEmpty(pov, parent)`

Defined in lister.t, line 1067

Show an empty list. If the list to be displayed has no items at all, this is called instead of the prefix/suffix routines. This can be left empty if no message is required for an empty list, or can display the complete message appropriate for an empty list (such as "You are empty-handed").


### `showListIndent(options, indent)`

Defined in lister.t, line 874

Show a list indent if necessary. If ListTall is included in the options, we'll indent to the given level; otherwise we'll do nothing.


### `showListItem(obj, options, pov, infoTab)`

Defined in lister.t, line 1122

show an item in a list


### `showListItemCounted(lst, options, pov, infoTab)`

Defined in lister.t, line 1138

Show a set of equivalent items as a counted item ("three coins"). The listing mechanism itself never calls this directly; instead, this is provided so that ListGroupEquivalent can ask the lister how to describe its equivalent sets, so that different listers can customize the display of equivalent items.


### `showListPrefixTall(itemCount, pov, parent)`

Defined in lister.t, line 1051

Show the list prefix for a 'tall' listing. Note that there is no list suffix for a tall listing, because the format doesn't allow it.


### `showListPrefixWide(itemCount, pov, parent, lst, :)`

Defined in lister.t, line 1038

Show the prefix for a 'wide' listing - this is a message that appears just before we start listing the objects. 'itemCount' is the number of items to be listed; the items might be grouped in the listing, so a list that comes out as "three boxes and two books" will have an itemCount of 5. (The purpose of itemCount is to allow the message to have grammatical agreement in number.)


### `showListSeparator(options, curItemNum, totalItems)`

Defined in lister.t, line 1161

Show a list separator after displaying an item. curItemNum is the number of the item just displayed (1 is the first item), and totalItems is the total number of items that will be displayed in the list.


### `showListSimple(pov, lst, options, indent, prevCnt, infoTab)`

Defined in lister.t, line 903

Show a simple list, recursing into contents lists if necessary. We pay no attention to grouping; we just show the items individually.


### `showListSuffixWide(itemCount, pov, parent)`

Defined in lister.t, line 1044

show the suffix for a 'wide' listing - this is a message that appears just after we finish listing the objects


### `showSeparateContents(pov, lst, options, infoTab)`

Defined in lister.t, line 835

Service routine: show the separately-listed contents of the items in the given list, and their separately-listed contents, and so on. This routine is not normally overridden in subclasses, and is not usually called except from the Lister implementation.


### `showTallListNewline(options)`

Defined in lister.t, line 888

Show a newline after a list item if we're in a tall list; does nothing for a wide list.
