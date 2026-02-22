# Wearable

Wearable : [Thing](thing-thebasics.md)

A Wearable is simply something that can be worn by an actor. Try defining the following:

```tads3
cap : Wearable 'sailor\'s cap' 'sailor\'s cap' @mainCave
  "It's a large round hat with a white top and a small blue peak. "
;
```

Now recompile the game, go to the mainCave, and try WEAR CAP, INVENTORY, REMOVE CAP, INVENTORY (four separate commands).

The most interesting methods and properties that Wearable introduces are wornBy, isWorn() and isWornBy(actor). None of these are properties or methods you'd normally want to override, but you might have occasion to test their values. **wornBy** returns the actor object that is currently wearing the Wearable (or nil if it is not being worn), **isWorn()** returns true if the Wearable is being worn and nil otherwise, and **isWornBy(actor)** similarly tests for its being worn by a specific Actor. We shall make use of isWorn() shortly, when we add some complications to this cap. Also, we shan't be leaving this cap in mainCave, but it'll have to stay there till we create a new location for it.
