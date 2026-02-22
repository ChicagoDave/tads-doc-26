

# HTTPRequest


The HTTPRequest intrinsic class represents a request from a client
connected to an HTTP server your program created.  This object
provides methods for getting information on the request the client
sent, and for sending your reply.


The TADS HTTP package is designed to handle all of the low-level
network plumbing automatically, while giving your program full control
over how the server responds to client requests.  HTTPRequest is a key
part of this design.  It handles the details of the network data
transmission and the standard protocol interpretation, and presents
you with the parsed information in a readily usable format.  Your
program can then interpret the request and determine the appropriate
action; once you've determined the response, the HTTPRequest object
handles the details of transmitting the bytes back to the client.


For more on how to create an HTTP server in a TADS program, refer
to the [HTTPServer](httpsrv.md) documentation.


## Headers and library files


To use the HTTPRequest class, you must `#include <httpreq.h>`
in your program.  In addition, we recommend that you add the
library file `tadsnet.t` to your build (by adding it to your project
.t3m file), since this file defines some helper classes often used
with HTTPRequest.


## Receiving requests


You can't create an HTTPRequest object with the `new` operator.
Instead, the system creates these automatically for you.  The HTTP
server creates an HTTPRequest whenever a request arrives from the
network client, and places the HTTPRequest in the network message
queue.  Your program retrieves the request object by calling the [`getNetEvent()`](../functions/tadsnet.md#getNetEvent) function.


The basic structure of a TADS program that creates an HTTP server
is an event loop: you call `getNetEvent()` to wait for an event, then
you interpreter and respond to the event.  You repeat this process as
long as the server is running.


## HTTPRequest methods


`endChunkedReply(headers?)`


Finishes a chunked reply.  This tells the client that the last chunk
has been sent and that the reply is completed.


The optional *headers* argument is a list of HTTP headers.
This works the same way as the corresponding argument to
`sendReply()`.  With a chunked reply, you can send headers at the
beginning of the reply when you call `startChunkedReply()`, at the
end of the reply when you call this method, or both.  Sending headers
at the end of the reply is useful when there's a header you can't
determine until you've generated the whole reply body.


This method must be called exactly once for a chunked reply, after
sending all of the pieces of a chunked reply.  After calling this method,
the request is completed, and no further reply can be sent.


`getBody()`


Returns the unparsed request message body as a [File](file.md) object.  The file is open with read-only
access.  The file is open in text mode if the Content-Type header
specifies a text-oriented MIME type (this includes posted form data),
or in "raw" mode for non-text MIME types.  Note that the client
determines the Content-Type header, and this is often just a guess
based on heuristics (such as the filename suffix), so it's not
necessarily reliable.  You can override the initial file mode if
necessary via the file's `setFileMode` method.


If the request doesn't have a message body, the method returns `nil`.
If the message body exceeds the upload size limit set in the
[HTTPServer](httpsrv.md) object, the method returns
the string `'overflow'`.


Some HTTP requests, such as POST and PUT, can include additional
data in the form of a message body.  This is essentially a file or
other data stream uploaded by the client.  The most common use in Web
browsers is to send the user-entered data on an HTML form, including
files uploaded via a form.


Note that you won't usually need to access the raw message body for
a POST, since it's much more convenient to use [`getFormFields`](#getFormFields), which parses the message
body using the standard HTTP encodings for form fields.
The unparsed POST body is useful mostly if you're handling
requests from custom clients that use custom form encodings.


`getClientAddress()`


Retrieves the network address of the client making the request.  The
return value is a list:


- [1] is a string giving the client's IP address, in decimal
     notation (e.g., '192.168.1.15')
- [2] is an integer giving the network port number on the client machine


`getCookie(name)`


Returns a string containing the value of the cookie identified by the
given *name* string.  This searches the cookies sent by the client
with the request for the given name; if a cookie with this name is found,
its text is returned, otherwise the return value is `nil`.


`getCookies()`


Returns a LookupTable with the HTTP cookies sent by the client with
the request.  Each cookie name is a key in the table, with the cookie
text as the corresponding value.


By design, HTTP is a "stateless" protocol, meaning that each
request that a client makes is a complete transaction, independent of
any past or future requests made by the same client.  However, many
server applications want to maintain some continuity from one request
to the next, to present a user interface that responds to the user's
actions throughout the session.  This is where cookies come in:
they're a way for the server to store information on the client side,
so that the server can tell how a new request is related to a previous
request.


The cookie mechanism is simple.  Each cookie is actually an
name/value pair, where the name and value are arbitrary text strings
chosen by the server.  For example, the server could remember the
logged-in user by setting a cookie with name 'USERNAME' and value
'BOB'.  The server can send one or more cookies with the response to a
request, via the 'Set-Cookie' header.  Upon receiving a response with
a Set-Cookie header, the client browser simply stores the name/value
pair for later retrieval.  Once a cookie is stored, the browser sends
it back with each subsequent request to the same site, via the
'Cookie' header.  The browser simply echoes back the same name/value
pairs the server sent in past requests, so the server can use the
information to connect the new request to the previous request that
set the cookie.


You can find more information on how cookies work in general in
many HTTP reference materials on the Web.


<a name="getFormFields"></a><a name="sendReply"></a>

`sendReply(body, contentType?, status?, headers?)`


Sends your reply to the request.


*body* is the content of the reply, which is typically
displayed in the client Web browser.  This might be an HTML page, some
plain text, a JPEG image, a binary file, or almost any other
information you wish to send.  This argument can be represented as a
string, a [StringBuffer](strbuf.md), a [ByteArray](bytearr.md), or a [File](file.md).


The formatting of the reply depends on the type of object used
for the *body* argument:


- String: the reply is sent as
  Unicode text formatted in the UTF-8 encoding.  This is a standard
  reply format that all modern browsers accept, and should be used for
  transmitting any textual information, such as HTML or plain text.
- StringBuffer: same as String.
- ByteArray: the reply is sent as the raw binary bytes of the
  byte array.  This allows you to send binary files, such as JPEG images
  or audio files.
- File: the reply format depends on the file mode.  If the file was
  opened in Text mode, the reply is sent as Unicode text in the UTF-8
  encoding.  If the file was opened in Raw mode, the reply is sent as
  raw binary bytes.  Data mode isn't allowed.
  The file must have been opened with at
  least Read access.  The reply will send the *entire* contents of
  the file: this methods seeks to the start of the file, then reads and
  sends the entire file.  As a side effect, the seek position of the
  file is at the very end of the file when this routine returns.
- Integer: the value must be a valid HTTP status code.  The reply
  is sent as a default HTML page generated for the status code.  For example,
  if the *body* value is 404, this generates a default "404 Not Found"
  error page in HTML format as the reply.  In this case, the *contentType*
  and *status* arguments are ignored: we know that the reply's content type
  is "text/html", and we use the *body* value as the status code.
  This option makes it convenient to send simple error replies, since
  all you have to do is specify the error code number.
- nil: the reply is sent without a message body; only the headers
  are sent.  The Content-Type and Content-Length headers are not automatically
  inserted in this case, and the *contentType* argument is ignored.


The optional *contentType* argument lets you specify the MIME
type of the reply.  This is given as a string.  A MIME type is an
Internet standard scheme that identifies data formats; this tells the
client browser how to interpret and display the content you send.  You
can find much more information on MIME types in reference material on
the Web, but here are a few common ones:


- 'text/html' - an HTML document
- 'text/xml' - an XML document
- 'text/plain' - plain text (without any markups or formatting codes)
- 'image/jpeg' - a JPEG image
- 'image/gif' - a GIF image
- 'image/png' - a PNG image
- 'audio/mpeg' - an MP3 audio file
- 'application/octet-stream' - any raw binary file


If you omit *contentType*, the method tries to infer the type
automatically based on the *body* argument.  If the *body*
is given as a string or StringBuffer, or a Text-mode file, one of the
'text' types is used; the system looks at the first section of the
text to see if it looks like HTML or XML source code, and if not the
default is 'text/plain'.  If *body* is a ByteArray or Raw-mode
file, one of the binary types is assumed.  The method looks at the
first few bytes of the file's contents to see if it looks like a JPEG
image, GIF image, PNG image, MP3 audio file, Ogg Vorbis audio file, or
MIDI file, or Flash object; if it finds the standard format header for
one of these types, it uses the corresponding MIME type.  Otherwise,
the default is 'application/octet-stream', which is the generic binary
file type.


The optional *status* is the HTTP status code to include in
the response.  This can be given as a string in the standard HTTP
"code-number message-text" format, such as '200 OK' or '404 Not Found'.
It can alternatively be an integer giving a standard HTTP status
code number, in which case the system will automatically supply
the standard corresponding message text.  If you omit *status*,
the default is '200 OK'.


*headers* is an optional list of header strings.  Each element
of the list must be a string in the standard 'Name: Value' format for
an HTTP reply header.  If you omit this argument, the reply will only
contain the basic headers that the server automatically generates,
which are:


- Content-Type: per the *contentType* argument
- Content-Length: length in bytes of the *body* value


A request can only have one reply, so you can only call this method
once on a given request.  A NetException is thrown if you try to reply
to the same request more than once.  Sending a reply has the effect
of completing the request on the client side, so the client will know
that it doesn't have to wait for any more data from the server as part
of this request.


<a name="sendReplyAsync"></a>

`sendReplyAsync(body, contentType?, status?, headers?)`


This method sends a reply asynchronously - that is, in a background
thread that runs concurrently with the main program.  This works like
[sendReply()](#sendReply), except that sendReply() doesn't
return until all of the reply data have been sent over the network
connection, whereas sendReplyAsync() launches a background thread to
carry out the data transfer and then returns immediately, without
waiting for any data to be sent.


The parameters are the same as for sendReply().  There's no return
value.


When the transfer completes, the system posts a network event of
type [NetEvReplyDone](../functions/tadsnet.md#NetEvReplyDone) to the
network event queue.  You can retrieve the event with
[getNetEvent()](../functions/tadsnet.md#getNetEvent).  The event
object has a reference to the HTTPRequest object, which lets you
relate the event back to the request that you were replying to, and
information on whether the reply succeeded or failed.  This is largely
advisory, useful mostly for purposes such as logging, since there's
not much the server can do if the reply data transfer fails.  HTTP
doesn't provide any way for a server to initiate contact with a
client, so when a reply fails, it's up to the client to take any
needed recovery action, which in most cases is simply to retry the
request.


If the *body* argument is a StringBuffer or ByteArray, the
method makes a private copy of the contents before returning, so any
changes you make to the object after the function returns won't affect
the data transmitted to the client.  If it's a File, the method
doesn't make a copy (doing so would be too big a performance hit for
large files), so if you write to the file after the method returns,
the transmitted data might be affected.  It's not advisable to do
this, because it could cause inconsistent data to be sent to the
client.  If the file is a read-only resource file, this obviously
isn't a concern.  When you send a file that you plan to modify in the
near future, though, you should be careful to avoid concurrent
updates.  One way to handle this is by waiting to do your updates
until the completion event (described above) is posted.  A simpler
(but slower) way is to create a temporary copy of the file for
sendReplyAsync().  For example:


```tads3
// send the current contents of a file we're actively
// updating - 'fp' is a File object, 'req' is the request
// we're replying to
sendActiveFile(fp, req)
{
    // create a temporary file
    local tempfile = new TemporaryFile();
    local fptemp = File.openRawFile(tempfile, FileAccessReadWriteTrunc);

    // remember the current seek position in the original file
    local origPos = fp.getPos();

    // copy the original file's contents into the temp file
    fptemp.writeBytes(fp, 0);

    // restore the original seek position
    fp.setPos(origPos);

    // send the request using the temporary file
    req.sendReplyAsync(fptemp);

    // we're done with the temporary file
    fptemp.closeFile();
}
```


When the *body* is a File, you're free to close the file any
time after the method returns.  (You can also keep it open if you plan
to continue accessing the file.)  The method creates its own duplicate
handle to the file internally, so the background thread sending the
data can continue to access the file as needed even after you call
closeFile() on your File object.


Asynchronous replies are useful when sending large content bodies,
such as image or audio files.  The client of an HTTP connection is
usually a Web browser, and most modern browsers download media objects
in background threads on the client side, so that the user interface
remains responsive while the downloads proceed, rather than making the
user wait for all of the images and sounds to download before
interacting with the page.  For the TADS Web UI, this means that the
browser can generate new XML requests while images and sounds are
being transferred over the network.  If the game program sends a large
file with sendReply(), it won't be able to service any new XML
requests until the entire file transfer has completed, since
sendReply() won't return until the transfer is done.  This makes the
user interface in the browser appear unresponsive for the duration of
the download, since the game server won't reply to any XML requests
generated by the browser during this period.  sendReplyAsync()
addresses this by letting you initiate the transfer of a large file
and then immediately return to servicing other requests, without
waiting for the file transfer to finish.  The file transfer will
proceed in the background thread, leaving the main program free to
respond to new requests.


`sendReplyChunk(chunk)`


Sends one piece of a "chunked" reply.  The *chunk* argument works
the same way as the *body* argument to `sendReply()`, so it can
be a string, StringBuffer, or ByteArray.


This method can be called repeatedly to send a reply in pieces.
You must call `startChunkedReply()` before the first call to
`sendReplyChunk()` for a request, and you must call
`endChunkedReply()` after sending the last chunk for the request.
See `startChunkedReply()` for more details.


`startChunkedReply(contentType, resultCode?, headers?)`


Starts sending a "chunked" reply to the request.  A chunked reply is
one that's sent in pieces, rather than all at once.  When you use
`sendReply()`, you must have the entire reply ready to go as a
single unit at the time you call the method.  In contrast, the chunked
reply methods let you assemble the reply a little bit at a time,
sending each piece as soon as it's ready.  This is especially useful
when the reply involves a large amount of data that's generated
dynamically, because it avoids the need to store the entire generated
data stream in memory at one time.


Sending a chunked reply involves three steps:


- Call `startChunkedReply()` to begin the reply.
- Call `sendReplyChunk()` for each chunk - each piece of
     data you wish to send in the reply.
- Call `endChunkedReply()` to finish the reply.


The *contentType*, *resultCode*, and *headers*
arguments work almost the same way they do with `sendReply()` - see
that method for full details.  There are two small differences,
though.  First, *contentType* is required with this method,
whereas it's optional with `sendReply()`.  The reason is that this
method doesn't have the reply content to work with - that'll be sent
later, in pieces, via one or more calls to `sendReplyChunk()`, so
there's no way for `startChunkedReply()` to infer the content type
from the data.  The second difference is that any headers you include
in this call aren't the last word: you'll get another chance to send
more headers with `endChunkedReply()`.  This is useful if some of
the headers depend on the content you're going to send, which you
might not have generated yet.


## Save, restore, undo


HTTPRequest objects are inherently [transient](../../language/objdef.md#transient).  This is because they're
associated with live network requests; saving and restoring the
program would resume with a new session without the same network client
connected, so it would be impossible to continue processing a request
from the original session at that time.


## Server shutdown


When you shut down an HTTPServer object, all of the client sessions
are terminated and the open requests aborted.  This is true whether
you shut down a server by explicitly calling the HTTPServer
`shutdown()` method, or by allowing the HTTPServer object to go out
of scope and be collected by the garbage collector.  Replying to an
aborted request is invalid and will throw a NetException error.
