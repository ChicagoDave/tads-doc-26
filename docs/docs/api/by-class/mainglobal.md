# mainGlobal

*object* — defined in [_main.t](../by-file/_main.t.md) (line 1182)


global data object for this module


**Superclass chain:** `object` > **mainGlobal**


## Properties


### `mainRestoreFunc`

Defined in _main.t, line 1212

pointer to mainRestore function, if defined


### `preinited_`

Defined in _main.t, line 1184

flag: we've run pre-initialization


### `reflectionObj`

Defined in _main.t, line 1196

The global reflection object - if the program is compiled with the standard reflection module, that module will set this property to point to the reflection object.


### `restartID`

Defined in _main.t, line 1209

Restart ID. This is an integer that indicates how the main entrypoint was last reached. This is initially zero; each time we restart the game, this is incremented.
