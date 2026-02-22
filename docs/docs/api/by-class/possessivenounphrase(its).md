# possessiveNounPhrase(its)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6801)


Possessive noun phrases. These are similar to possessive phrases, but are stand-alone phrases that can act as nouns rather than as qualifiers for other noun phrases. For example, for a first-person player character, "mine" would be a possessive noun phrase referring to an object owned by the player character.


**Superclass chain:** [ItsNounProd](itsnounprod.md) > [PossessivePronounNounProd](possessivepronounnounprod.md) > [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **possessiveNounPhrase(its)**


## Inherited Properties


*From [ItsNounProd](itsnounprod.md):* [`pronounType`](itsnounprod.md#pronounType)


*From [PossessivePronounNounProd](possessivepronounnounprod.md):* [`isPossessive`](possessivepronounnounprod.md#isPossessive)


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding), [`resolveNouns`](pronounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
