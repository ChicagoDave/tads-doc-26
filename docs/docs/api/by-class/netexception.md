# NetException

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 360)


A NetException is the base class for network errors.


**Superclass chain:** [Exception](exception.md) > `object` > **NetExceptionSubclasses:** [NetSafetyException](netsafetyexception.md), [SocketDisconnectException](socketdisconnectexception.md)


## Properties


### `errMsg`

Defined in tadsnet.t, line 371

a descriptive error message provided by the system


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(msg?, errno?)` *(overridden)*

Defined in tadsnet.t, line 361


### `displayException` *(overridden)*

Defined in tadsnet.t, line 368


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
