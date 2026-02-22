# settingsUI

*object* — defined in [misc.t](../by-file/misc.t.md) (line 2350)


The settings user interface. This is a subclass of the Settings Manager that adds a command-line user interface, particularly to allow the user to view, save, and load the default settings.


**Superclass chain:** [settingsManager](settingsmanager.md) > `object` > **settingsUI**


## Methods


### `restoreSettingsMsg`

Defined in misc.t, line 2401

Restore settings, and display an acknowledgment or error message, as appropriate.


### `saveSettingsMsg`

Defined in misc.t, line 2379

Save settings, and display an acknowledgment message (or an error message, if necessary) for the user's edification.


### `showAll`

Defined in misc.t, line 2352

display all of the current settings


## Inherited Methods


*From [settingsManager](settingsmanager.md):* [`restoreSettings`](settingsmanager.md#restoreSettings), [`retrieveSettings`](settingsmanager.md#retrieveSettings), [`saveSettings`](settingsmanager.md#saveSettings), [`storeSettings`](settingsmanager.md#storeSettings)
