# FirstCommandProdWithActor

*class* — defined in [parser.t](../by-file/parser.t.md) (line 884)


First-on-line command with target actor. As with CommandProdWithActor, instantiating grammar rules must set the property actor_ to the actor match tree, and cmd_ to the underlying commandPhrase match.


**Superclass chain:** [CommandProdWithActor](commandprodwithactor.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > [FirstCommandProd](firstcommandprod.md) > **FirstCommandProdWithActorSubclasses:** [actorBadCommandPhrase(main)](actorbadcommandphrase%28main%29.md), [firstCommandPhrase(askTellActorTo)](firstcommandphrase%28asktellactorto%29.md), [firstCommandPhrase(withActor)](firstcommandphrase%28withactor%29.md)


## Inherited Properties


*From [CommandProdWithActor](commandprodwithactor.md):* [`resolvedActor_`](commandprodwithactor.md#resolvedActor_), [`resolver_`](commandprodwithactor.md#resolver_)


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [CommandProdWithActor](commandprodwithactor.md):* [`execActorPhrase`](commandprodwithactor.md#execActorPhrase), [`getActorPhrase`](commandprodwithactor.md#getActorPhrase), [`getResolver`](commandprodwithactor.md#getResolver), [`getTargetActor`](commandprodwithactor.md#getTargetActor), [`hasTargetActor`](commandprodwithactor.md#hasTargetActor), [`resolveNouns`](commandprodwithactor.md#resolveNouns)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [FirstCommandProd](firstcommandprod.md):* [`countCommands`](firstcommandprod.md#countCommands), [`getCommandSepIndex`](firstcommandprod.md#getCommandSepIndex), [`getCommandTokens`](firstcommandprod.md#getCommandTokens), [`getNextCommandIndex`](firstcommandprod.md#getNextCommandIndex), [`isEndOfSentence`](firstcommandprod.md#isEndOfSentence), [`resolveFirstAction`](firstcommandprod.md#resolveFirstAction)
