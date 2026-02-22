# SuggestedTopic

*class* — defined in [actor.t](../by-file/actor.t.md) (line 1151)


A "suggested" topic. These provide suggestions for things the player might want to ASK or TELL another actor about. At certain times (specifically, when starting a conversation with HELLO or TALK TO, or when the player enters a TOPICS command to explicitly ask for a list of topic suggestions), we'll look for these objects in the actor or actor state for the actor to whom we're talking. We'll show a list of each currently active suggestion we find. This gives the player some guidance of what to talk about. For example:


**Superclass chain:** `object` > **SuggestedTopicSubclasses:** [SuggestedAskForTopic](suggestedaskfortopic.md), [SuggestedAskTopic](suggestedasktopic.md), [SuggestedGiveTopic](suggestedgivetopic.md), [SuggestedNoTopic](suggestednotopic.md), [SuggestedShowTopic](suggestedshowtopic.md), [SuggestedTellTopic](suggestedtelltopic.md), [SuggestedTopicTree](suggestedtopictree.md), [SpecialTopic](specialtopic.md), [SuggestedYesTopic](suggestedyestopic.md)


## Properties


### `associatedTopic`

Defined in actor.t, line 1185

Our associated topic. In most cases, this will be initialized automatically: if this suggested topic object is also a TopicEntry object (using multiple inheritance), we'll set this during start-up to 'self', or if our location is a TopicEntry, we'll set this to our location. This only needs to be initialized manually if neither of those conditions is true.


### `curiositySatisfied`

Defined in actor.t, line 1316

Have we satisfied our curiosity about this topic? Returns true if so, nil if not. We'll never suggest a topic when this returns true, because this means that the player no longer feels the need to ask about the topic.


### `fullName`

Defined in actor.t, line 1174

The name of the suggestion. The rules for setting this vary by language; in the English version, we'll display the fullName when we show a stand-alone item, and the groupName when we appear in a list group (such as a group of ASK ABOUT or TELL ABOUT suggestions).


### `location`

Defined in actor.t, line 1199

Set the location to the actor to ask or tell about this topic. This is the target of the ASK ABOUT or TELL ABOUT command, NOT the actor who's doing the asking. This can also be set to a TopicEntry object, in which case we'll be associated with the actor with which the topic entry is associated, and we'll also automatically tie the topic entry to this suggestion.


### `name`

Defined in actor.t, line 1175


### `suggestionGroup`

Defined in actor.t, line 1224

the ListGroup with which we're to list this suggestion


### `suggestTo`

Defined in actor.t, line 1221

The actor who *wants* to ask or tell about this topic. Our location property gives the actor to be asked or told, because we're associated with the target actor - the same actor who has the TopicEntry information for the topic. This property, in contrast, gives the actor who's doing the asking.


### `timesToSuggest`

Defined in actor.t, line 1308

The number of times to suggest asking about our topic. When we've asked about our associated topic this many times, we'll have satisfied our curiosity. In most cases, we'll only want to suggest a topic until it's asked about once, since most topics only have a single meaningful response, so we'll use 1 as the default. This should be overridden in cases where a topic will reveal more information when asked several times. If this is nil, it means that there's no limit to the number of times to suggest asking about this.


## Methods


### `associatedTopicCanMatch(actor, scopeList)`

Defined in actor.t, line 1351

is it possible to match the associated topic?


### `associatedTopicIsActive`

Defined in actor.t, line 1345

is the associated topic active?


### `associatedTopicTalkCount`

Defined in actor.t, line 1348

get the number of previous invocations of the associated topic


### `findEnclosingSuggestedTopic`

Defined in actor.t, line 1227

find the nearest enclosing SuggestedTopic parent


### `findOuterSuggestedTopic`

Defined in actor.t, line 1242

find the outermost enclosing SuggestedTopic parent


### `fromEnclosingSuggestedTopic(prop, defaultVal)`

Defined in actor.t, line 1263

get a property from the nearest enclosing SuggestedTopic, or return the given default value if there is no enclosing SuggestedTopic


### `initializeSuggestedTopic`

Defined in actor.t, line 1320

initialize - this is called automatically during pre-initialization


### `isSuggestionActive(actor, scopeList)`

Defined in actor.t, line 1282

Should we suggest this topic to the given actor? We'll return true if the actor is the same actor for which this suggestion is intended, and the associated topic entry is currently active, and we haven't already satisfied our curiosity about the topic.


### `noteSuggestion`

Defined in actor.t, line 1359

Note that we're being shown in a topic inventory listing. By default, we don't do anything here, but subclasses can use this to do any extra work they want to do on being listed.
