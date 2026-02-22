# ByteArray

*class* — defined in [bytearr.h](../by-file/bytearr.h.md) (line 26)


'ByteArray' intrinsic class. This class provides a fixed-size array of unsigned 8-bit byte values; each array element is an integer in the range 0-255.


**Superclass chain:** [Object](object.md) > **ByteArray**


## Methods


### `copyFrom(src, srcStartIndex, dstStartIndex, length)`

Defined in bytearr.h, line 70

Copy bytes from the source array into this array. Bytes are copied into this array starting at the given index. The specified number of bytes are copied from the source array starting at the given index.


### `digestMD5`

Defined in bytearr.h, line 213

Get the MD5 digest of the string. This calculates the 128-bit RSA MD5 digest value, returning the digest as a 32-character string of hex digits. The hash value is computed on the UTF-8 representation of the string. If 'idx' and 'len' are specified, the give the range of bytes to include in the hash; the default is to hash the whole array.


### `fillValue(val, startIndex?, length?)`

Defined in bytearr.h, line 78

Fill bytes in this array with the given value. If no starting index or length values are given, the entire array is filled with the given byte value. The byte value must be an integer in the range 0 to 255.


### `length`

Defined in bytearr.h, line 55

Get the number of bytes in the array. The length is fixed at creation time.


### `mapToString(charset, startIndex?, length?)`

Defined in bytearr.h, line 88

Convert a range of bytes in the array to a string, interpreting the bytes in the array as characters in the given character set.


### `packBytes(idx, format, ...)`

Defined in bytearr.h, line 180

Pack data values into bytes according to a format definition string, and store the packed bytes in the byte array starting at the given index.


### `readInt(startIndex, format)`

Defined in bytearr.h, line 127

Read an integer value from the byte array. Reads bytes from the starting index; the number of bytes read depends on the format. Returns an integer giving the value read.


### `sha256(idx?, len?)`

Defined in bytearr.h, line 203

Get the SHA-256 hash of the bytes in the array. This calculates the 256-bit Secure Hash Algorithm 2 hash value, returning the hash as a 64-character string of hex digits. The hash value is computed on the UTF-8 representation of the string. If 'idx' and 'len' are specified, they give the range of bytes to include in the hash; the default is to hash the whole array.


### `subarray(startIndex, length?)`

Defined in bytearr.h, line 62

create a new ByteArray as a copy of the given range of this array; if the length is not given, bytes from the starting index to the end of this array are included in the new array


### `unpackBytes(idx, format)`

Defined in bytearr.h, line 193

Unpack bytes from the byte array starting at the given index, and translate the bytes into data values according to the given format string.


### `writeInt(startIndex, format, val)`

Defined in bytearr.h, line 151

Write an integer value to the byte array. Writes bytes starting at the given index; the number of bytes written depends on the format. The 'format' parameter gives the format, using the same codes as in readInt(). 'val' is the integer value to be written. If 'val' is outside of the bounds of the format to be written, the written value is truncated.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
