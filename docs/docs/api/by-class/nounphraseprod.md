# NounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 1205)


Basic noun phrase production class.


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **NounPhraseProd**


<details><summary>Subclasses (173)</summary>

- [ButProd](butprod.md)
- [EverythingButProd](everythingbutprod.md)
- [terminalNounPhrase(allBut)](terminalnounphrase%28allbut%29.md)
- [IndefiniteNounButProd](indefinitenounbutprod.md)
- [terminalNounPhrase(anyBut)](terminalnounphrase%28anybut%29.md)
- [ListButProd](listbutprod.md)
- [terminalNounPhrase(pluralExcept)](terminalnounphrase%28pluralexcept%29.md)
- [completeNounPhrase(miscPrep)](completenounphrase%28miscprep%29.md)
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
- [EmptyNounPhraseProd](emptynounphraseprod.md)
- [ImpliedActorNounPhraseProd](impliedactornounphraseprod.md)
- [nounList(empty)](nounlist%28empty%29.md)
- [singleNoun(empty)](singlenoun%28empty%29.md)
- [IndefiniteNounProd](indefinitenounprod.md)
- [ArbitraryNounProd](arbitrarynounprod.md)
- [qualifiedSingularNounPhrase(anyPlural)](qualifiedsingularnounphrase%28anyplural%29.md)
- [qualifiedSingularNounPhrase(arbitrary)](qualifiedsingularnounphrase%28arbitrary%29.md)
- [qualifiedSingularNounPhrase(indefinite)](qualifiedsingularnounphrase%28indefinite%29.md)
- [LayeredNounPhraseProd](layerednounphraseprod.md)
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
- [NounPhraseWithVocab](nounphrasewithvocab.md)
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
- [PluralProd](pluralprod.md)
- [AllPluralProd](allpluralprod.md)
- [explicitDetPluralOnlyNounPhrase(definite)](explicitdetpluralonlynounphrase%28definite%29.md)
- [qualifiedPluralNounPhrase(all)](qualifiedpluralnounphrase%28all%29.md)
- [DefinitePluralProd](definitepluralprod.md)
- [explicitDetPluralNounPhrase(definite)](explicitdetpluralnounphrase%28definite%29.md)
- [implicitDetPluralOnlyNounPhrase(main)](implicitdetpluralonlynounphrase%28main%29.md)
- [QuantifiedPluralProd](quantifiedpluralprod.md)
- [ExactQuantifiedPluralProd](exactquantifiedpluralprod.md)
- [BothPluralProd](bothpluralprod.md)
- [qualifiedPluralNounPhrase(both)](qualifiedpluralnounphrase%28both%29.md)
- [explicitDetPluralNounPhrase(definiteNumber)](explicitdetpluralnounphrase%28definitenumber%29.md)
- [explicitDetPluralOnlyNounPhrase(definiteNumber)](explicitdetpluralonlynounphrase%28definitenumber%29.md)
- [qualifiedPluralNounPhrase(allNum)](qualifiedpluralnounphrase%28allnum%29.md)
- [qualifiedPluralNounPhrase(anyNum)](qualifiedpluralnounphrase%28anynum%29.md)
- [PronounProd](pronounprod.md)
- [HerProd](herprod.md)
- [completeNounPhraseWithoutAll(her)](completenounphrasewithoutall%28her%29.md)
- [HimProd](himprod.md)
- [completeNounPhraseWithoutAll(him)](completenounphrasewithoutall%28him%29.md)
- [ItProd](itprod.md)
- [completeNounPhraseWithoutAll(it)](completenounphrasewithoutall%28it%29.md)
- [MeProd](meprod.md)
- [completeNounPhraseWithoutAll(me)](completenounphrasewithoutall%28me%29.md)
- [PossessivePronounAdjProd](possessivepronounadjprod.md)
- [HerAdjProd](heradjprod.md)
- [possessiveAdjPhrase(her)](possessiveadjphrase%28her%29.md)
- [HisAdjProd](hisadjprod.md)
- [possessiveAdjPhrase(his)](possessiveadjphrase%28his%29.md)
- [ItsAdjProd](itsadjprod.md)
- [possessiveAdjPhrase(its)](possessiveadjphrase%28its%29.md)
- [MyAdjProd](myadjprod.md)
- [possessiveAdjPhrase(my)](possessiveadjphrase%28my%29.md)
- [TheirAdjProd](theiradjprod.md)
- [possessiveAdjPhrase(their)](possessiveadjphrase%28their%29.md)
- [YourAdjProd](youradjprod.md)
- [possessiveAdjPhrase(your)](possessiveadjphrase%28your%29.md)
- [PossessivePronounNounProd](possessivepronounnounprod.md)
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
- [ReflexivePronounProd](reflexivepronounprod.md)
- [HerselfProd](herselfprod.md)
- [completeNounPhraseWithoutAll(herself)](completenounphrasewithoutall%28herself%29.md)
- [HimselfProd](himselfprod.md)
- [completeNounPhraseWithoutAll(himself)](completenounphrasewithoutall%28himself%29.md)
- [ItselfProd](itselfprod.md)
- [completeNounPhraseWithoutAll(itself)](completenounphrasewithoutall%28itself%29.md)
- [ThemselvesProd](themselvesprod.md)
- [completeNounPhraseWithoutAll(themselves)](completenounphrasewithoutall%28themselves%29.md)
- [ThemProd](themprod.md)
- [completeNounPhraseWithoutAll(them)](completenounphrasewithoutall%28them%29.md)
- [YouProd](youprod.md)
- [completeNounPhraseWithoutAll(yourself)](completenounphrasewithoutall%28yourself%29.md)
- [SingleNounProd](singlenounprod.md)
- [PrepSingleNounProd](prepsinglenounprod.md)
- [atSingleNoun(main)](atsinglenoun%28main%29.md)
- [forSingleNoun(main)](forsinglenoun%28main%29.md)
- [fromSingleNoun(main)](fromsinglenoun%28main%29.md)
- [inSingleNoun(main)](insinglenoun%28main%29.md)
- [onSingleNoun(main)](onsinglenoun%28main%29.md)
- [outOfSingleNoun(main)](outofsinglenoun%28main%29.md)
- [throughSingleNoun(main)](throughsinglenoun%28main%29.md)
- [toSingleNoun(main)](tosinglenoun%28main%29.md)
- [withSingleNoun(main)](withsinglenoun%28main%29.md)
- [singleNounOnly(main)](singlenounonly%28main%29.md)
- [TopicProd](topicprod.md)
- [EmptyTopicPhraseProd](emptytopicphraseprod.md)
- [PrepSingleTopicProd](prepsingletopicprod.md)
- [aboutTopicPhrase(main)](abouttopicphrase%28main%29.md)
- [topicPhrase(main)](topicphrase%28main%29.md)
- [topicPhrase(misc)](topicphrase%28misc%29.md)
- [SingleNounWithListProd](singlenounwithlistprod.md)
- [singleNoun(multiple)](singlenoun%28multiple%29.md)

</details>


## Properties


### `filterForCollectives`

Defined in parser.t, line 1213

Determine whether this kind of noun phrase prefers to keep a collective or the collective's individuals when filtering. If this is true, we'll keep a collective and discard its individuals when filtering a resolution list; otherwise, we'll drop the collective and keep the individuals.


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `filterTruncations(lst, resolver)`

Defined in parser.t, line 1248

Filter a match list of results for truncated matches. If we have a mix of truncated matches and exact matches, we'll keep only the exact matches. If we have only truncated matches, though, we'll return the list unchanged, as we don't have a better offer going.


### `getVerifyKeepers(results)`

Defined in parser.t, line 1227

Filter a "verify" result list for the results we'd like to keep in the final resolution of the noun phrase. This is called after we've run through the verification process on the list of candidate matches, so 'lst' is a list of ResolveInfo objects, sorted in descending order of logicalness.


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
