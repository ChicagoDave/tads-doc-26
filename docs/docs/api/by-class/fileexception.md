# FileException

*class* — defined in [file.t](../by-file/file.t.md) (line 92)


File Exception classes. All File exceptions derive from FileException, to allow for generic 'catch' clauses which catch any file-related error.


**Superclass chain:** [Exception](exception.md) > `object` > **FileExceptionSubclasses:** [FileClosedException](fileclosedexception.md), [FileCreationException](filecreationexception.md), [FileIOException](fileioexception.md), [FileModeException](filemodeexception.md), [FileNotFoundException](filenotfoundexception.md), [FileOpenException](fileopenexception.md), [FileSafetyException](filesafetyexception.md), [FileSyncException](filesyncexception.md)


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `displayException` *(overridden)*

Defined in file.t, line 93


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
