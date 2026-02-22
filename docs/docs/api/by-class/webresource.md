# WebResource

*class* — defined in [webui.t](../by-file/webui.t.md) (line 798)


A WebResource is a virtual file accessible via the HTTP server. Each resource object has a path, which can be given as a simple string that must be matched exactly, or as a RexPattern object with a regular expression to be matched. Each object also has a "processRequest" method, which the server invokes to answer the request when the path is matched.


**Superclass chain:** `object` > **WebResourceSubclasses:** [WebResourceResFile](webresourceresfile.md), [WebWindow](webwindow.md), [WebCommandWin](webcommandwin.md), [WebLayoutWindow](weblayoutwindow.md), [WebStatusWin](webstatuswin.md)


**Global objects:** [eventPage](eventpage.md), [flushEventsPage](flusheventspage.md), [guestConnectPage](guestconnectpage.md), [inputDialogPage](inputdialogpage.md), [inputEventPage](inputeventpage.md), [inputFileCancel](inputfilecancel.md), [inputFilePage](inputfilepage.md), [inputLinePage](inputlinepage.md), [menuSysEventPage](menusyseventpage.md), [morePromptDonePage](morepromptdonepage.md), [setPrefsPage](setprefspage.md), [setScreenNamePage](setscreennamepage.md), [tempFileDownloadPage](tempfiledownloadpage.md), [uiStatePage](uistatepage.md), [uploadFilePage](uploadfilepage.md)


## Properties


### `group`

Defined in webui.t, line 865

The group this resource is part of. This is the object that "contains" the resource, via its 'contents' property; any object will work here, since it's just a place to put the contents list for the resource group.


### `priority`

Defined in webui.t, line 849

The priority of this resource. If the path is given as a regular expression, a given request might match more than one resource. In such cases, the matching resource with the highest priority is the one that's actually used to process the request.


### `vpath`

Defined in webui.t, line 827

The virtual path to the resource. This is the apparent URL path to this resource, as seen by the client.


## Methods


### `matchRequest(query, req)`

Defined in webui.t, line 883

Determine if this resource matches the given request. 'query' is the parsed query from the request, as returned by req.parseQuery(). 'req' is the HTTPRequest object representing the request; you can use this to extract more information from the request, such as cookies or the client's network address.


### `processRequest(req, query)`

Defined in webui.t, line 837

Process the request. This is invoked when we determine that this is the highest priority resource object matching the request. 'req' is the HTTPRequest object; 'query' is the parsed query data as returned by req.parseQuery(). The query information is provided for convenience, in case the result depends on the query parameters.


### `sendAck(req, xml, =, ', <, ok, /, >, ')`

Defined in webui.t, line 911

Send a generic request acknowledgment or reply. This wraps the given XML fragment in an XML document with the root type given by the last element in our path name. If the 'xml' value is omitted, we send "<ok/>" by default.


### `sendXML(req, root, xml)`

Defined in webui.t, line 932

Send an XML reply. This wraps the given XML fragment in an XML document with the given root element.
