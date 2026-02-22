# FileName

*class* — defined in [filename.h](../by-file/filename.h.md) (line 72)


A FileName represents the name of a file in the local operating system. The File object methods that take filename specifications accept FileName objects as well as ordinary strings.


**Superclass chain:** [Object](object.md) > **FileName**


## Methods


### `addToPath(element)`

Defined in filename.h, line 127

Add a path element (a string or FileName object) to the end of this filename, yielding a new FileName object with the combined path. Uses the correct local syntax to combine the path elements. This yields the same results as FileName + element.


### `createDirectory(createParents?)`

Defined in filename.h, line 285

Create a directory with the name contained in this object. The file safety settings must allow write access to the parent folder.


### `deleteFile`

Defined in filename.h, line 228

Delete the disk file named by this object. The file safety level must allow write access to the file; a file safety exception is thrown if not.


### `forEachFile(func, recursive?)`

Defined in filename.h, line 270

Invoke a callback for each file in the directory named by this object. 'func' is a callback function; for each file in the directory, this is invoked as func(f), where 'f' is a FileName object describing the file. If 'recursive' is true, the method recursively scans the contents of subdirectories; if 'recursive' is nil or is omitted, only the direct contents of the directory are scanned.


### `getAbsolutePath`

Defined in filename.h, line 156

Get a FileName giving the absolute path to this file. This applies the current working directory and/or volume (e.g., drive letter on Windows) to produce the full path in absolute notation, using the appropriate syntax for the local operating system. If the name is already in absolute format, the result will usually be unchanged, although the exact syntax might be modified on some systems to change the name to a more canonical format.


### `getBaseName`

Defined in filename.h, line 90

Get the base filename portion, without the path. This returns a string giving the filename without any directory location information; for a Unix-style path or Windows-style path, this is simply the last element of the path.


### `getFileInfo(followLinks?)`

Defined in filename.h, line 221

Get extended information on the file named by this object. This retrieves the size of the file, timestamps, and the file's type, and returns the information as a FileInfo object (see file.t). If the file doesn't exist, or can't be accessed for some other reason at the operating system level, returns nil.


### `getFileType(followLinks?)`

Defined in filename.h, line 207

Get the type of the file. If the file named by this object exists, returns an integer with a bitwise combination of FileTypeXxx values indicating the type of the file. If the file doesn't exist, or can't be accessed due to file system permissions or some other operating system error, the return value is nil. Note that it's also possible for the return value to be zero, which means something different from nil: zero means that the file exists, but it doesn't fit any of the FileTypeXxx classifications.


### `getName`

Defined in filename.h, line 82

Get the filename. This returns a string with the filename this object represents, in the local syntax used by the host operating system, including the path and base filename portions. (This is the same string returned for toString(self), and the same string used if the filename is displayed as though it were a string, such as with "<< >>".)


### `getPath`

Defined in filename.h, line 99

Get the path portion name, without the file name. This returns a FileName object containing the path portion of the file name, with the last path element removed. If the path only contains one path element (so it contains only a file name, not a directory path), this returns nil.


### `isAbsolute`

Defined in filename.h, line 142

Is this an absolute path on the local system? An absolute path is one that contains a root folder specification, such as a Unix path starting with "/", Windows path starting with "C:\", or a Windows UNC name such as "\\SERVER\SHARE".


### `listDir`

Defined in filename.h, line 259

Get a list of files in the directory named by this object. Returns a list of FileName objects giving the names of the files.


### `removeDirectory(removeContents?)`

Defined in filename.h, line 311

Remove the directory named by this object. The file safety settings must allow write access to the directory.


### `renameFile(newname)`

Defined in filename.h, line 238

Rename or move the file. This changes the name and/or file path location of the file named by 'self' to the given new path, which can be a string giving a filename in local path notation, or a FileName object with the new name. The file safety settings must allow write access to both the original file and the new file. The new file must not already exist.


### `toUniversal`

Defined in filename.h, line 114

Get the universal URL-style notation for this file name. Returns a string giving the universal notation for the file name (including any path portion).


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
