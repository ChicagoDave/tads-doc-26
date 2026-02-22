# DropTypeShortThrow

*class* — defined in [sense.t](../by-file/sense.t.md) (line 843)


A drop-type descriptor for a "short throw," which occurs when the target is too far away to reach with our throw (i.e., the thrown object falls short of the target).


**Superclass chain:** [DropTypeThrow](droptypethrow.md) > [DropType](droptype.md) > `object` > **DropTypeShortThrow**


## Inherited Properties


*From [DropTypeThrow](droptypethrow.md):* [`path_`](droptypethrow.md#path_), [`target_`](droptypethrow.md#target_)


## Methods


### `construct(target, path)` *(overridden)*

Defined in sense.t, line 844


### `getReportPrefix(obj, dest)` *(overridden)*

Defined in sense.t, line 860

show the short-throw report


### `standardReport(obj, dest)` *(overridden)*

Defined in sense.t, line 853

we care about the *intended* target, not the distance connector
