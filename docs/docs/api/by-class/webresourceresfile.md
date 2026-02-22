# WebResourceResFile

*class* — defined in [webui.t](../by-file/webui.t.md) (line 980)


A resource file request handler. This handles a request by sending the contents of the resource file matching the given name.


**Superclass chain:** [WebResource](webresource.md) > `object` > **WebResourceResFileSubclasses:** [WebWindow](webwindow.md), [WebCommandWin](webcommandwin.md), [WebLayoutWindow](weblayoutwindow.md), [WebStatusWin](webstatuswin.md)


**Global objects:** [coverArtResource](coverartresource.md), [webMainWin](webmainwin.md), [webuiResources](webuiresources.md)


## Properties


### `binaryExts`

Defined in webui.t, line 1083

table of common binary file extensions


### `browserExtToMime`

Defined in webui.t, line 1043

extension to MIME type map for important browser file types


## Inherited Properties


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority), [`vpath`](webresource.md#vpath)


## Methods


### `isTextFile(fname)`

Defined in webui.t, line 1061

Determine if the given file is a text file or a binary file. By default, we base the determination solely on the filename suffix, checking the extension against a list of common file types.


### `matchRequest(query, req)` *(overridden)*

Defined in webui.t, line 986

Match a request. A resource file resource matches if we match the virtual path setting for the resource, and the requested resource file exists.


### `processName(n)`

Defined in webui.t, line 1054

Process the name. This takes the path string from the query, and returns the resource file name to look for. By default, we simply return the same name specified by the client, minus the leading '/' (since resource paths are always relative).


### `processRequest(req, query)` *(overridden)*

Defined in webui.t, line 992

process the request: send the resource file's contents


## Inherited Methods


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
