# WebWindow

*class* — defined in [webui.t](../by-file/webui.t.md) (line 1667)


Web Window tracker. This is a game object that controls and remembers the state of a "window" in the browser user interface. By "window", we basically mean an HTML page, which might reside at the top level of the browser itself, or inside an IFRAME element within an enclosing page.


**Superclass chain:** [WebResourceResFile](webresourceresfile.md) > [WebResource](webresource.md) > `object` > **WebWindowSubclasses:** [WebCommandWin](webcommandwin.md), [WebLayoutWindow](weblayoutwindow.md), [WebStatusWin](webstatuswin.md)


## Properties


### `name`

Defined in webui.t, line 1750

the name of this window


### `pathName`

Defined in webui.t, line 1753

the full path name of this window, in "win.sub.sub" format


### `src`

Defined in webui.t, line 1689

The window's actual source location, as a resource path. A given WebWindow subclass corresponds to a particular HMTL page, since the class and the page are facets of the same conceptual object (one facet is the browser expression, the other is the game program expression).


### `sthCtx`

Defined in webui.t, line 1747

specialsToHtml context


### `vpath` *(overridden)*

Defined in webui.t, line 1680

The URL path to the window's HTML definition file, as seen by the browser. For the pre-defined library window types, we expose the HTML file in the root of the URL namespace - e.g., "/main.htm". The files are actually stored in the /webuires folder, but we expose them to the browser as though they were in the root folder to make embedded object references on the pages simpler. The browser figures the path to an embedded object relative to the containing page, so by placing the containing page in the root folder, embedded object paths don't have to worry about referencing parent folders.


## Inherited Properties


*From [WebResourceResFile](webresourceresfile.md):* [`binaryExts`](webresourceresfile.md#binaryExts), [`browserExtToMime`](webresourceresfile.md#browserExtToMime)


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `clearWindow`

Defined in webui.t, line 1718

Clear the window. Subclasses must override this.


### `flushWin`

Defined in webui.t, line 1707

Flush the window. This sends any buffered text to the UI.


### `getState(client)`

Defined in webui.t, line 1728

Get the window's current state. This returns a string containing an XML fragment that describes the state of the window. This information is sent to the HTML page when the browser asks for the current layout state when first loaded or when the page is refreshed. The XML format for each subclass is specific to the Javascript on the class's HTML page.


### `processName(n)` *(overridden)*

Defined in webui.t, line 1692

process a request path referencing me into my actual resource path


### `sendWinEvent(evt)`

Defined in webui.t, line 1731

send an event related to this window to all clients


### `sendWinEventTo(evt, client)`

Defined in webui.t, line 1741

send a window event to a specific client


### `winFromPath(path)`

Defined in webui.t, line 1699

Resolve a window path name. For container windows, this should search the sub-windows for the given path. By default, we match simply if the path matches our name.


### `write(txt)`

Defined in webui.t, line 1713

Write text to the window. Subclasses with stream-oriented APIs must override this.


## Inherited Methods


*From [WebResourceResFile](webresourceresfile.md):* [`isTextFile`](webresourceresfile.md#isTextFile), [`matchRequest`](webresourceresfile.md#matchRequest), [`processRequest`](webresourceresfile.md#processRequest)


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
