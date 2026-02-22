# _multiMethodRegistry

*object* — defined in [multmeth.t](../by-file/multmeth.t.md) (line 775)


Multi-method registry. This is where we keep the registry information that we build during initialization.


**Superclass chain:** `object` > **_multiMethodRegistry**


## Properties


### `baseFuncTab_`

Defined in multmeth.t, line 789

function -> base function


### `boundFuncTab_`

Defined in multmeth.t, line 786

base function -> initial binding property


### `funcNameTab_`

Defined in multmeth.t, line 783

function name table


### `funcParamTab_`

Defined in multmeth.t, line 780

table of function parameter lists, indexed by function


### `funcTab_`

Defined in multmeth.t, line 777

table of registered functions, indexed by base function


### `inhTab_`

Defined in multmeth.t, line 793

table of cached inherited() information, indexed by function
