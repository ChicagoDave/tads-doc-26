# HTTPServer

*class* — defined in [httpsrv.h](../by-file/httpsrv.h.md) (line 82)


HTTP Server Object. This implements a multi-threaded, background server that runs concurrently with the game program. The server listens for and accepts incoming connection requests from clients, and then handles HTTP protocol transactions with connected clients. Client requests are routed to the byte code program via network events, which the program can retrieve via the getNetEvent() function.


**Superclass chain:** [Object](object.md) > **HTTPServer**


## Methods


### `getAddress`

Defined in httpsrv.h, line 120

Get the listening address. This returns a string giving the original binding address specified when the object was constructed. This can contain either a host name or an IP address, since either form can be used in the constructor.


### `getIPAddress`

Defined in httpsrv.h, line 126

Get the listening IP address. This returns the numerical IP address where the server is listening for connections.


### `getPortNum`

Defined in httpsrv.h, line 136

Get the port number. This returns an integer giving the TCP/IP network port number on which this server is listening for incoming connections. Clients connect to the port by including it in the HTTP URL, after the host name. For example, if the server is on port 10815, the client would connect to a URL of the form http://myserver.com:10815/index.htm.


### `shutdown(wait?)`

Defined in httpsrv.h, line 112

Shut down the server. This immediately disconnects the server from its network port; no further client connections will be accepted once the server shuts down. In addition, all of the server threads that were started by this server object will be notified to terminate.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
