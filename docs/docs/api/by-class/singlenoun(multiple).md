# singleNoun(multiple)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5431)


A user could attempt to use a noun list with more than one entry (a "multi list") where a single noun is required. This is not a grammatical error, so we accept it grammatically; however, for disambiguation purposes we score it lower than a singleNoun production with only one noun phrase, and if we try to resolve it, we'll fail with an error.


**Superclass chain:** [SingleNounWithListProd](singlenounwithlistprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **singleNoun(multiple)**


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [SingleNounWithListProd](singlenounwithlistprod.md):* [`resolveNouns`](singlenounwithlistprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
