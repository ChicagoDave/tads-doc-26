# RetryCommandTokensException

*class* — defined in [parser.t](../by-file/parser.t.md) (line 7003)


Exception: Retry a command with new tokens. In some cases, the parser processes a command by replacing the command with a new one and processing the new one instead of the original. When this happens, the parser will throw this exception, filling in newTokens_ with the replacement token list.


**Superclass chain:** [ParserException](parserexception.md) > [Exception](exception.md) > `object` > **RetryCommandTokensException**


## Properties


### `newTokens_`

Defined in parser.t, line 7016

The replacement token list. Note that this is in the same format as the token list returned from the tokenizer, so this is a list consisting of two sublists - one for the token strings, the other for the corresponding token types.


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(lst)` *(overridden)*

Defined in parser.t, line 7004


## Inherited Methods


*From [Exception](exception.md):* [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
