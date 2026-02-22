# Changes for v3.0.6p

- In [InitiateTopic](initiatetopic.md) remove the modification to ActorTopicDatabase.initiateTopic(), which has now been incorporated into the library.

- Change to [RoomTemplate](roomtemplate.md), which also affects the introductory discussion of [Templates](templates.md) and the discussion of [OutdoorRoom](outdoorroom.md).

- Change from initDesc to initSpecialDesc and initExamineDesc to initDesc throughout (see especially [initDesc & initSpecialDesc](initdesc+initspecialdesc.md)).

- Change of name of cannotAttachMsg to explainCannotAttachTo on [Attachable](attachable.md).

- Discussion and example of the new deferToEntry method in relation to [DefaultGiveTopic](defaultgivetopic.md).

- Add dest to the argument list of monolith.beforePushTravel in [TravelPushable](travelpushable.md).

- The use of remoteInitSpecialDesc instead of distantInitDesc in the [DistanceConnector](distanceconnector.md) section.

- Add example of inRoomName(pov) to the [DistanceConnector](distanceconnector.md) section.

- Removal of snowmobile.out=nil in the [Vehicle](vehicle.md) section (now incorporated in the library).

- Removal of bug-fix to AltTopic discussed in relation to [HelloTopic](hellotopic.md) (now incorporated in the library)

- Alteration in [ByeTopic](byetopic.md) to reflect the fact that ByeTopic now handles both explicit and implicit conversation termination as standard.
