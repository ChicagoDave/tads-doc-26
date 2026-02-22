# misc.t


## Classes

- [CyclicEventList](../by-class/cycliceventlist.md)
- [EventList](../by-class/eventlist.md)
- [ExternalEventList](../by-class/externaleventlist.md)
- [FinishOption](../by-class/finishoption.md)
- [FinishType](../by-class/finishtype.md)
- [GameMainDef](../by-class/gamemaindef.md)
- [RandomEventList](../by-class/randomeventlist.md)
- [RandomFiringScript](../by-class/randomfiringscript.md)
- [Script](../by-class/script.md)
- [ShuffledEventList](../by-class/shuffledeventlist.md)
- [ShuffledIntegerList](../by-class/shuffledintegerlist.md)
- [ShuffledList](../by-class/shuffledlist.md)
- [StopEventList](../by-class/stopeventlist.md)
- [SyncEventList](../by-class/synceventlist.md)


## Global Objects

- [adv3LibInit](../by-class/adv3libinit.md)
- [adv3LibPreinit](../by-class/adv3libpreinit.md)
- [finishOptionAmusing](../by-class/finishoptionamusing.md)
- [finishOptionCredits](../by-class/finishoptioncredits.md)
- [finishOptionFullScore](../by-class/finishoptionfullscore.md)
- [finishOptionQuit](../by-class/finishoptionquit.md)
- [finishOptionRestart](../by-class/finishoptionrestart.md)
- [finishOptionRestore](../by-class/finishoptionrestore.md)
- [finishOptionScore](../by-class/finishoptionscore.md)
- [finishOptionUndo](../by-class/finishoptionundo.md)
- [ftDeath](../by-class/ftdeath.md)
- [ftFailure](../by-class/ftfailure.md)
- [ftGameOver](../by-class/ftgameover.md)
- [ftVictory](../by-class/ftvictory.md)
- [libGlobal](../by-class/libglobal.md)
- [restoreOptionRestoreAnother](../by-class/restoreoptionrestoreanother.md)
- [restoreOptionStartOver](../by-class/restoreoptionstartover.md)
- [settingsUI](../by-class/settingsui.md)
- [verboseModeSettingsItem](../by-class/verbosemodesettingsitem.md)
- cls
- failedRestoreOptions
- finishGame
- finishGameMsg
- isListSubset
- main
- mainCommon
- mainRestore
- nilToList
- overrides
- partitionList
- processOptions
- runGame


## Functions


### `cls`

Defined in misc.t, line 550

Clear the main game window. In most cases, you should call this rather than calling the low-level clearScreen() function directly, since this routine takes care of a couple of chores that should usually be done at the same time.


### `failedRestoreOptions`

Defined in misc.t, line 1992

Show failed startup restore options. If a restore operation fails at startup, we won't just proceed with the game, but ask the user what they want to do; we'll offer the options of restoring another game, quitting, or starting the game from the beginning.


### `finishGame(extra)`

Defined in misc.t, line 1981

finish the game, offering the given extra options but no message


### `finishGameMsg(msg, extra)`

Defined in misc.t, line 1903

Finish the game, showing a message explaining why the game has ended. This can be called when an event occurs that ends the game, such as the player character's death, winning, or any other endpoint in the story.


### `isListSubset(a, b)`

Defined in misc.t, line 2469

Determine if list a is a subset of list b. a is a subset of b if every element of a is in b.


### `main(args)`

Defined in misc.t, line 599

Main program entrypoint. The core run-time start-up code calls this after running pre-initialization and load-time initialization. This entrypoint is called when we're starting the game normally; when the game is launched through a saved-position file, mainRestore() will be invoked instead.


### `mainCommon(prop, [args])`

Defined in misc.t, line 624

Common main entrypoint - this handles starting a new game or restoring an existing saved state.


### `mainRestore(args, restoreFile)`

Defined in misc.t, line 614

Main program entrypoint for restoring a saved-position file. This is invoked from the core run-time start-up code when the game is launched from the operating system via a saved-position file. For example, on Windows, double-clicking on a saved-position file on the Windows desktop launches the interpreter, which looks in the save file to find the game executable to run, then starts the game and invokes this entrypoint.


### `nilToList(val)`

Defined in misc.t, line 2438

nilToList - convert a 'nil' value to an empty list. This can be useful for mix-in classes that will be used in different inheritance contexts, since the classes might or might not inherit a base class definition for list-valued methods such as preconditions. This provides a usable default for list-valued methods that return nothing from superclasses.


### `overrides(obj, base, prop)`

Defined in misc.t, line 678

Determine if the given object overrides the definition of the given property inherited from the given base class. Returns true if the object derives from the given base class, and the object's definition of the property comes from a different place than the base class's definition of the property.


### `partitionList(lst, fn)`

Defined in misc.t, line 2457

partitionList - partition a list into a pair of two lists, the first containing items that match the predicate 'fn', the second containing items that don't match 'fn'. 'fn' is a function pointer (usually an anonymous function) that takes a single argument - a list element - and returns true or nil.


### `processOptions(lst)`

Defined in misc.t, line 2003

Process a list of finishing options. We'll loop, showing prompts and reading responses, until we get a response that terminates the loop.


### `runGame(look)`

Defined in misc.t, line 577

Run the game. We start by showing the description of the initial location, if desired, and then we read and interpret commands until the game ends (via a "quit" command, winning, death of the player character, or any other way of terminating the game).
