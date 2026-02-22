# statusLine

*object* — defined in [status.t](../by-file/status.t.md) (line 173)


Status line - this is an abstract object that controls the status line display.


**Superclass chain:** `object` > **statusLine**


## Properties


### `statusDispMode`

Defined in status.t, line 566

The status mode we're using. If this is nil, it means we haven't chosen a mode yet.


## Methods


### `beginStatusLine`

Defined in status.t, line 394

Begin status-line mode. This sets up the output manager so that text written to the default output stream is displayed on the status line. Returns the original output stream.


### `endStatusLine(oldStr)`

Defined in status.t, line 472

end statusline display


### `getEstimatedHeightHtml`

Defined in status.t, line 300

Get the estimated HTML-style banner height, in lines of text. This is used to set the status line banner size for platforms where sizing to the exact height of the rendered contents isn't supported.


### `initBannerWindow(win)`

Defined in status.t, line 515

Initialize the banner window, given the BannerWindow object representing the status line banner API window.


### `setColorScheme`

Defined in status.t, line 383

Set up the status line's color scheme. This is called each time we redraw the status line to set the background and text colors. We call the statusline banner window to do the work, since the mechanism is different between the traditional and Web UIs.


### `showStatusHtml`

Defined in status.t, line 259

Show the status line in HTML format. Our default implementation shows the traditional two-part (left/right) status line, using showStatusLeft() and showStatusRight() to display the parts.


### `showStatusLeft`

Defined in status.t, line 343

Show the left part of a standard left/right statusline. By default, we'll show the player character's location, by calling statusName() on the PC's immediate container.


### `showStatusLine`

Defined in status.t, line 180

Show the status line, in HTML or text mode, as appropriate. By default, the library sets this up as a "prompt daemon," which means that this will be called automatically just before each command line is read.


### `showStatusLineDaemon`

Defined in status.t, line 239

prompt-daemon showing the status line


### `showStatusRight`

Defined in status.t, line 364

Show the right part of a standard left/right statusline. By default, we'll show the current score, a slash, and the number of turns.


### `showStatusText`

Defined in status.t, line 323

Show the statusline in text mode. Our default implementation shows the traditional two-part (left/right) status line, using showStatusLeft() and showStatusRight() to display the parts.
