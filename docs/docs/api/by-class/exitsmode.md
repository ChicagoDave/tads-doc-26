# exitsMode

*object* — defined in [exits.t](../by-file/exits.t.md) (line 405)


Settings item - show defaults in status line


**Superclass chain:** [SettingsItem](settingsitem.md) > `object` > **exitsMode**


## Properties


### `inRoomDesc`

Defined in exits.t, line 440


### `inStatusLine`

Defined in exits.t, line 439

Our value is in two parts. inStatusLine controls whether or not we show the exit list in the status line; inRoomDesc controls the exit listing in room descriptions.


### `settingDesc` *(overridden)*

Defined in exits.t, line 410

show our description


### `settingID` *(overridden)*

Defined in exits.t, line 407

our ID


## Inherited Properties


*From [SettingsItem](settingsitem.md):* [`factoryDefault`](settingsitem.md#factoryDefault), [`includeInListing`](settingsitem.md#includeInListing)


## Methods


### `settingFromText(str)` *(overridden)*

Defined in exits.t, line 422

just return the two binary variables


### `settingToText` *(overridden)*

Defined in exits.t, line 414

convert to text


## Inherited Methods


*From [SettingsItem](settingsitem.md):* [`restoreItem`](settingsitem.md#restoreItem), [`saveItem`](settingsitem.md#saveItem)
