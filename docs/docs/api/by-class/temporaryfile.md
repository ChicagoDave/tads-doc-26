# TemporaryFile

*class* — defined in [file.h](../by-file/file.h.md) (line 598)


The TemporaryFile intrinsic class represents a temporary file name in the local file system. Temporary files can be used to store data too large to conveniently store in memory.


**Superclass chain:** [Object](object.md) > **TemporaryFile**


## Methods


### `deleteFile`

Defined in file.h, line 633

Delete the underlying file system object. This deletes the temporary file and marks the TemporaryFile object as invalid. After calling this, you can no longer open the file via the File.openXxxFile methods.


### `getFilename`

Defined in file.h, line 611

Get the name of the underlying file system object. This returns a string with the local filename. This is mostly for debugging purposes or for displaying to the user. You can't necessarily use this filename in a call to File.openXxxFile, because the file path is usually in a system directory reserved for temporary files, and the file safety level settings often prohibit opening files outside of the program's own home directory. To open the temp file, you should always pass the TemporaryFile object itself in place of the filename.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
