# WebStatusWin

*class* — defined in [webui.t](../by-file/webui.t.md) (line 2575)


Status line window


**Superclass chain:** [WebWindow](webwindow.md) > [WebResourceResFile](webresourceresfile.md) > [WebResource](webresource.md) > `object` > **WebStatusWinGlobal objects:** [statuslineBanner](statuslinebanner.md)


## Properties


### `deltas_`

Defined in webui.t, line 2684

do we have any deltas since the last flush?


### `src` *(overridden)*

Defined in webui.t, line 2578


### `txt_`

Defined in webui.t, line 2687

the current status message


### `vpath` *(overridden)*

Defined in webui.t, line 2577

my request path and actual resource path


## Inherited Properties


*From [WebWindow](webwindow.md):* [`name`](webwindow.md#name), [`pathName`](webwindow.md#pathName), [`sthCtx`](webwindow.md#sthCtx)


*From [WebResourceResFile](webresourceresfile.md):* [`binaryExts`](webresourceresfile.md#binaryExts), [`browserExtToMime`](webresourceresfile.md#browserExtToMime)


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `clearWindow` *(overridden)*

Defined in webui.t, line 2644

clear the window


### `flushWin` *(overridden)*

Defined in webui.t, line 2650

flush pending text to the window


### `getState(client)` *(overridden)*

Defined in webui.t, line 2678

get the current state to send to the browser


### `resize`

Defined in webui.t, line 2675

Refigure the window size. The status line is generally set up to be automatically sized to its contents, which requires that we tell the UI when it's time to recalculate the layout to reflect the current contents after a change.


### `setStatus(room, score?, turns?)`

Defined in webui.t, line 2589

Set the room and score/turns portions of the status line. This sets the left side of the status line to the 'room' text (which can contain HTML markups), and the right side to the the score/turns values, if present. If the turn counter is omitted but the score value is present, we'll just show the score value; otherwise we'll format these as "score/turns". If no score value is present, we'll leave the right side blank.


### `setStatusText(msg)`

Defined in webui.t, line 2620

Set the text of the status line. This sets the entire status window to the given HTML text, without any additional formatting.


### `write(msg)` *(overridden)*

Defined in webui.t, line 2634

add text to the status line


## Inherited Methods


*From [WebWindow](webwindow.md):* [`processName`](webwindow.md#processName), [`sendWinEvent`](webwindow.md#sendWinEvent), [`sendWinEventTo`](webwindow.md#sendWinEventTo), [`winFromPath`](webwindow.md#winFromPath)


*From [WebResourceResFile](webresourceresfile.md):* [`isTextFile`](webresourceresfile.md#isTextFile), [`matchRequest`](webresourceresfile.md#matchRequest), [`processRequest`](webresourceresfile.md#processRequest)


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
