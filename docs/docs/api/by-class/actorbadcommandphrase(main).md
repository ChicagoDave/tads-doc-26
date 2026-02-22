# actorBadCommandPhrase(main)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5147)


An actor-targeted command with a bad command phrase. This is used as a fallback if we fail to match anything on the first attempt at parsing the first command on a line. The point is to at least detect the target actor phrase, if that much is valid, so that we better customize error messages for the rest of the command.


**Superclass chain:** [FirstCommandProdWithActor](firstcommandprodwithactor.md) > [CommandProdWithActor](commandprodwithactor.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > [FirstCommandProd](firstcommandprod.md) > **actorBadCommandPhrase(main)**


## Inherited Properties


*From [CommandProdWithActor](commandprodwithactor.md):* [`resolvedActor_`](commandprodwithactor.md#resolvedActor_), [`resolver_`](commandprodwithactor.md#resolver_)


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(issuingActor, targetActor, results)` *(overridden)*

Defined in en_us.t, line 5153

to resolve nouns, we merely resolve the actor


## Inherited Methods


*From [CommandProdWithActor](commandprodwithactor.md):* [`execActorPhrase`](commandprodwithactor.md#execActorPhrase), [`getActorPhrase`](commandprodwithactor.md#getActorPhrase), [`getResolver`](commandprodwithactor.md#getResolver), [`getTargetActor`](commandprodwithactor.md#getTargetActor), [`hasTargetActor`](commandprodwithactor.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [FirstCommandProd](firstcommandprod.md):* [`countCommands`](firstcommandprod.md#countCommands), [`getCommandSepIndex`](firstcommandprod.md#getCommandSepIndex), [`getCommandTokens`](firstcommandprod.md#getCommandTokens), [`getNextCommandIndex`](firstcommandprod.md#getNextCommandIndex), [`isEndOfSentence`](firstcommandprod.md#isEndOfSentence), [`resolveFirstAction`](firstcommandprod.md#resolveFirstAction)
