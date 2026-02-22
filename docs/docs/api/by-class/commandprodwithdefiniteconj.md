# CommandProdWithDefiniteConj

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1035)


Match class for a command phrase that is separated from anything that follows with an unambiguous conjunction.


**Superclass chain:** [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **CommandProdWithDefiniteConjSubclasses:** [commandPhrase(definiteConj)](commandphrase%28definiteconj%29.md)


## Properties


### `cmdCounted_`

Defined in parser.t, line 1052

counter: have we counted our command in the results object yet?


## Inherited Properties


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `countCommands(results)`

Defined in parser.t, line 1044

count commands


### `getCommandSepIndex`

Defined in parser.t, line 1075

Get the token index of the first command separator token. This is the first token that is not part of the underlying command.


### `getNextCommandIndex`

Defined in parser.t, line 1093

get the token index of the next command - this is the index of the next token after our conjunction if we have one, or after our command if we don't have a conjunction


### `isEndOfSentence`

Defined in parser.t, line 1061

does this command end a sentence


### `resolveFirstAction(issuingActor, targetActor)`

Defined in parser.t, line 1055

resolve my first action


### `resolveNouns(issuingActor, targetActor, results)`

Defined in parser.t, line 1036


## Inherited Methods


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
