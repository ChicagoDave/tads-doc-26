# Introduction

In the sections that follow we shall endeavour to make use of all the main types of room and travel connector in the TADS 3 library.

Rooms are locations in which actors and other objects may exist, and between which actors may travel. Since travel is possible directly from one Room  to another, Rooms are also Travel Connectors. TravelConnectors allow travel between Rooms: their class hierarchy is

```tads3
TravelConnector
   Passage
      Stairway
             StairwayDown
         StairwayUp
      ThroughPassage
         BasicDoor
            Door
               AutoClosingDoor
            SecretDoor
               HiddenDoor
         ExitOnlyPassage
         PathPassage
   RoomConnector
      OneWayRoomConnector
      RoomAutoConnector
         Room
            DarkRoom
            FloorlessRoom
            OutdoorRoom
   TravelMessage
      DeadEndConnector
      NoTravelMessage
         FakeConnector



 AskConnector

Note that Passage also descends from Fixture, so that Passage and all its subclasses represent physical game objects as well as connectors. This is not the case with RoomConnector and its descendants or TravelMessage and its.
Note that TravelMessage also descends from TravelWithMessage.
There is also a ShipBoardRoom class that can be used as a mix-in class for other kinds of room.
Room and its subclasses have a number of methods and properties that it is sometimes useful to override, these include:
atmosphereList
brightness
destName
enteringRoom
roomAfterAction
roomBeforeAction
roomParts
```
