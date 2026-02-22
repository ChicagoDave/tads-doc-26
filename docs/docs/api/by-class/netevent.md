# NetEvent

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 39)


A NetEvent instance describes an event read via the getNetEvent() function.


**Superclass chain:** `object` > **NetEventSubclasses:** [NetReplyDoneEvent](netreplydoneevent.md), [NetReplyEvent](netreplyevent.md), [NetRequestEvent](netrequestevent.md), [NetTimeoutEvent](nettimeoutevent.md)


## Properties


### `evArgs`

Defined in tadsnet.t, line 66

Extra event-specific arguments. This is primarily for debugging purposes, since it's only used when getNetEvent() needs to construct a NetEvent subclass that isn't defined in the game. In this case, the absence of a subclass definition in the game presumably means that the game isn't written to handle the type of event generated (for example, because it was written for an older interpreter version that didn't have the event type).


### `evType`

Defined in tadsnet.t, line 44

The event type. This is a NetEvXxx value (see tadsnet.h) indicating which type of event this is.


## Methods


### `construct(t, [args])`

Defined in tadsnet.t, line 51

Construction. getNetEvent() only constructs this object directly when the subclass it's looking for isn't defined in the game program.
