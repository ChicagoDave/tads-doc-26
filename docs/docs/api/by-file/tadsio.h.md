# tadsio.h


## Classes

- bannerClear
- bannerCreate
- bannerDelete
- bannerFlush
- bannerGetInfo
- bannerGoTo
- bannerSay
- bannerSetScreenColor
- bannerSetSize
- bannerSetTextColor
- bannerSizeToContents
- clearScreen
- flushOutput
- getLocalCharSet
- inputDialog
- inputEvent
- inputFile
- inputKey
- inputLine
- inputLineCancel
- inputLineTimeout
- logConsoleClose
- logConsoleCreate
- logConsoleSay
- logInputEvent
- morePrompt
- resExists
- setLogFile
- setScriptFile
- statusMode
- statusRight
- systemInfo
- tadsSay
- timeDelay


## Functions


### `bannerClear(handle)`

Defined in tadsio.h, line 350

Clear the contents of a banner window. 'color' is the color to use for the screen color after clearing the window, given as a ColorXxx value (see below).


### `bannerCreate(parent, where, other, windowType, align, size, sizeUnits, styleFlags)`

Defined in tadsio.h, line 336

Create a banner window. Returns the "handle" of the new window, which is used to identify the window in subsequent bannerXxx() functions. Not all interpreters support banner windows; if the interpreter does not support this feature, the return value is nil.


### `bannerDelete(handle)`

Defined in tadsio.h, line 343

Delete a banner window. 'handle' is the handle to the window to be removed.


### `bannerFlush(handle)`

Defined in tadsio.h, line 368

Flush all buffers for a banner window. This ensures that any text written with bannerSay() is actually displayed for the user to see (rather than being held in internal buffers).


### `bannerGetInfo(handle)`

Defined in tadsio.h, line 418

Get information on the banner. This returns a list giving a detailed set of information describing the banner.


### `bannerGoTo(handle, row, col)`

Defined in tadsio.h, line 393

Go to to an output position. This is meaningful only for BannerTypeTextGrid windows. This sets the next text output position to the given row and column in the text grid; the next call to bannerSay() will display its output starting at this position.


### `bannerSay(handle, ...)`

Defined in tadsio.h, line 361

Write text to a banner window. The text is displayed in the given banner. For a BannerTypeText window, HTML tags in the text are interpreted; for a BannerTypeTextGrid window, the text is written exactly as given, without any HTML interpretation.


### `bannerSetScreenColor(handle, color)`

Defined in tadsio.h, line 412

Set the "screen color" in the banner window. This is the color used to fill parts of the window that aren't displaying any text, and as the background color for all text displayed when the text background color is ColorTransparent. Setting the screen color immediately sets the color for the entire window - even text previously displayed in the window is affected by this change.


### `bannerSetSize(handle, size, sizeUnits, isAdvisory)`

Defined in tadsio.h, line 432

Set the size of a banner. This explicitly sets the banner's height (for a top or bottom banner) or width (for a left or right) banner to the 'size', which is specified in units given by 'sizeUnits', which is a BannerSizeXxx constant. If 'isAdvisory' is true, the caller is indicating that this call will be followed soon by a call to bannerSizeToContents(). On systems that support sizing to contents, an "advisory" call to bannerSetSize() will simply be ignored in anticipation of the upcoming call to bannerSizeToContents(). On systems that don't support sizing to contents, an advisory call will actually resize the window.


### `bannerSetTextColor(handle, fg, bg)`

Defined in tadsio.h, line 402

Set text foreground and background colors. This affects the color of subsequently displayed text; text displayed previously is not affected. The colors are given as ColorXxx values (see below). If 'bg' is ColorTransparent, then text is shown with the current screen color in the window.


### `bannerSizeToContents(handle)`

Defined in tadsio.h, line 385

Size a banner to fit its contents. This resizes the banner such that the contents just fit. In the case of a top- or bottom-aligned banner, the height is set just high enough to hold all of the text currently displayed. In the case of a left- or right-aligned banner, the width is set just wide enough to hold the widest single word that can't be broken across lines. In all cases, the size includes any fixed margin space, to ensure that all of the text in the window is actually visible without scrolling.


### `clearScreen`

Defined in tadsio.h, line 48

Clear the display. This clears the main window.


### `flushOutput`

Defined in tadsio.h, line 265

Flush text output and update the main display window. This ensures that any text displayed with tadsSay() is actually displayed, for the user to see (rather than being held in internal buffers).


### `getLocalCharSet(which)`

Defined in tadsio.h, line 258

Get the local default character set. 'which' is a CharsetXxx value giving which local character set to retrieve. Returns a string giving the name of the given local character set.


### `inputDialog(icon, prompt, buttons, defaultButton, cancelButton)`

Defined in tadsio.h, line 123

Display a simple "message box" dialog (known on some systems as an "alert" dialog). This displays a dialog that includes a short message for the user to read, an icon indicating the general nature of the condition that gave rise to the dialog (an error, a warning, a choice for the user to make, etc.), and a set of push-buttons that dismiss the dialog and (in some cases) let the user choose among options. 'icon' is an InDlgIconXxx value giving the type of icon to show, if any; 'prompt' is the message string to display; 'buttons' gives the set of buttons to display; 'defaultButton' is the index (starting at 1) among the buttons of the default button; and 'cancelButton' is the index of the cancellation button.


### `inputEvent(timeout?)`

Defined in tadsio.h, line 79

Read a single input event. Waits until an input event is available, then returns the event as a list. The first element of the list is an InEvtXxx value indicating the type of the event; the remainder of the list varies according to the event type. If 'timeout' is provided, it gives the maximum waiting interval in milliseconds; if no input event occurs within this interval, the function returns an InEvtTimeout event.


### `inputFile(prompt, dialogType, fileType, flags)`

Defined in tadsio.h, line 183

Display a file selector dialog. This prompts the user to select a file. On GUI systems, this will typically display the standard system file selection dialog; on character-mode systems, it might simply display the prompt string and let the user type the name of a file directly.


### `inputKey`

Defined in tadsio.h, line 68

Read a single keystroke from the keyboard. Waits until the user presses a key, then returns the keystroke as a string.


### `inputLine`

Defined in tadsio.h, line 62

Read a line of text from the keyboard. Pauses to let the user edit and enter a command line, then returns the entered text as a string.


### `inputLineCancel(reset)`

Defined in tadsio.h, line 315

Cancel an input line that was interrupted by timeout. This function must be called after an inputLineTimeout() returns with an InEvtTimeout status indication and before any subsequent output function that displays anything in the main window, or any input fucntion other than inputLineTimeout().


### `inputLineTimeout(timeout?)`

Defined in tadsio.h, line 288

Read a line of text from the keyboard. Waits for the user to edit and enter a command line. If a 'timeout' value is specified, it gives the maximum interval to wait for the user to finish entering the input, in milliseconds. If the timeout expires before the user finishes entering the line, the function stops waiting and returns.


### `logConsoleClose(handle)`

Defined in tadsio.h, line 449

Close a log console. This closes the file associated with the log console and deletes the console object. The given console handle is no longer valid after this function is called.


### `logConsoleCreate(filename, charset, width)`

Defined in tadsio.h, line 442

Create a log file console. This creates a console that has no display, but simply captures its output to the given log file. Writing to a log console is different from writing to a regular text file in that we apply all of the normal formatting (including text-only-mode HTML interpretation) to the output sent to this console.


### `logConsoleSay(handle, ...)`

Defined in tadsio.h, line 456

Write text to a log console. This works the same as tadsSay(), but writes the output to the given log console rather than to the main output window.


### `logInputEvent(evt)`

Defined in tadsio.h, line 479

Log an input event that's obtained externally - i.e., from a source other than the system input APIs (inputLine, inputKey, inputEvent, etc). This adds the event to any command or event log that the system is currently writing, as set with setLogFile().


### `morePrompt`

Defined in tadsio.h, line 56

Show the "more" prompt, if supported on the platform. This causes a "more" prompt to be displayed, according to local system conventions, as though consecutive text output had exceeded the screen/window height.


### `resExists(fname)`

Defined in tadsio.h, line 220

Determine if a multimedia resource exists. 'fname' is the name of a resource (a JPEG image file, PNG image file, etc), given in URL-style path notation. Returns true if the resource is available, nil if not.


### `setLogFile(fname, logType?)`

Defined in tadsio.h, line 43

Set the output log file (which records the output transcript) or the command log file (which records command lines the user enters). 'fname' is the name of the file to open, and 'logType' gives the type of log to open, as a LogTypeXxx value.


### `setScriptFile(filename, flags?)`

Defined in tadsio.h, line 251

Set the script input file. This opens the given file as the script input file. 'filename' is a string giving the name of the file to open, and 'flags' is a combination of ScriptFileXxx bit flags giving the mode to use to read the file. When a script file is active, the system reads command-line input from the file rather than from the keyboard. This lets the program replay an input script.


### `statusMode(mode)`

Defined in tadsio.h, line 203

Set the status-line display mode. This is meaningful only with text-only interpreters that don't support banner windows; other interpreters ignore this. 'mode' is a StatModeXxx constant giving the new mode.


### `statusRight(txt)`

Defined in tadsio.h, line 212

Write text on the right half of the status line. This is meaningful only for text-only interpreters that don't support banner windows; other interpreters ignore this. On non-banner interpreters, this sets the right half of the status line to display the given text, right-justified.


### `systemInfo(infoType, ...)`

Defined in tadsio.h, line 195

Retrieve local system information. 'infoType' is a SysInfoXxx constant giving the type of information to retrieve. Additional arguments and the return value vary according to the infoType value.


### `tadsSay(val, ...)`

Defined in tadsio.h, line 35

Display values on the console. One or more values can be displayed. Each value can be a string, in which case the string is displayed as given (with HTML interpretation); an integer, in which case it's converted to a string, using a decimal (base 10) radix and displayed; a BigNumber, in which case it's converted to a string using the default formatting; or nil, in which case nothing is displayed.


### `timeDelay(delayMilliseconds)`

Defined in tadsio.h, line 188

Pause for the given number of milliseconds.
