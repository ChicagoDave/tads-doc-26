# PronounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1398)


Basic class for pronoun phrases. The specific pronouns are language-dependent; each instance should define its pronounType property to an appropriate PronounXxx constant.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **PronounProd**


<details><summary>Subclasses (47)</summary>

- [HerProd](herprod.md)
- [completeNounPhraseWithoutAll(her)](completenounphrasewithoutall%28her%29.md)
- [HimProd](himprod.md)
- [completeNounPhraseWithoutAll(him)](completenounphrasewithoutall%28him%29.md)
- [ItProd](itprod.md)
- [completeNounPhraseWithoutAll(it)](completenounphrasewithoutall%28it%29.md)
- [MeProd](meprod.md)
- [completeNounPhraseWithoutAll(me)](completenounphrasewithoutall%28me%29.md)
- [PossessivePronounAdjProd](possessivepronounadjprod.md)
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
- [PossessivePronounNounProd](possessivepronounnounprod.md)
- [HersNounProd](hersnounprod.md)
- [possessiveNounPhrase(hers)](possessivenounphrase%28hers%29.md)
- [HisNounProd](hisnounprod.md)
- [possessiveNounPhrase(his)](possessivenounphrase%28his%29.md)
- [ItsNounProd](itsnounprod.md)
- [possessiveNounPhrase(its)](possessivenounphrase%28its%29.md)
- [MineNounProd](minenounprod.md)
- [possessiveNounPhrase(mine)](possessivenounphrase%28mine%29.md)
- [TheirsNounProd](theirsnounprod.md)
- [possessiveNounPhrase(theirs)](possessivenounphrase%28theirs%29.md)
- [YoursNounProd](yoursnounprod.md)
- [possessiveNounPhrase(yours)](possessivenounphrase%28yours%29.md)
- [ReflexivePronounProd](reflexivepronounprod.md)
- [HerselfProd](herselfprod.md)
- [completeNounPhraseWithoutAll(herself)](completenounphrasewithoutall%28herself%29.md)
- [HimselfProd](himselfprod.md)
- [completeNounPhraseWithoutAll(himself)](completenounphrasewithoutall%28himself%29.md)
- [ItselfProd](itselfprod.md)
- [completeNounPhraseWithoutAll(itself)](completenounphrasewithoutall%28itself%29.md)
- [ThemselvesProd](themselvesprod.md)
- [completeNounPhraseWithoutAll(themselves)](completenounphrasewithoutall%28themselves%29.md)
- [ThemProd](themprod.md)
- [completeNounPhraseWithoutAll(them)](completenounphrasewithoutall%28them%29.md)
- [YouProd](youprod.md)
- [completeNounPhraseWithoutAll(yourself)](completenounphrasewithoutall%28yourself%29.md)

</details>


## Properties


### `isPlural`

Defined in parser.t, line 1481

Is this pronoun a singular or a plural? A pronoun like "it" or "he" is singular, because it refers to a single antecedent; "them" is plural. Language modules that define their own custom pronoun subclasses should override this as needed.


### `isPossessive`

Defined in parser.t, line 1473

is this a possessive usage?


### `pronounType`

Defined in parser.t, line 1470

our pronoun specifier - this must be set in each rule instance to one of the PronounXxx constants to specify which pronoun to use when resolving the pronoun phrase


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAnaphoricBinding(resolver, results)`

Defined in parser.t, line 1492

Check for an anaphoric binding. Returns a list (which is allowed to be empty) if this can refer back to an earlier noun phrase in the same command, nil if not. By default, we consider pronouns to be non-anaphoric, meaning they refer to something from a previous sentence, not something in this same sentence. In most languages, pronouns don't refer to objects in other noun phrases within the same predicate unless they're reflexive.


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1399


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
