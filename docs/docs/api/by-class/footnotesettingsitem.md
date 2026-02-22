# footnoteSettingsItem

*object* — defined in [footnote.t](../by-file/footnote.t.md) (line 213)


our FOOTNOTES settings item


**Superclass chain:** [SettingsItem](settingsitem.md) > `object` > **footnoteSettingsItem**


## Properties


### `settingDesc` *(overridden)*

Defined in footnote.t, line 221

show our short description


### `settingID` *(overridden)*

Defined in footnote.t, line 218

our config file variable ID


### `showFootnotes`

Defined in footnote.t, line 215

our current status - the factory default is "medium"


## Inherited Properties


*From [SettingsItem](settingsitem.md):* [`factoryDefault`](settingsitem.md#factoryDefault), [`includeInListing`](settingsitem.md#includeInListing)


## Methods


### `execute`

Defined in footnote.t, line 265

pre-initialization - set up the footnote explanation daemon


### `settingFromText(str)` *(overridden)*

Defined in footnote.t, line 239


### `settingToText` *(overridden)*

Defined in footnote.t, line 224

get the setting's external file string representation


## Inherited Methods


*From [SettingsItem](settingsitem.md):* [`restoreItem`](settingsitem.md#restoreItem), [`saveItem`](settingsitem.md#saveItem)
