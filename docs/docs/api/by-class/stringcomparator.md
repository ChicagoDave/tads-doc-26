# StringComparator

*class* — defined in [strcomp.h](../by-file/strcomp.h.md) (line 29)


StringComparator intrinsic class. This class provides support for dictionaries based on complex string matches, including truncation (matching an input word to a dictionary word when the input word is at least some minimum length, and matches the dictionary word up to the full length of the input word, but the input word is shorter than the dictionary word); case folding (matching upper-case letters to lower-case letters and vice versa); and character equivalences (for matching accented characters to non-accented equivalents, or matching special characters to multi-character equivalents, such as matching a German "ess-zet" ("sharp-s") ligature to a pair of lower-case "s" characters in input).


**Superclass chain:** [Object](object.md) > **StringComparator**


## Methods


### `calcHash(str)`

Defined in strcomp.h, line 82

Calculate a hash value. This returns an integer giving the hash value for the given string.


### `matchValues(inputStr, dictStr)`

Defined in strcomp.h, line 100

Match two values. The first value is the input string, and the second is the dictionary string. Each character in the dictionary string can match the corresponding input string character exactly (with or without case sensitivity, as specified in our constructor), or can match the equivalence mapping sequence for the dictionary character.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
