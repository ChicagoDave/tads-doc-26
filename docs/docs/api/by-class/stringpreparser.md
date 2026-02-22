# StringPreParser

*class* — defined in [input.t](../by-file/input.t.md) (line 844)


Base class for command input string preparsers.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **StringPreParserGlobal objects:** [commentPreParser](commentpreparser.md), [specialTopicPreParser](specialtopicpreparser.md)


## Properties


### `regList`

Defined in input.t, line 941

class property containing the list of registered parsers


### `regListSorted`

Defined in input.t, line 944

class property - the registration list has been sorted


### `runOrder`

Defined in input.t, line 850

My execution order number. When multiple preparsers are registered, we'll run the preparsers in ascending order of this value (i.e., smallest runOrder goes first).


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `construct`

Defined in input.t, line 876

construction - when we dynamically create a preparser, register it by default


### `doParsing(str, which)`

Defined in input.t, line 866

Do our parsing. Each instance should override this method to define the parsing that it does.


### `execute` *(overridden)*

Defined in input.t, line 883

run pre-initialization


### `registerPreParser(pp)`

Defined in input.t, line 890

register a preparser


### `runAll(str, which)`

Defined in input.t, line 907

Class method - Run all preparsers. Returns the result of successively calling each preparser on the given string.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
