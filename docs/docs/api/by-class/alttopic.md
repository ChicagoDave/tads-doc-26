# AltTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 2668)


An alternative topic entry. This makes it easy to define different responses to a topic according to the game state; for example, we might want to provide a different response for a topic after some event has occurred, so that we can reflect knowledge of the event in the response.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > **AltTopic**


## Properties


### `altTalkCount` *(overridden)*

Defined in actor.t, line 2756

our AltTopic counter is the AltTopic counter for the enclosing topic


### `altTopicOrder`

Defined in actor.t, line 2742

Our relative order within our parent's list of alternatives. By default, we simply return the source file ordering, which ensures that static AltTopic objects (i.e., those defined directly in source files, not dynamically created with 'new') will be ordered just as they're laid out in the source file.


### `impliesGreeting` *(overridden)*

Defined in actor.t, line 2730

take our implied-greeting status from our parent


### `includeInList` *(overridden)*

Defined in actor.t, line 2685

include in the same lists as our parent


### `isConversational` *(overridden)*

Defined in actor.t, line 2733

take our conversational status from our parent


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTopicList`](topicentry.md#altTopicList), [`isActive`](topicentry.md#isActive), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


## Methods


### `checkIsActive` *(overridden)*

Defined in actor.t, line 2700

Determine if this topic is active. An AltTopic is active if its own isActive indicates true, AND none of its subsequent siblings are active.


### `initializeAltTopic`

Defined in actor.t, line 2688

AltTopic initialization


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 2674

we can match if our parent can match


### `matchPreParse(str, pstr)`

Defined in actor.t, line 2678

we can match a pre-parse string if our parent can


### `matchTopic(fromActor, topic)` *(overridden)*

Defined in actor.t, line 2670

we match if our parent matches, and with the same score


### `noteInvocation(fromActor)` *(overridden)*

Defined in actor.t, line 2745

note invocation


### `setTopicPronouns(fromActor, topic)` *(overridden)*

Defined in actor.t, line 2681

set pronouns for the topic


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation)
