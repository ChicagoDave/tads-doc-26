# TopicOrThingMatchTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3139)


A TopicEntry that can match a Thing or a Topic. This can be used to combine ASK/TELL-type responses and GIVE/SHOW-type responses in a single topic entry.


**Superclass chain:** [ThingMatchTopic](thingmatchtopic.md) > [TopicEntry](topicentry.md) > `object` > [TopicMatchTopic](topicmatchtopic.md) > **TopicOrThingMatchTopicSubclasses:** [AskTellGiveShowTopic](asktellgiveshowtopic.md), [AskTellShowTopic](asktellshowtopic.md)


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`includeInList`](topicentry.md#includeInList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


*From [TopicMatchTopic](topicmatchtopic.md):* [`matchExactCase`](topicmatchtopic.md#matchExactCase), [`matchPattern`](topicmatchtopic.md#matchPattern)


## Methods


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3153

if we're being asked to match a ResolvedTopic, use the inherited TopicMatchTopic handling; otherwise, use the inherited ThingMatchTopic handling


### `matchTopic(fromActor, obj)` *(overridden)*

Defined in actor.t, line 3140


### `setTopicPronouns(fromActor, obj)` *(overridden)*

Defined in actor.t, line 3160

if a match is possible from either subclass, allow it


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)


*From [TopicMatchTopic](topicmatchtopic.md):* [`findMatchObj`](topicmatchtopic.md#findMatchObj)
