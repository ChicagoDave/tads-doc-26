# GrammarProd

*class* — defined in [gramprod.h](../by-file/gramprod.h.md) (line 44)


The GrammarProd intrinsic class is a specialized type that's designed for creating parsers. An object of this type is created automatically by the TADS 3 compiler for each 'grammar' statement. This class encapsulates the prototype token list and mapping information defined in a 'grammar' statement, and provides a method to match its prototype to an input token string.


**Superclass chain:** [Object](object.md) > **GrammarProd**


## Methods


### `addAlt(alt, matchObj, dict?, symtab?)`

Defined in gramprod.h, line 84

Add a new alternative set of alternatives to the rule list for this grammar production.


### `clearAlts(dict?)`

Defined in gramprod.h, line 123

Delete all alternatives from the rule list for this grammar production. This resets the rule to an empty production with no alternatives to match, which is convenient if you want to redefine the entire rule set with a subsequent addAlt() call.


### `deleteAlt(id, dict?)`

Defined in gramprod.h, line 111

Delete onen or more alternatives from the rule list for this grammar production. 'id' identifies the rule(s) to delete:


### `getGrammarInfo`

Defined in gramprod.h, line 58

Retrieve a detailed description of the production. This returns a list of GrammarAltInfo objects that describe the rule alternatives that make up this production.


### `parseTokens(tokenList, dict)`

Defined in gramprod.h, line 51

Parse the token list, starting at this production, using the given dictionary to look up tokens. Returns a list of match objects. If there are no matches to the grammar, simply returns an empty list.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
