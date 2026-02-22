# WebUIPrefs

*class* — defined in [webui.t](../by-file/webui.t.md) (line 2367)


Web UI preferences. This object contains the in-memory version of the display style preferences file.


**Superclass chain:** `object` > **WebUIPrefs**


## Properties


### `clientSession`

Defined in webui.t, line 2558

the client session for this preference list


### `curProfile`

Defined in webui.t, line 2567

current active profile selected by the user


### `curProPat`

Defined in webui.t, line 2434

current profile ID pattern - current-profile:xxx


### `profileTab`

Defined in webui.t, line 2564

profile table - this is a LookupTable of WebUIProfile objects keyed by profile name


### `proItemPat`

Defined in webui.t, line 2437

setting ID pattern for profile items - nnn.xxx=yyy


## Methods


### `construct(c)`

Defined in webui.t, line 2368


### `getSettingsFile`

Defined in webui.t, line 2504

get the settings file path


### `getXML`

Defined in webui.t, line 2523

get the current settings as XML, to send to the web UI


### `loadSettings`

Defined in webui.t, line 2378

read the settings file


### `openSettingsFile(access)`

Defined in webui.t, line 2483

open the settings file


### `readSettings(f)`

Defined in webui.t, line 2393

read settings from a file


### `saveSettings`

Defined in webui.t, line 2440

save the current settings to the user's config file
