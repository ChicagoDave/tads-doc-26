# TerminateCommandException

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6938)


Terminate Command exception - when the parser encounters an error that makes it impossible to go any further processing a command, we throw this error to abandon the current command and proceed to the next. This indicates a syntax error or semantic resolution error that renders the command meaningless or makes it impossible to proceed.


**Superclass chain:** [ParserException](parserexception.md) > [Exception](exception.md) > `object` > **TerminateCommandExceptionSubclasses:** [CancelCommandLineException](cancelcommandlineexception.md)


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
