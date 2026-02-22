# HTTPRequest

*class* — defined in [httpreq.h](../by-file/httpreq.h.md) (line 29)


HTTP Request object. This object represents an HTTP protocol request from a client to one of our servers. HTTPRequest objects are created by the HTTPServer object as requests arrive, and are passed to the byte code program as network events, via the getNetEvent() function. The program uses the object to get information on the request and to send back the reply.


**Superclass chain:** [Object](object.md) > **HTTPRequest**


## Methods


### `endChunkedReply(headers?)`

Defined in httpreq.h, line 340

Finish a chunked reply. This completes a chunked reply started with startChunkedReply(). After calling this routine, the request is completed, and no further reply can be sent.


### `getBody`

Defined in httpreq.h, line 184

Get the body of the request, if any. Some types of HTTP requests, such as POST and PUT, contain a message body. This returns the raw, unparsed message body. Returns a File object, open with read-only access. If there's no message body at all, this returns nil.


### `getClientAddress`

Defined in httpreq.h, line 193

Get the network address of the client. This returns a list: ['ip-address', port], where 'ip-address' is a string with the IP address of the client, in decimal notation ('192.168.1.15', for example), and 'port' is an integer giving the network port number on the client side.


### `getCookie(name)`

Defined in httpreq.h, line 123

Look up a cookie. This looks for the given cookie name in the cookies sent by the client, and returns a string containing the cookie's text if found. If the cookie isn't found, returns nil.


### `getCookies`

Defined in httpreq.h, line 132

Get the cookies sent with the request by the client. This returns a LookupTable of the cookies, with each key set to a cookie name and the corresponding value set to the cookie's text. Cookies are assumed to contain only plan ASCII characters; any 8-bit characters in a cookie's name or value will be replaced by '?' characters.


### `getFormFields`

Defined in httpreq.h, line 161

Get the form data-entry field values. This returns a LookupTable containing the field values sent with the request. Each key in the table is a field name (given by the NAME property of the HTML <INPUT> tag for the field), and each corresponding value is a string giving the value of the field as entered by the user.


### `getHeaders`

Defined in httpreq.h, line 116

Get the headers sent with the request by the client. This returns a LookupTable object: the keys are the header names, and the values are the corresponding header values. For example, for a POST, there might be a 'Content-type' key with the corresponding value 'application/x-www-form-urlencoded'.


### `getQuery`

Defined in httpreq.h, line 60

Get the query string. This is the portion of the URL after the server address. For example, if the client web browser navigated to the URL "http://www.tads.org:1234/path/resource?a=1&b=2" would return "/path/resource?a=1&b=2".


### `getQueryParam(name)`

Defined in httpreq.h, line 100

Get a parameter from the query string. This parses the query string and returns the parameter with the specified name, if present, or nil if not. This does the same parsing as parseQuery(), but it returns just the specified parameter value rather than building a lookup table with all of the parameters. This is more efficient than parseQuery() if you're just looking up one or two parameters, since it avoids building the whole table, but it's less efficient if you're looking up many parameters because this routine has to re-parse the query string on each call.


### `getServer`

Defined in httpreq.h, line 35

Get the HTTPServer object. This is the server that received the network request that 'self' represents.


### `getVerb`

Defined in httpreq.h, line 48

Get the verb. This is the HTTP verb that the client sent with the request to indicate what action to perform. The standard HTTP verbs are GET (this is the most common request type; it simply retrieves a resource from the server), POST (used to submit form data), OPTIONS, HEAD, PUT, DELETE, TRACE, CONNECT, and PATCH. If the client sends a non-standard verb, the system simply passes it through to the request, allowing you to write a custom server for a custom client; however, this isn't recommended, since proxies and firewalls often block what they consider ill-formed requests.


### `parseQuery`

Defined in httpreq.h, line 87

Parse the query string. This returns a LookupTable containing the parsed elements of the query. The element table[1] is the base resource name: this is the part of the query string up to the first '?', if any, or the entire query string if there are no parameters. If there are any parameters, they're entered in the table under the parameter names as keys. For example, for this query string:


### `sendReply(body, contentType?, status?, headers?)`

Defined in httpreq.h, line 289

Send the reply to the request.


### `sendReplyAsync(body, contentType?, status?, headers?)`

Defined in httpreq.h, line 375

Send the reply to the request asynchronously. This works like sendReply(), except that this method starts a new background thread to handle the data transfer and then immediately returns. This allows the caller to continue servicing other requests while the data transfer proceeds, which is important when sending a large file (such as a large image or audio file) as the reply body. Most browsers allow the user to continue interacting with the displayed page while images and audio files are transfered in the background, so it's likely that the browser will generate new requests during the time it takes to send a single large reply body. When you use sendReply(), the server won't be able to service any of those new requests until the reply is fully sent, so the browser will appear unresponsive for the duration of the reply data transfer. Using sendReplyAsync() allows you to service new requests immediately, without waiting for the data transfer to complete.


### `sendReplyCatch(reply, contType?, stat?, headers?)`

Defined in webui.t, line 122

Send a reply, catching "socket disconnect" exceptions. In most cases, server objects will want to use this method rather than the native sendReply() so that they won't have to handle disconnect exceptions manually.


### `sendReplyChunk(body)`

Defined in httpreq.h, line 324

Send a piece of a chunked reply. This can be called any number of times after calling startChunkedReply() to send the pieces of a chunked reply.


### `setCookie(name, value)`

Defined in httpreq.h, line 223

Set a cookie in the reply. This sets a cookie with the given name and value, both given as strings. The value string starts with the text to set for the cookie, and can be followed by additional parameters, delimited by semicolons:


### `startChunkedReply(contentType, resultCode?, headers?)`

Defined in httpreq.h, line 313

Start a chunked reply. This sends the initial headers of a reply that will be generated in pieces. This is an alternative to sending the entire reply as a single string via sendReply(), for situations where you're generating the reply algorithmically and want to send a little bit at a time, rather than buffering up the entire reply in a string or StringBuffer to send all at once. This is particularly useful for cases where the reply will take a while to generate, since it allows the client to interpret partial data before the entire reply is completed; and for very large reply bodies, where it would consume a lot of memory to buffer the whole reply.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
