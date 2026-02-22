# FileCreationException

*class* — defined in [file.t](../by-file/file.t.md) (line 112)


File creation error - this is thrown when attempting to open a file for writing and the file can't be created; this can happen because the disk or the directory is full, due to privilege failures, or due to sharing violations, among other reasons.


**Superclass chain:** [FileException](fileexception.md) > [Exception](exception.md) > `object` > **FileCreationException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `displayException` *(overridden)*

Defined in file.t, line 113


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
