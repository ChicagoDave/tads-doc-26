# rankByVerbStructure

*object* — defined in [parser.t](../by-file/parser.t.md) (line 6057)


Rank by "verb structure." This gives more weight to an interpretation that has more structural noun phrases in the verb. For example, "DETACH dobj FROM iobj" is given more weight than "DETACH dobj", because the former has two structural noun phrases whereas the latter has only one. This will make us prefer to treat DETACH WIRE FROM BOX as a two-object action, for example, even if we could treat WIRE FROM BOX as a single "locational" noun phrase.


**Superclass chain:** [CommandRankingCriterion](commandrankingcriterion.md) > `object` > **rankByVerbStructure**


## Methods


### `comparePass2(a, b)` *(overridden)*

Defined in parser.t, line 6058


## Inherited Methods


*From [CommandRankingCriterion](commandrankingcriterion.md):* [`comparePass1`](commandrankingcriterion.md#comparePass1)
