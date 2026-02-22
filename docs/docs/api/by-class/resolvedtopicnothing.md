# resolvedTopicNothing

*object* — defined in [action.t](../by-file/action.t.md) (line 6319)


A special topic for "nothing." It's occasionally useful to be able to construct a TopicTAction with an empty topic phrase. For the topic phrase to be well-formed, we need a valid ResolvedTopic object, even though it won't refer to anything.


**Superclass chain:** [ResolvedTopic](resolvedtopic.md) > `object` > **resolvedTopicNothing**


## Properties


### `inScopeList` *(overridden)*

Defined in action.t, line 6320


### `likelyList` *(overridden)*

Defined in action.t, line 6321


### `otherList` *(overridden)*

Defined in action.t, line 6322


## Inherited Properties


*From [ResolvedTopic](resolvedtopic.md):* [`canMatchLiterally`](resolvedtopic.md#canMatchLiterally), [`resInfoTab`](resolvedtopic.md#resInfoTab), [`topicProd`](resolvedtopic.md#topicProd)


## Methods


### `getTopicText` *(overridden)*

Defined in action.t, line 6324


### `getTopicTokens` *(overridden)*

Defined in action.t, line 6325


### `getTopicWords` *(overridden)*

Defined in action.t, line 6326


## Inherited Methods


*From [ResolvedTopic](resolvedtopic.md):* [`canMatchObject`](resolvedtopic.md#canMatchObject), [`construct`](resolvedtopic.md#construct), [`getBestMatch`](resolvedtopic.md#getBestMatch), [`getResolveInfo`](resolvedtopic.md#getResolveInfo), [`wrapActionObject`](resolvedtopic.md#wrapActionObject), [`wrapObject`](resolvedtopic.md#wrapObject)
