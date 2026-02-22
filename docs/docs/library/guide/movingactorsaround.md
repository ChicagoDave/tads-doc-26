# Moving Actors Around

Since Actors are meant to model living beings, there's no reason to assume they'll always stay in the same place. That means that we need some means of moving them around the game world.

The basic rule when moving actors around in code is *never* use moveInto(dest). Use **moveIntoForTravel(dest)** instead, or travelTo(destination, connector, backConnector) or scriptedTravelTo(dest); or else nestedActorAction(bob,North) or nestedActorAction(TravelVia, redDoor).

For a fuller discussion, see Mike Roberts's technical article on [NPC Travel in TADS 3](http://www.tads.org/howto/t3npcTravel.htm ).

It's also possible to have one actor automatically follow another (normally, but not necessarily, the player character) by putting it in an [AccompanyingState](accompanyingstate.md). This is one of the ActorState classes, which is what we'll be looking at next.
