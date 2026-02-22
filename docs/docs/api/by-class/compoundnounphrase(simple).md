# compoundNounPhrase(simple)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6084)


Compound noun phrase. This is one or more noun phrases connected with 'of', as in "piece of paper". The part after the 'of' is another compound noun phrase.


**Superclass chain:** [NounPhraseWithVocab](nounphrasewithvocab.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **compoundNounPhrase(simple)**


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getAdjustedTokens` *(overridden)*

Defined in en_us.t, line 6090


### `getVocabMatchList(resolver, results, extraFlags)` *(overridden)*

Defined in en_us.t, line 6086


## Inherited Methods


*From [NounPhraseWithVocab](nounphrasewithvocab.md):* [`combineWordMatches`](nounphrasewithvocab.md#combineWordMatches), [`combineWordMatchItems`](nounphrasewithvocab.md#combineWordMatchItems), [`dictMatchIsExact`](nounphrasewithvocab.md#dictMatchIsExact), [`dictMatchIsStronger`](nounphrasewithvocab.md#dictMatchIsStronger), [`filterDictMatches`](nounphrasewithvocab.md#filterDictMatches), [`getWordMatches`](nounphrasewithvocab.md#getWordMatches), [`inScopeMatches`](nounphrasewithvocab.md#inScopeMatches), [`intersectWordMatches`](nounphrasewithvocab.md#intersectWordMatches), [`resolveNouns`](nounphrasewithvocab.md#resolveNouns), [`resolveNounsMatchName`](nounphrasewithvocab.md#resolveNounsMatchName)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
