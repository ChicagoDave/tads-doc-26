# rankByLiteralLength

*object* — defined in [parser.t](../by-file/parser.t.md) (line 5980)


Command ranking by literal phrase length. We prefer interpretations that treat less text as uninterpreted literal text. By "less text," we simply mean that one has a shorter string treated as literal text than the other. (We prefer shorter literals because when the parser matches a string of literal text, it's essentially throwing up its hands and admitting it can't parse the text; so the less text is contained in literals, the more text the parser is actually parsing, and more parsed is better.)


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankByLiteralLength**


## Methods


### `comparePass1(a, b)` *(overridden)*

Defined in parser.t, line 5982

first pass


## Inherited Methods


*From [CommandRankingCriterion](commandrankingcriterion.md):* [`comparePass2`](commandrankingcriterion.md#comparePass2)
