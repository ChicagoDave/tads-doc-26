# RuntimeError

*class* — defined in [_main.t](../by-file/_main.t.md) (line 777)


RuntimeError exception class. The VM creates and throws an instance of this class when any run-time error occurs. The VM explicitly sets the exceptionMessage property to a string giving the VM error message for the run-time error that occurred.


**Superclass chain:** [Exception](exception.md) > `object` > **RuntimeErrorSubclasses:** [StorageServerError](storageservererror.md)


## Properties


### `errno_`

Defined in _main.t, line 828

the VM error number of the exception


### `exceptionMessage`

Defined in _main.t, line 831

the exception message, provided to us by the VM after creation


### `stack_`

Defined in _main.t, line 834

the stack trace, which we store at the time we're created


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(errno, ...)` *(overridden)*

Defined in _main.t, line 778


### `displayException` *(overridden)*

Defined in _main.t, line 809

display the exception


### `isDebuggerSignal`

Defined in _main.t, line 819

check to see if it's a debugger signal of some kind


### `newRuntimeError(errno, msg)`

Defined in _main.t, line 801

create a runtime error with a given error message


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
