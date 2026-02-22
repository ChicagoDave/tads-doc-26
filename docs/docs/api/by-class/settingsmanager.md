# settingsManager

*object* — defined in [settings.t](../by-file/settings.t.md) (line 289)


The settings manager. This object gathers up some global methods for managing the saved settings. This base class provides only a programmatic interface - it doesn't have a user interface.


**Superclass chain:** `object` > **settingsManager**


## Methods


### `restoreSettings`

Defined in settings.t, line 327

Restore all of the settings. If an error occurs, we'll throw an exception:


### `retrieveSettings`

Defined in settings.t, line 347

Retrieve the settings from the global settings file. This returns a SettingsFileData object that describes the file's contents. Note that if there simply isn't an existing settings file, we'll successfully return a SettingsFileData object with no data - the absence of a settings file isn't an error, but is merely equivalent to an empty settings file.


### `saveSettings`

Defined in settings.t, line 300

Save the current settings. This writes out the current settings to the global settings file.


### `storeSettings(s)`

Defined in settings.t, line 429

store the given SettingsFileData to the global settings file
