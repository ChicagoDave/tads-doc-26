# WebCommandWin

*class* — defined in [webui.t](../by-file/webui.t.md) (line 1936)


Command Window. This object keeps track of the state of command window within the web UI.


**Superclass chain:** [WebWindow](webwindow.md) > [WebResourceResFile](webresourceresfile.md) > [WebResource](webresource.md) > `object` > **WebCommandWinGlobal objects:** [commandWin](commandwin.md)


## Properties


### `isInputOpen`

Defined in webui.t, line 2201

Is an input line open? This is true between sending an <inputLine> event and either getting a reply, or explicitly sending a close or cancel event.


### `lastInput`

Defined in webui.t, line 2188

the text of the last input line we received from the client


### `lastInputClient`

Defined in webui.t, line 2194

client session who sent the last input line


### `lastInputReady`

Defined in webui.t, line 2191

is input ready?


### `mode`

Defined in webui.t, line 2212

Current UI mode. This is 'working' if the program is running and in the process of computing and/or generating output; 'inputLine' if we're waiting for the user to enter a line of input; 'morePrompt' if we're showing a "More" prompt.


### `moreMode`

Defined in webui.t, line 2204

flag: we're in More mode


### `outbuf`

Defined in webui.t, line 2185

pending output buffer, since last flush


### `scrollback`

Defined in webui.t, line 2174

Scrollback list. After each input, we add the contents of 'textbuf' to this list. If this pushes the list past the limit, we drop the oldest item. This is used to reconstruct a reasonable amount of scrollback history when a new client connects, or when an existing client refreshes the page.


### `scrollbackLimit`

Defined in webui.t, line 2182

The scrollback limit, as a number of command inputs. Each input interaction adds one item to the scrollback list. When the number of items in the list exceeds the limit set here, we drop the oldest item.


### `src` *(overridden)*

Defined in webui.t, line 2216


### `textbuf`

Defined in webui.t, line 2165

main window text buffer since last input read


### `vpath` *(overridden)*

Defined in webui.t, line 2215

my virtual path, and the actual resource file location


## Inherited Properties


*From [WebWindow](webwindow.md):* [`name`](webwindow.md#name), [`pathName`](webwindow.md#pathName), [`sthCtx`](webwindow.md#sthCtx)


*From [WebResourceResFile](webresourceresfile.md):* [`binaryExts`](webresourceresfile.md#binaryExts), [`browserExtToMime`](webresourceresfile.md#browserExtToMime)


*From [WebResource](webresource.md):* [`group`](webresource.md#group), [`priority`](webresource.md#priority)


## Methods


### `cancelInputLine(reset)`

Defined in webui.t, line 2026

Cancel an input line that was interrupted by a timeout


### `clearWindow` *(overridden)*

Defined in webui.t, line 2086

Clear the window


### `endMoreMode`

Defined in webui.t, line 2158

receive notification from the client that the user has responded to the More prompt, ending the pause


### `flushWin` *(overridden)*

Defined in webui.t, line 1949

Flush the buffers


### `getInputLine(timeout?)`

Defined in webui.t, line 1968

Read a line of input in this window. Blocks until the reply is received. Returns nil on timeout.


### `getState(client)` *(overridden)*

Defined in webui.t, line 2046

Get the state of this command window


### `receiveInput(req, query)`

Defined in webui.t, line 2057

Receive input from the client


### `showMorePrompt`

Defined in webui.t, line 2137

Show a "More" prompt


### `textbufToScrollback(cmd)`

Defined in webui.t, line 2114

Move the current text buffer contents to the scrollback list. If this would make the scrollback list exceed the limit, we'll drop the oldest item.


### `write(txt)` *(overridden)*

Defined in webui.t, line 1940

Write to the window


## Inherited Methods


*From [WebWindow](webwindow.md):* [`processName`](webwindow.md#processName), [`sendWinEvent`](webwindow.md#sendWinEvent), [`sendWinEventTo`](webwindow.md#sendWinEventTo), [`winFromPath`](webwindow.md#winFromPath)


*From [WebResourceResFile](webresourceresfile.md):* [`isTextFile`](webresourceresfile.md#isTextFile), [`matchRequest`](webresourceresfile.md#matchRequest), [`processRequest`](webresourceresfile.md#processRequest)


*From [WebResource](webresource.md):* [`sendAck`](webresource.md#sendAck), [`sendXML`](webresource.md#sendXML)
