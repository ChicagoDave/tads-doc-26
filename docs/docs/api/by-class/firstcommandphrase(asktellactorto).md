# firstCommandPhrase(askTellActorTo)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5107)


flag that the actor's being addressed in the second person


**Superclass chain:** [FirstCommandProdWithActor](firstcommandprodwithactor.md) > [CommandProdWithActor](commandprodwithactor.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > [FirstCommandProd](firstcommandprod.md) > **firstCommandPhrase(askTellActorTo)**


## Inherited Properties


*From [CommandProdWithActor](commandprodwithactor.md):* [`resolvedActor_`](commandprodwithactor.md#resolvedActor_), [`resolver_`](commandprodwithactor.md#resolver_)


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execActorPhrase(issuingActor)` *(overridden)*

Defined in en_us.t, line 5113

"execute" the target actor phrase


## Inherited Methods


*From [CommandProdWithActor](commandprodwithactor.md):* [`getActorPhrase`](commandprodwithactor.md#getActorPhrase), [`getResolver`](commandprodwithactor.md#getResolver), [`getTargetActor`](commandprodwithactor.md#getTargetActor), [`hasTargetActor`](commandprodwithactor.md#hasTargetActor), [`resolveNouns`](commandprodwithactor.md#resolveNouns)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [FirstCommandProd](firstcommandprod.md):* [`countCommands`](firstcommandprod.md#countCommands), [`getCommandSepIndex`](firstcommandprod.md#getCommandSepIndex), [`getCommandTokens`](firstcommandprod.md#getCommandTokens), [`getNextCommandIndex`](firstcommandprod.md#getNextCommandIndex), [`isEndOfSentence`](firstcommandprod.md#isEndOfSentence), [`resolveFirstAction`](firstcommandprod.md#resolveFirstAction)
