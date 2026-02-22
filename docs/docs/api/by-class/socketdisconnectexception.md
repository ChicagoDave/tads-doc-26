# SocketDisconnectException

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 393)


A SocketDisconnectException is thrown when attempting to read or write a network socket that's been closed, either by us or by the peer (the computer on the other end of the network connection). If we didn't close the socket on this side, this error usually means simply that the peer program has terminated or otherwise disconnected, so we should consider the conversation terminated.


**Superclass chain:** [NetException](netexception.md) > [Exception](exception.md) > `object` > **SocketDisconnectException**


## Properties


### `errMsg` *(overridden)*

Defined in tadsnet.t, line 394


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [NetException](netexception.md):* [`construct`](netexception.md#construct), [`displayException`](netexception.md#displayException)


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
