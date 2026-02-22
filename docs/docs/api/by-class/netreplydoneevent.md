# NetReplyDoneEvent

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 242)


Network Reply Done event. This type of event occurs when an asynchronous network reply (such as HTTPRequest.sendReplyAsync()) completes.


**Superclass chain:** [NetEvent](netevent.md) > `object` > **NetReplyDoneEvent**


## Properties


### `errMsg`

Defined in tadsnet.t, line 276

Error message, if any. If the reply failed, this contains a string with a description of the error that occurred. If the reply was sent successfully, this is nil.


### `evType` *(overridden)*

Defined in tadsnet.t, line 253

our default event type is NetEvReplyDone


### `requestObj`

Defined in tadsnet.t, line 259

The object representing the request we replied to. For HTTP requests, this is an HTTPRequest object.


### `socketErr`

Defined in tadsnet.t, line 269

The socket error, if any. If the reply failed due to a network error, this contains the error number. If no network error occurred, this is zero.


## Inherited Properties


*From [NetEvent](netevent.md):* [`evArgs`](netevent.md#evArgs)


## Methods


### `construct(t, req, err, msg)` *(overridden)*

Defined in tadsnet.t, line 244

construction


### `isSuccessful`

Defined in tadsnet.t, line 262

was the reply successfully sent?
