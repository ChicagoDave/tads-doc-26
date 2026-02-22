# FirstCommandProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 691)


A first-on-line command. The first command on a command line can optionally start with an actor specification, to give orders to the actor.


**Superclass chain:** [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **FirstCommandProdSubclasses:** [firstCommandPhrase(commandOnly)](firstcommandphrase%28commandonly%29.md), [FirstCommandProdWithActor](firstcommandprodwithactor.md), [actorBadCommandPhrase(main)](actorbadcommandphrase%28main%29.md), [firstCommandPhrase(askTellActorTo)](firstcommandphrase%28asktellactorto%29.md), [firstCommandPhrase(withActor)](firstcommandphrase%28withactor%29.md)


## Inherited Properties


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `countCommands(results)`

Defined in parser.t, line 692


### `getCommandSepIndex`

Defined in parser.t, line 756

Get the token index of the first command separator token. This is the first token that is not part of the underlying command.


### `getCommandTokens`

Defined in parser.t, line 715

The tokens of the entire command except for the target actor specification. By default, we take all of the tokens starting with the first command's first token and running to the end of the token list. This assumes that the target actor is specified at the beginning of the command - languages that use some other word ordering must override this accordingly.


### `getNextCommandIndex`

Defined in parser.t, line 767

get the token index of the next command - this is the index of the next token after our conjunction if we have one, or after our command if we don't have a conjunction


### `getTargetActor`

Defined in parser.t, line 698

count commands in the underlying command


### `isEndOfSentence`

Defined in parser.t, line 746

Does this command end a sentence? The exact meaning of a sentence may vary by language; in English, a sentence ends with certain punctuation marks (a period, a semicolon, an exclamation point).


### `resolveFirstAction(issuingActor, targetActor)`

Defined in parser.t, line 725

Resolve my first action. This returns an instance of a subclass of Action that represents the resolved action. We'll ask our first subcommand to resolve its action.


### `resolveNouns(issuingActor, targetActor, results)`

Defined in parser.t, line 731

resolve nouns in the command


## Inherited Methods


*From [CommandProd](commandprod.md):* [`execActorPhrase`](commandprod.md#execActorPhrase), [`hasTargetActor`](commandprod.md#hasTargetActor)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
