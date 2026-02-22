# completeNounPhraseWithoutAll(herself)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5640)


the result is required to be singular and masculine


**Superclass chain:** [HerselfProd](herselfprod.md) > [ReflexivePronounProd](reflexivepronounprod.md) > [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **completeNounPhraseWithoutAll(herself)**


## Inherited Properties


*From [HerselfProd](herselfprod.md):* [`pronounType`](herselfprod.md#pronounType)


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`isPossessive`](pronounprod.md#isPossessive)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAgreement(lst)` *(overridden)*

Defined in en_us.t, line 5642

check agreement of our binding


## Inherited Methods


*From [ReflexivePronounProd](reflexivepronounprod.md):* [`resolveNouns`](reflexivepronounprod.md#resolveNouns)


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
