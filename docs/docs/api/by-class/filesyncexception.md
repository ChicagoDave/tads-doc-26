# FileSyncException

*class* — defined in [file.t](../by-file/file.t.md) (line 135)


File synchronization exception. This is thrown when an operation (such as a read or write) is attempted during normal execution on a file object that was originally opened during pre-initialization. A file object created during pre-initialization can't be used to access the file during ordinary execution, since the state of the external file might have changed since the pre-init session ended. In such cases, a new file object must be created instead.


**Superclass chain:** [FileException](fileexception.md) > [Exception](exception.md) > `object` > **FileSyncException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `displayException` *(overridden)*

Defined in file.t, line 136


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
