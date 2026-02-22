# DisambigOrdinalOutOfRangeException

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 518)


Disambiguation Ordinal Out Of Range - this is thrown when the user answers a disambiguation question with an ordinal, but the ordinal is outside the bounds of the offered list (for example, we ask "which book do you mean, the red book, or the blue book?", and the user answers "the fourth one").


**Superclass chain:** [DisambigException](disambigexception.md) > [Exception](exception.md) > `object` > **DisambigOrdinalOutOfRangeException**


## Properties


### `ord_`

Defined in disambig.t, line 526

a string giving the ordinal word entered by the user


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(ord)` *(overridden)*

Defined in disambig.t, line 519


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
