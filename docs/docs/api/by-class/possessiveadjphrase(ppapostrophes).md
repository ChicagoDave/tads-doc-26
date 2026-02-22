# possessiveAdjPhrase(ppApostropheS)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6763)


return just the basic noun phrase part


**Superclass chain:** [LayeredNounPhraseProd](layerednounphraseprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **possessiveAdjPhrase(ppApostropheS)**


## Properties


### `isPluralPossessive`

Defined in en_us.t, line 6785

the possessive phrase is plural


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getOrigMainText`

Defined in en_us.t, line 6769

get the original text without the "'s" suffix


### `resolveNouns(resolver, results)` *(overridden)*

Defined in en_us.t, line 6775

return just the basic noun phrase part


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
