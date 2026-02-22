# StringBuffer

*class* — defined in [strbuf.h](../by-file/strbuf.h.md) (line 44)


A StringBuffer is a mutable character string object. You can insert, append, delete, and replace characters in the buffer in place. These operations don't create new objects as they do with ordinary strings, but simply modify the existing StringBuffer object's contents.


## Methods


### `append(str)`

Defined in strbuf.h, line 65

Append text to the current contents of the buffer. This adds the new text at the end of the current text. The value is automatically converted to a string if possible; this includes numbers and true and nil values.


### `charAt(idx)`

Defined in strbuf.h, line 57

Retrieve the Unicode character value of the character at the given index. Returns an integer with the Unicode value. If idx is negative, it's an index from the end of the string: -1 is the last character, -2 is the second to last, etc.


### `copyChars(txt, idx)`

Defined in strbuf.h, line 82

Copy text into the buffer, starting at the given index (the first character in the buffer is at index 1). Overwrites any text currently in the buffer at this point.


### `deleteChars(idx, len?)`

Defined in strbuf.h, line 90

Delete the given text. This deletes 'len' characters starting at the given index (the first character is at index 1). If the length is omitted, the portion from idx to the end of the string is deleted. A negative idx value indexes from the end of the string.


### `insert(txt, idx)`

Defined in strbuf.h, line 75

Insert text into the buffer just before the character at the given index. The first character is at index 1, so to insert the new text before the first current character, insert at index 1. If the index is past the end of the current text, this has the same effect as append(). A negative value indexes from the end of the string. The text is automatically converted to a string if possible.


### `length`

Defined in strbuf.h, line 49

Get the length in characters of the current text in the buffer.


### `splice(idx, len, str)`

Defined in strbuf.h, line 101

Splice text. This deletes 'len' characters starting at the given index (the first character is at index 1), and replaces them with the given new text. If the new text is nil, this simply deletes the old characters without inserting anything new. If 'len' is zero, simply inserts the new text without deleting any old text. A negative idx value indexes from the end of the string. The 'str' value is automatically converted to a string if possible.


### `substr(idx, len?)`

Defined in strbuf.h, line 110

Retrieve the substring of the buffer starting at the given index and running for the given character length. If the length is omitted, everything from the starting index to the end of the buffer is included in the result string. A negative value for 'idx' indexes from the end of the string.
