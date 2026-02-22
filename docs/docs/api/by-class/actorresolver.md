# ActorResolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 882)


Actor Resolver. We use this to resolve the actor to whom a command is directed: the actor must be in scope for the player character.


**Superclass chain:** [Resolver](resolver.md) > `object` > **ActorResolver**


## Properties


### `whichMessageObject` *(overridden)*

Defined in resolver.t, line 1048


### `whichObject` *(overridden)*

Defined in resolver.t, line 1047

we resolve target actors


## Inherited Properties


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`actor_`](resolver.md#actor_), [`equivs_`](resolver.md#equivs_), [`isGlobalScope`](resolver.md#isGlobalScope), [`isSubResolver`](resolver.md#isSubResolver), [`issuer_`](resolver.md#issuer_), [`scope_`](resolver.md#scope_)


## Methods


### `construct(issuingActor)` *(overridden)*

Defined in resolver.t, line 883


### `filterAmbiguousNounPhrase(lst, requiredNum, np)` *(overridden)*

Defined in resolver.t, line 929

Filter an ambiguous list of objects. We will filter according to which objects are most logical as targets of commands.


### `filterPluralPhrase(lst, np)` *(overridden)*

Defined in resolver.t, line 976

Filter a plural list


### `getAll(np)` *(overridden)*

Defined in resolver.t, line 912

Get the "all" list - this is the list of objects that we should use when the object of the command is the special word "all". By default, we'll return everything in scope.


### `getAllDefaults` *(overridden)*

Defined in resolver.t, line 919

get the default object list


### `getDefaultObject(np)` *(overridden)*

Defined in resolver.t, line 987

get a default object


### `getRawPronounAntecedent(typ)` *(overridden)*

Defined in resolver.t, line 1004

Get a raw pronoun antecedent list. Since we are resolving the target actor, pronouns are relative to the issuing actor.


### `resolveUnknownNounPhrase(tokList)` *(overridden)*

Defined in resolver.t, line 994

resolve a noun phrase involving unknown words


## Inherited Methods


*From [Resolver](resolver.md):* [`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`filterPossRank`](resolver.md#filterPossRank), [`getAction`](resolver.md#getAction), [`getPossessiveResolver`](resolver.md#getPossessiveResolver), [`getPronounDefault`](resolver.md#getPronounDefault), [`getQualifierResolver`](resolver.md#getQualifierResolver), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`objInScope`](resolver.md#objInScope), [`resetResolver`](resolver.md#resetResolver), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)
