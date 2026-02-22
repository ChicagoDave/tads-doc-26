# RoomActorGrouper

*class* — defined in [lister.t](../by-file/lister.t.md) (line 1479)


Grouper for actors in a common posture and in a common location. We create one of these per room per posture when we discover actors in the room during "look around" (or "examine" on a nested room). This grouper lets us group actors like so: "Dan and Jane are sitting on the couch."


**Superclass chain:** [ListGroup](listgroup.md) > `object` > **RoomActorGrouper**


## Inherited Properties


*From [ListGroup](listgroup.md):* [`groupDisplaysSublist`](listgroup.md#groupDisplaysSublist), [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `construct(location, posture)`

Defined in lister.t, line 1480


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 1486


## Inherited Methods


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`groupNounPhraseCount`](listgroup.md#groupNounPhraseCount), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
