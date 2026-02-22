# tempFileDownloadPage

*object* — defined in [webui.t](../by-file/webui.t.md) (line 3237)


Temporary file download page. This page serves temporary files created via inputFile() as HTTP downloads to the client.


**Superclass chain:** [WebResource](webresource.md) > `object` > **tempFileDownloadPage**


## Properties


### `nextID`

Defined in webui.t, line 3359

next available ID


### `vpath` *(overridden)*

Defined in webui.t, line 3238


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `addFile(fileType, client)`

Defined in webui.t, line 3319

add a file to our list of downloadable files


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 3239


## Inherited Methods


*From [WebResource](webresource.md):* [`matchRequest`](webresource.md#matchRequest), [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
