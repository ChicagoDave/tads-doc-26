# TravelMessage

TravelMessage :[TravelWithMessage](travelwithmessage.md), [TravelConnector](travelconnector.md)

Up to this point, you can get into the small cave but not out of it again. This time we won't explicitly mention the tunnel in the room description or implement it as an object, but we might want to mention the walk down the tunnel when the PC travels south. The simplest way to do that is with a TravelMessage. We do not need to define this as a separate object, it can simply be an anonymous nested object attached to the south property of smallCave:

```tads3
smallCave : DarkRoom 'Small Cave' 'the small cave'
  "The long narrow tunnel from the south comes to an end in this cramped,
    sandy-floored cave, whose rough rocky walls press in claustrophobically
    on every side. Anyone much taller than average would have to stoop here. "
  south : TravelMessage
    {
      -> secretPassage
      "You walk south for quite some way down a long tunnel. ";
    }
;
```

This time, we have used the [TravelMessage template](travelmessagetemplate.md) to simplify the definition here. The first template property here, -> secretPassage, is in fact the **destination** property of the TravelMessage, while the second, the double-quoted string, is its **travelDesc** property (defined on TravelWithMessage, from which TravelMessage inherits).
