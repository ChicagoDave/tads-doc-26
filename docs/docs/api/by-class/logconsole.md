# LogConsole

*class* — defined in [output.t](../by-file/output.t.md) (line 1876)


Log Console output stream. This is a simple wrapper for the system log console, which allows console-style output to be captured to a file, with full processing (HTML expansion, word wrapping, etc) but without displaying anything to the game window.


**Superclass chain:** [OutputStream](outputstream.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **LogConsole**


## Properties


### `handle_`

Defined in output.t, line 1936

our system log console handle


## Inherited Properties


*From [OutputStream](outputstream.md):* [`filterList_`](outputstream.md#filterList_), [`justDidPara`](outputstream.md#justDidPara), [`justDidParaSuppressor`](outputstream.md#justDidParaSuppressor), [`myInputManager`](outputstream.md#myInputManager)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `captureToFile(filename, charset, width, func)`

Defined in output.t, line 1884

Utility method: create a log file, set up to capture all console output to the log file, run the given callback function, and then close the log file and restore the console output. This can be used as a simple means of creating a file that captures the output of a command.


### `closeConsole`

Defined in output.t, line 1919

Close the console. This closes the underlying system log console, which closes the operating system file. No further text can be written to the console after it's closed.


### `construct(filename, charset, width)` *(overridden)*

Defined in output.t, line 1899

create a log console


### `writeFromStream(txt)` *(overridden)*

Defined in output.t, line 1933

low-level stream writer - write to our system log console


## Inherited Methods


*From [OutputStream](outputstream.md):* [`addOutputFilter`](outputstream.md#addOutputFilter), [`addOutputFilterBelow`](outputstream.md#addOutputFilterBelow), [`applyFilters`](outputstream.md#applyFilters), [`applyTextFilters`](outputstream.md#applyTextFilters), [`captureOutput`](outputstream.md#captureOutput), [`execute`](outputstream.md#execute), [`inputLineEnd`](outputstream.md#inputLineEnd), [`removeOutputFilter`](outputstream.md#removeOutputFilter), [`watchForOutput`](outputstream.md#watchForOutput), [`writeToStream`](outputstream.md#writeToStream)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
