# ProgramException

*class* — defined in [_main.t](../by-file/_main.t.md) (line 872)


A Program Exception terminates the entire program, passing an error indication to the operating system. The VM doesn't provide a way to specify the *particular* error code to return to the OS, as there's no portable set of error codes; rather, the VM simply returns a code to the OS that means generically that an error occurred, if there's any such concept on the local operating system. The VM will normally display this message just before it terminates the program, possibly with some additional text mentioning that a program error occurred (such as "unhandled exception: <your message>").


**Superclass chain:** [Exception](exception.md) > `object` > **ProgramException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(msg)` *(overridden)*

Defined in _main.t, line 873


### `displayException` *(overridden)*

Defined in _main.t, line 874


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
