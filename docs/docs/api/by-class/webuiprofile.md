# WebUIProfile

*class* — defined in [webui.t](../by-file/webui.t.md) (line 2333)


UI Settings list. This represents a named UI settings profile in the Web UI. A profile is a list of name/value pairs.


**Superclass chain:** `object` > **WebUIProfile**


## Properties


### `profileID`

Defined in webui.t, line 2353

internal ID of the profile


### `settings`

Defined in webui.t, line 2356

table of style value strings, keyed by style ID


## Methods


### `construct(id)`

Defined in webui.t, line 2334


### `forEach(func)`

Defined in webui.t, line 2347

call a callback for each style: func(id, val)


### `setItem(id, val)`

Defined in webui.t, line 2341

set a preference item in the profile
