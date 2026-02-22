# CheckStatus

*class* — defined in [thing.t](../by-file/thing.t.md) (line 185)


Command check status object. This is an abstract object that we use in to report results from a check of various kinds.


**Superclass chain:** `object` > **CheckStatusSubclasses:** [CheckStatusFailure](checkstatusfailure.md)


**Global objects:** [checkStatusSuccess](checkstatussuccess.md)


## Properties


### `isSuccess`

Defined in thing.t, line 187

did the check succeed or fail?


### `msgParams`

Defined in thing.t, line 194


### `msgProp`

Defined in thing.t, line 193

the message property or string, and parameters, for failure - this is for use with reportFailure or the like
