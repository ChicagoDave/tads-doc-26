# commandPhrase(definiteConj)

*grammar* — defined in [parser.t](../by-file/parser.t.md) (line 1177)


The basic grammar rule for an unambiguous end-of-sentence command. This matches either a predicate with nothing following, or a predicate with an unambiguous command-only conjunction following.


**Superclass chain:** [CommandProdWithDefiniteConj](commandprodwithdefiniteconj.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **commandPhrase(definiteConj)**


## Inherited Properties


*From [CommandProdWithDefiniteConj](commandprodwithdefiniteconj.md):* [`cmdCounted_`](commandprodwithdefiniteconj.md#cmdCounted_)


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [CommandProdWithDefiniteConj](commandprodwithdefiniteconj.md):* [`countCommands`](commandprodwithdefiniteconj.md#countCommands), [`getCommandSepIndex`](commandprodwithdefiniteconj.md#getCommandSepIndex), [`getNextCommandIndex`](commandprodwithdefiniteconj.md#getNextCommandIndex), [`isEndOfSentence`](commandprodwithdefiniteconj.md#isEndOfSentence), [`resolveFirstAction`](commandprodwithdefiniteconj.md#resolveFirstAction), [`resolveNouns`](commandprodwithdefiniteconj.md#resolveNouns)


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
