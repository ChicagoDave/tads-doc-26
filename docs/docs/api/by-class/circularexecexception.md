# CircularExecException

*class* — defined in [_main.t](../by-file/_main.t.md) (line 506)


Exception: circular execution dependency in ModuleExecObject


**Superclass chain:** [Exception](exception.md) > `object` > **CircularExecException**


## Properties


### `obj_`

Defined in _main.t, line 520

The object that detected the circular dependency. We can't use this for much ourselves, but it might be useful to store this information so that it's available to the programmer from within the debugger.


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(obj)` *(overridden)*

Defined in _main.t, line 507


### `displayException` *(overridden)*

Defined in _main.t, line 508


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
