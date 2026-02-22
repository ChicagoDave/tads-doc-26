# sessionHintStatus

*object* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 657)


We keep several pieces of information about the status of the hint system. Some of it pertains to the current session, independently of any saving/restoring/restarting, so we keep this information in a transient object. Some pertains to the present game, so we keep it in an ordinary persistent object, so that it's saved and restored along with the game.


**Superclass chain:** `object` > **sessionHintStatus**


## Properties


### `hintsDisabled`

Defined in hintsys.t, line 662

flag: we've disabled hints for this session


### `hintWarning`

Defined in hintsys.t, line 659

flag: we've warned about the hint system in this session
