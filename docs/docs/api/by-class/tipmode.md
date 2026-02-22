# tipMode

*object* — defined in [tips.t](../by-file/tips.t.md) (line 202)


Next, we want to allow turning all tips on and off during the game. It should also be possible to turn the tips off for ALL games that use them, and thus we define a SettingsItem for this purpose. This means that the player can turn the tips off and then save this setting as the default.


**Superclass chain:** [BinarySettingsItem](binarysettingsitem.md) > [SettingsItem](settingsitem.md) > `object` > **tipMode**


## Properties


### `isOn` *(overridden)*

Defined in tips.t, line 204

we show tips by default


### `settingDesc` *(overridden)*

Defined in tips.t, line 210

show our description


### `settingID` *(overridden)*

Defined in tips.t, line 207

the ID string to use in the configuration file


## Inherited Properties


*From [SettingsItem](settingsitem.md):* [`factoryDefault`](settingsitem.md#factoryDefault), [`includeInListing`](settingsitem.md#includeInListing)


## Inherited Methods


*From [BinarySettingsItem](binarysettingsitem.md):* [`settingFromText`](binarysettingsitem.md#settingFromText), [`settingToText`](binarysettingsitem.md#settingToText)


*From [SettingsItem](settingsitem.md):* [`restoreItem`](settingsitem.md#restoreItem), [`saveItem`](settingsitem.md#saveItem)
