# rankByTokenCount

*object* — defined in [parser.t](../by-file/parser.t.md) (line 6037)


Rank by token count. Other things being equal, we'd rather pick a longer match. If one match is shorter than the other in terms of the number of tokens it encompasses, then it means that the shorter match left more tokens at the end of the command to be interpreted as separate commands. If we have an interpretation that can take more of those tokens and parse them as part of the current command, that interpretation is probably better.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankByTokenCount**


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 6039

first pass - compare token counts


## Inherited Methods


*From [CommandRankingCriterion](commandrankingcriterion.md):* [`comparePass2`](commandrankingcriterion.md#comparePass2)
