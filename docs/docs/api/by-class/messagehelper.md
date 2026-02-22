# MessageHelper

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 3153)


Some helper routines for the library messages.


**Superclass chain:** `object` > **MessageHelperGlobal objects:** [libMessages](libmessages.md), [playerActionMessages](playeractionmessages.md)


## Methods


### `askDisambigList(matchList, fullMatchList, showIndefCounts, dist)`

Defined in en_us.t, line 3160

Show a list of objects for a disambiguation query. If 'showIndefCounts' is true, we'll show the number of equivalent items for each equivalent item; otherwise, we'll just show an indefinite noun phrase for each equivalent item.


### `shortTIMsg(short, long)`

Defined in en_us.t, line 3270

For a TIAction result, select the short-form or long-form message. This works just like shortTIMsg(), but takes into account both the direct and indirect objects.


### `shortTMsg(short, long)`

Defined in en_us.t, line 3247

For a TAction result, select the short-form or long-form message, according to the disambiguation status of the action. This is for the ultra-terse default messages, such as "Taken" or "Dropped", that sometimes need more descriptive variations.
