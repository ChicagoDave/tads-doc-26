# mainAtExit

*object* — defined in [_main.t](../by-file/_main.t.md) (line 1220)


At-exit handlers. This is a registry for custom handlers that are to be invoked just before the program terminates.


**Superclass chain:** `object` > **mainAtExit**


## Properties


### `handlers`

Defined in _main.t, line 1250

list of exit handlers


## Methods


### `addHandler(func)`

Defined in _main.t, line 1225

Add an at-exit handler. User code can call this to register a handler that will be invoked just before the program exits.


### `callHandlers`

Defined in _main.t, line 1231

call our exit handlers
