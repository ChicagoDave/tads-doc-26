# SettingsFileComment

*class* — defined in [settings.t](../by-file/settings.t.md) (line 587)


SettingsFileComment - this object describes an unparsed line in the settings file. We treat lines that don't match our parsing rules as comments. We preserve the contents and order of these lines, but we don't otherwise try to interpret them.


**Superclass chain:** `object` > **SettingsFileComment**


## Properties


### `str_`

Defined in settings.t, line 602

the text from the file


## Methods


### `construct(str)`

Defined in settings.t, line 588


### `writeToFile(f)`

Defined in settings.t, line 599

write the comment line to a file
