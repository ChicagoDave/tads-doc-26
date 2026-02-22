# PendingCommandMarker

*class* — defined in [actor.t](../by-file/actor.t.md) (line 10566)


A pending command marker. This is not an actual pending command; rather, it's just a queue marker. We sometimes want to synchronize some other activity with an actor's progress through its command queue; for example, we might want one actor to wait until another actor has executed a particular pending action. These markers can be used for this kind of synchronization; they move through the queue like ordinary pending commands, so we can tell if an actor has reached a particular command by observing the marker's progress through the queue.


**Superclass chain:** [PendingCommandInfo](pendingcommandinfo.md) > `object` > **PendingCommandMarker**


## Properties


### `hasCommand` *(overridden)*

Defined in actor.t, line 10568

I have no command to execute


## Inherited Properties


*From [PendingCommandInfo](pendingcommandinfo.md):* [`issuer_`](pendingcommandinfo.md#issuer_), [`startOfSentence_`](pendingcommandinfo.md#startOfSentence_)


## Inherited Methods


*From [PendingCommandInfo](pendingcommandinfo.md):* [`construct`](pendingcommandinfo.md#construct), [`executePending`](pendingcommandinfo.md#executePending)
