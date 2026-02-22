# DefiniteNounProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1996)


Base class for noun phrase productions with definite articles.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > [AmbigResponseKeeper](ambigresponsekeeper.md) > **DefiniteNounProd**


<details><summary>Subclasses (23)</summary>

- [BasicPossessiveProd](basicpossessiveprod.md)
- [ButPossessiveProd](butpossessiveprod.md)
- [exceptNounPhrase(singlePossessive)](exceptnounphrase%28singlepossessive%29.md)
- [DisambigPossessiveProd](disambigpossessiveprod.md)
- [disambigListItem(possessive)](disambiglistitem%28possessive%29.md)
- [PossessiveNounProd](possessivenounprod.md)
- [qualifiedSingularNounPhrase(possessive)](qualifiedsingularnounphrase%28possessive%29.md)
- [PossessivePluralProd](possessivepluralprod.md)
- [explicitDetPluralNounPhrase(possessive)](explicitdetpluralnounphrase%28possessive%29.md)
- [explicitDetPluralOnlyNounPhrase(possessive)](explicitdetpluralonlynounphrase%28possessive%29.md)
- [ContainerNounPhraseProd](containernounphraseprod.md)
- [indetPluralNounPhrase(locational)](indetpluralnounphrase%28locational%29.md)
- [indetPluralOnlyNounPhrase(locational)](indetpluralonlynounphrase%28locational%29.md)
- [indetSingularNounPhrase(locational)](indetsingularnounphrase%28locational%29.md)
- [PreResolvedAmbigProd](preresolvedambigprod.md)
- [qualifiedSingularNounPhrase(definite)](qualifiedsingularnounphrase%28definite%29.md)
- [VagueContainerNounPhraseProd](vaguecontainernounphraseprod.md)
- [AllInContainerNounPhraseProd](allincontainernounphraseprod.md)
- [qualifiedPluralNounPhrase(theOnesIn)](qualifiedpluralnounphrase%28theonesin%29.md)
- [VagueContainerDefiniteNounPhraseProd](vaguecontainerdefinitenounphraseprod.md)
- [qualifiedSingularNounPhrase(theOneIn)](qualifiedsingularnounphrase%28theonein%29.md)
- [VagueContainerIndefiniteNounPhraseProd](vaguecontainerindefinitenounphraseprod.md)
- [qualifiedSingularNounPhrase(anyOneIn)](qualifiedsingularnounphrase%28anyonein%29.md)

</details>


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`ambigResponses_`](ambigresponsekeeper.md#ambigResponses_)


## Methods


### `reduceDefinite(lst, resolver, results)`

Defined in parser.t, line 2086

Do any additional subclass-specific filtering to further reduce the list before we decide whether or not we have sufficient specificity. We call this just before deciding whether or not to prompt for more information ("which book do you mean...?"). By default, this simply returns the same list unchanged; subclasses that have some further way of narrowing down the options can use this opportunity to apply that extra narrowing.


### `resolveDefinite(asker, origText, lst, responseKeeper, resolver, results)`

Defined in parser.t, line 2008

Resolve an underlying phrase using definite noun phrase rules.


### `resolveNouns(resolver, results)`

Defined in parser.t, line 1997


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)


*From [AmbigResponseKeeper](ambigresponsekeeper.md):* [`addAmbigResponse`](ambigresponsekeeper.md#addAmbigResponse), [`getAmbigResponses`](ambigresponsekeeper.md#getAmbigResponses)
