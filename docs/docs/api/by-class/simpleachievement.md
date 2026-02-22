# SimpleAchievement

*class* — defined in [score.t](../by-file/score.t.md) (line 180)


Generic text achievement. When we add an achievement to the full score list and the achievement is a simple string description, we'll create one of these to encapsulate the achievement.


**Superclass chain:** [Achievement](achievement.md) > `object` > **SimpleAchievement**


## Properties


### `desc_`

Defined in score.t, line 188

my description string


## Inherited Properties


*From [Achievement](achievement.md):* [`desc`](achievement.md#desc), [`maxPoints`](achievement.md#maxPoints), [`points`](achievement.md#points), [`scoreCount`](achievement.md#scoreCount), [`totalPoints`](achievement.md#totalPoints)


## Methods


### `construct(str)`

Defined in score.t, line 182

create dynamically with a given string as our description


### `desc`

Defined in score.t, line 185

show my description


## Inherited Methods


*From [Achievement](achievement.md):* [`addToScoreOnce`](achievement.md#addToScoreOnce), [`awardPoints`](achievement.md#awardPoints), [`awardPointsOnce`](achievement.md#awardPointsOnce), [`listFullScoreItem`](achievement.md#listFullScoreItem)
