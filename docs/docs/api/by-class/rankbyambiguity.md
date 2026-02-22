# rankByAmbiguity

*object* — defined in [parser.t](../by-file/parser.t.md) (line 6077)


Rank by ambiguous noun phrases. We apply this criterion on the second pass only, because it's a weak test: we might end up narrowing things down through automatic "logicalness" tests during the noun resolution process, so ambiguity at this stage in the parsing process doesn't necessarily indicate that there's real ambiguity in the command. However, if we can already tell that one interpretation is unambiguous and another is ambiguous, and the two interpretations are otherwise equally good, pick the one that's already unambiguous: the ambiguous interpretation might or might not stay ambiguous, but the unambiguous interpretation will definitely stay unambiguous.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankByAmbiguity**


## Methods


### `comparePass2(a, b)` *(overridden)*

Defined in parser.t, line 6083

Do nothing on the first pass, because we want any first-pass criterion to prevail over our weak test. Instead, check for a difference in ambiguity only on the second pass.


## Inherited Methods


*From [CommandRankingCriterion](commandrankingcriterion.md):* [`comparePass1`](commandrankingcriterion.md#comparePass1)
