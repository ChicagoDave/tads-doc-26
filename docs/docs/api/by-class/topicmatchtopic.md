# TopicMatchTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 2783)


A "topic match" topic entry. This is a topic entry that matches topic phrases in the grammar.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **TopicMatchTopicSubclasses:** [AskTellTopic](asktelltopic.md), [AskAboutForTopic](askaboutfortopic.md), [AskForTopic](askfortopic.md), [AskTellAboutForTopic](asktellaboutfortopic.md), [AskTopic](asktopic.md), [TellTopic](telltopic.md), [ConsultTopic](consulttopic.md), [TopicOrThingMatchTopic](topicorthingmatchtopic.md), [AskTellGiveShowTopic](asktellgiveshowtopic.md), [AskTellShowTopic](asktellshowtopic.md)


## Properties


### `matchExactCase`

Defined in actor.t, line 2800


### `matchPattern`

Defined in actor.t, line 2799

A regular expression pattern that we'll match to the actual topic text as entered in the command. If 'matchExactCase' is true, we'll match the exact text in its original upper/lower case rendering; otherwise, we'll convert the player input to lower-case before matching it against the pattern. In most cases, we'll want to match the input no matter what combination of upper and lower case the player entered, so matchExactCase is nil by default.


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`includeInList`](topicentry.md#includeInList), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `findMatchObj(obj, rt)`

Defined in actor.t, line 2876

Match an individual item from our match list to the given ResolvedTopic object. We'll check each object in the resolved topic's "in scope" and "likely" lists.


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 2893

It's possible for us to match if any of our matchObj objects are known to the actor. If we have no matchObj objects, we must be matching on a regular expression or on a custom condition, so we can't speculate on matchability; we'll simply return true in those cases.


### `matchTopic(fromActor, topic)` *(overridden)*

Defined in actor.t, line 2814

Match the topic. By default, we'll match to either the simulation object or objects in matchObj, or the pattern in matchPattern. Note that we always try both ways of matching, so a single AskTellTopic can define both a pattern and an object list.


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 2926

set the topic pronouns


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation)
