# RandomFiringScript

RandomFiringScript: object

RandomFiringScript is a mix-in class that can be added to any Script-like object to reduce the percentage of time it fires. [ShuffledEventList](shuffledeventlist.md) and [RandomEventList](randomeventlist.md) already inherit from RandomFiringScript, but you can mix with any of the other Script subclasses, provided you list it first, e.g.

```tads3
myScript: RandomFiringScript, EventList
     [
        'The golden banana emits a cloud of purple smoke. ',
        ...
     ]
     eventPercent = 50
  ;
```

You can set the **eventPercent**property (an integer between 0 and 100) to define the proportion of turns in which you want one of the events (normally just displaying a string) to occur (for example, setting eventPercent = 75 would cause a random event to be selected on average in three turns out of every four).  By default, eventPercent is 100. Additionally, if you wish, you can have this percentage fall (or even rise!) to a new value, **eventReduceTo** after **eventReduceAfter** turns. If **eventReduceAfter** is nil (as it is by default) then the eventPercent never changes.
