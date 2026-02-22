# ExitSignal

*class* — defined in [exec.t](../by-file/exec.t.md) (line 1309)


Exit signal. This signal indicates that we're finished with the entire command execution sequence for an action; the remainder of the command execution sequence is to be skipped for the action. Throw this from within the command execution sequence in order to skip directly to the end-of-turn processing. This skips everything remaining in the action, including after-action notification and the like. This signal skips directly past the 'afterAction' phase of the command.


**Superclass chain:** [Exception](exception.md) > `object` > **ExitSignal**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
