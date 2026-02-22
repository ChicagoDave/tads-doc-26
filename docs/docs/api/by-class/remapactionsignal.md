# RemapActionSignal

*class* — defined in [exec.t](../by-file/exec.t.md) (line 1353)


Action Remap signal. This signal can be thrown only during the noun phrase resolution phase of execution, and indicates that we want to remap the action to a different action, specified in the signal.


**Superclass chain:** [Exception](exception.md) > `object` > **RemapActionSignal**


## Properties


### `action_`

Defined in exec.t, line 1361

the new action that should replace the original action


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(action)` *(overridden)*

Defined in exec.t, line 1354


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
