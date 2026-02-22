# PostRestoreObject

*class* — defined in [actions.t](../by-file/actions.t.md) (line 194)


PostRestoreObject - every instance of this class is notified, via its execute() method, immediately after we restore the game.


**Superclass chain:** [ModuleExecObject](moduleexecobject.md) > `object` > **PostRestoreObjectGlobal objects:** [bannerTracker](bannertracker.md), [inputManager](inputmanager.md), [tipManager](tipmanager.md)


## Properties


### `restoreCode`

Defined in actions.t, line 217

The "restore code," which is the (normally integer) value passed as the second argument to restoreGame(). The restore code gives us some idea of what triggered the restoration. By default, we define the following restore codes:


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec), [`execute`](moduleexecobject.md#execute)
