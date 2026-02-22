# NetRequestEvent

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 80)


Network Request Event. This type of event occurs when a server (such as an HTTPServer object) receives a request from a network client.


**Superclass chain:** [NetEvent](netevent.md) > `object` > **NetRequestEvent**


## Properties


### `evRequest`

Defined in tadsnet.t, line 97

The request object. When the event type is NetEvRequest, this contains a request object describing the request. The class of the request object varies according to the server type; you can use ofKind() to check which type of request it is. For example, for an HTTP request, this will be an object of class HTTPRequest.


### `evType` *(overridden)*

Defined in tadsnet.t, line 88


## Inherited Properties


*From [NetEvent](netevent.md):* [`evArgs`](netevent.md#evArgs)


## Methods


### `construct(t, req)` *(overridden)*

Defined in tadsnet.t, line 82

construction
