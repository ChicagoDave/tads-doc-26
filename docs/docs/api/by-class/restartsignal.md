# RestartSignal

*class* — defined in [_main.t](../by-file/_main.t.md) (line 219)


Restart signal. This can be used to restart from the main entrypoint. The caller should create one of these objects, then use restartGame() (or an equivalent from a different function set, if appropriate) to reset static object state to the initial program load conditions, then throw the signal object.


**Superclass chain:** [Exception](exception.md) > `object` > **RestartSignal**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct` *(overridden)*

Defined in _main.t, line 220


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
