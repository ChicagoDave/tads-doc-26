# wornState

*object* — defined in [en_us.t](../by-file/en_us.t.md) (line 3628)


"worn"


**Superclass chain:** [ThingState](thingstate.md) > `object` > **wornState**


## Inherited Properties


*From [ThingState](thingstate.md):* [`listingOrder`](thingstate.md#listingOrder), [`listName_`](thingstate.md#listName_), [`stateTokens`](thingstate.md#stateTokens)


## Methods


### `wornName(lst)` *(overridden)*

Defined in en_us.t, line 3635

In listings of worn items, don't bother mentioning our 'worn' status, as the entire list consists of items being worn - it would be redundant to point out that the items in a list of items being worn are being worn.


## Inherited Methods


*From [ThingState](thingstate.md):* [`findStateToken`](thingstate.md#findStateToken), [`inventoryName`](thingstate.md#inventoryName), [`listName`](thingstate.md#listName), [`matchName`](thingstate.md#matchName)
