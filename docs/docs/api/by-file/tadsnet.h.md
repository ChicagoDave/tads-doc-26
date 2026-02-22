# tadsnet.h


## Classes

- connectWebUI
- getHostName
- getLaunchHostAddr
- getLocalIP
- getNetEvent
- getNetStorageURL
- sendNetRequest


## Functions


### `connectWebUI(server, path)`

Defined in tadsnet.h, line 54

Connect to the Web UI client. This connects the Web browser client to the game's HTTP server. 'server' is the HTTPServer object where the Web UI is found, and 'path' is the URL path of the game's main UI start page. This will tell the client to navigate to the given start path on the given server.


### `getHostName`

Defined in tadsnet.h, line 96

Get the local network host name. This is the name (or a name) that other computers can use to connect to this computer across the network.


### `getLaunchHostAddr`

Defined in tadsnet.h, line 149

Get the host address that the user used to launch the game. For standard client/server TADS Web play, this is the network address that you should specify as the listening address when setting up the HTTPServer object.


### `getLocalIP`

Defined in tadsnet.h, line 112

Get the local host's IP address. This is the IP address (or an IP address) that other computers can use to connect to this computer via the network. IP addresses are the basic addressing scheme of the Internet.


### `getNetEvent(timeout?)`

Defined in tadsnet.h, line 72

Read an event from the network message queue. When a listener receives a connection request from a client, it creates a network server thread to handle the connection; then when the server thread receives data from the client, it packages the data into an event message and places it in the queue. This function retrieves the next message from the queue.


### `getNetStorageURL(resource)`

Defined in tadsnet.h, line 126

Get the URL to the storage server. When running in Web mode, the interpreter is generally configured to store files on a separate "storage server" rather than on the game server. This function retrieves the interpreter's configuration data and returns the storage server URL.


### `sendNetRequest(id, url, ...)`

Defined in tadsnet.h, line 214

Send a network request to a remote server. This initiates processing the request and immediately returns; the process of setting up the network connection to the remote server, sending the request data, and receiving the reply proceeds asynchronously while the program continues running. When the request completes (or fails due to an error), a NetEvent of type NetEvReply is queued.
