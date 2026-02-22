# AmbigResponseKeeper

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1974)


Mix-in class for noun phrase productions that use ResolveResults.ambiguousNounPhrase(). This mix-in provides the methods that ambiguousNounPhrase() uses to keep track of past responses to the disambiguation question.


**Superclass chain:** `object` > **AmbigResponseKeeper**


<details><summary>Subclasses (30)</summary>

- [DefiniteNounProd](definitenounprod.md)
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
- [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md)
- [BothPluralProd](bothpluralprod.md)
- [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md)
- [explicitDetPluralNounPhrase(definiteNumber)](explicitdetpluralnounphrase%28definitenumber%29.md)
- [explicitDetPluralOnlyNounPhrase(definiteNumber)](explicitdetpluralonlynounphrase%28definitenumber%29.md)
- [qualifiedPluralNounPhrase(allNum)](qualifiedpluralnounphrase%28allnum%29.md)

</details>


## Properties


### `ambigResponses_`

Defined in parser.t, line 1988

our list of saved interactive disambiguation responses


## Methods


### `addAmbigResponse(resp)`

Defined in parser.t, line 1975


### `getAmbigResponses`

Defined in parser.t, line 1981

add an ambiguous response to our list
