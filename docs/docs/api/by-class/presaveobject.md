# PreSaveObject

*class* — defined in [actions.t](../by-file/actions.t.md) (line 183)


PreSaveObject - every instance of this class is notified, via its execute() method, just before we save the game. This uses the ModuleExecObject framework, so the sequencing lists (execBeforeMe, execAfterMe) can be used to control relative ordering of execution among instances.


**Superclass chain:** [ModuleExecObject](moduleexecobject.md) > `object` > **PreSaveObject**


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec), [`execute`](moduleexecobject.md#execute)
