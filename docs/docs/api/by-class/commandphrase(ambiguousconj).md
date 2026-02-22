# commandPhrase(ambiguousConj)

*grammar* — defined in [parser.t](../by-file/parser.t.md) (line 1188)


the basic grammar rule for a pair of commands with an ambiguous separator (i.e., a separator that could separate commands or conjunctions)


**Superclass chain:** [CommandProdWithAmbiguousConj](commandprodwithambiguousconj.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **commandPhrase(ambiguousConj)**


## Inherited Properties


*From [CommandProdWithAmbiguousConj](commandprodwithambiguousconj.md):* [`cmdCounted_`](commandprodwithambiguousconj.md#cmdCounted_)


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [CommandProdWithAmbiguousConj](commandprodwithambiguousconj.md):* [`countCommands`](commandprodwithambiguousconj.md#countCommands), [`getCommandSepIndex`](commandprodwithambiguousconj.md#getCommandSepIndex), [`getNextCommandIndex`](commandprodwithambiguousconj.md#getNextCommandIndex), [`isEndOfSentence`](commandprodwithambiguousconj.md#isEndOfSentence), [`resolveFirstAction`](commandprodwithambiguousconj.md#resolveFirstAction), [`resolveNouns`](commandprodwithambiguousconj.md#resolveNouns)


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
