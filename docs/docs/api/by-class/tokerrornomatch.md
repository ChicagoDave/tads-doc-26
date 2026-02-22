# TokErrorNoMatch

*class* — defined in [tok.t](../by-file/tok.t.md) (line 35)


no match for token


**Superclass chain:** [TokenizerError](tokenizererror.md) > [Exception](exception.md) > `object` > **TokErrorNoMatch**


## Properties


### `curChar_`

Defined in tok.t, line 59

current character (first character of remainingStr_)


### `remainingStr_`

Defined in tok.t, line 56

The remainder of the string. This is the part that couldn't be matched; we were successful in matching up to this point.


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(str)` *(overridden)*

Defined in tok.t, line 36


### `displayException` *(overridden)*

Defined in tok.t, line 49

for convenience, separately remember the single character that we don't recognize - this is simply the first character of the rest of the line


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
