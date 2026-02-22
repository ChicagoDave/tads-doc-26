# libScore

*object* — defined in [score.t](../by-file/score.t.md) (line 297)


The main game score object.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **libScore**


## Properties


### `fullScoreList`

Defined in score.t, line 445

Vector for the full score achievement list. This is a list of all of the Achievement objects awarded for accomplishments so far.


### `scoreNotify`

Defined in score.t, line 455

current score notification status - if on, we'll show a message at the end of each turn where the score changes, otherwise we won't mention anything


### `totalScore`

Defined in score.t, line 448

the total number of points scored so far


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `addToScore_(points, desc)`

Defined in score.t, line 310

Add to the score. 'points' is the number of points to add to the score, and 'desc' is a string describing the reason the points are being awarded, or an Achievement object describing the points.


### `calcMaxScore`

Defined in score.t, line 463

Compute the sum of the maximum point values of the Achievement objects in the game. Point values are optional in Achievement objects; if there are no Achievement objects with non-nil point values, this will simply return nil.


### `execute` *(overridden)*

Defined in score.t, line 503

execute pre-initialization


### `runScoreNotifier`

Defined in score.t, line 369

Explicitly run the score notification daemon.


### `showFullScore`

Defined in score.t, line 430

Display the full score. 'explicit' is true if the player asked for the full score explicitly, as with a FULL SCORE command; if we're showing the full score automatically in the course of some other action, 'explicit' should be nil.


### `showScore`

Defined in score.t, line 378

Show the simple score


### `showScoreRank(points)`

Defined in score.t, line 400

show the score rank message


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
