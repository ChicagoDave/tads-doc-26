# BagAffinityInfo

*class* — defined in [thing.t](../by-file/thing.t.md) (line 373)


Bag Affinity Info - this class keeps track of the affinity of a bag of holding for an object it might contain. We use this class in building bag affinity lists.


**Superclass chain:** `object` > **BagAffinityInfo**


## Properties


### `aff_`

Defined in thing.t, line 450

affinity of the bag for the object


### `bag_`

Defined in thing.t, line 447

the bag that wants to contain the object


### `bulk_`

Defined in thing.t, line 444

the object's bulk


### `obj_`

Defined in thing.t, line 441

the object the bag wants to contain


## Methods


### `compareAffinityTo(other)`

Defined in thing.t, line 389

Compare this item to another item, for affinity ranking purposes. Returns positive if I should rank higher than the other item, zero if we have equal ranking, negative if I rank lower than the other item.


### `construct(obj, bulk, aff, bag)`

Defined in thing.t, line 374


### `removeMostRecent(vec)`

Defined in thing.t, line 421

given a vector of affinities, remove the most recent item (as indicated by holdingIndex) and return the BagAffinityInfo object
