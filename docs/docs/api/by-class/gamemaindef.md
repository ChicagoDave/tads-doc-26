# GameMainDef

*class* — defined in [misc.t](../by-file/misc.t.md) (line 55)


The library base class for the gameMain object.


**Superclass chain:** `object` > **GameMainDef**


## Properties


### `allowYouMeMixing`

Defined in misc.t, line 350

Option flag: allow the player to use "you" and "me" interchangeably in referring to the player character. We set this true by default, so that the player can refer to the player character in either the first or second person, regardless of how the game refers to the PC.


### `allVerbsAllowAll`

Defined in misc.t, line 385

Option flag: allow ALL to be used for every verb. This is true by default, which means that players will be allowed to use ALL with any command - OPEN ALL, EXAMINE ALL, etc.


### `ambigAnnounceMode`

Defined in misc.t, line 499

How should we handle object announcements when an object is automatically disambiguated? This controls how an action is described when the parser uses the logicalness rules to narrow down the object for a noun phrase when the noun phrase could refer to multiple in-scope objects. There are three options:


### `beforeRunsBeforeCheck`

Defined in misc.t, line 518

Should the "before" notifications (beforeAction, roomBeforeAction, and actorAction) run before or after the "check" phase?


### `cancelCmdLineOnFailure`

Defined in misc.t, line 421

When a command fails, should we continue processing any remaining commands on the same command line, or simply ignore them? The reason we might want to ignore additional commands is that they might not do what the player was expecting if an earlier command failed; this can sometimes create confusing situations, because the player expected one effect but got something quite different. On the other hand, *not* executing all the commands on the command line could be confusing in its own way, since the game's assessment of what constitutes "failure" might not be clear to the player; from the player's perspective, the game might appear to be inexplicably skipping commands.


### `filterPluralMatches`

Defined in misc.t, line 366

Option flag: filter plural phrase matches exclude the most obvious illogicalities, such as trying to TAKE an object that's already being held, or trying to OPEN an object that's already open.


### `initialPlayerChar`

Defined in misc.t, line 61

The initial player character. Each game's 'gameMain' object MUST define this to refer to the Actor object that serves as the initial player character.


### `parserTruncLength`

Defined in en_us.t, line 191

Option setting: the parser's truncation length for player input. As a convenience to the player, we can allow the player to truncate long words, entering only the first, say, 6 characters. For example, rather than typing "x flashlight", we could allow the player to simply type "x flashl" - truncating "flashlight" to six letters.


### `scoreRankTable`

Defined in misc.t, line 297

The score ranking list - this provides a list of names for various score levels. If the game provides a non-nil list here, the SCORE and FULL SCORE commands will show the rank along with the score ("This makes you a Master Adventurer").


### `useDistinguishersInAnnouncements`

Defined in misc.t, line 456

Should we use distinguishers when generating action object announcement messages? If this is set, announcement messages that list objects by name will add distinguishing details to indicate specifically which objects are being referred to. This applies to messages announcing default objects, vaguely matched objects, and multiple objects.


### `usePastTense`

Defined in en_us.t, line 206

Option: are we currently using a past tense narrative? By default, we aren't.


### `verboseMode`

Defined in misc.t, line 312

Verbose mode. If this is on, the full room description is displayed each time the player enters a room, regardless of whether or not the player has seen the room before; if this is nil, the full description is only displayed on the player's first entry to a room, and only the short description on re-entry. Note that the library provides VERBOSE and TERSE commands that let the player change this setting dynamically.


## Methods


### `getSaveDesc(userDesc)`

Defined in misc.t, line 219

Build a saved game metadata table. This returns a LookupTable containing string key/value pairs that are stored in saved game files, providing descriptive information that can be displayed to the user when browsing a collection of save files. This is called each time we execute a SAVE command, so that we store the current context of the game.


### `maxScore`

Defined in misc.t, line 264

The maximum number of points possible in the game. If the game includes the scoring module at all, and this is non-nil, the SCORE and FULL SCORE commands will display this value to the player as a rough indication of how much farther there is to go in the game.


### `newGame`

Defined in misc.t, line 97

Begin a new game. This default implementation shows the introductory message, calls the main command loop, and finally shows the goodbye message.


### `restoreAndRunGame(filename)`

Defined in misc.t, line 133

Restore a game and start it running. This is invoked when the user launches the interpreter using a saved game file; for example, on a Macintosh, this happens when the user double-clicks on a saved game file on the desktop.


### `setAboutBox`

Defined in misc.t, line 181

Set up the HTML-mode about-box. By default, this does nothing. Games can use this routine to show an <ABOUTBOX> tag, if desired, to set up the contents of an about-box for HTML TADS platforms.


### `setGameTitle`

Defined in misc.t, line 166

Set the interpreter window title, if applicable to the local platform. This simply displays a <TITLE> tag to set the title to the string found in the versionInfo object.


### `showGoodbye`

Defined in misc.t, line 83

Show the "goodbye" message. This is called after the main command loop terminates.


### `showIntro`

Defined in misc.t, line 73

Show the game's introduction. This routine is called by the default newGame() just before entering the main command loop. The command loop starts off by showing the initial room description, so there's no need to do that here.
