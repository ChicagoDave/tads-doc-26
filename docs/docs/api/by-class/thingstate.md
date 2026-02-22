# ThingState

*class* — defined in [thing.t](../by-file/thing.t.md) (line 471)


"State" of a Thing. This is an object abstractly describing the state of an object that can assume different states.


**Superclass chain:** `object` > **ThingStateGlobal objects:** [lightSourceStateOff](lightsourcestateoff.md), [lightSourceStateOn](lightsourcestateon.md), [matchStateLit](matchstatelit.md), [matchStateUnlit](matchstateunlit.md), [unwornState](unwornstate.md), [wornState](wornstate.md)


## Properties


### `listingOrder`

Defined in thing.t, line 504

the relative listing order


### `listName_`

Defined in en_us.t, line 325

our list name setting - we define this so that we can be easily initialized with a template (we can't initialize listName() directly in this manner because it's a method, but we define the listName() method to simply return this property value, which we can initialize with a template)


### `stateTokens`

Defined in en_us.t, line 242

Our state-specific tokens. This is a list of vocabulary words that are state-specific: that is, if a word is in this list, the word can ONLY refer to this object if the object is in a state with that word in its list.


## Methods


### `findStateToken(toks)`

Defined in en_us.t, line 293

Check a token list for any tokens matching any of our state-specific words. Returns true if we find any such words, nil if not.


### `inventoryName(lst)`

Defined in thing.t, line 494

The state name to use in inventory lists. By default, we just use the base name. 'lst' has the same meaning as in listName().


### `listName(lst)`

Defined in en_us.t, line 316

The name of the state to use in ordinary room/object contents listings. If the name is nil, no extra state information is shown in a listing for an object in this state. (It's often desirable to leave the most ordinary state an object can be in unnamed, to avoid belaboring the obvious. For example, a match that isn't burning would probably not want to mention "(not lit)" every time it's listed.)


### `matchName(obj, origTokens, adjustedTokens, states)`

Defined in en_us.t, line 250

Match the name of an object in this state. 'obj' is the object to be matched; 'origTokens' and 'adjustedTokens' have the same meanings they do for Thing.matchName; and 'states' is a list of all of the possible states the object can assume.


### `wornName(lst)`

Defined in thing.t, line 501

The state name to use in listings of items being worn. By default, we just use the base name. 'lst' has the same meaning as in listName().
