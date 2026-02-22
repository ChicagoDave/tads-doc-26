# giveMeToAskFor

*object* — defined in [actions.t](../by-file/actions.t.md) (line 2177)


Define a global remapping to transform commands of the form "X, GIVE ME Y" to the format "ME, ASK X FOR Y". This makes it easier to write the code to handle these sorts of exchanges, since it means you only have to write it in the ASK FOR handler.


**Superclass chain:** [GlobalRemapping](globalremapping.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **giveMeToAskFor**


## Inherited Properties


*From [GlobalRemapping](globalremapping.md):* [`allGlobalRemappings`](globalremapping.md#allGlobalRemappings), [`listNeedsSorting`](globalremapping.md#listNeedsSorting), [`remappingOrder`](globalremapping.md#remappingOrder)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `getRemapping(issuingActor, targetActor, action)` *(overridden)*

Defined in actions.t, line 2184

Remap a command, if applicable. We look for commands of the form "X, GIVE ME Y": we look for a GiveTo action whose indirect object is the same as the issuing actor. When we find this form of command, we rewrite it to "ME, ASK X FOR Y".


## Inherited Methods


*From [GlobalRemapping](globalremapping.md):* [`construct`](globalremapping.md#construct), [`execute`](globalremapping.md#execute), [`findGlobalRemapping`](globalremapping.md#findGlobalRemapping), [`registerGlobalRemapping`](globalremapping.md#registerGlobalRemapping), [`unregisterGlobalRemapping`](globalremapping.md#unregisterGlobalRemapping)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
