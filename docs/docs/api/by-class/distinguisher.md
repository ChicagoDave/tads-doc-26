# Distinguisher

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 25)


Distinguisher. This object encapsulates logic that determines whether or not we can tell two objects apart.


**Superclass chain:** `object` > **DistinguisherGlobal objects:** [basicDistinguisher](basicdistinguisher.md), [litUnlitDistinguisher](litunlitdistinguisher.md), [locationDistinguisher](locationdistinguisher.md), [nullDistinguisher](nulldistinguisher.md), [ownershipDistinguisher](ownershipdistinguisher.md)


## Methods


### `canDistinguish(a, b)`

Defined in disambig.t, line 27

can we distinguish the given two objects?


### `matchName(obj, origTokens, adjustedTokens, matchList, fullMatchList)`

Defined in disambig.t, line 79

Try matching an object to a noun phrase in a disambiguation reply from the player (that is, the player's response to a "Which foo did you mean" question). By default, we call the object's matchNameDisambig() method to let it try to match its disambiguation name.


### `notePrompt(lst)`

Defined in disambig.t, line 42

Note that we're showing a prompt to the player asking for help in narrowing the object list, based on this distinguisher. 'lst' is the list of ResolveInfo objects which we're mentioning in the prompt.


### `objInScope(obj, matchList, fullMatchList)`

Defined in disambig.t, line 55

Is the object in scope for the purposes of the disambiguation reply from the player? By default, any object in the full match list is in scope.
