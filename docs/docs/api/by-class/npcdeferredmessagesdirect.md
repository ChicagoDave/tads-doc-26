# npcDeferredMessagesDirect

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 2457)


Deferred NPC messages. We use this to report deferred messages from an NPC to the player. A message is deferred when a parsing error occurs, but the NPC can't talk to the player because there's no sense path to the player. When this happens, the NPC queues the message for eventual delivery; when a sense path appears later that lets the NPC talk to the player, we deliver the message through this object. Since these messages describe conditions that occurred in the past, we use the past tense to phrase the messages.


**Superclass chain:** [npcDeferredMessages](npcdeferredmessages.md) > `object` > **npcDeferredMessagesDirect**


## Methods


### `ambiguousNounPhrase(actor, originalText, matchList, fullMatchList)`

Defined in msg_neu.t, line 2526

we found an ambiguous noun phrase, but we were unable to perform interactive disambiguation


### `askMissingObject(actor, action, which)`

Defined in msg_neu.t, line 2533

an object phrase was missing


### `commandNotUnderstood(actor)`

Defined in msg_neu.t, line 2458


### `emptyNounPhrase(actor)`

Defined in msg_neu.t, line 2488

empty noun phrase ('take the')


### `insufficientQuantity(actor, txt, matchList, requiredNum)`

Defined in msg_neu.t, line 2502

insufficient quantity to meet a command request ('take five books')


### `noMatchCannotSee(actor, txt)`

Defined in msg_neu.t, line 2465

no match for a noun phrase


### `noMatchForAll(actor)`

Defined in msg_neu.t, line 2475

no match for 'all'


### `noMatchForAllBut(actor)`

Defined in msg_neu.t, line 2481

nothing left for 'all' after removing 'except' items


### `noMatchNotAware(actor, txt)`

Defined in msg_neu.t, line 2469


### `singleObjectRequired(actor, txt)`

Defined in msg_neu.t, line 2516

a unique object is required, but multiple objects were specified


### `uniqueObjectRequired(actor, txt, matchList)`

Defined in msg_neu.t, line 2509

a unique object is required, but multiple objects were specified


### `wordIsUnknown(actor, txt)`

Defined in msg_neu.t, line 2542

tell the user they entered a word we don't know


### `zeroQuantity(actor, txt)`

Defined in msg_neu.t, line 2495

'take zero books'
