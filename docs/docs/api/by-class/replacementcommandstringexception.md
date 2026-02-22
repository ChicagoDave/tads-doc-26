# ReplacementCommandStringException

*class* — defined in [parser.t](../by-file/parser.t.md) (line 7025)


Replacement command string exception. Abort any current command line, and start over with a brand new input string. Note that any pending, unparsed tokens on the previous command line should be discarded.


**Superclass chain:** [ParserException](parserexception.md) > [Exception](exception.md) > `object` > **ReplacementCommandStringException**


## Properties


### `issuingActor_`

Defined in parser.t, line 7045

the actor issuing the command


### `newCommand_`

Defined in parser.t, line 7042

the new command string


### `targetActor_`

Defined in parser.t, line 7048

the default target actor of the command


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(str, issuer, target)` *(overridden)*

Defined in parser.t, line 7026


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
