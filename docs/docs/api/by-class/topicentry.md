# TopicEntry

*class* — defined in [actor.t](../by-file/actor.t.md) (line 2133)


A topic database entry. Actors and actor state objects store topic databases; a topic database is essentially a set of these entries.


**Superclass chain:** `object` > **TopicEntry**


<details><summary>Subclasses (44)</summary>

- [AltTopic](alttopic.md)
- [CommandTopic](commandtopic.md)
- [DefaultTopic](defaulttopic.md)
- [DefaultAnyTopic](defaultanytopic.md)
- [DefaultAskForTopic](defaultaskfortopic.md)
- [DefaultAskTellTopic](defaultasktelltopic.md)
- [DefaultAskTopic](defaultasktopic.md)
- [DefaultCommandTopic](defaultcommandtopic.md)
- [DefaultConsultTopic](defaultconsulttopic.md)
- [DefaultGiveShowTopic](defaultgiveshowtopic.md)
- [DefaultGiveTopic](defaultgivetopic.md)
- [DefaultInitiateTopic](defaultinitiatetopic.md)
- [DefaultShowTopic](defaultshowtopic.md)
- [DefaultTellTopic](defaulttelltopic.md)
- [MiscTopic](misctopic.md)
- [ActorByeTopic](actorbyetopic.md)
- [ActorHelloTopic](actorhellotopic.md)
- [BoredByeTopic](boredbyetopic.md)
- [ByeTopic](byetopic.md)
- [HelloGoodbyeTopic](hellogoodbyetopic.md)
- [HelloTopic](hellotopic.md)
- [ImpByeTopic](impbyetopic.md)
- [ImpHelloTopic](imphellotopic.md)
- [LeaveByeTopic](leavebyetopic.md)
- [YesNoTopic](yesnotopic.md)
- [NoTopic](notopic.md)
- [YesTopic](yestopic.md)
- [SpecialTopic](specialtopic.md)
- [ThingMatchTopic](thingmatchtopic.md)
- [GiveShowTopic](giveshowtopic.md)
- [GiveTopic](givetopic.md)
- [ShowTopic](showtopic.md)
- [InitiateTopic](initiatetopic.md)
- [TopicOrThingMatchTopic](topicorthingmatchtopic.md)
- [AskTellGiveShowTopic](asktellgiveshowtopic.md)
- [AskTellShowTopic](asktellshowtopic.md)
- [TopicMatchTopic](topicmatchtopic.md)
- [AskTellTopic](asktelltopic.md)
- [AskAboutForTopic](askaboutfortopic.md)
- [AskForTopic](askfortopic.md)
- [AskTellAboutForTopic](asktellaboutfortopic.md)
- [AskTopic](asktopic.md)
- [TellTopic](telltopic.md)
- [ConsultTopic](consulttopic.md)

</details>


## Properties


### `altTalkCount`

Defined in actor.t, line 2317

The number of times this topic or any nested AltTopic has been invoked by the player. Each time the player asks/tells/etc about this topic OR any of its AltTopic children, we'll increment this count.


### `altTopicList`

Defined in actor.t, line 2373

our list of AltTopic children


### `impliesGreeting`

Defined in actor.t, line 2175

Do we imply a greeting? By default, all conversational topics imply a greeting. We separate this out so that the implied greeting can be controlled independently of whether or not we're actually conversational, if desired.


### `includeInList`

Defined in actor.t, line 2294

The set of database lists we're part of. This is a list of property pointers, giving the TopicDatabase properties of the lists we participate in.


### `isActive`

Defined in actor.t, line 2152

Is this topic active? This can be used to control how an actor can respond without have to worry about adding and removing topics manually at key events, or storing the topics in state objects. Sometimes, it's easier to just put a topic entry in the actor's database from the start, and test some condition dynamically when the topic is actually queried. To do this, override this method to test the condition that determines when the topic entry should become active. We'll never show the topic's response when isActive returns nil. By default, we simply return true to indicate that the topic entry is active.


### `isConversational`

Defined in actor.t, line 2167

Flag: we are a "conversational" topic. This is true by default. When this is set to nil, a ConversationReadyState will NOT show its greeting and will not enter its InConversationState to show this topic entry's response.


### `matchObj`

Defined in actor.t, line 2138

My matching simulation object or objects. This can be either a single object or a list of objects.


### `matchScore`

Defined in actor.t, line 2287

Our match strength score. By default, we'll use a score of 100, which is just an arbitrary base score.


### `talkCount`

Defined in actor.t, line 2309

The number of times this topic has invoked by the player. Each time the player asks/tells/etc about this topic, we'll increment this count.


### `topicGroupActive`

Defined in actor.t, line 2370

check the group isActive status (for AltTopics nested within)


### `topicGroupScoreAdjustment`

Defined in actor.t, line 2367

get the topic group score adjustment (for AltTopics nested within)


### `topicResponse`

Defined in actor.t, line 2302

Our response. This is displayed when we're the topic entry selected to handle an ASK or TELL. Each topic entry must override this to show our response text (or, alternatively, an entry can override handleTopic so that it doesn't call this property).


## Methods


### `addAltTopic(entry)`

Defined in actor.t, line 2360

Add an AltTopic entry. This is called by our AltTopic children during initialization; we'll simply add the entry to our list of AltTopic children.


### `addSuggestedTopic(t)`

Defined in actor.t, line 2550

Add a suggested topic. A suggested topic can be nested within a topic entry; doing this associates the suggested topic with the topic entry, and automatically associates the suggested topic with the entry's actor or actor state.


### `addTopic(entry)`

Defined in actor.t, line 2348

add a topic nested within us


### `adjustScore(score)`

Defined in actor.t, line 2252

Adjust my score value for any hierarchical adjustments. We'll add the score adjustment for each enclosing object.


### `anyAltIsActive`

Defined in actor.t, line 2228

Check to see if any alternative in the alternative group is active. This returns true if we're active or if any of our nested AltTopics is active.


### `breakTopicTie(matchList, topic, fromActor, toks)`

Defined in actor.t, line 2443

Break a tie among matching topics entries. The topic database searcher calls this on each matching topic entry when it finds multiple entries tied for first place, based on their match scores. This gives the entries a chance to figure out which one is actually the best match for the input, given the other entries that also matched.


### `checkIsActive`

Defined in actor.t, line 2205

Determine if this topic is active. This checks the isActive property, and also takes into account our relationship to alternative entries for the topic. Generally, you should *define* (override) isActive, and *call* this method.


### `// deferToEntry (other)`

Defined in actor.t, line 2281

Check to see if we want to defer to the given topic from an inferior topic database. By default, we never defer to a topic from an inferior database: we choose a matching topic from the top database in the hierarchy where we find a match.


### `getActor`

Defined in actor.t, line 2184

Get the actor associated with the topic, if any. By default, we'll return our enclosing database's topic owner, if it's an actor - in almost all cases, if there's any actor associated with a topic, it's simply the owner of the database containing the topic.


### `getTopicOwner`

Defined in actor.t, line 2323

the owner of any AltTopic nested within me is the same as my own topic owner, which we take from our location


### `handleTopic(fromActor, topic)`

Defined in actor.t, line 2492

Handle the topic. This is called when we find that this is the best topic entry for the current topic.


### `initializeTopicEntry`

Defined in actor.t, line 2336

Initialize. If we have a location property, we'll assume that the location is a topic database object, and we'll add ourselves to that database.


### `// isMatchPossible (actor, scopeList)`

Defined in actor.t, line 2408

Check to see if a match to this topic entry is *possible* right now for the given actor. For most subclasses, this is inherently imprecise, because the 'match' function simply isn't reversible in general: to know if we can be matched, we'd have to determine if there's a non-empty set of possible inputs that can match us. This method is complementary to matchTopic(), so subclasses must override with a corresponding implementation.


### `// matchTopic (fromActor, topic)`

Defined in actor.t, line 2387

Match a topic. This is abstract in this base class; it must be defined by each concrete subclass. This returns nil if there's no match, or an integer value if there's a match. The higher the number's value, the stronger the match.


### `noteAltInvocation(fromActor, alt)`

Defined in actor.t, line 2532

Note that something in our entire alternative group has been invoked. We count as a member of our own group, so this is invoked when we're invoked; this is also invoked when any AltTopic child of ours is invoked.


### `noteInvocation(fromActor)`

Defined in actor.t, line 2514

note that we've been invoked


### `setTopicPronouns(fromActor, topic)`

Defined in actor.t, line 2458

Set pronouns for the topic, if possible. If the topic corresponds to a game-world object, then we should set the pronoun antecedent to the game object. This must be handled per subclass because of the range of possible meanings of 'topic'.
