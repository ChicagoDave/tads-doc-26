# TravelMessageHandler

*class* — defined in [travel.t](../by-file/travel.t.md) (line 210)


Travel Message Handler. This contains a set of messages that are specific to different types of TravelConnector objects, to describe NPC arrivals and departures via these connectors when the NPC's are in view of the player character.


**Superclass chain:** `object` > **TravelMessageHandler**


<details><summary>Subclasses (13)</summary>

- [ActorState](actorstate.md)
- [AccompanyingInTravelState](accompanyingintravelstate.md)
- [GuidedInTravelState](guidedintravelstate.md)
- [AccompanyingState](accompanyingstate.md)
- [GuidedTourState](guidedtourstate.md)
- [ConversationReadyState](conversationreadystate.md)
- [HermitActorState](hermitactorstate.md)
- [InConversationState](inconversationstate.md)
- [Traveler](traveler.md)
- [Actor](actor.md)
- [UntakeableActor](untakeableactor.md)
- [Person](person.md)
- [Vehicle](vehicle.md)

</details>


## Methods


### `getNominalTraveler`

Defined in travel.t, line 216

Get the traveler for the purposes of arrival/departure messages. Implementations that aren't themselves the travelers should override this to supply the correct nominal traveler.


### `sayArriving(conn)`

Defined in travel.t, line 219

generic arrival/departure - for the base TravelConnector class


### `sayArrivingDir(dir, conn)`

Defined in travel.t, line 233

directional arrival/departure - for RoomConnector


### `sayArrivingDownStairs(conn)`

Defined in travel.t, line 255


### `sayArrivingLocally(dest, conn)`

Defined in travel.t, line 223

generic local arrival and departure messages


### `sayArrivingThroughPassage(conn)`

Defined in travel.t, line 237

arrival/departure via a ThroughPassage


### `sayArrivingUpStairs(conn)`

Defined in travel.t, line 253

arrival/departure up/down stairs


### `sayArrivingViaPath(conn)`

Defined in travel.t, line 247

arrival/departure via a PathPassage


### `sayDeparting(conn)`

Defined in travel.t, line 220


### `sayDepartingDir(dir, conn)`

Defined in travel.t, line 234


### `sayDepartingDownStairs(conn)`

Defined in travel.t, line 259


### `sayDepartingLocally(dest, conn)`

Defined in travel.t, line 225


### `sayDepartingThroughPassage(conn)`

Defined in travel.t, line 241


### `sayDepartingUpStairs(conn)`

Defined in travel.t, line 257


### `sayDepartingViaPath(conn)`

Defined in travel.t, line 249


### `sayTravelingRemotely(dest, conn)`

Defined in travel.t, line 229

generic remote travel message
