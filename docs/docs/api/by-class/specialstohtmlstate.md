# SpecialsToHtmlState

*class* — defined in [_main.t](../by-file/_main.t.md) (line 1133)


Stream state object for String.specialsToHtml().


**Superclass chain:** `object` > **SpecialsToHtmlState**


## Properties


### `flags_`

Defined in _main.t, line 1170

Internal output state flags at end of last string parsed. This is a combination of bit flags:


### `tag_`

Defined in _main.t, line 1173

tag in progress at end of last string parsed


## Methods


### `resetLine`

Defined in _main.t, line 1149

Explicitly reset to the start of a line. This can be called after a non-output operation that resets the line position, such as reading an input line.


### `resetState`

Defined in _main.t, line 1138

Reset the state. This should be used when the output stream context is reset, such as when clearing the window.
