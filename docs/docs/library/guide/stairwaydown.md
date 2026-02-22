# StairwayDown

StairwayDown : Stairway

The description of entranceCave refers to a sturdy steel ladder leading down through a hole in the floor. This ladder is best implemented as a stairwayDown, which is both a physical game object that can be examined and a TravelConnector that can be traversed, by CLIMB and CLIMB DOWN commands. The ladder can simply be defined as:

```tads3
+ downLadder : StairwayDown 'sturdy steel ladder' 'sturdy steel ladder'
  "The ladder leads down through a large hole in the floor. "
;
```

Here we are simply using the standard [Thing template](thingtemplate.md), although since StairwayDown inherits (indirectly) from Passage, it can also use the [Passage template](passagetemplate.md).

We can then add a down property to the room definition to point to this connector:

```tads3
entranceCave : Room 'Entrance Cave' 'the entrance cave'
  "Compared with the narrow tunnel leading out to the north, this
   rough-walled cave seems positively spacious. A red sign fixed to
   one wall suggests that the narrow tunnel is the only way back out to
   the valley, while a blue sign next to it welcomes you to the cave.
   Directly under the signs a narrow ledge has been carved into the
   wall. There appear to be no other caves at this level, but a sturdy
   steel ladder leads down through a large round hole in the floor. "
   north = entranceTunnel
   out asExit(north)
   down = downLadder
;
```

Note that as yet nothing defines where we end up when we go down the ladder. This is because there will be a corresponding [StairwayUp](stairwayup.md) in the cave below, and the StairwayUp will point to downLadder as its **masterObject**. The game will automatically link the StairwayUp to its masterObject and *vice versa*, so that when we traverse the StairwayDown it will know that its destination is in the corresponding StairwayUp's location. (We could equally well do this the other way round and make the StairwayUp the masterObject of the StairwayDown).
