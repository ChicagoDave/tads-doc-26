# CommandProdWithAmbiguousConj

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1107)


Match class for two command phrases separated by an ambiguous conjunction (i.e., a conjunction that could also separate two noun phrases). Grammar rules based on this class must set the properties 'cmd1_' to the underlying 'predicate' production match of the first command, and 'cmd2_' to the underlying 'commandPhrase' production match of the second command.


**Superclass chain:** [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **CommandProdWithAmbiguousConjSubclasses:** [commandPhrase(ambiguousConj)](commandphrase%28ambiguousconj%29.md)


## Properties


### `cmdCounted_`

Defined in parser.t, line 1137

counter: have we counted our command in the results object yet?


## Inherited Properties


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `countCommands(results)`

Defined in parser.t, line 1126

count our commands


### `getCommandSepIndex`

Defined in parser.t, line 1159

Get the token index of the first command separator token. This is the first token that is not part of the underlying command.


### `getNextCommandIndex`

Defined in parser.t, line 1169

get the token index of the next command - this is simply the starting index for our second subcommand tree


### `isEndOfSentence`

Defined in parser.t, line 1146

does this command end a sentence


### `resolveFirstAction(issuingActor, targetActor)`

Defined in parser.t, line 1140

resolve my first action


### `resolveNouns(issuingActor, targetActor, results)`

Defined in parser.t, line 1108


## Inherited Methods


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
