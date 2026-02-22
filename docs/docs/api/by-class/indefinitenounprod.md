# IndefiniteNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2427)


Noun phrase with an indefinite article


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **IndefiniteNounProdSubclasses:** [ArbitraryNounProd](arbitrarynounprod.md), [qualifiedSingularNounPhrase(anyPlural)](qualifiedsingularnounphrase%28anyplural%29.md), [qualifiedSingularNounPhrase(arbitrary)](qualifiedsingularnounphrase%28arbitrary%29.md), [qualifiedSingularNounPhrase(indefinite)](qualifiedsingularnounphrase%28indefinite%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `areAllEquiv(lst)`

Defined in parser.t, line 2499

are all of the items in the resolve list equivalents?


### `resolveMainPhrase(resolver, results)`

Defined in parser.t, line 2432

resolve the main phrase - this is separately overridable to allow subclassing


### `resolveNouns(resolver, results)`

Defined in parser.t, line 2438

by default, resolve the main noun phrase


### `selectFromList(resolver, results, lst)`

Defined in parser.t, line 2525

Select an item from the list of potential matches, given the list sorted from most likely to least likely (according to the resolver's ambiguous match filter). We'll ask the resolver to make the selection, because indefinite noun phrases can mean different things in different contexts.


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
