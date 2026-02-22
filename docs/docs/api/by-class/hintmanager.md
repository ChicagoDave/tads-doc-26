# hintManager

*object* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 517)


The default hint system user interface implementation. All of the hint-related verbs operate by calling methods in the object stored in the global variable gHintSystem, which we'll by default initialize with a reference to this object. Games can replace this with their own implementations if desired.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **hintManager**


## Properties


### `topHintMenuObj`

Defined in hintsys.t, line 562

The top-level hint menu. This must be provided by the game, and should be set during initialization. If this is nil, hints won't be available.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `disableHints`

Defined in hintsys.t, line 535

Disable hints - this is invoked by the HINTS OFF action.


### `execute` *(overridden)*

Defined in hintsys.t, line 519

during pre-initialization, register as the global hint manager


### `showHints`

Defined in hintsys.t, line 567

Show hints - invoke the hint system.


### `showHintWarning`

Defined in hintsys.t, line 609

Show a warning before showing any hints. By default, we'll show this at most once per session or once per saved game. Returns true if we are to proceed to the hints, nil if not.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
