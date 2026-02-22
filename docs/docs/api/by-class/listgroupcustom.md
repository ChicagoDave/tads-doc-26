# ListGroupCustom

*class* — defined in [lister.t](../by-file/lister.t.md) (line 2029)


A "custom" List Group implementation. This type of lister uses a completely custom message to show the group, without a need to recursively invoke a lister to list the individual elements. The main difference between this and the base ListGroup is that the interface to the custom message generator is very simple - we can dispense with most of the numerous arguments that the base group message receives, since most of those arguments are there to allow recursive listing of the group list.


**Superclass chain:** [ListGroup](listgroup.md) > `object` > **ListGroupCustom**


## Properties


### `groupDisplaysSublist` *(overridden)*

Defined in lister.t, line 2040

assume our listing message doesn't look like a sublist


## Inherited Properties


*From [ListGroup](listgroup.md):* [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 2030


### `showGroupMsg(lst)`

Defined in lister.t, line 2037

show the custom group message - subclasses should override


## Inherited Methods


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`groupNounPhraseCount`](listgroup.md#groupNounPhraseCount), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
