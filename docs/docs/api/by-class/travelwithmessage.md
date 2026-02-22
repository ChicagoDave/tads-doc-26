# TravelWithMessage

*class* — defined in [travel.t](../by-file/travel.t.md) (line 2015)


A mix-in class that can be added to objects that also inherit from TravelConnector to add a message as the connector is traversed.


**Superclass chain:** `object` > **TravelWithMessageSubclasses:** [TravelMessage](travelmessage.md), [DeadEndConnector](deadendconnector.md), [NoTravelMessage](notravelmessage.md), [FakeConnector](fakeconnector.md)


## Properties


### `npcTravelDesc`

Defined in travel.t, line 2033

My message to display when any non-player character traverses the connector. If this is not overridden, no message will be displayed when an NPC travels through the connector.


## Methods


### `noteTraversal(traveler)`

Defined in travel.t, line 2048

on traversing the connector, show our message


### `showTravelDesc`

Defined in travel.t, line 2039

Display my message. By default, we show one message for the player character and another message for NPC's.


### `travelDesc`

Defined in travel.t, line 2022

My message to display when the player character traverses the connector. This should be overridden with the custom message for the connector. By default, if we're a Script, we'll invoke the script to show the next message.
