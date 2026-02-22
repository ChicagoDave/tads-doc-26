# flushEventsPage

*object* — defined in [webui.t](../by-file/webui.t.md) (line 1437)


Flush events. This cancels any pending event requests for the client. The client can use this after being reloaded to flush any outstanding event requests from a past incarnation of the page.


**Superclass chain:** [WebResource](webresource.md) > `object` > **flushEventsPage**


## Properties


### `vpath` *(overridden)*

Defined in webui.t, line 1438


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 1439


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
