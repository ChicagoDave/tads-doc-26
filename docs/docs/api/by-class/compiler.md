# Compiler

*object* — defined in [dynfunc.t](../by-file/dynfunc.t.md) (line 40)


Compiler: This object provides a simplified interface to the dynamic compiler. The methods here can be used instead of manually creating DynamicFunc instances.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **Compiler**


## Properties


### `macros_`

Defined in dynfunc.t, line 149

a saved referenced to the preprocessor macro table


### `symtab_`

Defined in dynfunc.t, line 146

a saved reference to the global symbol table


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `compile(str, locals?)`

Defined in dynfunc.t, line 73

Compile an expression or function. 'str' is a string giving the code to compile. This can be a simple value expression, such as 'Me.location' or 'new BigNumber(12345).sqrt()'. Or, it can be a complete unnamed function definition, using this syntax:


### `defineFunc(name, str, locals?)`

Defined in dynfunc.t, line 85

Compile a dynamic function string, and add it to the global symbol table as a function with the given name. This effectively creates a new named function that you can call from other dynamic code objects.


### `eval(str, locals?)`

Defined in dynfunc.t, line 118

Evaluate an expression. 'str' is a string giving code to compile. In most cases, this is simply a simple value expression, although it's also acceptable to use the 'function()' syntax to create a function that takes no arguments.


### `execute` *(overridden)*

Defined in dynfunc.t, line 138

During preinit, save a reference to the program's global symbol table in a property of self. The VM always makes the global symbols available during preinit, but by default it discards the table after that because most programs don't need it. That means that the symbols aren't available by default during normal execution. However, saving a reference here prevents the garbage collector from discarding the table when preinit finishes, which forces it to be saved in the final .t3 file and thus makes it available permanently.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
