# styleTagFilter

*object* — defined in [output.t](../by-file/output.t.md) (line 925)


"Style tag" filter. This is an output filter that expands our special style tags in output text.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **styleTagFilter**


## Properties


### `tagPattern`

Defined in output.t, line 927

pre-compile our frequently-used tag search pattern


### `tagTable`

Defined in output.t, line 1035

Our tag translation table. We'll initialize this during preinit to a lookup table with all of the defined StyleTag objects.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in output.t, line 1017

preinitialization


### `filterText(ostr, val)` *(overridden)*

Defined in output.t, line 931

filter for a style tag


### `translateTag(tag)`

Defined in output.t, line 994

Translate a tag


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
