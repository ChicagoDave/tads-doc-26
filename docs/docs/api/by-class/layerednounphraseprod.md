# LayeredNounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1293)


Basic "layered" noun phrase production. It's often useful to define a grammar rule that simply defers to an underlying grammar rule; we make this simpler by defining this class that automatically delegates resolveNouns to the underlying noun phrase given by the property np_.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **LayeredNounPhraseProd**


<details><summary>Subclasses (15)</summary>

- [completeNounPhrase(main)](completenounphrase%28main%29.md)
- [completeNounPhraseWithoutAll(qualified)](completenounphrasewithoutall%28qualified%29.md)
- [detPluralNounPhrase(main)](detpluralnounphrase%28main%29.md)
- [detPluralOnlyNounPhrase(main)](detpluralonlynounphrase%28main%29.md)
- [indetPluralNounPhrase(basic)](indetpluralnounphrase%28basic%29.md)
- [indetPluralOnlyNounPhrase(basic)](indetpluralonlynounphrase%28basic%29.md)
- [indetSingularNounPhrase(basic)](indetsingularnounphrase%28basic%29.md)
- [nounPhrase(main)](nounphrase%28main%29.md)
- [pluralPhrase(main)](pluralphrase%28main%29.md)
- [possessiveAdjPhrase(npApostropheS)](possessiveadjphrase%28npapostrophes%29.md)
- [possessiveAdjPhrase(ppApostropheS)](possessiveadjphrase%28ppapostrophes%29.md)
- [possessiveNounPhrase(npApostropheS)](possessivenounphrase%28npapostrophes%29.md)
- [qualifiedNounPhrase(main)](qualifiednounphrase%28main%29.md)
- [qualifiedPluralNounPhrase(determiner)](qualifiedpluralnounphrase%28determiner%29.md)
- [singleNoun(normal)](singlenoun%28normal%29.md)

</details>


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1294


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
