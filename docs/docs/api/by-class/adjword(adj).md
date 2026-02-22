# adjWord(adj)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 6664)


An adjective word. This can be either a simple 'adjective' vocabulary word, or it can be an 'adjApostS' vocabulary word plus a 's token.


**Superclass chain:** [AdjPhraseWithVocab](adjphrasewithvocab.md) > [NounPhraseWithVocab](nounphrasewithvocab.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **adjWord(adj)**


## Inherited Properties


*From [AdjPhraseWithVocab](adjphrasewithvocab.md):* [`adjVocabProp`](adjphrasewithvocab.md#adjVocabProp)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getAdjustedTokens` *(overridden)*

Defined in en_us.t, line 6672

return a list of objects in scope matching our adjective


### `getVocabMatchList(resolver, results, extraFlags)` *(overridden)*

Defined in en_us.t, line 6666

generate a list of resolved objects


## Inherited Methods


*From [AdjPhraseWithVocab](adjphrasewithvocab.md):* [`addNounMatchList`](adjphrasewithvocab.md#addNounMatchList)


*From [NounPhraseWithVocab](nounphrasewithvocab.md):* [`combineWordMatches`](nounphrasewithvocab.md#combineWordMatches), [`combineWordMatchItems`](nounphrasewithvocab.md#combineWordMatchItems), [`dictMatchIsExact`](nounphrasewithvocab.md#dictMatchIsExact), [`dictMatchIsStronger`](nounphrasewithvocab.md#dictMatchIsStronger), [`filterDictMatches`](nounphrasewithvocab.md#filterDictMatches), [`getWordMatches`](nounphrasewithvocab.md#getWordMatches), [`inScopeMatches`](nounphrasewithvocab.md#inScopeMatches), [`intersectWordMatches`](nounphrasewithvocab.md#intersectWordMatches), [`resolveNouns`](nounphrasewithvocab.md#resolveNouns), [`resolveNounsMatchName`](nounphrasewithvocab.md#resolveNounsMatchName)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
