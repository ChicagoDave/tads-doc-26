# CommandProdWithActor

*class* — defined in [parser.t](../by-file/parser.t.md) (line 793)


A command with an actor specification. This should be instantiated with grammar rules in a language-specific module.


**Superclass chain:** [CommandProd](commandprod.md) > [BasicProd](basicprod.md) > `object` > **CommandProdWithActorSubclasses:** [FirstCommandProdWithActor](firstcommandprodwithactor.md), [actorBadCommandPhrase(main)](actorbadcommandphrase%28main%29.md), [firstCommandPhrase(askTellActorTo)](firstcommandphrase%28asktellactorto%29.md), [firstCommandPhrase(withActor)](firstcommandphrase%28withactor%29.md)


## Properties


### `resolvedActor_`

Defined in parser.t, line 872

my resolved actor object


### `resolver_`

Defined in parser.t, line 875

my actor resolver object


## Inherited Properties


*From [CommandProd](commandprod.md):* [`getActorPhrase`](commandprod.md#getActorPhrase)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execActorPhrase(issuingActor)` *(overridden)*

Defined in parser.t, line 815

Execute the target actor phrase. This is a notification, for use by subclasses; we don't have anything we need to do in this base class implementation.


### `getActorPhrase`

Defined in parser.t, line 804

return my resolved actor object


### `getResolver(issuingActor)`

Defined in parser.t, line 861

get or create my actor resolver


### `getTargetActor`

Defined in parser.t, line 799

this command explicitly specifies an actor


### `hasTargetActor` *(overridden)*

Defined in parser.t, line 794


### `resolveNouns(issuingActor, targetActor, results)`

Defined in parser.t, line 824

Resolve nouns. We'll resolve only the nouns in the target actor phrase; we do not resolve nouns in the command phrase, because we must re-parse the command phrase after we've finished resolving the actor phrase, and thus we can't resolve nouns in the command phrase until after the re-parse is completed.


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
