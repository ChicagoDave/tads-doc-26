# TopicQualifierResolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 845)


Basic topic qualifier resolver. This can be used to resolve qualifier phrases (such as possessives or locationals) within topic phrases.


**Superclass chain:** [Resolver](resolver.md) > `object` > **TopicQualifierResolver**


## Inherited Properties


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`actor_`](resolver.md#actor_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`issuer_`](resolver.md#issuer_), [`scope_`](resolver.md#scope_), [`whichMessageObject`](resolver.md#whichMessageObject), [`whichObject`](resolver.md#whichObject)


## Methods


### `filterAmbiguousNounPhrase(lst, requiredNum, np)` *(overridden)*

Defined in resolver.t, line 858

we don't need defaults for a qualifier


### `filterPluralPhrase(lst, np)` *(overridden)*

Defined in resolver.t, line 864

we have no basis for any filtering; return the list unchanged


### `getAll(np)` *(overridden)*

Defined in resolver.t, line 846


### `getAllDefaults` *(overridden)*

Defined in resolver.t, line 852

'all' doesn't make sense as a qualifier; return an empty list


### `getDefaultObject(np)` *(overridden)*

Defined in resolver.t, line 870

we have no basis for any filtering


## Inherited Methods


<details><summary>From [Resolver](resolver.md) (21)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`construct`](resolver.md#construct), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
