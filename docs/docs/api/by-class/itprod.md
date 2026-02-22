# ItProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1502)


For simplicity, define subclasses of PronounProd for the basic set of pronouns found in most languages. Language-specific grammar definitions can choose to use these or not, and can add their own extra subclasses as needed for types of pronouns we don't define here.


**Superclass chain:** [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **ItProdSubclasses:** [completeNounPhraseWithoutAll(it)](completenounphrasewithoutall%28it%29.md)


## Properties


### `pronounType` *(overridden)*

Defined in parser.t, line 1503


## Inherited Properties


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`isPossessive`](pronounprod.md#isPossessive)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding), [`resolveNouns`](pronounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
