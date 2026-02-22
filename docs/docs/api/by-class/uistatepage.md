# uiStatePage

*object* — defined in [webui.t](../by-file/webui.t.md) (line 1464)


getState request. The web page can send this to get a full accounting of the current state of the UI. It does this automatically when first loaded, and again when the user manually refreshes the page.


**Superclass chain:** [WebResource](webresource.md) > `object` > **uiStatePage**


## Properties


### `vpath` *(overridden)*

Defined in webui.t, line 1465


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 1466


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
