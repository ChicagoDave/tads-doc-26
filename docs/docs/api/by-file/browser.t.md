# browser.t


## Classes

- [WebBannerWin](../by-class/webbannerwin.md)
- [WebWinOutputStream](../by-class/webwinoutputstream.md)


## Global Objects

- [browserGlobals](../by-class/browserglobals.md)
- [commandWin](../by-class/commandwin.md)
- [statuslineBanner](../by-class/statuslinebanner.md)
- aHref
- aHrefAlt
- aioClearScreen
- aioInputDialog
- aioInputEvent
- aioInputFile
- aioInputLineCancel
- aioInputLineTimeout
- aioLogInputEvent
- aioMorePrompt
- aioSay
- aioSetLogFile
- checkHtmlMode
- evtCharForScript
- initDisplay
- initUI
- readingEventScript
- readingScript
- statusHTML
- terminateUI


## Functions


### `aHref(href, txt?, title?, flags, =, 0)`

Defined in browser.t, line 642

Generate a string to show hyperlinked text. The browser UI is always in HTML mode, so we unconditionally generate the hyperlink.


### `aHrefAlt(href, linkedText, altText, title?)`

Defined in browser.t, line 667

Generate a string to show hyperlinked text, with alternate text if we're not in HTML mode. The browser UI is always in HTML mode, so we unconditionally generate the hyperlink.


### `aioClearScreen`

Defined in browser.t, line 277

Clear the screen


### `aioInputDialog(icon, prompt, buttons, defaultButton, cancelButton)`

Defined in browser.t, line 398

Show an input dialog


### `aioInputEvent(timeout)`

Defined in browser.t, line 241

Read an input event


### `aioInputFile(prompt, dialogType, fileType, flags)`

Defined in browser.t, line 288

Show a file selector dialog


### `aioInputLineCancel(reset)`

Defined in browser.t, line 230

Cancel a suspended input line


### `aioInputLineTimeout(timeout)`

Defined in browser.t, line 195

Get a line of input from the keyboard, with timeout


### `aioLogInputEvent(evt)`

Defined in browser.t, line 525

Log an input event. We call this internally from each of the event input routines to add the event to any event or command log we're creating.


### `aioMorePrompt`

Defined in browser.t, line 267

Show a "More" prompt


### `aioSay(txt)`

Defined in browser.t, line 163

Write text to the main game window


### `aioSetLogFile(fname, typ, =, 1)`

Defined in browser.t, line 429

Set/remove the output logging file


### `checkHtmlMode`

Defined in browser.t, line 147

Check to see if we're in HTML mode


### `evtCharForScript(c)`

Defined in browser.t, line 613

Get an InEvtKey event parameter in suitable format for script file output. This returns the key as it appears in the event, except that ASCII control characters are translated to '[ctrl-X]'.


### `initDisplay`

Defined in browser.t, line 72

Initialize the display. We call this when we first enter the interpreter, and again at each RESTART, to set up the main game window's initial layout. We set up the conventional IF screen layout, with the status line across the top and the transcript/command window filling the rest of the display.


### `initUI`

Defined in browser.t, line 48

Initialize the user interface. The library calls this once at the start of the interpreter session to set up the UI. For the Web UI, we create the HTTP server and send connection instructions to the client.


### `readingEventScript`

Defined in browser.t, line 185

Is an event script active?


### `readingScript`

Defined in browser.t, line 177

Is a script file active?


### `statusHTML(stage)`

Defined in browser.t, line 688

Generate HTML to wrap the left/right portions of the status line. The basic status line has three stages: stage 0 precedes the left portion, stage 1 comes between the left and right portions, and stage 2 follows the right portion. If we're listing exits, we get two more stages: stage 3 precedes the exit listing, stage 4 follows it.


### `terminateUI`

Defined in browser.t, line 113

Shut down the user interface. The library calls this when the game is about to terminate.
