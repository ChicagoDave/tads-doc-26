# rankByNonMatchPoss

*object* — defined in [parser.t](../by-file/parser.t.md) (line 5947)


Rank by unmatched possessive-qualified phrases. If we have two unknown phrases, one with a possessive qualifier and one without, and other things being equal, prefer the one with the possessive qualifier.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankByNonMatchPoss**


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 5953

ignore on pass 1 - this only counts if other factors are equal, so we want to consider all of the other factors on pass 1 before taking this criterion into account


### `comparePass2(a, b)` *(overridden)*

Defined in parser.t, line 5956

pass 2 - more possessives are better
