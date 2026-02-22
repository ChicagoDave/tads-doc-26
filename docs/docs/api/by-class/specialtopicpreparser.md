# specialTopicPreParser

*object* — defined in [actor.t](../by-file/actor.t.md) (line 1903)


Pre-parser for special ConvNode-specific commands. When the player character is talking to another character, and the NPC's current ConvNode includes topics with their own commands, we'll check the player's input to see if it matches any of these topics.


**Superclass chain:** [StringPreParser](stringpreparser.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **specialTopicPreParser**


## Properties


### `aOrTPat`

Defined in en_us.t, line 2731

pattern for string starting with "A" or "T" verbs


### `punctPat`

Defined in en_us.t, line 2735

pattern to eliminate punctuation marks from the string


## Inherited Properties


*From [StringPreParser](stringpreparser.md):* [`regList`](stringpreparser.md#regList), [`regListSorted`](stringpreparser.md#regListSorted), [`runOrder`](stringpreparser.md#runOrder)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `doParsing(str, which)` *(overridden)*

Defined in actor.t, line 1904


### `processInputStr(str)`

Defined in en_us.t, line 2714

Process the input string, as desired, for special-topic parsing. This method is for the language module's use; by default, we do nothing.


## Inherited Methods


*From [StringPreParser](stringpreparser.md):* [`construct`](stringpreparser.md#construct), [`execute`](stringpreparser.md#execute), [`registerPreParser`](stringpreparser.md#registerPreParser), [`runAll`](stringpreparser.md#runAll)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
