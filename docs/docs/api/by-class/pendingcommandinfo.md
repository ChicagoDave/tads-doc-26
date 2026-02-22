# PendingCommandInfo

*class* — defined in [actor.t](../by-file/actor.t.md) (line 10474)


Pending Command Information structure. This is an abstract base class that we subclass for particular ways of representing the command to be executed.


**Superclass chain:** `object` > **PendingCommandInfoSubclasses:** [PendingCommandAction](pendingcommandaction.md), [PendingCommandMarker](pendingcommandmarker.md), [PendingCommandToks](pendingcommandtoks.md)


## Properties


### `hasCommand`

Defined in actor.t, line 10482

Check to see if this pending command item has a command to perform. This returns true if we have a command, nil if we're just a queue placeholder without any actual command to execute.


### `issuer_`

Defined in actor.t, line 10488

the issuer of the command


### `startOfSentence_`

Defined in actor.t, line 10491

we're at the start of a "sentence"


## Methods


### `construct(issuer)`

Defined in actor.t, line 10475


### `executePending(targetActor)`

Defined in actor.t, line 10485

execute the command
