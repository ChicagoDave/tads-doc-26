# ExitActionSignal

*class* — defined in [exec.t](../by-file/exec.t.md) (line 1326)


Exit Action signal. This signal indicates that we're finished with the execAction portion of processing the command, but we still want to proceed with the rest of the command as normal. This can be used when a step in the action processing wants to preempt any of the more default processing that would normally follow. This skips directly to the 'afterAction' phase of the command.


**Superclass chain:** [Exception](exception.md) > `object` > **ExitActionSignal**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
