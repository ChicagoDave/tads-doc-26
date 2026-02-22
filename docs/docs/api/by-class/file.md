# File

*class* — defined in [file.h](../by-file/file.h.md) (line 131)


The File intrinsic class provides access to files in the external file system. This lets you create, read, and write files. The class supports text files (with translations to and from local character sets), "data" files (using the special TADS 2 binary file format), and "raw" files (this mode lets you manipulate files in arbitrary text or binary formats by giving you direct access to the raw bytes in the file).


**Superclass chain:** [Object](object.md) > **File**


## Methods


### `closeFile`

Defined in file.h, line 292

Close the file. Flushes any buffered information to the underlying system file and releases any system resources (such as share locks or system buffers) associated with the file. After this routine is called, no further operations on the file can be performed (a FileClosedException will be thrown if any subsequent operations are attempted).


### `digestMD5(length?)`

Defined in file.h, line 563

Calculate the MD5 digest of bytes read from the file, starting at the current seek location and continuing for the given number of bytes. If the length is omitted, the whole rest of the file is digested. This has the side effect of reading the given number of bytes from the file, so it leaves the seek position set to the next byte after the bytes digested.


### `getCharacterSet`

Defined in file.h, line 241

get the CharacterSet object the File is currently using; returns nil for a non-text file


### `getFileMode`

Defined in file.h, line 458

Get the file mode. This returns one of the FileModeXxx constants, indicating the mode used to open the file (text, data, raw).


### `getFileSize`

Defined in file.h, line 452

get the size in bytes of the file


### `getPos`

Defined in file.h, line 396

Get the current read/write position in the file. Returns the byte offset in the file of the next byte to be read or written. Note that this value is an offset, so 0 is the offset of the first byte in the file.


### `packBytes(format, ...)`

Defined in file.h, line 522

Pack the given data values into bytes according to a format definition string, and write the packed bytes to the file. This function is designed to simplify writing files that use structured binary formats defined by third parties, such as JPEG or PDF. The function translates native TADS data values into selected binary formats, and writes the resulting bytes to the file, all in a single operation.


### `readBytes(byteArr, start?, cnt?)`

Defined in file.h, line 365

Read bytes from the file into the given ByteArray object. This can only be used for a file opened in 'raw' mode. If 'start' and 'cnt' are given, they give the starting index in the byte array at which the bytes read are to be stored, and the number of bytes to read, respectively; if these are omitted, one byte is read from the file for each byte in the byte array.


### `readFile`

Defined in file.h, line 322

Read from the file. Returns a data value that depends on the file mode, as described below, or nil at end of file.


### `setCharacterSet(charset)`

Defined in file.h, line 251

Set the CharacterSet object the File is to use from now on. This isn't meaningful except for text files. 'charset' can be a CharacterSet object, a string giving the name of a character mapping (in which case a CharacterSet object is automatically created based on the name), or nil (in which case the local system's default character set for text files is used).


### `setFileMode(mode, charset?)`

Defined in file.h, line 501

Change the file mode. 'mode' is a FileModeXxx value giving the desired new file mode.


### `setPos(pos)`

Defined in file.h, line 416

Set the current read/write position in the file. 'pos' is a byte offset in the file; 0 is the offset of the first byte.


### `setPosEnd`

Defined in file.h, line 425

Set the current read/write position to the end of the file. This can be used, for example, to open a 'data' mode file for read/write/keep access (keeping the contents of an existing file) and then adding more data after all of the existing data in the file.


### `sha256(length?)`

Defined in file.h, line 549

Calculate the 256-bit SHA-2 hash of bytes read from the file, starting at the current seek location and continuing for the given number of bytes. If the length is omitted, the whole rest of the file is hashed. This has the side effect of reading the given number of bytes from the file, so it leaves the seek position set to the next byte after the bytes hashed.


### `unpackBytes(format)`

Defined in file.h, line 535

Read bytes and unpack into a data structure, according to the format description string 'desc'.


### `writeBytes(source, start?, cnt?)`

Defined in file.h, line 388

Write bytes from the given source object into the file. This can only be used for a file opened in 'raw' mode.


### `writeFile(val)`

Defined in file.h, line 349

Write to the file. Writes the given value to the file in a format that depends on the file mode, as described below. No return value; if an error occurs writing the data, this throws a FileIOException.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
