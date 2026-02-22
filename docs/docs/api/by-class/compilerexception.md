# CompilerException

*class* — defined in [dynfunc.t](../by-file/dynfunc.t.md) (line 158)


Compiler Exception. 'new DynamicFunc()' throws an exception of this class if an error occurs compiling the source code of the new object.


**Superclass chain:** [Exception](exception.md) > `object` > **CompilerException**


## Properties


### `errmsg_` *(overridden)*

Defined in dynfunc.t, line 169

the error message from the compiler


## Methods


### `construct(msg)` *(overridden)*

Defined in dynfunc.t, line 159


### `displayException` *(overridden)*

Defined in dynfunc.t, line 160


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
