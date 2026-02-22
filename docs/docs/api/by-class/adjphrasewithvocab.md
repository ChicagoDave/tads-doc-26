# AdjPhraseWithVocab

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 6457)


An AdjPhraseWithVocab is an English-specific subclass of NounPhraseWithVocab, specifically for noun phrases that contain entirely adjectives.


**Superclass chain:** [NounPhraseWithVocab](nounphrasewithvocab.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **AdjPhraseWithVocabSubclasses:** [adjPhrase(adj)](adjphrase%28adj%29.md), [adjWord(adj)](adjword%28adj%29.md), [adjWord(adjAbbr)](adjword%28adjabbr%29.md), [adjWord(adjApostS)](adjword%28adjaposts%29.md), [literalAdjPhrase(literalAdj)](literaladjphrase%28literaladj%29.md), [literalAdjPhrase(number)](literaladjphrase%28number%29.md), [literalAdjPhrase(string)](literaladjphrase%28string%29.md)


## Properties


### `adjVocabProp`

Defined in en_us.t, line 6459

the property for the adjective literal - this is usually adj_


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `addNounMatchList(lst, resolver, results, extraFlags)`

Defined in en_us.t, line 6466

Add the vocabulary matches that we'd get if we were treating our adjective as a noun. This combines the noun interpretation with a list of matches we got for the adjective version.


## Inherited Methods


*From [NounPhraseWithVocab](nounphrasewithvocab.md):* [`combineWordMatches`](nounphrasewithvocab.md#combineWordMatches), [`combineWordMatchItems`](nounphrasewithvocab.md#combineWordMatchItems), [`dictMatchIsExact`](nounphrasewithvocab.md#dictMatchIsExact), [`dictMatchIsStronger`](nounphrasewithvocab.md#dictMatchIsStronger), [`filterDictMatches`](nounphrasewithvocab.md#filterDictMatches), [`getAdjustedTokens`](nounphrasewithvocab.md#getAdjustedTokens), [`getVocabMatchList`](nounphrasewithvocab.md#getVocabMatchList), [`getWordMatches`](nounphrasewithvocab.md#getWordMatches), [`inScopeMatches`](nounphrasewithvocab.md#inScopeMatches), [`intersectWordMatches`](nounphrasewithvocab.md#intersectWordMatches), [`resolveNouns`](nounphrasewithvocab.md#resolveNouns), [`resolveNounsMatchName`](nounphrasewithvocab.md#resolveNounsMatchName)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
