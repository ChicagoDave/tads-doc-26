# specialTopicHistory

*object* — defined in [actor.t](../by-file/actor.t.md) (line 3948)


A history of special topics listed in topic inventories. This keeps track of special topics that we've recently offered, so that we can provide better feedback if the player tries to use a recently-listed special topic after it's gone out of context.


**Superclass chain:** `object` > **specialTopicHistory**


## Properties


### `historyList`

Defined in actor.t, line 4051

The list of entries. Create it when we first need it, which perInstance does for us.


### `maxEntries`

Defined in actor.t, line 3979

Maximum number of topics to keep in our inventory. When the history exceeds this number, we'll throw away the oldest entry each time we need to add a new entry - thus, we'll always have the N most recent suggestions.


## Methods


### `checkHistory(toks)`

Defined in actor.t, line 4008

Scan the history list (or, if there's no limit to the history, scan all of the special topics in the entire game) for a match to an unrecognized command. Returns true if we find a match, nil if not.


### `noteListing(t)`

Defined in actor.t, line 3982

note that a special topic 't' is being listed in a topic inventory
