# tipManager

*object* — defined in [tips.t](../by-file/tips.t.md) (line 23)


The tip manager keeps track of which tips we have shown. Since we don't want to unnecessarily show any tips more than once, we store this information both transiently (in the tipManager) and persistently (in the tip objects themselves). This should make sure that we at least cover these two types of cases:


**Superclass chain:** [InitObject](initobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > [PostRestoreObject](postrestoreobject.md) > [PostUndoObject](postundoobject.md) > **tipManager**


## Properties


### `pendingTips`

Defined in tips.t, line 76

a vector of tips to be displayed before the next prompt


### `shownTips`

Defined in tips.t, line 87

A transient list of shown tips. Note that this must be a list and not a vector. When updating a list, we actually replace it with a new list, since lists are immutable. This is a transient change - it affects only the value of the shownTips property. Updating a vector, however, modifies the vector itself and leaves the property with the same reference. A vector itself is always persistent, so this change would be lost after E.G. a restore.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


*From [PostRestoreObject](postrestoreobject.md):* [`restoreCode`](postrestoreobject.md#restoreCode)


## Methods


### `execute` *(overridden)*

Defined in tips.t, line 45

update tip information after a restore, restart or undo


### `showTips`

Defined in tips.t, line 28

Show pending tips. This is called by a PromptDaemon before each new round of input.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
