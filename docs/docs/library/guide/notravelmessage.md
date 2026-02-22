# NoTravelMessage

NoTravelMessage : [TravelMessage](travelmessage.md)

We have described the lakeShore room as being on the northern shore of a giant underground lake. This means that it should be fairly apparent that the PC cannot proceed south. In this situation we may want to display a custom message if the player nevertheless attempts to walk out onto the lake; a NoTravelMessage will perform this role (using the [NoTravelMessage template](notravelmessagetemplate.md)):

```tads3
lakeRoom: Room 'Lake Shore'
  "This is the northern shore of a giant underground lake. A door leads north. "
  north = lakeDoor2
  south : NoTravelMessage { "You never learnt to walk on water. " }
  southeast asExit(south)
  southwest asExit(south)
;
```

This is very similar to a [FakeConnector](fakeconnector.md). The only difference is a direction attached to a NoTravelMessage won't be included in a list of exits (e.g. in response to an EXITS command, or in the status line), whereas that attached to a FakeConnector will. A NoTravelMessage should therefore be used to explain why travel is not possible in a direction in which it's reasonably apparent that travel isn't possible, while a FakeConnector should be used to make travel apparently possible in a direction in which it isn' t really, e.g.. to provide a "soft boundary" to the map.
