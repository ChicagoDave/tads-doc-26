# TopicResolver

*class* — defined in [action.t](../by-file/action.t.md) (line 6332)


Topic Resolver


**Superclass chain:** [Resolver](resolver.md) > `object` > **TopicResolverSubclasses:** [ConvTopicResolver](convtopicresolver.md), [TActionTopicResolver](tactiontopicresolver.md)


## Properties


### `isGlobalScope` *(overridden)*

Defined in action.t, line 6405

our scope is global, because we don't limit the scope to the physical senses


### `qualifierResolver_`

Defined in action.t, line 6385

our qualifier resolver


### `topicProd`

Defined in action.t, line 6531

the production match tree for the topic phrase we're resolving


## Inherited Properties


*From [Resolver](resolver.md):* [`action_`](resolver.md#action_), [`actor_`](resolver.md#actor_), [`equivs_`](resolver.md#equivs_), [`isSubResolver`](resolver.md#isSubResolver), [`issuer_`](resolver.md#issuer_), [`scope_`](resolver.md#scope_), [`whichMessageObject`](resolver.md#whichMessageObject), [`whichObject`](resolver.md#whichObject)


## Methods


### `construct(action, issuingActor, targetActor, prod, which, qualifierResolver)` *(overridden)*

Defined in action.t, line 6333


### `filterAmbiguousNounPhrase(lst, requiredNum, np)` *(overridden)*

Defined in action.t, line 6459

Filter an ambiguous noun list.


### `filterPluralPhrase(lst, np)` *(overridden)*

Defined in action.t, line 6503

filter a plural


### `filterPossRank(lst, num)` *(overridden)*

Defined in action.t, line 6431

Filter an ambiguous noun phrase list using the strength of possessive qualification, if any. For a topic phrase, we want to keep all of the possibilities.


### `getAll(np)` *(overridden)*

Defined in action.t, line 6527

we don't allow ALL or provide defaults


### `getAllDefaults` *(overridden)*

Defined in action.t, line 6528


### `getDefaultObject(np)` *(overridden)*

Defined in action.t, line 6515

get a default object


### `getPossessiveResolver` *(overridden)*

Defined in action.t, line 6389


### `getQualifierResolver` *(overridden)*

Defined in action.t, line 6388

get our qualifier resolver


### `noMatch(action, txt)`

Defined in action.t, line 6523


### `noMatchPoss(action, txt)`

Defined in action.t, line 6524


### `noVocabMatch(action, txt)`

Defined in action.t, line 6522

it's fine not to match a topic phrase


### `objInPhysicalScope(obj)`

Defined in action.t, line 6417

Determine if an object is in physical scope. We'll accept anything that's in physical scope, and we'll also accept any topic object that the actor knows about.


### `objInScope(obj)` *(overridden)*

Defined in action.t, line 6399

Determine if the object is in scope. We consider any vocabulary match to be in scope for the purposes of a topic phrase, since the subject matter of topics is mere references to things, not the things themselves; we can, for example, ASK ABOUT things that aren't physically present, or even about completely abstract ideas.


### `packageTopicList(lst, match)`

Defined in action.t, line 6365

package a resolved topic list - if it's not already represented as a ResolvedTopic object, we'll apply that wrapping


### `resetResolver` *(overridden)*

Defined in action.t, line 6352

remember the resolver for qualifier phrases


### `resolveTopic(lst, requiredNum, np)`

Defined in action.t, line 6478

Resolve the topic phrase. This returns a ResolvedTopic object encapsulating the resolution of the phrase.


### `resolveUnknownNounPhrase(tokList)` *(overridden)*

Defined in action.t, line 6489

Resolve an unknown phrase. We allow unknown words to be used in topics; we simply return a ResolvedTopic that doesn't refer to any simulation objects at all.


## Inherited Methods


*From [Resolver](resolver.md):* [`allowAll`](resolver.md#allowAll), [`cacheScopeList`](resolver.md#cacheScopeList), [`filterAll`](resolver.md#filterAll), [`filterAmbiguousEquivalents`](resolver.md#filterAmbiguousEquivalents), [`getAction`](resolver.md#getAction), [`getPronounDefault`](resolver.md#getPronounDefault), [`getRawPronounAntecedent`](resolver.md#getRawPronounAntecedent), [`getReflexiveBinding`](resolver.md#getReflexiveBinding), [`getScopeList`](resolver.md#getScopeList), [`getTargetActor`](resolver.md#getTargetActor), [`matchName`](resolver.md#matchName), [`resolvePronounAntecedent`](resolver.md#resolvePronounAntecedent), [`selectIndefinite`](resolver.md#selectIndefinite), [`withGlobals`](resolver.md#withGlobals)
