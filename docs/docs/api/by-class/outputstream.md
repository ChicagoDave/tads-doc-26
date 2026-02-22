# OutputStream

*class* — defined in [output.t](../by-file/output.t.md) (line 125)


Output Stream. This class provides a stream-oriented interface to displaying text on the console. "Stream-oriented" means that we write text as a sequential string of characters.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **OutputStreamSubclasses:** [BannerOutputStream](banneroutputstream.md), [LogConsole](logconsole.md), [WebWinOutputStream](webwinoutputstream.md)


**Global objects:** [mainOutputStream](mainoutputstream.md), [menuOutputStream](menuoutputstream.md), [statusLeftOutputStream](statusleftoutputstream.md), [statusRightOutputStream](statusrightoutputstream.md), [statusTagOutputStream](statustagoutputstream.md)


## Properties


### `filterList_`

Defined in output.t, line 271

The list of active filters on this stream, in the order in which they are to be called. This should normally be initialized to a Vector in each instance.


### `justDidPara`

Defined in output.t, line 391

Internal state: we just wrote a paragraph break, and there has not yet been any intervening text. By default, we set this to true initially, so that we suppress any paragraph breaks at the very start of the text.


### `justDidParaSuppressor`

Defined in output.t, line 399

Internal state: we just wrote a character that suppresses paragraph breaks that immediately follow. In this state, we'll suppress any paragraph marker that immediately follows, but we won't suppress any other characters.


### `myInputManager`

Defined in output.t, line 230

my associated input manager, if I have one


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `addOutputFilter(filter)`

Defined in output.t, line 281

Add an output filter. The argument is an object of class OutputFilter, or any object implementing the filterText() method.


### `addOutputFilterBelow(newFilter, existingFilter)`

Defined in output.t, line 296

Add an output filter at a given point in the filter stack: add the filter so that it is "below" the given existing filter in the stack. This means that the new filter will be called just after the existing filter during output.


### `applyFilters(val)`

Defined in output.t, line 336

call the filters


### `applyTextFilters(val)`

Defined in output.t, line 356

Apply the current set of text transformation filters to a string. This applies only the non-capturing filters; we skip any capture filters.


### `captureOutput(func, [args])`

Defined in output.t, line 207

Call the given function, capturing all text output to this stream in the course of the function call. Return a string containing the captured text.


### `construct`

Defined in output.t, line 233

dynamic construction


### `execute` *(overridden)*

Defined in output.t, line 243

execute pre-initialization


### `inputLineEnd`

Defined in output.t, line 379

Receive notification from the input manager that we have just ended reading a line of input from the keyboard.


### `removeOutputFilter(filter)`

Defined in output.t, line 322

Remove an output filter. Since filters are arranged in a stack, only the LAST output filter added may be removed. It's an error to remove a filter other than the last one.


### `watchForOutput(func)`

Defined in output.t, line 179

Watch the stream for output. It's sometimes useful to be able to call out to some code and determine whether or not the code generated any text output. This routine invokes the given callback function, monitoring the stream for output; if any occurs, we'll return true, otherwise we'll return nil.


### `writeFromStream(txt)`

Defined in output.t, line 264

Write text out from this stream; this writes to the lower-level stream underlying this stream. This routine is intended to be called only from within this class.


### `writeToStream(val)`

Defined in output.t, line 132

Write a value to the stream. If the value is a string, we'll display the text of the string; if it's nil, we'll ignore it; if it's anything else, we'll try to convert it to a string (with the toString() function) and display the resulting text.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
