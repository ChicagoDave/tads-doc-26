# UnboundMultiMethod

*class* — defined in [multmeth.t](../by-file/multmeth.t.md) (line 413)


Unbound multi-method exception. This is thrown when a call to resolve a multi-method fails to find a binding, meaning that there's no definition of the method that matches the types of the arguments.


**Superclass chain:** [Exception](exception.md) > `object` > **UnboundMultiMethodSubclasses:** [UnboundInheritedMultiMethod](unboundinheritedmultimethod.md)


## Properties


### `args_`

Defined in multmeth.t, line 437

the number of arguments


### `func_`

Defined in multmeth.t, line 431

the base function pointer


### `name_`

Defined in multmeth.t, line 434

the symbol name of the base function


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(func, args)` *(overridden)*

Defined in multmeth.t, line 414


### `displayException` *(overridden)*

Defined in multmeth.t, line 425

display an error message describing the exception


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
