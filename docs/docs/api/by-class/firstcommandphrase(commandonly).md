# firstCommandPhrase(commandOnly)

*grammar* — defined in [parser.t](../by-file/parser.t.md) (line 781)


Define the simplest grammar rule for a first-on-line command phrase, which is just an ordinary command phrase. The language-specific grammar must define any other alternatives; specifically, the language might provide an "actor, command" syntax to direct a command to a particular actor.


**Superclass chain:** [FirstCommandProd](firstcommandprod.md) > [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **firstCommandPhrase(commandOnly)**


## Inherited Properties


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [FirstCommandProd](firstcommandprod.md):* [`countCommands`](firstcommandprod.md#countCommands), [`getCommandSepIndex`](firstcommandprod.md#getCommandSepIndex), [`getCommandTokens`](firstcommandprod.md#getCommandTokens), [`getNextCommandIndex`](firstcommandprod.md#getNextCommandIndex), [`getTargetActor`](firstcommandprod.md#getTargetActor), [`isEndOfSentence`](firstcommandprod.md#isEndOfSentence), [`resolveFirstAction`](firstcommandprod.md#resolveFirstAction), [`resolveNouns`](firstcommandprod.md#resolveNouns)


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
