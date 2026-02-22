# PendingCommandToks

*class* — defined in [actor.t](../by-file/actor.t.md) (line 10495)


a pending command based on a list of tokens from an input string


**Superclass chain:** [PendingCommandInfo](pendingcommandinfo.md) > `object` > **PendingCommandToks**


## Properties


### `tokens_`

Defined in actor.t, line 10515

the token list for the command


## Inherited Properties


*From [PendingCommandInfo](pendingcommandinfo.md):* [`hasCommand`](pendingcommandinfo.md#hasCommand), [`issuer_`](pendingcommandinfo.md#issuer_), [`startOfSentence_`](pendingcommandinfo.md#startOfSentence_)


## Methods


### `construct(startOfSentence, issuer, toks)` *(overridden)*

Defined in actor.t, line 10496


### `executePending(targetActor)` *(overridden)*

Defined in actor.t, line 10508

Execute the command. We'll parse our tokens and execute the parsed results.
