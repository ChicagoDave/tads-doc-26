# UnmatchedDisambigException

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 499)


Unmatched disambiguation - we throw this when the user answers a disambiguation question with a syntactically valid response that doesn't refer to any of the objects in the list of choices offered.


**Superclass chain:** [DisambigException](disambigexception.md) > [Exception](exception.md) > `object` > **UnmatchedDisambigException**


## Properties


### `resp_`

Defined in disambig.t, line 507

the response text


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(resp)` *(overridden)*

Defined in disambig.t, line 500


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
