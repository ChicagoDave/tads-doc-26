# inputFileCancel

*object* — defined in [webui.t](../by-file/webui.t.md) (line 3501)


Cancel the input dialog. This is called from the UI directly to cancel the file selection, when the user closes the dialog through the enclosing main page UI rather than from within the dialog. This is useful if the dialog page fails to load, for example.


**Superclass chain:** [WebResource](webresource.md) > `object` > **inputFileCancel**


## Properties


### `vpath` *(overridden)*

Defined in webui.t, line 3502


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 3503


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
