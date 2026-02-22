# AbortImplicitSignal

*class* — defined in [exec.t](../by-file/exec.t.md) (line 1337)


Abort implicit command signal. This exception indicates that we are aborting an implicit command without having tried to execute the command at all. This is thrown when an implied command is to be aborted before it's even attempted, such as when verification shows the command is obviously dangerous and thus should never be attempted without the player having explicitly requesting it.


**Superclass chain:** [Exception](exception.md) > `object` > **AbortImplicitSignal**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
