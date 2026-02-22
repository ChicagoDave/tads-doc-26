# CommandRankingByWeakness

*class* — defined in [parser.t](../by-file/parser.t.md) (line 5902)


A "weakness" criterion. This is similar to the rank-by-problem criterion, but rather than ranking on an actual structural problem, it ranks on a structural weakness. This is suitable for things like adjective endings and truncations, where the weakness isn't on the same order as a "problem" but where we'd still rather avoid the weakness if we can.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **CommandRankingByWeaknessGlobal objects:** [rankByEndAdj](rankbyendadj.md), [rankByPluralTrunc](rankbypluraltrunc.md), [rankByPronoun](rankbypronoun.md), [rankByTrunc](rankbytrunc.md), [rankByWeakness](rankbyweakness.md)


## Properties


### `prop_`

Defined in parser.t, line 5910

our command-ranking property


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 5904

on pass 1, ignore weaknesses


### `comparePass2(a, b)` *(overridden)*

Defined in parser.t, line 5907

on pass 2, compare based on weaknesses
