# PendingCommandAction

*class* — defined in [actor.t](../by-file/actor.t.md) (line 10519)


a pending command based on a pre-resolved Action and its objects


**Superclass chain:** [PendingCommandInfo](pendingcommandinfo.md) > `object` > **PendingCommandAction**


## Properties


### `action_`

Defined in actor.t, line 10549

the resolved Action to perform


### `objs_`

Defined in actor.t, line 10552

the resolved objects for the action


## Inherited Properties


*From [PendingCommandInfo](pendingcommandinfo.md):* [`hasCommand`](pendingcommandinfo.md#hasCommand), [`issuer_`](pendingcommandinfo.md#issuer_), [`startOfSentence_`](pendingcommandinfo.md#startOfSentence_)


## Methods


### `construct(startOfSentence, issuer, action, [objs])` *(overridden)*

Defined in actor.t, line 10520


### `executePending(targetActor)` *(overridden)*

Defined in actor.t, line 10530

execute the pending command
