# SpecialTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 3751)


A "special" topic. This is a topic that responds to its own unique, custom command input. In other words, rather than responding to a normal command like ASK ABOUT or SHOW TO, we'll respond to a command for which we define our own syntax. Our special syntax doesn't have to follow any of the ordinary parsing conventions, because whenever our ConvNode is active, we get a shot at parsing player input before the regular parser gets to see it.


**Superclass chain:** [TopicEntry](topicentry.md) > `object` > [SuggestedTopicTree](suggestedtopictree.md) > [SuggestedTopic](suggestedtopic.md) > **SpecialTopic**


## Properties


### `fullName` *(overridden)*

Defined in actor.t, line 3816

our suggestion (topic inventory) full name is usually the same as the base name; special topics usually aren't grouped in topic suggestion listings, since each topic usually has its own unique, custom syntax


### `includeInList` *(overridden)*

Defined in actor.t, line 3822

include in the specialTopics list of our parent topic database


### `keywordList`

Defined in actor.t, line 3766

Our keyword list. Each special topic instance must define a list of strings giving the keywords we match. The special topic will match user input if the user input consists exclusively of words from this keyword list. The user input doesn't have to include all of the words defined here, but all of the words in the user's input have to appear here to match.


### `matchPat`

Defined in actor.t, line 3805

our regular expression pattern - we'll build this automatically from the keyword list if this isn't otherwise defined


### `name` *(overridden)*

Defined in actor.t, line 3808

our suggestion (topic inventory) base name


### `timesToSuggest` *(overridden)*

Defined in actor.t, line 3830

By default, don't limit the number of times we'll suggest this topic. Since a special topic is valid only in a particular ConvNode context, we normally want all of the topics in that context to be available, even if they've been used before.


### `weakPat`

Defined in en_us.t, line 2762

Our "weak" strings - 'i', 'l', 'look': these are weak because a user typing one of these strings by itself is probably actually trying to enter the command of the same name, rather than entering a special topic. These come up in cases where the special topic is something like "say I don't know" or "tell him you'll look into it".


## Inherited Properties


*From [TopicEntry](topicentry.md):* [`altTalkCount`](topicentry.md#altTalkCount), [`altTopicList`](topicentry.md#altTopicList), [`impliesGreeting`](topicentry.md#impliesGreeting), [`isActive`](topicentry.md#isActive), [`isConversational`](topicentry.md#isConversational), [`matchObj`](topicentry.md#matchObj), [`matchScore`](topicentry.md#matchScore), [`talkCount`](topicentry.md#talkCount), [`topicGroupActive`](topicentry.md#topicGroupActive), [`topicGroupScoreAdjustment`](topicentry.md#topicGroupScoreAdjustment), [`topicResponse`](topicentry.md#topicResponse)


*From [SuggestedTopic](suggestedtopic.md):* [`associatedTopic`](suggestedtopic.md#associatedTopic), [`curiositySatisfied`](suggestedtopic.md#curiositySatisfied), [`location`](suggestedtopic.md#location), [`suggestionGroup`](suggestedtopic.md#suggestionGroup), [`suggestTo`](suggestedtopic.md#suggestTo)


## Methods


### `getConvNode`

Defined in actor.t, line 3900

find our enclosing ConvNode object


### `initializeSpecialTopic`

Defined in actor.t, line 3780

Initialize the special topic. This runs during pre-initialization, to give us a chance to do pre-game set-up.


### `isMatchPossible(actor, scopeList)` *(overridden)*

Defined in actor.t, line 3860

a special topic is always matchable, since we match on literal text


### `matchPreParse(str, procStr)`

Defined in en_us.t, line 2744

Match a string during pre-parsing. By default, we'll match the string if all of its words (as defined by the regular expression parser) match our keywords.


### `matchTopic(fromActor, topic)` *(overridden)*

Defined in actor.t, line 3833

check for a match


### `noteSuggestion` *(overridden)*

Defined in actor.t, line 3819

on being suggested, update the special topic history


## Inherited Methods


*From [TopicEntry](topicentry.md):* [`addAltTopic`](topicentry.md#addAltTopic), [`addSuggestedTopic`](topicentry.md#addSuggestedTopic), [`addTopic`](topicentry.md#addTopic), [`adjustScore`](topicentry.md#adjustScore), [`anyAltIsActive`](topicentry.md#anyAltIsActive), [`breakTopicTie`](topicentry.md#breakTopicTie), [`checkIsActive`](topicentry.md#checkIsActive), [`deferToEntry`](topicentry.md#deferToEntry), [`getActor`](topicentry.md#getActor), [`getTopicOwner`](topicentry.md#getTopicOwner), [`handleTopic`](topicentry.md#handleTopic), [`initializeTopicEntry`](topicentry.md#initializeTopicEntry), [`noteAltInvocation`](topicentry.md#noteAltInvocation), [`noteInvocation`](topicentry.md#noteInvocation), [`setTopicPronouns`](topicentry.md#setTopicPronouns)


*From [SuggestedTopicTree](suggestedtopictree.md):* [`associatedTopicIsActive`](suggestedtopictree.md#associatedTopicIsActive), [`associatedTopicTalkCount`](suggestedtopictree.md#associatedTopicTalkCount)


*From [SuggestedTopic](suggestedtopic.md):* [`associatedTopicCanMatch`](suggestedtopic.md#associatedTopicCanMatch), [`findEnclosingSuggestedTopic`](suggestedtopic.md#findEnclosingSuggestedTopic), [`findOuterSuggestedTopic`](suggestedtopic.md#findOuterSuggestedTopic), [`fromEnclosingSuggestedTopic`](suggestedtopic.md#fromEnclosingSuggestedTopic), [`initializeSuggestedTopic`](suggestedtopic.md#initializeSuggestedTopic), [`isSuggestionActive`](suggestedtopic.md#isSuggestionActive)
