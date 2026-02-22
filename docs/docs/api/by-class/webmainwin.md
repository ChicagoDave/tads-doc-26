# webMainWin

*object* — defined in [webui.t](../by-file/webui.t.md) (line 2714)


The standard "main window" of our user interface. This is the game object that represents the default initial HTML page that the player's web browser connects to. We build this out of three base classes:


**Superclass chain:** [WebResourceInit](webresourceinit.md) > `object` > [WebLayoutWindow](weblayoutwindow.md) > [WebWindow](webwindow.md) > [WebResourceResFile](webresourceresfile.md) > [WebResource](webresource.md) > **webMainWin**


## Properties


### `curCmdClient`

Defined in webui.t, line 2744

Client session for current command line input. Certain modal interactions, such as file dialogs, are directed only to the client that initiated the current command.


### `fileDialogResult`

Defined in webui.t, line 3202

file dialog result - this is a result list using the same format as the native inputFile() function


### `fileDialogState`

Defined in webui.t, line 3196

file dialog state - this is the XML describing the currently open file dialog; if the dialog isn't open, this is an empty string


### `inputDialogResult`

Defined in webui.t, line 3211

input dialog result - this is the button number the user selected


### `inputDialogState`

Defined in webui.t, line 3208

input dialog state - this is the XML describing an input dialog while a dialog is running, or an empty string if not


### `inputEventResult`

Defined in webui.t, line 3217

input event result


### `inputEventState`

Defined in webui.t, line 3214

input event state


### `menuSysState`

Defined in webui.t, line 3220

menuSys state - menu system state (maintained by the menu module)


### `name` *(overridden)*

Defined in webui.t, line 2723

the top window is always called "main"


### `pathName` *(overridden)*

Defined in webui.t, line 2724


### `synthEventQueue`

Defined in webui.t, line 3229

Synthetic event queue. This is a vector of synthetic events, set up in the [type, params...] format that the system inputEvent() function and related functions use. The 'type' code for a synthetic evente is a string instead of the numeric identifier that the system functions use.


### `title`

Defined in webui.t, line 2727

the window title


### `vpath` *(overridden)*

Defined in webui.t, line 2719

match the webuires directory path as the URL path, but map this to main.htm as the underlying resource name


## Inherited Properties


*From [WebResourceInit](webresourceinit.md):* [`server`](webresourceinit.md#server)


*From [WebLayoutWindow](weblayoutwindow.md):* [`frames`](weblayoutwindow.md#frames), [`src`](weblayoutwindow.md#src)


*From [WebWindow](webwindow.md):* [`sthCtx`](webwindow.md#sthCtx)


*From [WebResourceResFile](webresourceresfile.md):* [`binaryExts`](webresourceresfile.md#binaryExts), [`browserExtToMime`](webresourceresfile.md#browserExtToMime)


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `getInputDialog(icon, prompt, buttons, defaultButton, cancelButton)`

Defined in webui.t, line 3100

show a generic inputDialog dialog


### `getInputEvent(timeout)`

Defined in webui.t, line 2779

wait for an input event


### `getInputFile(prompt, dialogType, fileType, flags)`

Defined in webui.t, line 2835

show the file selector dialog


### `getInputFileFromClient(prompt, dialogType, fileType, flags)`

Defined in webui.t, line 2912

Get an input file from the client PC. We'll attempt to upload or download a file from/to the client PC, using a local temporary file for the actual file operations. This is a special form of the input file dialog that we use when we're not connected to a storage server.


### `getState(client)` *(overridden)*

Defined in webui.t, line 2747

get the state


### `getSyntheticEvent`

Defined in webui.t, line 3190

pull the next synthetic event from the queue


### `inputFileDismissed`

Defined in webui.t, line 3033

receive notification that the file dialog has been closed


### `offerDownload(file)`

Defined in webui.t, line 2986

Offer a file for download to the client. 'file' is a DownloadTempFile object previously created by a call to inputFile().


### `postSyntheticEvent(id, [params])`

Defined in webui.t, line 3180

Post a synthetic event. A synthetic event looks like a regular UI or network event, but is generated internally instead of being delivered from the underlying browser or network subsystems.


### `processName(n)` *(overridden)*

Defined in webui.t, line 2720


### `receiveFileSelection(req, query)`

Defined in webui.t, line 2999

receive a file selection from the file selector dialog


### `receiveFileUpload(req, query)`

Defined in webui.t, line 3040

receive a file upload from the file upload dialog


### `receiveInputDialog(req, query)`

Defined in webui.t, line 3159

receive a selection from the input dialog


### `receiveInputEvent(req, query)`

Defined in webui.t, line 2813

receive an input event


### `setTitle(title)`

Defined in webui.t, line 2730

set the window title


### `syntheticEventReady`

Defined in webui.t, line 3187

is a synthetic event ready?


## Inherited Methods


*From [WebResourceInit](webresourceinit.md):* [`connectUI`](webresourceinit.md#connectUI), [`processRequest`](webresourceinit.md#processRequest)


*From [WebLayoutWindow](weblayoutwindow.md):* [`createFrame`](weblayoutwindow.md#createFrame), [`flushWin`](weblayoutwindow.md#flushWin), [`winFromPath`](weblayoutwindow.md#winFromPath)


*From [WebWindow](webwindow.md):* [`clearWindow`](webwindow.md#clearWindow), [`sendWinEvent`](webwindow.md#sendWinEvent), [`sendWinEventTo`](webwindow.md#sendWinEventTo), [`write`](webwindow.md#write)


*From [WebResourceResFile](webresourceresfile.md):* [`isTextFile`](webresourceresfile.md#isTextFile), [`matchRequest`](webresourceresfile.md#matchRequest)


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
