# completeNounPhraseWithoutAll(himself)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5631)


For 'themselves', allow anything; we could balk at this matching a single object that isn't a mass noun, but that would be overly picky, and it would probably reject at least a few things that really ought to be acceptable. Besides, 'them' is the closest thing English has to a singular gender-neutral pronoun, and some people intentionally use it as such.


**Superclass chain:** [HimselfProd](himselfprod.md) > [ReflexivePronounProd](reflexivepronounprod.md) > [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **completeNounPhraseWithoutAll(himself)**


## Inherited Properties


*From [HimselfProd](himselfprod.md):* [`pronounType`](himselfprod.md#pronounType)


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`isPossessive`](pronounprod.md#isPossessive)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `checkAgreement(lst)` *(overridden)*

Defined in en_us.t, line 5633

check agreement of our binding


## Inherited Methods


*From [ReflexivePronounProd](reflexivepronounprod.md):* [`resolveNouns`](reflexivepronounprod.md#resolveNouns)


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
