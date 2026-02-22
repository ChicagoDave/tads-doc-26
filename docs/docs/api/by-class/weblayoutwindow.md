# WebLayoutWindow

*class* — defined in [webui.t](../by-file/webui.t.md) (line 1778)


Layout Window. This is a specialized Web Window tracker for our layout page type, which is displayed using the resource file webuires/layout.htm. This page is designed as a container of more specialized sub-window pages; its job is to divide up the window space into IFRAME elements that display the sub-windows, and to manage the geometry of the IFRAMEs.


**Superclass chain:** [WebWindow](webwindow.md) > [WebResourceResFile](webresourceresfile.md) > [WebResource](webresource.md) > `object` > **WebLayoutWindowGlobal objects:** [webMainWin](webmainwin.md)


## Properties


### `frames`

Defined in webui.t, line 1924

The table of active frames within this layout. This table is keyed by window name; each entry is a list of [win, pos], where 'win' is the WebWindow object for the window, and 'pos' is its position parameter.


### `src` *(overridden)*

Defined in webui.t, line 1928


### `vpath` *(overridden)*

Defined in webui.t, line 1927

my virtual path and the actual resource file location


## Inherited Properties


*From [WebWindow](webwindow.md):* [`name`](webwindow.md#name), [`pathName`](webwindow.md#pathName), [`sthCtx`](webwindow.md#sthCtx)


*From [WebResourceResFile](webresourceresfile.md):* [`binaryExts`](webresourceresfile.md#binaryExts), [`browserExtToMime`](webresourceresfile.md#browserExtToMime)


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `createFrame(win, name, pos)`

Defined in webui.t, line 1873

Create a new window within the layout. This creates an IFRAME in the browser, laid out according to the 'pos' argument, and displays the given window object within the frame.


### `flushWin` *(overridden)*

Defined in webui.t, line 1894

Flush this window. For a layout window, we simply flush each child window.


### `getState(client)` *(overridden)*

Defined in webui.t, line 1903

Get the state.


### `winFromPath(path)` *(overridden)*

Defined in webui.t, line 1782

Resolve a window path name


## Inherited Methods


*From [WebWindow](webwindow.md):* [`clearWindow`](webwindow.md#clearWindow), [`processName`](webwindow.md#processName), [`sendWinEvent`](webwindow.md#sendWinEvent), [`sendWinEventTo`](webwindow.md#sendWinEventTo), [`write`](webwindow.md#write)


*From [WebResourceResFile](webresourceresfile.md):* [`isTextFile`](webresourceresfile.md#isTextFile), [`matchRequest`](webresourceresfile.md#matchRequest), [`processRequest`](webresourceresfile.md#processRequest)


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
