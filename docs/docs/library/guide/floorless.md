# Floorless

Floorless : object

Floorless is a mix-in class which adds Floorless behaviour to any Room class; that is it takes away the floor from the list of [room parts](roomparts.md), and provides the handling for a dropped object to end up in another location.

Since the top of the mast is not exactly an (indoor) Room, in the sense of having four walls and a ceiling, it would be better defined using a mix of Floorless and a more appropriate class:

```tads3
topOfMast : Floorless, Deck 'Top of Mast' 'the top of the mast'
  "From the top of the mast you can see miles out across the lake to starboard
   and the shore over to port. The deck below looks a sickeningly long way down. "
   down = mainDeck
   bottomRoom = (mainDeck.destination)
;
```

Although the randomizing maindeck connector works fine, as you'll have seen if you've experiment with it, it is actually not a very good idea in practice. Not only will the random connector be potentially confusing to players, when we come to define an NPC who will follow the PC around, it can result in accidentally losing her (for example if the PC goes south from the foredeck and the NPC tries to follow him, she may end up on the port deck and he on the starboard, which is simply wrong if she's meant to be following him). Thus, once you've experimented with this random connector (assuming you want to), I suggest you remove its random element and change it to:

```tads3
mainDeck : OneWayRoomConnector
  destination = portDeck
;
```
