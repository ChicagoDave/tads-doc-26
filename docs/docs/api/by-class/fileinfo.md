# FileInfo

*class* — defined in [file.t](../by-file/file.t.md) (line 21)


File status information. This is returned from file.getFileInfo().


**Superclass chain:** `object` > **FileInfo**


## Properties


### `fileAccessTime`

Defined in file.t, line 81


### `fileAttrs`

Defined in file.t, line 69

file attributes, as a combination of FileAttrXxx bit flags (see filename.h)


### `fileCreateTime`

Defined in file.t, line 79

The file's time of creation, last modification, and last access, as Date objects. On some systems, these timestamps might not all be available; an item that's not available is set to nil.


### `fileLinkTarget`

Defined in file.t, line 57

Link target. If the file is a symbolic link, this contains a string giving the target file's path. This is the direct target of this link, which might itself be another link.


### `fileModifyTime`

Defined in file.t, line 80


### `fileSize`

Defined in file.t, line 72

size of the file in bytes


### `fileType`

Defined in file.t, line 63

type of the file, as a combination of FileTypeXxx bit flags (see filename.h)


### `isDir`

Defined in file.t, line 38

is this file a directory?


### `specialLink`

Defined in file.t, line 50

Is this a special link directory? This is FileTypeSelfLink for a directory link to itself; it's FileTypeParentLink for a directory link to the parent; it's zero for all other files. On Windows and Unix, these flags will be set for the special "." and ".." directories, respectively. These flags only apply to the *system-defined* special links; they aren't set for user-created links that happen to point to self or parent. This is zero for all other files.


## Methods


### `construct(typ, siz, ctime, mtime, atime, target, attrs, ...)`

Defined in file.t, line 22
