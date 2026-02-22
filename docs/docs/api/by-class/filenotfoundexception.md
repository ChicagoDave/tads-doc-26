# FileNotFoundException

*class* — defined in [file.t](../by-file/file.t.md) (line 102)


File not found - this is thrown when attempting to open a file for reading and the file doesn't exist or can't be opened (because the user doesn't have privileges to read the file, or the file is already being used by another user, for example).


**Superclass chain:** [FileException](fileexception.md) > [Exception](exception.md) > `object` > **FileNotFoundException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `displayException` *(overridden)*

Defined in file.t, line 103


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
