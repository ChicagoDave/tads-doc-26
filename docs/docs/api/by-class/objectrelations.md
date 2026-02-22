# objectRelations

*object* — defined in [action.t](../by-file/action.t.md) (line 21)


Object associations lists. We use this object to store some lookup tables that we build during preinitialization to relate object usages (DirectObject, IndirectObject) to certain properties.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **objectRelations**


## Properties


### `actionAllProps`

Defined in action.t, line 80

lookup table for catch-all action properties


### `actionDefaultProps`

Defined in action.t, line 77

lookup table for default action properties


### `checkAllProps`

Defined in action.t, line 74

lookup table for catch-all check properties


### `checkDefaultProps`

Defined in action.t, line 71

lookup table for default check properties


### `preCondAllProps`

Defined in action.t, line 62

lookup table for catch-all precondition properties


### `preCondDefaultProps`

Defined in action.t, line 59

lookup table for default precondition properties


### `verifyAllProps`

Defined in action.t, line 68

lookup table for catch-all verification properties


### `verifyDefaultProps`

Defined in action.t, line 65

lookup table for default verification properties


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in action.t, line 23

preinitialization - build the lookup tables


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
