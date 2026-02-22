# eventPage

*object* — defined in [webui.t](../by-file/webui.t.md) (line 1397)


getEvent request. This is the mechanism we use to "send" events to the client. The client sends a getEvent request to us, and we simply put it in a queue - we don't send back any response immediately. As soon as we want to send an event to the client, we go through the queue of pending getEvent requests, and reply to each one with the event we want to send.


**Superclass chain:** [WebResource](webresource.md) > `object` > **eventPage**


## Properties


### `vpath` *(overridden)*

Defined in webui.t, line 1398


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 1399


### `sendEvent(msg)`

Defined in webui.t, line 1412

broadcast an event message to each client


### `sendEventTo(msg, client)`

Defined in webui.t, line 1422

send an event to a particular client


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
