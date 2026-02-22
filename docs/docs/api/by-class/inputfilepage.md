# inputFilePage

*object* — defined in [webui.t](../by-file/webui.t.md) (line 3471)


File dialog event page. This page is used by the IFDB Storage Server file dialog to return information to the game UI. The IFDB dialog page can't itself perform scripting actions on the enclosing dialog frame, since it's being served from a different domain - browsers prohibit cross-domain scripting for security reasons. The IFDB dialog must therefore navigate back to a page within the game server domain in order to return information through scripting. This is that page: when the IFDB page is ready to return information, it navigates its frame to this page, passing the return values in the request parameters. Since this page is served by the game server, within the game server domain, the browser allows it to use scripting actions on its enclosing frame. We finish the job by dismissing the dialog in the UI.


**Superclass chain:** [WebResource](webresource.md) > `object` > **inputFilePage**


## Properties


### `vpath` *(overridden)*

Defined in webui.t, line 3472


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 3473


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
