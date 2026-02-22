# BinarySettingsItem

*class* — defined in [settings.t](../by-file/settings.t.md) (line 187)


A binary settings item - this is for variables that have simple true/nil values.


**Superclass chain:** [SettingsItem](settingsitem.md) > `object` > **BinarySettingsItemGlobal objects:** [scoreNotifySettingsItem](scorenotifysettingsitem.md), [tipMode](tipmode.md), [verboseModeSettingsItem](verbosemodesettingsitem.md)


## Properties


### `isOn`

Defined in settings.t, line 203

our value is true (on) or nil (off)


## Inherited Properties


*From [SettingsItem](settingsitem.md):* [`factoryDefault`](settingsitem.md#factoryDefault), [`includeInListing`](settingsitem.md#includeInListing), [`settingDesc`](settingsitem.md#settingDesc), [`settingID`](settingsitem.md#settingID)


## Methods


### `settingFromText(str)` *(overridden)*

Defined in settings.t, line 192

parse text


### `settingToText` *(overridden)*

Defined in settings.t, line 189

convert to text - use ON or OFF as the representation


## Inherited Methods


*From [SettingsItem](settingsitem.md):* [`restoreItem`](settingsitem.md#restoreItem), [`saveItem`](settingsitem.md#saveItem)
