# NetSafetyException

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 380)


A NetSafetyException is thrown when the program attempts to perform a network operation that isn't allowed by the current network safety level settings. The user controls the safety level; the program can't override this.


**Superclass chain:** [NetException](netexception.md) > [Exception](exception.md) > `object` > **NetSafetyException**


## Properties


### `errMsg` *(overridden)*

Defined in tadsnet.t, line 381


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [NetException](netexception.md):* [`construct`](netexception.md#construct), [`displayException`](netexception.md#displayException)


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
