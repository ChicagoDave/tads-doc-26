# input.t


## Classes

- [BasicInputDef](../by-class/basicinputdef.md)
- [EndOfFileException](../by-class/endoffileexception.md)
- [InputDef](../by-class/inputdef.md)
- [QuittingException](../by-class/quittingexception.md)
- [StringPreParser](../by-class/stringpreparser.md)


## Global Objects

- [commentPreParser](../by-class/commentpreparser.md)
- [inputManager](../by-class/inputmanager.md)
- readMainCommand
- readMainCommandTokens


## Functions


### `readMainCommand(which)`

Defined in input.t, line 797

Read a command line from the player. Displays the main command prompt and returns a line of input.


### `readMainCommandTokens(which)`

Defined in input.t, line 1049

Read a line of text and return the token list and the original text. We keep going until a non-empty line of text is read.
