# scriptStatus

*object* — defined in [actions.t](../by-file/actions.t.md) (line 1129)


A state object that keeps track of our logging (scripting) status. This is transient, because logging is controlled through the output layer in the interpreter, which does not participate in any of the persistence mechanisms.


**Superclass chain:** `object` > **scriptStatus**


## Properties


### `noteWithoutScriptWarning`

Defined in actions.t, line 1141

have we warned about using NOTE without logging in effect?


### `recordFile`

Defined in actions.t, line 1138

RECORD file name


### `scriptFile`

Defined in actions.t, line 1135

Script file name. This is nil when logging is not in effect, and is set to the name of the scripting file when a log file is active.
