# StringSettingsItem

*class* — defined in [settings.t](../by-file/settings.t.md) (line 210)


A string settings item. This is for variables that have scalar string values. Value strings can contain anything except newlines.


**Superclass chain:** [SettingsItem](settingsitem.md) > `object` > **StringSettingsItem**


## Properties


### `leadTrailSpPat`

Defined in settings.t, line 242

no leading quote; just trim spaces


### `needQuotePat`

Defined in settings.t, line 274

quotes aren't needed


### `trimSpPat`

Defined in settings.t, line 243


### `val`

Defined in settings.t, line 277

our current value string


## Inherited Properties


*From [SettingsItem](settingsitem.md):* [`factoryDefault`](settingsitem.md#factoryDefault), [`includeInListing`](settingsitem.md#includeInListing), [`settingDesc`](settingsitem.md#settingDesc), [`settingID`](settingsitem.md#settingID)


## Methods


### `quoteValue(str)`

Defined in settings.t, line 251

Class method: quote a string value for storing in the file. If the string has any leading or trailing spaces, starts with a double quote, or contains any newlines, we'll quote it; otherwise we'll return it as-is.


### `settingFromText(str)` *(overridden)*

Defined in settings.t, line 219

parse text


### `settingToText` *(overridden)*

Defined in settings.t, line 212

convert to text


## Inherited Methods


*From [SettingsItem](settingsitem.md):* [`restoreItem`](settingsitem.md#restoreItem), [`saveItem`](settingsitem.md#saveItem)
