# webSession

*object* — defined in [webui.t](../by-file/webui.t.md) (line 145)


Web UI Session object. This keeps track of miscellaneous items associated with the game session.


**Superclass chain:** `object` > **webSession**


## Properties


### `clientSessions`

Defined in webui.t, line 272

list of active client sessions (ClientSession objects)


### `collabKey`

Defined in webui.t, line 199

The collaborative session key. This is a secondary session key that allows additional users to connect to the session for collaborative play.


### `everHadClient`

Defined in webui.t, line 352

have we ever had a client connection?


### `hkTime`

Defined in webui.t, line 346

system time (ms ticks) of next scheduled housekeeping pass


### `lastClientTime`

Defined in webui.t, line 349

the last time we noticed that we had a client connected


### `launcherGameID`

Defined in webui.t, line 236

The launcher's game ID. This is the ID passed from the web server that launched the game, to let us know how the game is identified in the launcher database. This is typically an IFDB TUID string.


### `launcherUsername`

Defined in webui.t, line 243

The launcher's user name. This is passed from the web server that launched the game, to let us know the host user's screen name. We use this as the user's default screen name in multi-user games.


### `server`

Defined in webui.t, line 290

the HTTPServer object running our web session


### `sessionKey`

Defined in webui.t, line 192

The session key. This identifies the server as a whole, and is essentially an authentication mechanism that lets clients prove they got our address from an authorized source (rather than just stumbling across it via a port scan, say). Clients must hand this to us on each request, either via a URL query parameter or via a cookie. The normal setup (via WebResourceInit) is for the client to send us the key as a URL parameter on the initial request, at which point we'll pass it back as a set-cookie, removing the need for the client to include the key in subsequent URLs.


### `storageSID`

Defined in webui.t, line 257

The primary storage server session ID, for the user who launched the server. If the user who launched the game logged in to a cloud storage server, this is the session ID that we use to transact business with the server on behalf of this logged-in user. This token identifies and authenticates the user, but it's ephemeral and it's only valid for the current game server session, so it's not quite like a password. This is the session for the launch user only; if other collaborative users join, they can get their own session IDs that will allow them to store files under their own private user folders on the server.


## Methods


### `addClient(s)`

Defined in webui.t, line 275

add a client session


### `connectUI(srv)`

Defined in webui.t, line 160

Connect to the UI. By default, we ask the webMainWin object to establish a connection, and we save the server object internally for future reference.


### `getCollabUrl`

Defined in webui.t, line 264

Get the collaborative player launch URL. This is a URL that the host can send to other players who wish to join the session as collaborative users.


### `getFullUrl(resname)`

Defined in webui.t, line 149

Get the full URL to the given resource.


### `housekeeping`

Defined in webui.t, line 297

Run housekeeping tasks. The network event processor calls this periodically to let us perform background cleanup tasks. Returns the system tick time of the next housekeeping run.


### `removeClient(s)`

Defined in webui.t, line 283

remove a client session


### `validateKey(req, query)`

Defined in webui.t, line 204

Validate a session key sent from the client
