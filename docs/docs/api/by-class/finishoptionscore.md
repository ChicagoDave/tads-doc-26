# finishOptionScore

*object* — defined in [misc.t](../by-file/misc.t.md) (line 2287)


Option to show the score in finishGame. This doesn't create a listed option in the set of offered options, but rather is simply a flag to finishGame() that the score should be announced along with the end-of-game announcement message.


**Superclass chain:** [FinishOption](finishoption.md) > `object` > **finishOptionScore**


## Properties


### `isListed` *(overridden)*

Defined in misc.t, line 2292

this is not a listed option


### `showScoreInFinish` *(overridden)*

Defined in misc.t, line 2289

show the score in the end-of-game announcement


## Inherited Properties


*From [FinishOption](finishoption.md):* [`desc`](finishoption.md#desc), [`responseChar`](finishoption.md#responseChar), [`responseKeyword`](finishoption.md#responseKeyword)


## Methods


### `doOption` *(overridden)*

Defined in misc.t, line 2295

this option isn't selectable, so it has no effect


## Inherited Methods


*From [FinishOption](finishoption.md):* [`responseMatches`](finishoption.md#responseMatches)
