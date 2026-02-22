# statusRightOutputStream

*object* — defined in [status.t](../by-file/status.t.md) (line 84)


A special OutputStream for the right half of the status line (the score/turn count area) in text mode. We use a separate stream for this because we have to write this text with the special statusRight() intrinsic in text mode.


**Superclass chain:** [OutputStream](outputstream.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **statusRightOutputStream**


## Properties


### `buf_`

Defined in status.t, line 109

our buffered text


## Inherited Properties


*From [OutputStream](outputstream.md):* [`filterList_`](outputstream.md#filterList_), [`justDidPara`](outputstream.md#justDidPara), [`justDidParaSuppressor`](outputstream.md#justDidParaSuppressor), [`myInputManager`](outputstream.md#myInputManager)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `flushStream`

Defined in status.t, line 99

Flush the buffer. This writes whatever we've buffered up to the right half of the text-mode status line.


### `writeFromStream(txt)` *(overridden)*

Defined in status.t, line 89

Write from the stream. We simply buffer up text until we're asked to display the final data.


## Inherited Methods


*From [OutputStream](outputstream.md):* [`addOutputFilter`](outputstream.md#addOutputFilter), [`addOutputFilterBelow`](outputstream.md#addOutputFilterBelow), [`applyFilters`](outputstream.md#applyFilters), [`applyTextFilters`](outputstream.md#applyTextFilters), [`captureOutput`](outputstream.md#captureOutput), [`construct`](outputstream.md#construct), [`execute`](outputstream.md#execute), [`inputLineEnd`](outputstream.md#inputLineEnd), [`removeOutputFilter`](outputstream.md#removeOutputFilter), [`watchForOutput`](outputstream.md#watchForOutput), [`writeToStream`](outputstream.md#writeToStream)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
