# adv3LibPreinit

*object* — defined in [misc.t](../by-file/misc.t.md) (line 697)


Library Pre-Initializer. This object performs the following initialization operations immediately after compilation is completed:


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **adv3LibPreinit**


## Properties


### `execBeforeMe` *(overridden)*

Defined in misc.t, line 825

Make sure the output streams we depend on are initialized before me (so that they set up properly internally). Also, make sure that the message builder object (langMessageBuilder) is set up first, so that we can add entries to its parameter substitution table.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in misc.t, line 698


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
