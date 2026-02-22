# RandomFiringScript

*class* — defined in [misc.t](../by-file/misc.t.md) (line 917)


Random-Firing script add-in. This is a mix-in class that you can add to the superclass list of any Script subclass to make the script execute only a given percentage of the time it's invoked. Each time doScript() is invoked on the script, we'll look at the probability settings (see the properties below) to determine whether we really want to execute the script this time; if so, we'll proceed with the scripted event, otherwise we'll just return immediately, doing nothing.


**Superclass chain:** `object` > **RandomFiringScriptSubclasses:** [RandomEventList](randomeventlist.md), [ShuffledEventList](shuffledeventlist.md)


## Properties


### `eventPercent`

Defined in misc.t, line 933

Percentage of the time an event occurs. By default, we execute an event 100% of the time - meaning every time that doScript() is invoked. If you set this to a lower percentage, then each time doScript() is invoked, we'll randomly decide whether or not to execute an event based on this percentage. For example, if you want an event to execute on average about a third of the time, set this to 33.


### `eventReduceAfter`

Defined in misc.t, line 948

Random atmospheric events can get repetitive after a while, so we provide an easy way to reduce the frequency of our events after a while. This way, we'll generate the events more frequently at first, but once the player has seen them enough to get the idea, we'll cut back. Sometimes, the player will spend a lot of time in one place trying to solve a puzzle, so the same set of random events can get stale. Set eventReduceAfter to the number of times you want the events to be generated at full frequency; after we've fired events that many times, we'll change eventPercent to eventReduceTo. If eventReduceAfter is nil, we won't ever change eventPercent.


### `eventReduceTo`

Defined in misc.t, line 949


## Methods


### `checkEventOdds`

Defined in misc.t, line 966

Check the event odds to see if we want to fire an event at all on this invocation.


### `doScript`

Defined in misc.t, line 955

When doScript() is invoked, check the event probabilities before proceeding.
