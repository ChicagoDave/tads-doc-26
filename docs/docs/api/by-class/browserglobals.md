# browserGlobals

*object* — defined in [browser.t](../by-file/browser.t.md) (line 28)


Browser globals


**Superclass chain:** `object` > **browserGlobals**


## Properties


### `httpServer`

Defined in browser.t, line 30

the HTTPServer object for the browser UI session


### `logFile`

Defined in browser.t, line 36

Log file handle. For a LogTypeTranscript file, this is a LogConsole object; for other types, it's a regular file handle.


### `logFileType`

Defined in browser.t, line 39

logging type (LogTypeXxx from tadsio.h, or nil if not logging)
