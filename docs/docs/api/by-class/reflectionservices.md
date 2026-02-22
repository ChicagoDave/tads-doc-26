# reflectionServices

*object* — defined in [reflect.t](../by-file/reflect.t.md) (line 21)


Main reflection services object.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **reflectionServices**


## Properties


### `reverseSymtab_`

Defined in reflect.t, line 221

the global reverse-lookup symbol table


### `symtab_`

Defined in reflect.t, line 218

the global symbol table


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in reflect.t, line 23

execute preinitialization


### `formatStackFrame(fr, includeSourcePos)`

Defined in reflect.t, line 132

Format a stack frame object (of class T3StackInfo).


### `valToSymbol(val)`

Defined in reflect.t, line 56

Convert a value to a symbol, or to a string representation if it's not of a symbolic type.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
