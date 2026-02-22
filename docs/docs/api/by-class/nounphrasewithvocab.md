# NounPhraseWithVocab

*class* — defined in [parser.t](../by-file/parser.t.md) (line 3578)


Noun phrase with vocabulary resolution. This is a base class for the various noun phrases that match adjective, noun, and plural tokens. This class provides dictionary resolution of a vocabulary word into a list of objects.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **NounPhraseWithVocab**


<details><summary>Subclasses (32)</summary>

- [adjPhrase(adjAdj)](adjphrase%28adjadj%29.md)
- [AdjPhraseWithVocab](adjphrasewithvocab.md)
- [adjPhrase(adj)](adjphrase%28adj%29.md)
- [adjWord(adj)](adjword%28adj%29.md)
- [adjWord(adjAbbr)](adjword%28adjabbr%29.md)
- [adjWord(adjApostS)](adjword%28adjaposts%29.md)
- [literalAdjPhrase(literalAdj)](literaladjphrase%28literaladj%29.md)
- [literalAdjPhrase(number)](literaladjphrase%28number%29.md)
- [literalAdjPhrase(string)](literaladjphrase%28string%29.md)
- [compoundNounPhrase(of)](compoundnounphrase%28of%29.md)
- [compoundNounPhrase(simple)](compoundnounphrase%28simple%29.md)
- [compoundPluralPhrase(of)](compoundpluralphrase%28of%29.md)
- [compoundPluralPhrase(simple)](compoundpluralphrase%28simple%29.md)
- [miscWordList(list)](miscwordlist%28list%29.md)
- [miscWordList(wordOrNumber)](miscwordlist%28wordornumber%29.md)
- [NounWordProd](nounwordprod.md)
- [nounWord(noun)](nounword%28noun%29.md)
- [nounWord(nounAbbr)](nounword%28nounabbr%29.md)
- [simpleNounPhrase(adj)](simplenounphrase%28adj%29.md)
- [simpleNounPhrase(adjAndOne)](simplenounphrase%28adjandone%29.md)
- [simpleNounPhrase(adjNP)](simplenounphrase%28adjnp%29.md)
- [simpleNounPhrase(empty)](simplenounphrase%28empty%29.md)
- [simpleNounPhrase(misc)](simplenounphrase%28misc%29.md)
- [simpleNounPhrase(noun)](simplenounphrase%28noun%29.md)
- [simpleNounPhrase(nounAndNumber)](simplenounphrase%28nounandnumber%29.md)
- [simpleNounPhrase(number)](simplenounphrase%28number%29.md)
- [simpleNounPhrase(numberAndNoun)](simplenounphrase%28numberandnoun%29.md)
- [simplePluralPhrase(adjAndOnes)](simplepluralphrase%28adjandones%29.md)
- [simplePluralPhrase(empty)](simplepluralphrase%28empty%29.md)
- [simplePluralPhrase(misc)](simplepluralphrase%28misc%29.md)
- [simplePluralPhrase(plural)](simplepluralphrase%28plural%29.md)
- [simplePluralPhrase(poundNum)](simplepluralphrase%28poundnum%29.md)

</details>


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `combineWordMatches(aLst, bLst)`

Defined in parser.t, line 3607

Combine two word match lists. This simply adds each entry from the second list that doesn't already have a corresponding entry in the first list, returning the combined list.


### `combineWordMatchItems(a, b)`

Defined in parser.t, line 3656

Combine the given word match entries. We'll merge the flags of the two entries to produce a single merged entry in 'a'.


### `dictMatchIsExact(flags)`

Defined in parser.t, line 3769

Check a dictionary match's string comparator flags to see if the match is "exact." The exact meaning of "exact" is dependent on the language's lexical rules; this generic base version considers a match to be exact if it doesn't have any string comparator flags other than the base "matched" flag and the case-fold flag. This should be suitable for most languages, as (1) case folding usually doesn't improve match strength, and (2) any additional comparator flags usually indicate some kind of inexact match status.


### `dictMatchIsStronger(flags1, flags2)`

Defined in parser.t, line 3795

Compare two dictionary matches for the same object and determine if the first one is stronger than the second. Both are for the same object; the only difference is the string comparator flags.


### `filterDictMatches(lst)`

Defined in parser.t, line 3702

Filter a dictionary match list. This is called to clean up the raw match list returned from looking up a vocabulary word in the dictionary.


### `getAdjustedTokens`

Defined in parser.t, line 4005

Each subclass must override getAdjustedTokens() to provide the appropriate set of tokens used to match the object. This is usually simply the original set of tokens, but in some cases it may differ; for example, spelled-out numbers normally adjust to the numeral form of the number.


### `getVocabMatchList(resolver, results, extraFlags)`

Defined in parser.t, line 4014

Get the vocabulary match list. This is simply the set of objects that match all of the words in the noun phrase. Each rule subclass must override this to return an appropriate list. Note that subclasses should use getWordMatches() and intersectWordMatches() to build the list.


### `getWordMatches(tok, partOfSpeech, resolver, flags, truncFlags)`

Defined in parser.t, line 3585

Get a list of the matches in the main dictionary for the given token as the given part of speech (&noun, &adjective, &plural, or others as appropriate for the local language) that are in scope according to the resolver.


### `inScopeMatches(dictionaryMatches, flags, truncFlags, resolver)`

Defined in parser.t, line 3832

Given a list of dictionary matches to a given word, construct a list of ResolveInfo objects for the matches that are in scope. For regular resolution, "in scope" means the resolver thinks the object is in scope.


### `intersectWordMatches(tok, partOfSpeech, resolver, flags, truncFlags, lst)`

Defined in parser.t, line 3811

Get a list of the matches in the main dictionary for the given token, intersecting the resulting list with the given list.


### `resolveNouns(resolver, results)`

Defined in parser.t, line 3882

Resolve the objects.


### `resolveNounsMatchName(results, resolver, matchList)`

Defined in parser.t, line 3912

Run a set of resolved objects through matchName() or a similar routine. Returns the filtered results.


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
