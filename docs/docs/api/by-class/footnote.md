# Footnote

*class* — defined in [footnote.t](../by-file/footnote.t.md) (line 38)


Footnote - this allows footnote references to be generated in displayed text, and the user to retrieve the contents of the footnote on demand.


**Superclass chain:** `object` > **Footnote**


## Properties


### `desc`

Defined in footnote.t, line 44

Display the contents of the footnote - this will be called when the user asks to show the footnote with the "NOTE n" command. Each instance must provide suitable text here.


### `everShownFootnote`

Defined in footnote.t, line 184

static property: we've never shown a footnote reference before


### `footnoteNum`

Defined in footnote.t, line 159

my footnote number - this is assigned the first time I'm referenced; initially we have no number, since we don't want to assign a number until the note is first referenced


### `footnoteRead`

Defined in footnote.t, line 167

Flag: this footnote's full text has been displayed. This refers to the text of the footnote itself, not the reference, so this is only set when the "FOOTNOTE n" command is used to read this footnote.


### `footnoteSettings`

Defined in footnote.t, line 152

SettingsItem tracking our current status


### `lastFootnote`

Defined in footnote.t, line 174

Static property: the highest footnote number currently in use. We start this at zero, because zero is never a valid footnote number.


### `numberedFootnotes`

Defined in footnote.t, line 181

Static property: a vector of all footnotes which have had numbers assigned. We use this to find a footnote object given its note number.


## Methods


### `checkNotification`

Defined in footnote.t, line 187

static property: per-command-prompt daemon entrypoint


### `showFootnote(num)`

Defined in footnote.t, line 120

Display a footnote given its number. If there is no such footnote, we'll display an error message saying so. (This is a class method, so it should be called directly on Footnote, not on instances of Footnote.)
