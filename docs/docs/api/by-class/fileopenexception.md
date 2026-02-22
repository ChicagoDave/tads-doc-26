# FileOpenException

*class* — defined in [file.t](../by-file/file.t.md) (line 122)


File cannot be opened - this is thrown when attempting to open a file for reading and writing but the file can't be opened. This can happen for numerous reasons: sharing violations, privilege failures, lack of space on the disk or in the directory.


**Superclass chain:** [FileException](fileexception.md) > [Exception](exception.md) > `object` > **FileOpenException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `displayException` *(overridden)*

Defined in file.t, line 123


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
