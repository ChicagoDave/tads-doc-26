# CommandRankingCriterion

*class* — defined in [parser.t](../by-file/parser.t.md) (line 5816)


Command ranking criterion. This is used by the CommandRanking class to represent one criterion for comparing two parse trees.


**Superclass chain:** `object` > **CommandRankingCriterionSubclasses:** [CommandRankingByProblem](commandrankingbyproblem.md), [CommandRankingByWeakness](commandrankingbyweakness.md)


**Global objects:** [rankByAmbiguity](rankbyambiguity.md), [rankByLiteralLength](rankbyliterallength.md), [rankByNonMatchPoss](rankbynonmatchposs.md), [rankBySubcommands](rankbysubcommands.md), [rankByTokenCount](rankbytokencount.md), [rankByVerbStructure](rankbyverbstructure.md)


## Methods


### `comparePass1(a, b)`

Defined in parser.t, line 5823

Compare two CommandRanking objects on the basis of this criterion, for the first, coarse-grained pass. Returns a positive number if a is better than b, 0 if they're indistinguishable, or -1 if a is worse than b.


### `comparePass2(a, b)`

Defined in parser.t, line 5826

compare two rankings for the second, fine-grained pass
