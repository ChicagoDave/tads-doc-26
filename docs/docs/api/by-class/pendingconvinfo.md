# PendingConvInfo

*class* — defined in [actor.t](../by-file/actor.t.md) (line 5463)


A pending conversation information object. An Actor keeps a list of these for pending conversations.


**Superclass chain:** `object` > **PendingConvInfo**


## Properties


### `node_`

Defined in actor.t, line 5479


### `state_`

Defined in actor.t, line 5478

our ActorState and ConvNode (or ConvNode name string), describing how we're to start the conversation


### `time_`

Defined in actor.t, line 5482

the minimum game clock time at which we can start the conversation


## Methods


### `construct(state, node, turns)`

Defined in actor.t, line 5464
