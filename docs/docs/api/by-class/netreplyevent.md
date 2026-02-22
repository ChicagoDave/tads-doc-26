# NetReplyEvent

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 112)


Network Reply event. This type of event occurs when we receive a reply to a network request made with sendNetRequest().


**Superclass chain:** [NetEvent](netevent.md) > `object` > **NetReplyEvent**


## Properties


### `evType` *(overridden)*

Defined in tadsnet.t, line 164

our default event type is NetEvReply


### `httpStatusLine`

Defined in tadsnet.t, line 211

the HTTP status string (the first line of the headers)


### `redirectLoc`

Defined in tadsnet.t, line 234

Redirect location, if applicable. By default, this will be nil whether or not a redirection took place, because sendNetRequest() normally follows redirection links transparently, returning only the final result from the final server we're redirected to. However, you can override automatic redirection with an option flag (NetReqNoRedirect) when calling sendNetRequest(). When that option is selected, the function won't follow redirection links at all, but will instead simply return the redirect information as the result from the request. When that happens, this property is set to a string giving the target of the redirect. You can then follow the redirect manually, if desired, by sending a new request to the target given here.


### `replyBody`

Defined in tadsnet.t, line 202

the content body from the reply


### `replyHeaders`

Defined in tadsnet.t, line 208

the HTTP headers from the reply, as a lookup table indexed by header name


### `replyHeadersRaw`

Defined in tadsnet.t, line 218

the HTTP headers from the reply, in the raw text format - this is simply a string of all the headers, separated by CR-LF (\r\n) sequences


### `requestID`

Defined in tadsnet.t, line 171

The request identifier. This is the ID value provided by the caller in the call to sendNetRequest(), so that the caller can relate the reply back to the corresponding request.


### `statusCode`

Defined in tadsnet.t, line 199

The network status code. This is an integer value indicating whether the request was successful or failed with an error. A negative value is a low-level TADS error indicating that the request couldn't be sent to the server, or that a network error occurred receiving the reply:


## Inherited Properties


*From [NetEvent](netevent.md):* [`evArgs`](netevent.md#evArgs)


## Methods


### `construct(t, id, status, body, headers, loc)` *(overridden)*

Defined in tadsnet.t, line 114

construction
