# StorageServerError

*class* — defined in [_main.t](../by-file/_main.t.md) (line 889)


A StorageServerError is thrown when a file operation on a remote storage server fails. The storage server is used when the game runs on a Web game server in client/server mode. In Web mode, files are stored on a separate storage server rather than on the Web server itself, so that the files can be transparently accessed if the game is continued from another Web server. This exception is used when a request to the storage server fails, which could be due to an error on the storage server, a network error communicating between the game server and the storage server, or an invalid request (e.g., incorrect user credentials).


**Superclass chain:** [RuntimeError](runtimeerror.md) > [Exception](exception.md) > `object` > **StorageServerError**


## Properties


### `errCode`

Defined in _main.t, line 938

the storage server error code


### `errMsg`

Defined in _main.t, line 946

error message - this is the message text we get back from the storage server for a request that's successful at the HTTP level but fails on the storage server, OR a message describing the HTTP error or network error that caused the request to fail


## Inherited Properties


*From [RuntimeError](runtimeerror.md):* [`errno_`](runtimeerror.md#errno_), [`exceptionMessage`](runtimeerror.md#exceptionMessage), [`stack_`](runtimeerror.md#stack_)


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(errno, msg)` *(overridden)*

Defined in _main.t, line 890


### `displayException` *(overridden)*

Defined in _main.t, line 949

display the exception


## Inherited Methods


*From [RuntimeError](runtimeerror.md):* [`isDebuggerSignal`](runtimeerror.md#isDebuggerSignal), [`newRuntimeError`](runtimeerror.md#newRuntimeError)


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
