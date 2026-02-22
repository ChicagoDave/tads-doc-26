# DropTypeThrow

*class* — defined in [thing.t](../by-file/thing.t.md) (line 327)


A drop-type descriptor for the THROW command. This object keeps track of the target (the object that was hit by the projectile) and the projectile's path to the target. The projectile is simply the direct object.


**Superclass chain:** [DropType](droptype.md) > `object` > **DropTypeThrowSubclasses:** [DropTypeShortThrow](droptypeshortthrow.md)


## Properties


### `path_`

Defined in thing.t, line 363

the path the projectile took to reach the target


### `target_`

Defined in thing.t, line 360

the object that was hit by the projectile


## Methods


### `construct(target, path)`

Defined in thing.t, line 328


### `getReportPrefix(obj, dest)` *(overridden)*

Defined in thing.t, line 353

if the actual target and the nominal destination are the same, just say that it lands on the destination; otherwise, say that it bounces off the target and falls to the nominal destination


### `standardReport(obj, dest)` *(overridden)*

Defined in thing.t, line 335

remember the target and path
