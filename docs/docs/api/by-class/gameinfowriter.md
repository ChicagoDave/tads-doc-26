# gameInfoWriter

*object* — defined in [gameinfo.t](../by-file/gameinfo.t.md) (line 71)


TADS GameInfo writer


**Superclass chain:** `object` > **gameInfoWriter**


## Methods


### `getGameInfoToday`

Defined in gameinfo.t, line 100

Get today's date as a string in the format YYYY-MM-DD. This can be used as a simple way of keeping the release date in the game information up to date with the latest compilation.


### `writeGameInfo(tab, fname)`

Defined in gameinfo.t, line 77

Write the game information from the given LookupTable to the given file. Each key/value pair in the LookupTable gives the GameInfo key and the corresponding value string for that key.
