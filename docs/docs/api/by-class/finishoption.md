# FinishOption

*class* — defined in [misc.t](../by-file/misc.t.md) (line 2072)


Finish Option class. This is the base class for the abstract objects representing options offered by finishGame.


**Superclass chain:** `object` > **FinishOptionGlobal objects:** [finishOptionAmusing](finishoptionamusing.md), [finishOptionCredits](finishoptioncredits.md), [finishOptionFullScore](finishoptionfullscore.md), [finishOptionQuit](finishoptionquit.md), [finishOptionRestart](finishoptionrestart.md), [finishOptionRestore](finishoptionrestore.md), [finishOptionScore](finishoptionscore.md), [finishOptionUndo](finishoptionundo.md)


## Properties


### `desc`

Defined in misc.t, line 2080

The description, as displayed in the list of options. For the default English messages, this is expected to be a verb phrase in infinitive form, and should show the keyword accepted as a response in all capitals: "RESTART", "see some AMUSING things to do", "show CREDITS".


### `isListed`

Defined in misc.t, line 2091

By default, the item is listed. If you want to create an invisible option that's accepted but which isn't listed in the prompt, just set this to nil. Invisible options are sometimes useful when the output of one option mentions another option; for example, the CREDITS message might mention a LICENSE command for displaying the license, so you want to make that command available without cluttering the prompt with it.


### `responseChar`

Defined in misc.t, line 2101

a single character we accept as an alternative to our full response keyword, or nil if we don't accept a single-character response


### `responseKeyword`

Defined in misc.t, line 2094

our response keyword


### `showScoreInFinish`

Defined in misc.t, line 2144

Flag: show the score with the end-of-game announcement. If any option in the list of finishing options has this flag set, we'll show the score using the same message that the SCORE command uses.


## Methods


### `doOption`

Defined in misc.t, line 2132

Carry out the option. This is called when the player enters a response that matches this option. This routine must perform the action of the option, then return true to indicate that we should ask for another option, or nil to indicate that the finishGame() routine should simply return.


### `responseMatches(response)`

Defined in misc.t, line 2111

Match a response string to this option. Returns true if the string matches our response, nil otherwise. By default, we'll return true if the string exactly matches responseKeyword or exactly matches our responseChar (if that's non-nil), but this can be overridden to match other strings if desired. By default, we'll match the response without regard to case.
