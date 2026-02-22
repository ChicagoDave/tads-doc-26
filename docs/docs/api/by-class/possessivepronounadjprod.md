# PossessivePronounAdjProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2621)


Possessive adjectives


**Superclass chain:** [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **PossessivePronounAdjProd**


<details><summary>Subclasses (12)</summary>

- [HerAdjProd](heradjprod.md)
- [possessiveAdjPhrase(her)](possessiveadjphrase%28her%29.md)
- [HisAdjProd](hisadjprod.md)
- [possessiveAdjPhrase(his)](possessiveadjphrase%28his%29.md)
- [ItsAdjProd](itsadjprod.md)
- [possessiveAdjPhrase(its)](possessiveadjphrase%28its%29.md)
- [MyAdjProd](myadjprod.md)
- [possessiveAdjPhrase(my)](possessiveadjphrase%28my%29.md)
- [TheirAdjProd](theiradjprod.md)
- [possessiveAdjPhrase(their)](possessiveadjphrase%28their%29.md)
- [YourAdjProd](youradjprod.md)
- [possessiveAdjPhrase(your)](possessiveadjphrase%28your%29.md)

</details>


## Properties


### `canBeAnaphor`

Defined in parser.t, line 2680

Can we be an anaphor? By default, we consider third-person possessive pronouns to be anaphoric, and others to be non-anaphoric. For example, in GIVE BOB MY BOOK, MY always refers to the speaker, so it's clearly not anaphoric within the sentence.


### `isPossessive` *(overridden)*

Defined in parser.t, line 2672

this is a possessive usage of the pronoun


## Inherited Properties


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`pronounType`](pronounprod.md#pronounType)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAnaphorAgreement(lst)`

Defined in parser.t, line 2691

Check agreement to a given anaphoric pronoun binding. The language module should override this for each pronoun type to ensure that the actual contents of the list agree in number and gender with this type of pronoun. If so, return true; if not, return nil. It's not an error or a ranking demerit if we don't agree; it just means that we'll fall back on the regular pronoun antecedent rather than trying to use an anaphoric binding.


### `checkAnaphoricBinding(resolver, results)` *(overridden)*

Defined in parser.t, line 2627

Possessive pronouns can refer to the earlier noun phrases of the same predicate, which is to say that they're anaphoric. For example, in GIVE BOB HIS BOOK, 'his' refers to Bob.


### `getOrigMainText`

Defined in parser.t, line 2697

By default, the "main text" of a possessive pronoun is the same as the actual token text. Languages can override this as needed>


## Inherited Methods


*From [PronounProd](pronounprod.md):* [`resolveNouns`](pronounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
