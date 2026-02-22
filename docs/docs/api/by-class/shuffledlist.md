# ShuffledList

*class* — defined in [misc.t](../by-file/misc.t.md) (line 1390)


Shuffled List - this class keeps a list of values that can be returned in random order, but with the constraint that we never repeat a value until we've handed out every value. Think of a shuffled deck of cards: the order of the cards handed out is random, but once a card is dealt, it can't be dealt again until we put everything back into the deck and reshuffle.


**Superclass chain:** `object` > **ShuffledListSubclasses:** [ShuffledIntegerList](shuffledintegerlist.md)


## Properties


### `suppressRepeats`

Defined in misc.t, line 1413

Flag: suppress repeated values. We mostly suppress repeats by our very design, since we run through the entire list before repeating anything in the list. However, there's one situation (in a list with more than one element) where a repeat can occur: immediately after a shuffle, we could select the last element from the previous shuffle as the first element of the new shuffle. If this flag is set, we'll suppress this type of repeat by choosing again any time we're about to choose a repeat.


### `valueList`

Defined in misc.t, line 1395

the list of values we want to shuffle - initialize this in each instance to the set of values we want to return in random order


### `valuesAvail`

Defined in misc.t, line 1536

number of values still available on this round


### `valuesVec`

Defined in misc.t, line 1533

Internal vector of available/used values. Elements from 1 to 'valuesAvail', inclusive, are still available for use on this round. Elements above 'valuesAvail' have already been used.


## Methods


### `construct(lst)`

Defined in misc.t, line 1416

create from a given list


### `getNextValue`

Defined in misc.t, line 1430

Get a random value. This will return a randomly-selected element from 'valueList', but we'll return every element of 'valueList' once before repeating any element.


### `reshuffle`

Defined in misc.t, line 1518

Shuffle the values. This puts all of the values back into the deck (as it were) for a new round. It's never required to call this, because getNextValue() automatically shuffles the deck and starts over each time it runs through the entire deck. This is provided in case the caller has a reason to want to put all the values back into play immediately, before every value has been dealt on the current round.
