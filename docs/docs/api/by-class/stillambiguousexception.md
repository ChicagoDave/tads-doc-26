# StillAmbiguousException

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 479)


Still Ambiguous Exception - this is thrown when the user answers a disambiguation question with insufficient specificity, so that we still have an ambiguous list.


**Superclass chain:** [DisambigException](disambigexception.md) > [Exception](exception.md) > `object` > **StillAmbiguousException**


## Properties


### `matchList_`

Defined in disambig.t, line 488

the narrowed, but still ambiguous, match list


### `origText_`

Defined in disambig.t, line 491

the text of the new phrasing


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(matchList, origText)` *(overridden)*

Defined in disambig.t, line 480


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
