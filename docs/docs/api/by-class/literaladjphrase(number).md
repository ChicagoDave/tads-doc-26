# literalAdjPhrase(number)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6482)


A "literal adjective" phrase is a number or string used as an adjective.


**Superclass chain:** [AdjPhraseWithVocab](adjphrasewithvocab.md) > [NounPhraseWithVocab](nounphrasewithvocab.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **literalAdjPhrase(number)**


## Properties


### `adj_`

Defined in en_us.t, line 6486


## Inherited Properties


*From [AdjPhraseWithVocab](adjphrasewithvocab.md):* [`adjVocabProp`](adjphrasewithvocab.md#adjVocabProp)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getAdjustedTokens` *(overridden)*

Defined in en_us.t, line 6505

return the combined lists


### `getVocabMatchList(resolver, results, extraFlags)` *(overridden)*

Defined in en_us.t, line 6487


## Inherited Methods


*From [AdjPhraseWithVocab](adjphrasewithvocab.md):* [`addNounMatchList`](adjphrasewithvocab.md#addNounMatchList)


*From [NounPhraseWithVocab](nounphrasewithvocab.md):* [`combineWordMatches`](nounphrasewithvocab.md#combineWordMatches), [`combineWordMatchItems`](nounphrasewithvocab.md#combineWordMatchItems), [`dictMatchIsExact`](nounphrasewithvocab.md#dictMatchIsExact), [`dictMatchIsStronger`](nounphrasewithvocab.md#dictMatchIsStronger), [`filterDictMatches`](nounphrasewithvocab.md#filterDictMatches), [`getWordMatches`](nounphrasewithvocab.md#getWordMatches), [`inScopeMatches`](nounphrasewithvocab.md#inScopeMatches), [`intersectWordMatches`](nounphrasewithvocab.md#intersectWordMatches), [`resolveNouns`](nounphrasewithvocab.md#resolveNouns), [`resolveNounsMatchName`](nounphrasewithvocab.md#resolveNounsMatchName)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
