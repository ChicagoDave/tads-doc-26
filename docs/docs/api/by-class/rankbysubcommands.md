# rankBySubcommands

*object* — defined in [parser.t](../by-file/parser.t.md) (line 6013)


Command ranking by subcommand count: we prefer the match with fewer subcommands. If one has fewer subcommands than the other, it means that we were able to interpret ambiguous conjunctions (such as "and") as noun phrase conjunctions rather than as command conjunctions; other things being equal, we'd rather take the interpretation that gives us noun phrases than the one that involves more separate commands.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankBySubcommands**


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 6015

first pass - compare subcommand counts


## Inherited Methods


*From [CommandRankingCriterion](commandrankingcriterion.md):* [`comparePass2`](commandrankingcriterion.md#comparePass2)
