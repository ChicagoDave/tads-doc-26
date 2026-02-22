# scoreNotifier

*object* — defined in [score.t](../by-file/score.t.md) (line 223)


Score notification daemon handler. We'll receive a checkNotification() call each turn; we'll display a notification message each time the score has changed since the last time we ran.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **scoreNotifier**


## Properties


### `everNotified`

Defined in score.t, line 228

we've never generated a notification about the score before


### `lastScore`

Defined in score.t, line 225

the score as it was the last time we displayed a notification


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `checkNotification`

Defined in score.t, line 231

daemon entrypoint


### `execute` *(overridden)*

Defined in score.t, line 277

execute pre-initialization


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
