# Dictionary

*class* — defined in [dict.h](../by-file/dict.h.md) (line 27)


The Dictionary intrinsic class is a specialized lookup table class designed for storing the vocabulary table for a parser. Dictionary works closely with GrammarProd to supply the vocabulary tokens for the productions.


**Superclass chain:** [Object](object.md) > **Dictionary**


## Methods


### `addWord(obj, str, voc_prop)`

Defined in dict.h, line 137

Add a word to the dictionary, associating the given object with the given string and property combination.


### `correctSpelling(str, maxEditDistance)`

Defined in dict.h, line 224

Get a list of possible spelling corrections for the given word. This searches the dictionary for words that match the given word within the given maximum "edit distance".


### `findWord(str, voc_prop?)`

Defined in dict.h, line 131

Find a word; returns a list giving the objects associated with the string in the dictionary. If voc_prop is specified, only objects associated with the word by the given vocabulary property are returned. We match the string using the comparator defined for the dictionary.


### `forEachWord(func)`

Defined in dict.h, line 175

Invoke the callback func(obj, str, prop) for each word in the dictionary. Note that the callback can be invoked with a single string multiple times, since the callback is invoked once per word/object/property association; in other words, the callback is invoked once for each association created with addWord() or during compilation.


### `isWordDefined(str, filter?)`

Defined in dict.h, line 165

Check to see if the given string 'str' is defined in the dictionary. Returns true if the word is defined, nil if not.


### `removeWord(obj, str, voc_prop)`

Defined in dict.h, line 144

Remove the given word association from the dictionary. This removes only the association for the given object; other objects associated with the same word are not affected.


### `setComparator(compObj)`

Defined in dict.h, line 104

Set the comparator object. This defines how words are compared. The object must provide the following methods, which comprise the "comparator" interface. Note that there's no class that defines this interface; this is simply a set of methods that we define here, and which the supplied object must define.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
