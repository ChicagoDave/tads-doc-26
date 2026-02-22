# CommandRankingByProblem

*class* — defined in [parser.t](../by-file/parser.t.md) (line 5848)


A command ranking criterion that measures a "problem" by a count of occurrences stored in a property of the CommandRanking object. For example, we could count the number of noun phrases that don't resolve to any objects.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **CommandRankingByProblemGlobal objects:** [rankByActorSpecified](rankbyactorspecified.md), [rankByAllExcluded](rankbyallexcluded.md), [rankByDisambigOrdinals](rankbydisambigordinals.md), [rankByEmptyBut](rankbyemptybut.md), [rankByIndefinite](rankbyindefinite.md), [rankByInsufficient](rankbyinsufficient.md), [rankByListForSingle](rankbylistforsingle.md), [rankByMiscWordList](rankbymiscwordlist.md), [rankByMissing](rankbymissing.md), [rankByNonMatch](rankbynonmatch.md), [rankByUnwantedPlural](rankbyunwantedplural.md), [rankByVocabNonMatch](rankbyvocabnonmatch.md)


## Properties


### `prop_`

Defined in parser.t, line 5854

our ranking property - this is a property of the CommandRanking object that gives us a count of the number of times our "problem" has occurred in the ranking object's parse tree


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 5857

first pass - compare by presence or absence of the problem


### `comparePass2(a, b)` *(overridden)*

Defined in parser.t, line 5875

second pass - compare by number of occurrences of the problem
