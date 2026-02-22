# statusTagOutputStream

*object* — defined in [status.t](../by-file/status.t.md) (line 35)


A special OutputStream for the <BANNER> tag contents. This is really just part of the main output stream, but we use a separate output stream object so that we have our own separate stream state variables (for paragraph breaking and so forth).


**Superclass chain:** [OutputStream](outputstream.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **statusTagOutputStream**


## Properties


### `myInputManager` *(overridden)*

Defined in status.t, line 41

We're really part of the main window's output stream as far as the underlying interpreter I/O system is concerned, so we have to coordinate with the main game window's input manager.


## Inherited Properties


*From [OutputStream](outputstream.md):* [`filterList_`](outputstream.md#filterList_), [`justDidPara`](outputstream.md#justDidPara), [`justDidParaSuppressor`](outputstream.md#justDidParaSuppressor)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `writeFromStream(txt)` *(overridden)*

Defined in status.t, line 44

we sit atop the system-level main console output stream


## Inherited Methods


*From [OutputStream](outputstream.md):* [`addOutputFilter`](outputstream.md#addOutputFilter), [`addOutputFilterBelow`](outputstream.md#addOutputFilterBelow), [`applyFilters`](outputstream.md#applyFilters), [`applyTextFilters`](outputstream.md#applyTextFilters), [`captureOutput`](outputstream.md#captureOutput), [`construct`](outputstream.md#construct), [`execute`](outputstream.md#execute), [`inputLineEnd`](outputstream.md#inputLineEnd), [`removeOutputFilter`](outputstream.md#removeOutputFilter), [`watchForOutput`](outputstream.md#watchForOutput), [`writeToStream`](outputstream.md#writeToStream)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
