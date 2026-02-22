# NestedRoom Overview

A NestedRoom is an object that can contain an actor without being a fully-fledged Room. A NestedRoom is typically an object an actor can stand, sit or lie on within a room, such as a bed or chair.

```tads3
NestedRoom
   BasicChair
      BasicBed
         BasicPlatform
            Booth
            Platform
               NominalPlatform
         Bed
      Chair
   HighNestedRoom
   Vehicle
```

Although it doesn't strictly belong in the NestedRoom category, we'll also look at the [OutOfReach](outofreach.md) class here, since it doesn't fit in any other obvious grouping, and it will be convenient to consider it alongside HighNestedRoom.
