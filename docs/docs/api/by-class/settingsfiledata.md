# SettingsFileData

*class* — defined in [settings.t](../by-file/settings.t.md) (line 465)


SettingsFileData - this is an object we use to represent the contents of the configuration file.


**Superclass chain:** `object` > **SettingsFileData**


## Properties


### `lst_`

Defined in settings.t, line 557

a list of SettingsFileItem objects giving the contents of the file


### `tab_`

Defined in settings.t, line 554

lookup table of values, keyed by variable name


## Methods


### `addComment(str)`

Defined in settings.t, line 532

add a comment line


### `addItem(id, val)`

Defined in settings.t, line 504

add a variable


### `construct`

Defined in settings.t, line 466


### `delItem(id)`

Defined in settings.t, line 539

delete an item


### `forEach(func)`

Defined in settings.t, line 492

iterate over all data (non-comment) items in the file


### `getItem(id)`

Defined in settings.t, line 485

find an item - returns a SettinsFileItem for the key, or nil if there's no existing item


### `setItem(id, val)`

Defined in settings.t, line 519

set a variable, adding a new variable if it doesn't already exist
