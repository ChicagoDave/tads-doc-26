# InitObject

*class* — defined in [_main.t](../by-file/_main.t.md) (line 489)


Initialization object. During initialization, just before calling the user's main(args) function, we'll invoke the execute() method on each instance of this class.


**Superclass chain:** [ModuleExecObject](moduleexecobject.md) > `object` > **InitObjectGlobal objects:** [adv3LibInit](adv3libinit.md), [bannerInit](bannerinit.md), [realTimeManager](realtimemanager.md), [tipManager](tipmanager.md)


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec), [`execute`](moduleexecobject.md#execute)
