# ReflexivePronounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1531)


Third-person anaphoric reflexive pronouns. These refer to objects that appeared earlier in the sentence: "ask bob about himself."


**Superclass chain:** [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ReflexivePronounProdSubclasses:** [HerselfProd](herselfprod.md), [completeNounPhraseWithoutAll(herself)](completenounphrasewithoutall%28herself%29.md), [HimselfProd](himselfprod.md), [completeNounPhraseWithoutAll(himself)](completenounphrasewithoutall%28himself%29.md), [ItselfProd](itselfprod.md), [completeNounPhraseWithoutAll(itself)](completenounphrasewithoutall%28itself%29.md), [ThemselvesProd](themselvesprod.md), [completeNounPhraseWithoutAll(themselves)](completenounphrasewithoutall%28themselves%29.md)


## Inherited Properties


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`isPossessive`](pronounprod.md#isPossessive), [`pronounType`](pronounprod.md#pronounType)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAgreement(lst)`

Defined in parser.t, line 1591

Check that the binding we found for our reflexive pronoun agrees with the pronoun in gender, number, and anything else that it has to agree with. This must be defined by each concrete subclass. Note that language-specific subclasses can and *should* override this to test agreement for the local language's rules.


### `resolveNouns(resolver, results)` *(overridden)*

Defined in parser.t, line 1532


## Inherited Methods


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
