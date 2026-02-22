# IobjResolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 783)


Basic resolver for indirect objects


**Superclass chain:** [Resolver](resolver.md) > `object` > **IobjResolver**


## Properties


### `whichMessageObject` *(overridden)*

Defined in resolver.t, line 788


### `whichObject` *(overridden)*

Defined in resolver.t, line 787

we resolve indirect objects for message generation purposes


## Inherited Properties


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`actor_`](resolver.md#actor_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`issuer_`](resolver.md#issuer_), [`scope_`](resolver.md#scope_)


## Methods


### `filterAmbiguousNounPhrase(lst, requiredNum, np)` *(overridden)*

Defined in resolver.t, line 812

filter an ambiguous noun phrase


### `filterPluralPhrase(lst, np)` *(overridden)*

Defined in resolver.t, line 823

Filter a plural phrase to reduce the set to the logical subset, if possible. If there is no logical subset, simply return the original set.


### `getAll(np)` *(overridden)*

Defined in resolver.t, line 791

resolve 'all' for the indirect object


### `getAllDefaults` *(overridden)*

Defined in resolver.t, line 802

get all possible default objects


### `getDefaultObject(np)` *(overridden)*

Defined in resolver.t, line 833

Get the default object or objects for this phrase. Since we resolve indirect objects, we'll ask the action for a default indirect object.


## Inherited Methods


<details><summary>From [Resolver](resolver.md) (21)</summary>

[`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`construct`](resolver.md#construct), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`resolveUnknownNounPhrase`](resolver.md#resolveUnknownNounPhrase), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)

</details>
