# console.t


## Global Objects

- [statuslineBanner](../by-class/statuslinebanner.md)
- aHref
- aHrefAlt
- aioClearScreen
- aioInputDialog
- aioInputEvent
- aioInputFile
- aioInputLineCancel
- aioInputLineTimeout
- aioMorePrompt
- aioSay
- aioSetLogFile
- checkHtmlMode
- initDisplay
- initUI
- statusHTML
- terminateUI


## Functions


### `aHref(href, txt?, title?, flags, =, 0)`

Defined in console.t, line 189

Generate a string to show hyperlinked text. If we're not in HTML mode, we'll simply return the text without the hyperlink; otherwise, we'll return the text with a hyperlink to the given HREF.


### `aHrefAlt(href, linkedText, altText, title?)`

Defined in console.t, line 224

Generate a string to show hyperlinked text, with alternate text if we're not in HTML mode. If we're in HTML mode, we'll return linkedTxt linked to the given HREF; if we're in plain text mode, we'll return the alternate text as-is.


### `aioClearScreen`

Defined in console.t, line 165

Clear the screen


### `aioInputDialog(icon, prompt, buttons, defaultButton, cancelButton)`

Defined in console.t, line 145

Show an input dialog


### `aioInputEvent(timeout)`

Defined in console.t, line 113

Read an input event


### `aioInputFile(prompt, dialogType, fileType, flags)`

Defined in console.t, line 135

Show a file selector dialog


### `aioInputLineCancel(reset)`

Defined in console.t, line 102

Cancel a suspended input line


### `aioInputLineTimeout(timeout)`

Defined in console.t, line 93

Get a line of input from the keyboard, with timeout


### `aioMorePrompt`

Defined in console.t, line 124

Show a "More" prompt


### `aioSay(txt)`

Defined in console.t, line 83

Write text to the main game window


### `aioSetLogFile(fname, logType?)`

Defined in console.t, line 155

Set/remove the output logging file


### `checkHtmlMode`

Defined in console.t, line 61

Check to see if we're in HTML mode


### `initDisplay`

Defined in console.t, line 39

Initialize the display. The library calls this at the start of the game, and after each RESTART, to set up the layout of the game window.


### `initUI`

Defined in console.t, line 31

Initialize the user interface. The library calls this once at the start of the interpreter session to set up the UI. For the console interpreter, we don't need to do anything here; the interpreter takes care of setting up the display window for us.


### `statusHTML(stage)`

Defined in console.t, line 249

Generate HTML to wrap the left/right portions of the status line. The basic status line has three stages: stage 0 precedes the left portion, stage 1 comes between the left and right portions, and stage 2 follows the right portion. If we're listing exits, we get two more stages: stage 3 precedes the exit listing, stage 4 follows it.


### `terminateUI`

Defined in console.t, line 52

Shut down the user interface. The library calls this once just before the game is about to terminate.
