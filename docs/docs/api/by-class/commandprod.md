# CommandProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 658)


The base class for commands. A command is the root of the grammar match tree for a single action. A command line can consist of a number of commands joined with command separators; in English, command separators are things like periods, semicolons, commas, and the words "and" and "then".


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **CommandProd**


<details><summary>Subclasses (11)</summary>

- [CommandProdWithActor](commandprodwithactor.md)
- [FirstCommandProdWithActor](firstcommandprodwithactor.md)
- [actorBadCommandPhrase(main)](actorbadcommandphrase%28main%29.md)
- [firstCommandPhrase(askTellActorTo)](firstcommandphrase%28asktellactorto%29.md)
- [firstCommandPhrase(withActor)](firstcommandphrase%28withactor%29.md)
- [CommandProdWithAmbiguousConj](commandprodwithambiguousconj.md)
- [commandPhrase(ambiguousConj)](commandphrase%28ambiguousconj%29.md)
- [CommandProdWithDefiniteConj](commandprodwithdefiniteconj.md)
- [commandPhrase(definiteConj)](commandphrase%28definiteconj%29.md)
- [FirstCommandProd](firstcommandprod.md)
- [firstCommandPhrase(commandOnly)](firstcommandphrase%28commandonly%29.md)

</details>


## Properties


### `getActorPhrase`

Defined in parser.t, line 674

Get the match tree for the target actor phrase, if any. By default, we have no target actor phrase, so just return nil.


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `execActorPhrase(issuingActor)`

Defined in parser.t, line 683

"Execute" the actor phrase. This lets us know that the parser has decided to use our phrasing to specify the target actor. We're not required to do anything here; it's just a notification for subclass use. Since we don't have a target actor phrase at all, we obviously don't need to do anything here.


### `hasTargetActor`

Defined in parser.t, line 659


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
