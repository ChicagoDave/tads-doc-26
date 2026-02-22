# Achievement

*class* — defined in [score.t](../by-file/score.t.md) (line 57)


An Achievement is an object used to award points in the score. For most purposes, an achievement can be described simply by a string, but the Achievement object provides more flexibility in describing combined scores when a set of similar achievements are to be grouped.


**Superclass chain:** `object` > **AchievementSubclasses:** [SimpleAchievement](simpleachievement.md)


## Properties


### `desc`

Defined in score.t, line 97

Describe the achievement - this must display a string explaining the reason the points associated with this achievement were awarded.


### `maxPoints`

Defined in score.t, line 76

The MAXIMUM number of points this Achievement can award. This is by default just our 'points' value, on the assumption that the achievement is scored only once. The library uses this value during pre-initialization to compute the maximum possible score in the game.


### `points`

Defined in score.t, line 67

The number of points this Achievement scores individually. By default, we set this to nil. If you use the awardPoints() or awardPointsOnce() methods, you MUST set this to a non-nil value.


### `scoreCount`

Defined in score.t, line 114

The number of times the achievement has been awarded. Each time the achievement is passed to addToScore(), this is incremented. Note that this is distinct from the number of points.


### `totalPoints`

Defined in score.t, line 122

the number of points awarded for the achievement; if this achievement has been accomplished multiple times, this reflects the aggregate number of points awarded for all of the times it has been accomplished


## Methods


### `addToScoreOnce(points)`

Defined in score.t, line 134

Add this achievement to the score one time only, awarding the given number of points. This can be used to score an achievement without separately tracking whether or not the achievement has been accomplished previously. If the achievement has already been scored before, this will do nothing at all; otherwise, it'll score the achievement with the given number of points. Returns true if we do award the points, nil if not (because we've awarded them before).


### `awardPoints`

Defined in score.t, line 156

Award this Achievement's score, using the score value specified in my 'points' property.


### `awardPointsOnce`

Defined in score.t, line 168

Award this Achievement's score, but ensure that we're never awarded more than one time. If this Achievement has already been awarded, this does nothing at all. Returns true if we do award the points, nil if not (because we've awarded them before).


### `listFullScoreItem`

Defined in score.t, line 100

show myself in a full-score listing
