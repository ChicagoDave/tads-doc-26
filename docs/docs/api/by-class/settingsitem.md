# SettingsItem

*class* — defined in [settings.t](../by-file/settings.t.md) (line 65)


A settings item. This encapsulates a single setting variable. When we're saving or restoring default settings, we'll simply loop over all objects of this class to get or set the current settings.


**Superclass chain:** `object` > **SettingsItemSubclasses:** [BinarySettingsItem](binarysettingsitem.md), [StringSettingsItem](stringsettingsitem.md)


**Global objects:** [exitsMode](exitsmode.md), [footnoteSettingsItem](footnotesettingsitem.md)


## Properties


### `factoryDefault`

Defined in settings.t, line 180

My "factory default" setting. At pre-init time, before we've loaded the settings file for the first time, we'll run through all SettingsItems and store their pre-defined source-code settings here, as though we were saving the values to a file. Later, when we load a file, if we find the file lacks an entry for this setting item, we'll simply re-load the factory default from this property.


### `includeInListing`

Defined in settings.t, line 109

Should this item be included in listings shown to the user? If this is true, the UI will include this setting in a display list of current settings shown to the user on request, by calling our settingDesc method.


### `settingDesc`

Defined in settings.t, line 101

Display a message fragment that shows the current setting value. We use this to show the player exactly what we're saving or restoring in response to a SAVE DEFAULTS or RESTORE DEFAULTS command, so that there's no confusion about which settings are included. In most cases, the best thing to show here is the command that selects the current setting: "NOTIFY ON," for example. This is for the UI's convenience; it's not used by the settings manager itself.


### `settingID`

Defined in settings.t, line 89

The setting's identifier string. This is the ID of the setting as it appears in the external configuration file.


## Methods


### `restoreItem(s)`

Defined in settings.t, line 140

Load from a settings file. By default, this simply calls the setting file object to load the data.


### `saveItem(s)`

Defined in settings.t, line 162

Save to a settings file. By default, this makes a string out of our value and updates or adds our corresponding entry in the file.


### `settingFromText(str)`

Defined in settings.t, line 128

Set the current value to the contents of the given string. The string contains a textual representation of a setting value, as previously generated with settingToText().


### `settingToText`

Defined in settings.t, line 119

Get the textual representation of the setting - returns a string representing the setting as it should appear in the external configuration file. We use this to write the setting to the file.
