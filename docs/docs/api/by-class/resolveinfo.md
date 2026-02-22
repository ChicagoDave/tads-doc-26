# ResolveInfo

*class* — defined in [parser.t](../by-file/parser.t.md) (line 345)


The resolveNouns() method returns a list of ResolveInfo objects describing the objects matched to the noun phrase.


**Superclass chain:** `object` > **ResolveInfoGlobal objects:** [dummyTentativeInfo](dummytentativeinfo.md)


## Properties


### `flags_`

Defined in parser.t, line 393

flags describing how we matched the object


### `multiAnnounce`

Defined in parser.t, line 440

The pre-calculated multi-object announcement text for this object. When we iterate over the object list in a command with multiple direct or indirect objects (TAKE THE BOOK, BELL, AND CANDLE), we calculate the little announcement messages ("book:") for the objects BEFORE we execute the actual commands. We then use the pre-calculated announcements during our iteration. This ensures consistency in the basis for choosing the names, which is important in cases where the names include state-dependent information for the purposes of distinguishing one object from another. The relevant state can change over the course of executing the command on the objects in the iteration, so if we calculated the names on the fly we could end up with inconsistent naming. The user thinks of the objects in terms of their state at the start of the command, so the pre-calculation approach is not only more internally consistent, but is also more consistent with the user's perspective.


### `np_`

Defined in parser.t, line 420

the noun phrase we parsed to come up with this object


### `obj_`

Defined in parser.t, line 390

the object matched


### `possRank_`

Defined in parser.t, line 414

The possessive ranking, if applicable. If this object is qualified by a possessive phrase ("my books"), we'll set this to a value indicating how strongly the possession applies to our object: 2 indicates that the object is explicitly owned by the object indicated in the possessive phrase, 1 indicates that it's directly held by the named possessor but not explicitly owned, and 0 indicates all else. In cases where there's no posessive qualifier, this will simply be zero.


### `pronounType_`

Defined in parser.t, line 417

the pronoun type we matched, if any (as a PronounXxx enum)


### `quant_`

Defined in parser.t, line 402

By default, each ResolveInfo counts as one object, for the purposes of a quantity specifier (as in "five coins" or "both hats"). However, in some cases, a single resolved object might represent a collection of discrete objects and thus count as more than one for the purposes of the quantifier.


## Methods


### `construct(obj, flags, np, =, nil)`

Defined in parser.t, line 346


### `isDistEquivInList(lst, dist)`

Defined in parser.t, line 378

Look for a ResolveInfo item in a list of ResolveInfo items that is equivalent to us according to a particular Distinguisher.


### `isEquivalentInList(lst)`

Defined in parser.t, line 363

Look for a ResolveInfo item in a list of ResolveInfo items that is equivalent to us. Returns true if we find such an item, nil if not.
