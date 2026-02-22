# String

*class* — defined in [systype.h](../by-file/systype.h.md) (line 307)


The native string type.


**Superclass chain:** [Object](object.md) > **String**


## Methods


### `endsWith(str)`

Defined in systype.h, line 337

determine if we end with the given string


### `find(str, index, ?)`

Defined in systype.h, line 322

find a substring


### `findReplace(origStr, newStr, flags, index, ?)`

Defined in systype.h, line 352

Replace one occurrence or all occurrences of the given substring with the given new string.


### `htmlify(flags, ?)`

Defined in systype.h, line 331

htmlify a string


### `length`

Defined in systype.h, line 310

get the length of the string


### `mapToByteArray(charset)`

Defined in systype.h, line 346

Map to a byte array, converting to the given character set. 'charset' must be an object of intrinsic class CharacterSet; the characters in the string will be mapped from the internal Unicode representation to the appropriate byte representation in the given character set.


### `startsWith(str)`

Defined in systype.h, line 334

determine if we start with the given string


### `substr(start, len, ?)`

Defined in systype.h, line 313

extract a substring


### `toLower`

Defined in systype.h, line 319

convert to lower case


### `toUnicode(idx, ?)`

Defined in systype.h, line 328

convert to a list of Unicode character codes, or get the Unicode character code for the single character at the given index


### `toUpper`

Defined in systype.h, line 316

convert to upper case


### `valToSymbol` *(overridden)*

Defined in reflect.t, line 237


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType)
