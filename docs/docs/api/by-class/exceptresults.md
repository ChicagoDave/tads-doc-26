# ExceptResults

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6867)


Except list results object


**Superclass chain:** `object` > **ExceptResults**


## Properties


### `origResults`

Defined in parser.t, line 6913

my original underlying results object


## Methods


### `ambiguousNounPhrase(keeper, asker, txt, matchList, fullMatchList, scopeList, requiredNum, resolver)`

Defined in parser.t, line 6898

in case of ambiguity, simply keep everything and treat it as unambiguous - if they say "take coin except copper", we simply want to treat "copper" as unambiguously excluding every copper coin in the original list


### `construct(results)`

Defined in parser.t, line 6868


### `noMatch(action, txt)`

Defined in parser.t, line 6879

ignore failed matches in the exception list - if they try to exclude something that's not in the original list, the object is excluded to begin with


### `noMatchForLocation(loc, txt)`

Defined in parser.t, line 6887

ignore failed matches for location in the exception list


### `noMatchForPossessive(owner, txt)`

Defined in parser.t, line 6884

ignore failed matches for possessives in the exception list


### `noMatchPoss(action, txt)`

Defined in parser.t, line 6880


### `nothingInLocation(loc)`

Defined in parser.t, line 6890

ignore failed matches for location in the exception list


### `noVocabMatch(action, txt)`

Defined in parser.t, line 6881


### `propNotDefined(prop, [args])`

Defined in parser.t, line 6907

proxy anything we don't override to the underlying results object
