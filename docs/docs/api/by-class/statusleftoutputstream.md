# statusLeftOutputStream

*object* — defined in [status.t](../by-file/status.t.md) (line 63)


A special OutputStream for the left half of the status line (the short description area) in text mode. We use a separate stream for this because we must write the text using the output mode switching for the status line.


**Superclass chain:** [OutputStream](outputstream.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **statusLeftOutputStream**


## Inherited Properties


*From [OutputStream](outputstream.md):* [`filterList_`](outputstream.md#filterList_), [`justDidPara`](outputstream.md#justDidPara), [`justDidParaSuppressor`](outputstream.md#justDidParaSuppressor), [`myInputManager`](outputstream.md#myInputManager)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `writeFromStream(txt)` *(overridden)*

Defined in status.t, line 65

we sit atop the system-level main console output stream


## Inherited Methods


*From [OutputStream](outputstream.md):* [`addOutputFilter`](outputstream.md#addOutputFilter), [`addOutputFilterBelow`](outputstream.md#addOutputFilterBelow), [`applyFilters`](outputstream.md#applyFilters), [`applyTextFilters`](outputstream.md#applyTextFilters), [`captureOutput`](outputstream.md#captureOutput), [`construct`](outputstream.md#construct), [`execute`](outputstream.md#execute), [`inputLineEnd`](outputstream.md#inputLineEnd), [`removeOutputFilter`](outputstream.md#removeOutputFilter), [`watchForOutput`](outputstream.md#watchForOutput), [`writeToStream`](outputstream.md#writeToStream)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
