# ParseFailureException

*class* — defined in [parser.t](../by-file/parser.t.md) (line 6961)


Parsing failure exception. This exception is parameterized with message information describing the failure, and can be used to route the failure notification to the issuing actor.


**Superclass chain:** [ParserException](parserexception.md) > [Exception](exception.md) > `object` > **ParseFailureException**


## Properties


### `args_`

Defined in parser.t, line 6988

the (varargs) parameters to the message


### `message_`

Defined in parser.t, line 6985

the message property ID


## Inherited Properties


*From [Exception](exception.md):* [`errmsg_`](exception.md#errmsg_)


## Methods


### `construct(messageProp, [args])` *(overridden)*

Defined in parser.t, line 6962


### `displayException` *(overridden)*

Defined in parser.t, line 6982

Tell the target actor to notify the issuing actor. We route the notification from the target to the issuer in keeping with conversation we're modelling: the issuer asked the target to do something, so the target is now replying with information explaining why the target can't do as asked.


### `notifyActor(targetActor, issuingActor)`

Defined in parser.t, line 6970

notify the issuing actor of the problem


## Inherited Methods


*From [Exception](exception.md):* [`getExceptionMessage`](exception.md#getExceptionMessage), [`showStackTrace`](exception.md#showStackTrace)
