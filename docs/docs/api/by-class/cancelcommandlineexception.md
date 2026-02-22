# CancelCommandLineException

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6952)


Cancel Command Line exception. This is used to cancel any *remaining* commands on a command line after finishing execution of one command on the line. For example, if the player types "TAKE BOX AND GO NORTH", the handler for TAKE BOX can throw this exception to cancel everything later on the command line (in this case, the GO NORTH part).


**Superclass chain:** [TerminateCommandException](terminatecommandexception.md) > [ParserException](parserexception.md) > [Exception](exception.md) > `object` > **CancelCommandLineException**


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Inherited Methods


*From [Exception](exception.md):* [`construct`](exception.md#construct), [`displayException`](exception.md#displayException), [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
