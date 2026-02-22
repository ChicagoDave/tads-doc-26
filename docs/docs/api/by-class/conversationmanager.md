# conversationManager

*object* — defined in [actor.t](../by-file/actor.t.md) (line 163)


Conversation manager output filter. We look for special tags in the output stream:


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **conversationManager**


## Properties


### `customTags`

Defined in actor.t, line 181

Custom extended tags. Games and library extensions can add their own tag processing as needed, by using 'modify' to extend this object. There are two things you have to do to add your own tags:


### `idToActor`

Defined in actor.t, line 495

a vector of actors, indexed by their convMgrID values


### `pendingTopicInventory`

Defined in actor.t, line 536

flag: we have a pending prompt-time topic inventory request


### `respondingActor`

Defined in actor.t, line 466

The current responding actor. Actors should set this when they're about to show a response to an ASK, TELL, etc.


### `revealedNameTab`

Defined in actor.t, line 492

The global lookup table of all revealed keys. This table is keyed by the string naming the revelation; the value associated with each key is not used (we always just set it to true).


### `tagPat`

Defined in actor.t, line 342

regular expression pattern for our tags


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `beginResponse(actor)`

Defined in actor.t, line 395

Note that an actor is about to give a response through a TopicEntry object. We'll remember the actor so that we'll know which actor is involved in a <.convnode> operation.


### `doCustomTag(tag, arg)`

Defined in actor.t, line 182


### `execute` *(overridden)*

Defined in actor.t, line 498

preinitialize


### `filterText(ostr, txt)` *(overridden)*

Defined in actor.t, line 185

filter text written to the output stream


### `finishResponse(actor, node)`

Defined in actor.t, line 421

Finish the response - call this after we finish handling the response. There must be a subsequent matching call to this routine whenever beginResponse() is called.


### `scheduleTopicInventory`

Defined in actor.t, line 357

Schedule a topic inventory request. Game code can call this at any time to request that the player character's topic inventory be shown automatically just before the next command prompt. In most cases, game code won't call this directly, but will request the same effect using the <.topics> tag in topic response text.


### `setRevealed(tag)`

Defined in actor.t, line 482

Mark a tag as revealed. This adds an entry for the tag to the revealedNameTab table. We simply set the table entry to 'true'; the presence of the tag in the table constitutes the indication that the tag has been revealed.


### `showOrScheduleTopicInventory(actor, otherActor)`

Defined in actor.t, line 374

Show or schedule a topic inventory request. If the current action has a non-default command report, schedule it; otherwise, show it now.


### `topicInventoryDaemon`

Defined in actor.t, line 518

Prompt daemon: show topic inventory when appropriate. When a response explicitly asks us to show a topic inventory using the <.topics> tag, or when other game code asks us to show topic inventory by calling scheduleTopicInventory(), we'll show the inventory just before the command input prompt.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
