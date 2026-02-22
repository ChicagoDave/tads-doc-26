# menuOutputStream

*object* — defined in [menusys.t](../by-file/menusys.t.md) (line 84)


Menu output stream. We run topic contents through this output stream to allow topics to use the special paragraph and style tag markups.


**Superclass chain:** [OutputStream](outputstream.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **menuOutputStream**


## Properties


### `buf_`

Defined in menusys.t, line 125

our capture buffer (a StringBuffer object)


## Inherited Properties


*From [OutputStream](outputstream.md):* [`filterList_`](outputstream.md#filterList_), [`justDidPara`](outputstream.md#justDidPara), [`justDidParaSuppressor`](outputstream.md#justDidParaSuppressor), [`myInputManager`](outputstream.md#myInputManager)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `captureOutput(val)` *(overridden)*

Defined in menusys.t, line 90

Process a function call through the stream. If the function generates any output, we capture it. If the function simply returns text, we run it through the filters.


### `execute` *(overridden)*

Defined in menusys.t, line 115

initialize


### `writeFromStream(txt)` *(overridden)*

Defined in menusys.t, line 112

we capture our output to a string buffer


## Inherited Methods


*From [OutputStream](outputstream.md):* [`addOutputFilter`](outputstream.md#addOutputFilter), [`addOutputFilterBelow`](outputstream.md#addOutputFilterBelow), [`applyFilters`](outputstream.md#applyFilters), [`applyTextFilters`](outputstream.md#applyTextFilters), [`construct`](outputstream.md#construct), [`inputLineEnd`](outputstream.md#inputLineEnd), [`removeOutputFilter`](outputstream.md#removeOutputFilter), [`watchForOutput`](outputstream.md#watchForOutput), [`writeToStream`](outputstream.md#writeToStream)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
