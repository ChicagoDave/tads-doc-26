# PossessivePronounNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 2729)


Possessive nouns


**Superclass chain:** [PronounProd](pronounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **PossessivePronounNounProd**


<details><summary>Subclasses (12)</summary>

- [HersNounProd](hersnounprod.md)
- [possessiveNounPhrase(hers)](possessivenounphrase%28hers%29.md)
- [HisNounProd](hisnounprod.md)
- [possessiveNounPhrase(his)](possessivenounphrase%28his%29.md)
- [ItsNounProd](itsnounprod.md)
- [possessiveNounPhrase(its)](possessivenounphrase%28its%29.md)
- [MineNounProd](minenounprod.md)
- [possessiveNounPhrase(mine)](possessivenounphrase%28mine%29.md)
- [TheirsNounProd](theirsnounprod.md)
- [possessiveNounPhrase(theirs)](possessivenounphrase%28theirs%29.md)
- [YoursNounProd](yoursnounprod.md)
- [possessiveNounPhrase(yours)](possessivenounphrase%28yours%29.md)

</details>


## Properties


### `isPossessive` *(overridden)*

Defined in parser.t, line 2731

this is a possessive usage of the pronoun


## Inherited Properties


*From [PronounProd](pronounprod.md):* [`isPlural`](pronounprod.md#isPlural), [`pronounType`](pronounprod.md#pronounType)


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [PronounProd](pronounprod.md):* [`checkAnaphoricBinding`](pronounprod.md#checkAnaphoricBinding), [`resolveNouns`](pronounprod.md#resolveNouns)


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
