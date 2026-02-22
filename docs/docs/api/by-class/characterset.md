# CharacterSet

*class* — defined in [charset.h](../by-file/charset.h.md) (line 22)


The CharacterSet intrinsic class provides information on character set translations and can be used to translate between the Unicode character set that the T3 VM uses internally for string values and the local character set or sets used for display, keyboard input, and file I/O.


**Superclass chain:** [Object](object.md) > **CharacterSet**


## Methods


### `getName`

Defined in charset.h, line 56

Get the name of the character set. This simply returns the name that was given to construct the character set.


### `isMappable(val)`

Defined in charset.h, line 76

Determine if a character or string of characters is mappable to this character set. If the input is an integer, it represents the Unicode character code for a single character; if the input is a string, each character in the string is checked. This returns true if every character given has a valid mapping in the local character set, nil if not. Note that if a string is given, and even one character is not mappable, this returns nil.


### `isMappingKnown`

Defined in charset.h, line 65

Determine if the mapping is known. This returns true if the character set has a known local mapping, nil if not. Note that it doesn't matter whether or not the character set is actually in use on the local platform; all that matters is that a T3 mapping file is available on this machine.


### `isRoundTripMappable(val)`

Defined in charset.h, line 93

Determine if a character or string of characters is "round-trip" mappable to this character set. If the input is an integer, it represents a Unicode character code to be tested; if the input is a string, each character in the string is tested. Returns true if every character given has a valid round-trip mapping, nil if not.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
