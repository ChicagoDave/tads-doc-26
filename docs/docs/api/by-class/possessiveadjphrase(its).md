# possessiveAdjPhrase(its)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6723)


Possessive phrase. This is a noun phrase expressing ownership of another object.


**Superclass chain:** [ItsAdjProd](itsadjprod.md) > [PossessivePronounAdjProd](possessivepronounadjprod.md) > [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **possessiveAdjPhrase(its)**


## Inherited Properties


*From [ItsAdjProd](itsadjprod.md):* [`pronounType`](itsadjprod.md#pronounType)


*From [PossessivePronounAdjProd](possessivepronounadjprod.md):* [`canBeAnaphor`](possessivepronounadjprod.md#canBeAnaphor), [`isPossessive`](possessivepronounadjprod.md#isPossessive)


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAnaphorAgreement(lst)` *(overridden)*

Defined in en_us.t, line 6725

we only agree with a singular ungendered noun


## Inherited Methods


*From [PossessivePronounAdjProd](possessivepronounadjprod.md):* [`checkAnaphoricBinding`](possessivepronounadjprod.md#checkAnaphoricBinding), [`getOrigMainText`](possessivepronounadjprod.md#getOrigMainText)


*From [PronounProd](pronounprod.md):* [`resolveNouns`](pronounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
