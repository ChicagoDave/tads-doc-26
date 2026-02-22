# Topic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 39)


A Topic is an object representing some piece of knowledge in the story. Actors can use Topic objects in commands such as "ask" and "tell".


**Superclass chain:** [VocabObject](vocabobject.md) > `object` > **Topic**


## Properties


### `canResolvePossessive` *(overridden)*

Defined in actor.t, line 69

a topic cannot by default be used to resolve a possessive phrase


### `isKnown`

Defined in actor.t, line 57

Is the topic known? If this is true, the topic is in scope for actions that operate on topics, such as "ask about" and "tell about." If this is nil, the topic isn't known.


## Inherited Properties


*From [VocabObject](vocabobject.md):* [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`owner`](vocabobject.md#owner), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `canBeSensed(sense, trans, ambient)`

Defined in actor.t, line 66

Topics are abstract objects, so they can't be sensed with any of the physical senses, even if they're ever included as part of a containment hierarchy (which might be convenient in some cases for purposes of associating a topic with a physical object, for example).


## Inherited Methods


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`construct`](vocabobject.md#construct), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`getNominalOwner`](vocabobject.md#getNominalOwner), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`isOwnedBy`](vocabobject.md#isOwnedBy), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
