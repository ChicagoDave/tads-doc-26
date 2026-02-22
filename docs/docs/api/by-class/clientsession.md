# ClientSession

*class* — defined in [webui.t](../by-file/webui.t.md) (line 379)


Client session. This represents a connection to one browser (or other client application). Each browser client is a separate session, so we create one instance of this class per connected browser. Note that browser instances don't necessarily represent different users - a single user could open multiple browser windows on the same server.


**Superclass chain:** `object` > **ClientSession**


## Properties


### `clientKey`

Defined in webui.t, line 439

The client session key. This identifies the client across requests. We send this to the client as a cookie when they connect, so we get it back on each request.


### `downloads`

Defined in webui.t, line 619

this client's list of downloadable temporary files


### `ifdbTuid`

Defined in webui.t, line 422

the client's IFDB user ID (a "TUID"), if logged in to IFDB


### `isAlive`

Defined in webui.t, line 463

Is this session alive? When we detect that the client has disconnected, we'll set this to nil. When waiting for a client in a modal event loop, this can be used to terminate the wait if the client disconnects.


### `isPrimary`

Defined in webui.t, line 455

Am I the primary player? This is true if the player connected using the primary session key. Collaborative players join through the separate collaborative session key.


### `lastEventTime`

Defined in webui.t, line 472

Last request time, in system ticks (ms). We use this to determine how long it's been since we've heard from the client, for timeout purposes. This is updated any time we receive a command or event request from the client, and each time we successfully send an event reply.


### `pendingEvts`

Defined in webui.t, line 432

The client's event queue. When a server-to-client event occurs, we post it to each current client's queue. When the client sends a get-event request, we satisfy it out of this queue.


### `pendingReqs`

Defined in webui.t, line 425

the list of pending event requests from this client


### `screenName`

Defined in webui.t, line 406

The client's "screen name" - this is the user-visible name that we'll show other users to identify commands and chat messages entered by this client.


### `storageSID`

Defined in webui.t, line 448

The storage server session key for the user connected to this session, if any. We can have multiple users logged in to the game in collaborative play mode, each with their own separate storage server session. This allows each user to have their own private preference settings, saved games, etc.


### `uiPrefs`

Defined in webui.t, line 399

the UI preferences object for this session


## Methods


### `addDownload(desc)`

Defined in webui.t, line 597

add a download to this client


### `allDownloads`

Defined in webui.t, line 622

get a list of all of my downloadable files


### `broadcastDownload(desc)`

Defined in webui.t, line 590

broadcast a downloadable file to all clients


### `broadcastEvent(msg)`

Defined in webui.t, line 478

class method: broadcast an event message to all connected clients


### `cancelDownload(desc)`

Defined in webui.t, line 607

Cancel a downloadable file. Removes the file from the download list and notifies the client that the file is no longer available.


### `checkDisconnect`

Defined in webui.t, line 693

Check to see if the client is still alive. If the client has no pending event requests, and we haven't heard from the client in more than the client session timeout interval, assume the client is no longer connected and kill the session object.


### `construct(skey, ssid)`

Defined in webui.t, line 380


### `disconnectAll`

Defined in webui.t, line 714

Class method: forcibly disconnect all clients. This simply deletes the list of active clients and deletes any pending events in their queues. This doesn't actually terminate their network connections, but simply clears out any pending work for each client that we've initiated on the server side.


### `find(key)`

Defined in webui.t, line 727

Class method: Find a client session, given the session key or an HTTPRequest object.


### `flushEvents`

Defined in webui.t, line 501

flush outstanding events for this client


### `getPrimary`

Defined in webui.t, line 755

Get the primary session. This is the session for the original initiating user (the "host" in a multi-user game).


### `processQueues`

Defined in webui.t, line 625

process the request and response queues


### `requestEvent(req)`

Defined in webui.t, line 493

receive an event request from the client


### `sendEvent(msg)`

Defined in webui.t, line 485

send an event to this client


### `sendKeepAlive`

Defined in webui.t, line 553

Send a keep-alive reply to each pending request from this client that's been waiting for longer than the timeout interval.


### `setDefaultScreenName`

Defined in webui.t, line 409

set the default screen name for a client


### `shutdownWait(timeout)`

Defined in webui.t, line 675

wait for the queues to empty in preparation for shutting down


### `updateEventTime`

Defined in webui.t, line 475

update the last event time for this client
