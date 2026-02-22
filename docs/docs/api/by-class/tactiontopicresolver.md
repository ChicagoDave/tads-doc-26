# TActionTopicResolver

*class* — defined in [action.t](../by-file/action.t.md) (line 6539)


A topic resolver specialized for TopicTActions - actions involving a topic and a physical object, such as CONSULT ABOUT. For these topics, we'll let the action handle the resolution.


**Superclass chain:** [TopicResolver](topicresolver.md) > [Resolver](resolver.md) > `object` > **TActionTopicResolver**


## Inherited Properties


*From [TopicResolver](topicresolver.md):* [`isGlobalScope`](topicresolver.md#isGlobalScope), [`qualifierResolver_`](topicresolver.md#qualifierResolver_), [`topicProd`](topicresolver.md#topicProd)


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`actor_`](resolver.md#actor_), [`equivs_`](resolver.md#equivs_), [`isSubResolver`](resolver.md#isSubResolver), [`issuer_`](resolver.md#issuer_), [`scope_`](resolver.md#scope_), [`whichMessageObject`](resolver.md#whichMessageObject), [`whichObject`](resolver.md#whichObject)


## Methods


### `resolveTopic(lst, requiredNum, np)` *(overridden)*

Defined in action.t, line 6540


## Inherited Methods


*From [TopicResolver](topicresolver.md):* [`construct`](topicresolver.md#construct), [`filterAmbiguousNounPhrase`](topicresolver.md#filterAmbiguousNounPhrase), [`filterPluralPhrase`](topicresolver.md#filterPluralPhrase), [`filterPossRank`](topicresolver.md#filterPossRank), [`getAll`](topicresolver.md#getAll), [`getAllDefaults`](topicresolver.md#getAllDefaults), [`getDefaultObject`](topicresolver.md#getDefaultObject), [`getPossessiveResolver`](topicresolver.md#getPossessiveResolver), [`getQualifierResolver`](topicresolver.md#getQualifierResolver), [`noMatch`](topicresolver.md#noMatch), [`noMatchPoss`](topicresolver.md#noMatchPoss), [`noVocabMatch`](topicresolver.md#noVocabMatch), [`objInPhysicalScope`](topicresolver.md#objInPhysicalScope), [`objInScope`](topicresolver.md#objInScope), [`packageTopicList`](topicresolver.md#packageTopicList), [`resetResolver`](topicresolver.md#resetResolver), [`resolveUnknownNounPhrase`](topicresolver.md#resolveUnknownNounPhrase)


*From [Resolver](resolver.md):* [`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`getAction`](resolver.md#getAction), [`getPronounDefault`](resolver.md#getPronounDefault), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)
