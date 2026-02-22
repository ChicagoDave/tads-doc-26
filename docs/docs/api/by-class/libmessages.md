# libMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 76)


Library Messages


**Superclass chain:** [MessageHelper](messagehelper.md) > `object` > **libMessages**


## Properties


### `commandFullScore`

Defined in msg_neu.t, line 114


### `commandInterruptionPrefix`

Defined in msg_neu.t, line 475

Command "interruption" group prefix. This is displayed after an interrupted command line - a command line editing session that was interrupted by a timeout event - just before the text that interrupted the command line.


### `commandLookAround`

Defined in msg_neu.t, line 113

some standard commands for insertion into <a> tags - these are in the messages so they can translated along with the command set


### `commandNotPresent`

Defined in msg_neu.t, line 1094

optional command is not supported in this game


### `commandResultsEmpty`

Defined in msg_neu.t, line 533

Empty command results - this is shown when we read a command line and then go back and read another without having displaying anything.


### `commandResultsPrefix`

Defined in msg_neu.t, line 464

Command group prefix - this is displayed after a command line and before the first command results shown after the command line.


### `commandResultsSeparator`

Defined in msg_neu.t, line 493

Command separator - this is displayed after the results from a command when another command is about to be executed without any more user input. That is, when a command line contains more than one command, this message is displayed between each successive command, to separate the results visually.


### `commandResultsSuffix`

Defined in msg_neu.t, line 523

Command results suffix - this is displayed just before a new command line is about to be read if any command results have been shown since the last command line.


### `complexResultsSeparator`

Defined in msg_neu.t, line 506

"Complex" result separator - this is displayed between a group of messages for a "complex" result set and adjoining messages. A command result list is "complex" when it's built up out of several generated items, such as object identification prefixes or implied command prefixes. We use additional visual separation to set off these groups of messages from adjoining messages, which is especially important for commands on multiple objects, where we would otherwise have several results shown together. By default, we use a paragraph break.


### `currentlyClosed`

Defined in msg_neu.t, line 1665


### `currentlyLocked`

Defined in msg_neu.t, line 1675

object is currently locked/unlocked


### `currentlyNoHints`

Defined in msg_neu.t, line 1077

there are currently no hints available (but there might be later)


### `currentlyOpen`

Defined in msg_neu.t, line 1664

object is currently open/closed


### `currentlyUnlocked`

Defined in msg_neu.t, line 1676


### `defaultsFileNotSupported`

Defined in msg_neu.t, line 1137

SAVE/RESTORE DEFAULTS not supported (old interpreter version)


### `defaultsFileWriteError`

Defined in msg_neu.t, line 1150

SAVE DEFAULTS file creation error


### `dlgButtonCancel`

Defined in msg_neu.t, line 1727


### `dlgButtonNo`

Defined in msg_neu.t, line 1729


### `dlgButtonOk`

Defined in msg_neu.t, line 1726

Standard dialog button labels, for the Web UI. These are built in to the conventional interpreters, but in the Web UI we have to generate these ourselves.


### `dlgButtonYes`

Defined in msg_neu.t, line 1728


### `dlgTitleError`

Defined in msg_neu.t, line 1719


### `dlgTitleInfo`

Defined in msg_neu.t, line 1717


### `dlgTitleNone`

Defined in msg_neu.t, line 1715

Standard dialog titles, for the Web UI. These are shown in the title bar area of the Web UI dialog used for inputDialog() calls. These correspond to the InDlgIconXxx icons. The conventional interpreters use built-in titles when titles are needed at all, but in the Web UI we have to generate these ourselves.


### `dlgTitleQuestion`

Defined in msg_neu.t, line 1718


### `dlgTitleWarning`

Defined in msg_neu.t, line 1716


### `emptyCommandResponse`

Defined in msg_neu.t, line 445

show the response to an empty command line


### `finishDeathMsg`

Defined in msg_neu.t, line 768

standard game-ending messages for the common outcomes


### `finishFailureMsg`

Defined in msg_neu.t, line 770


### `finishGameOverMsg`

Defined in msg_neu.t, line 771


### `finishVictoryMsg`

Defined in msg_neu.t, line 769


### `getRecordingPrompt`

Defined in msg_neu.t, line 959

get the RECORD prompt


### `getReplayPrompt`

Defined in msg_neu.t, line 988

REPLAY prompt


### `getRestorePrompt`

Defined in msg_neu.t, line 781

get the restore-game prompt


### `getSavePrompt`

Defined in msg_neu.t, line 778

Get the save-game file prompt. Note that this must return a single-quoted string value, not display a value itself, because this prompt is passed to inputFile().


### `getScriptingPrompt`

Defined in msg_neu.t, line 920

get the scripting inputFile prompt message


### `hintsDisabled`

Defined in msg_neu.t, line 1064

acknowledge HINTS OFF


### `hintsDone`

Defined in msg_neu.t, line 1091

done with hints


### `hintsNotPresent`

Defined in msg_neu.t, line 1073

this game has no hints


### `inputFileScriptWarningButtons`

Defined in msg_neu.t, line 1748

build the message


### `inputScriptFailed`

Defined in msg_neu.t, line 910

error opening input script


### `internalResultsSeparator`

Defined in msg_neu.t, line 514

Internal results separator - this is displayed to visually separate the results of an implied command from the results for the initiating command, which are shown after the results from the implied command. By default, we show a paragraph break.


### `intraCommandSeparator`

Defined in msg_neu.t, line 541

Intra-command report separator. This is used to separate report messages within a single command's results. By default, we show a paragraph break.


### `listSepEnd`

Defined in msg_neu.t, line 265

the list separator for the end of a list of at least three elements


### `listSepMiddle`

Defined in msg_neu.t, line 259

the list separator character in the middle of a list


### `listSepTwo`

Defined in msg_neu.t, line 262

the list separator character for a two-element list


### `longListSepEnd`

Defined in msg_neu.t, line 277

the list separator for the end of a long list


### `longListSepMiddle`

Defined in msg_neu.t, line 271

the list separator for the middle of a long list (a list with embedded lists not otherwise set off, such as by parentheses)


### `longListSepTwo`

Defined in msg_neu.t, line 274

the list separator for a two-element list of sublists


### `menuKeyList`

Defined in msg_neu.t, line 1166

Command key list for the menu system. This uses the format defined for MenuItem.keyList in the menu system. Keys must be given as lower-case in order to match input, since the menu system converts input keys to lower case before matching keys to this list.


### `menuLongTopicEnd`

Defined in msg_neu.t, line 1220

Message to display at the end of a "long topic" in the menu system. We'll display this at the end of the long topic's contents.


### `menuTopicListEnd`

Defined in msg_neu.t, line 1213

Message to display at the end of a topic list. We'll display this after we've displayed all available items from a MenuTopicItem's list of items, to let the user know that there are no more items available.


### `nextMenuTopicLink`

Defined in msg_neu.t, line 1178

link title for 'next topic' navigation link in topic lists


### `noAboutInfo`

Defined in msg_neu.t, line 163

there's no "about" information in this game


### `noteWithoutScript`

Defined in msg_neu.t, line 1015


### `noteWithoutScriptWarning`

Defined in msg_neu.t, line 1018

on the first comment without transcript recording, warn about it


### `noteWithScript`

Defined in msg_neu.t, line 1014

comment accepted, with or without transcript recording in effect


### `notOnboardShip`

Defined in msg_neu.t, line 1564

a shipboard direction was attempted while not onboard a ship


### `noTopicsNotTalking`

Defined in msg_neu.t, line 575

no topics to suggest when we're not talking to anyone


### `offerOopsNote`

Defined in msg_neu.t, line 107

Flag: offer an explanation of the "OOPS" command when it first comes up. We'll only show this the first time the player enters an unknown word. If you never want to offer this message at all, simply set this flag to nil initially.


### `oopsMissingWord`

Defined in msg_neu.t, line 594

OOPS in context, but without the word to correct


### `oopsOutOfContext`

Defined in msg_neu.t, line 589

can't use OOPS right now


### `prevMenuLink`

Defined in msg_neu.t, line 1175

link title for 'previous menu' navigation link


### `recordingCanceled`

Defined in msg_neu.t, line 978

acknowledge cancellation


### `recordingFailed`

Defined in msg_neu.t, line 968

recording failed


### `recordingOkay`

Defined in msg_neu.t, line 962

acknowledge recording on


### `recordOffIgnored`

Defined in msg_neu.t, line 984

RECORD OFF ignored because we're not recording commands


### `recordOffOkay`

Defined in msg_neu.t, line 981

recording turned off


### `replayCanceled`

Defined in msg_neu.t, line 991

REPLAY file selection canceled


### `roomDarkDesc`

Defined in msg_neu.t, line 1325

generic long description of a dark room


### `roomDarkName`

Defined in msg_neu.t, line 1322

generic short description of a dark room


### `scoreNotPresent`

Defined in msg_neu.t, line 1098

this game doesn't use scoring


### `scriptingCanceled`

Defined in msg_neu.t, line 949

acknowledge cancellation of script file dialog


### `scriptingFailed`

Defined in msg_neu.t, line 939

scripting failed


### `scriptOffIgnored`

Defined in msg_neu.t, line 955

SCRIPT OFF ignored because we're not in a script file


### `scriptOffOkay`

Defined in msg_neu.t, line 952

acknowledge scripting off


### `settingsItemSeparator`

Defined in msg_neu.t, line 1134

show a separator for the settingsUI.showAll() list


### `showFullScorePrefix`

Defined in msg_neu.t, line 302

show the list prefix for the full score listing; this is shown on a line by itself before the list of full score items, shown indented and one item per line


### `showHintWarning`

Defined in msg_neu.t, line 1081

show the hint system warning


### `sorryHintsDisabled`

Defined in msg_neu.t, line 1067

rebuff a request for hints when they've been previously disabled


### `webUploadTooBig`

Defined in msg_neu.t, line 879

Web UI inputFile error: uploaded file is too large


### `whomPronoun`

Defined in msg_neu.t, line 97

The pronoun to use for the objective form of the personal interrogative pronoun. Strictly speaking, the right word for this usage is "whom"; but regardless of what the grammar books say, most American English speakers these days use "who" for both the subjective and objective cases; to many ears, "whom" sounds old-fashioned, overly formal, or even pretentious. (Case in point: a recent television ad tried to make a little kid look ultra-sophisticated by having him answer the phone by asking "*whom* may I ask is calling?", with elaborate emphasis on the "whom." Of course, the correct usage in this case is "who," so the ad only made the kid look pretentious. It goes to show that, at least in the mind of the writer of the ad, "whom" is just the snooty, formal version of "who" that serves only to signal the speaker's sophistication.)


## Methods


### `acknowledgeFootnoteStatus(stat)`

Defined in msg_neu.t, line 412

acknowledge a change in the footnote status


### `acknowledgeNotifyStatus(stat)`

Defined in msg_neu.t, line 620

acknowledge a change in the score notification status


### `acknowledgeTipStatus(stat)`

Defined in msg_neu.t, line 341

acknowledge turning tips on or off


### `acknowledgeVerboseMode(verbose)`

Defined in msg_neu.t, line 598

acknowledge setting VERBOSE mode (true) or TERSE mode (nil)


### `actorHereGroupPrefix(posture, lst)`

Defined in msg_neu.t, line 1449

Prefix/suffix messages for listing actors in a room description, for cases when the actors' nominal container cannot be seen or is not to be stated: "Bob and Bill are standing here."


### `actorHereGroupSuffix(posture, lst)`

Defined in msg_neu.t, line 1450


### `actorInGroupPrefix(posture, cont, lst)`

Defined in msg_neu.t, line 1416

Prefix/suffix messages for listing actors in a room description, for cases when the actors are in the local room in a nominal container that we want to mention: "Bob and Bill are sitting on the couch."


### `actorInGroupSuffix(posture, cont, lst)`

Defined in msg_neu.t, line 1417


### `actorInRemoteGroupPrefix(pov, posture, cont, remote, lst)`

Defined in msg_neu.t, line 1429

Prefix/suffix messages for listing actors in a room description, for cases when the actors are inside a nested room that's inside a remote location: "Bob and Bill are in the courtyard, sitting on the bench."


### `actorInRemoteGroupSuffix(pov, posture, cont, remote, lst)`

Defined in msg_neu.t, line 1430


### `actorInRemoteNestedRoom(actor, inner, outer, pov)`

Defined in msg_neu.t, line 1399

mention that the given actor is visible, at a distance or remotely, in the given nested room within the given outer location; this is used in room descriptions


### `actorInRemoteRoom(actor, room, pov)`

Defined in msg_neu.t, line 1387

mention that the given actor is visible, at a distance or remotely, in the given location; this is used in room descriptions when an NPC is visible in a remote or distant location


### `actorInRoom(actor, cont)`

Defined in msg_neu.t, line 1352

Mention that an actor is in a given local room, as part of a room description. This is used as a default "special description" for an actor.


### `actorInRoomPosture(actor, room)`

Defined in msg_neu.t, line 1364

Describe an actor as standing/sitting/lying on something, as part of the actor's EXAMINE description. This is additional information added to the actor's description, so we refer to the actor with a pronoun ("He's standing here").


### `actorInRoomStatus(actor, room)`

Defined in msg_neu.t, line 1318

show a status line addendum: standing in/on something


### `actorThereGroupPrefix(pov, posture, remote, lst)`

Defined in msg_neu.t, line 1462

Prefix/suffix messages for listing actors in a room description, for cases when the actors' immediate container cannot be seen or is not to be stated, and the actors are in a remote location: "Bob and Bill are in the courtyard."


### `actorThereGroupSuffix(pov, posture, remote, lst)`

Defined in msg_neu.t, line 1463


### `againCannotChangeActor`

Defined in msg_neu.t, line 695

'again' cannot be directed to a different actor


### `againCannotTalkToTarget(issuer, target)`

Defined in msg_neu.t, line 702

'again': can no longer talk to target actor


### `againNotPossible(issuer)`

Defined in msg_neu.t, line 708

the last command cannot be repeated in the present context


### `allInSameListState(lst, stateName)`

Defined in msg_neu.t, line 174

a set of equivalents are all in a given state


### `alreadyTalkingTo(actor, greeter)`

Defined in msg_neu.t, line 568

greeting actor while actor is already talking to us


### `announceAmbigActionObject(obj, whichObj, action)`

Defined in msg_neu.t, line 655

Announce a singleton object that we selected from a set of ambiguous objects. This is used when we disambiguate a command and choose an object over other objects that are also logical but are less likely. In such cases, it's courteous to tell the player what we chose, because it's possible that the user meant one of the other logical objects - announcing this type of choice helps reduce confusion by making it immediately plain to the player when we make a choice other than what they were thinking.


### `announceDefaultObject(obj, whichObj, action, resolvedAllObjects)`

Defined in msg_neu.t, line 677

Announce a singleton object we selected as a default for a missing noun phrase.


### `announceImplicitAction(action, ctx)`

Defined in msg_neu.t, line 129

Get a string to announce an implicit action. This announces the current global action. 'ctx' is an ImplicitAnnouncementContext object describing the context in which the message is being displayed.


### `announceMoveToBag(action, ctx)`

Defined in msg_neu.t, line 149

Get a string to announce that we're implicitly moving an object to a bag of holding to make room for taking something new. If 'trying' is true, it means we want to phrase the message as merely trying the action, not actually performing it.


### `announceMultiActionObject(obj, whichObj, action)`

Defined in msg_neu.t, line 632

Announce the current object of a set of multiple objects on which we're performing an action. This is used to tell the player which object we're acting upon when we're iterating through a set of objects specified in a command targeting multiple objects.


### `announceRemappedAction(action)`

Defined in msg_neu.t, line 117

announce a completely remapped action


### `basicScoreChange(delta)`

Defined in msg_neu.t, line 332

basic score change notification message - this is an internal service routine for scoreChange and firstScoreChange


### `candleBurnedOut(obj)`

Defined in msg_neu.t, line 1694

daemon report for burning out a candle


### `cannotReachContents(obj, loc)`

Defined in msg_neu.t, line 1259

cannot reach an object, because the object is inside the given container


### `cannotReachObject(obj)`

Defined in msg_neu.t, line 1250

cannot reach (i.e., touch) an object that is to be manipulated in a command - this is a generic message used when we cannot identify the specific reason that the object is in scope but cannot be touched


### `cannotReachOutside(obj, loc)`

Defined in msg_neu.t, line 1267

cannot reach an object because it's outisde the given container


### `cannotTalkTo(targetActor, issuingActor)`

Defined in msg_neu.t, line 561

a command was issued to a non-actor


### `closedMsg(obj)`

Defined in msg_neu.t, line 1661


### `confirmQuit`

Defined in msg_neu.t, line 721

confirm that we really want to quit


### `confirmRestart`

Defined in msg_neu.t, line 751

confirm that they really want to restart


### `currentExitsSettings(statusLine, roomDesc)`

Defined in msg_neu.t, line 1050

describe the current EXITS settings


### `defaultsFileReadError(exc)`

Defined in msg_neu.t, line 1143

RESTORE DEFAULTS file open/read error


### `dimReadDesc(obj)`

Defined in msg_neu.t, line 234

dim light "read" description


### `distantThingDesc(obj)`

Defined in msg_neu.t, line 178

generic long description of a Thing from a distance


### `distantThingSmellDesc(obj)`

Defined in msg_neu.t, line 203

generic "smell" description of a Thing at a distance


### `distantThingSoundDesc(obj)`

Defined in msg_neu.t, line 192

generic "listen" description of a Thing at a distance


### `exitsOnOffOkay(stat, look)`

Defined in msg_neu.t, line 1029

acknowledge new "exits on/off" status


### `explainExitsOnOff`

Defined in msg_neu.t, line 1044

explain how to turn exit display on and off


### `filePromptFailed`

Defined in msg_neu.t, line 865

error showing the input file dialog (or character-mode equivalent)


### `filePromptFailedMsg(msg)`

Defined in msg_neu.t, line 873

error showing the input file dialog, with a system error message


### `firstFootnote`

Defined in msg_neu.t, line 360

first footnote notification


### `firstScoreChange(delta)`

Defined in msg_neu.t, line 315

score change - first notification


### `footnoteRef(num)`

Defined in msg_neu.t, line 353

get the string to display for a footnote reference


### `fullScoreItemPoints(points)`

Defined in msg_neu.t, line 309

show the item prefix, with the number of points, for a full score item - immediately after this is displayed, we'll display the description message for the achievement


### `inputFileScriptWarning(warning, filename)`

Defined in msg_neu.t, line 1740

Warning prompt for inputFile() warnings generated when reading a script file, for the Web UI. The interpreter normally displays these warnings directly, but in Web UI mode, the program is responsible, so we need localized messages.


### `inputScriptFailedException(exc)`

Defined in msg_neu.t, line 914

exception opening input script


### `inputScriptOkay(fname)`

Defined in msg_neu.t, line 903

acknowledge starting an input script


### `invalidCommandToken(ch)`

Defined in msg_neu.t, line 448

invalid token (i.e., punctuation) in command line


### `invalidFinishOption(resp)`

Defined in msg_neu.t, line 1023

invalid finishGame response


### `litCandleDesc(obj)`

Defined in msg_neu.t, line 245

lit candle description


### `litMatchDesc(obj)`

Defined in msg_neu.t, line 241

lit/unlit match description


### `lockedMsg(obj)`

Defined in msg_neu.t, line 1671

locked/unlocked status - adjectives describing lock states


### `mainCommandPrompt(which)`

Defined in msg_neu.t, line 436

Show the main command prompt.


### `makeSentence(msg)`

Defined in msg_neu.t, line 809

make an error message into a sentence, by capitalizing the first letter and adding a period at the end if it doesn't already have one


### `matchBurnedOut(obj)`

Defined in msg_neu.t, line 1686

daemon report for burning out a match


### `mentionFullScore`

Defined in msg_neu.t, line 1102

mention the FULL SCORE command


### `menuInstructions(keylist, prevLink)`

Defined in msg_neu.t, line 1227

instructions text for banner-mode menus - this is displayed in the instructions bar at the top of the screen, above the menu banner area


### `menuNextChapter(keylist, title, hrefNext, hrefUp)`

Defined in msg_neu.t, line 1238

show a 'next chapter' link


### `menuTopicProgress(cur, tot)`

Defined in msg_neu.t, line 1205

Position indicator for topic list items - this is displayed after a topic list item to show the current item number and the total number of items in the list, to give the user an idea of where they are in the overall list.


### `noCommandForAgain`

Defined in msg_neu.t, line 689

'again' used with no prior command


### `noSuchFootnote(num)`

Defined in msg_neu.t, line 366

there is no such footnote as the given number


### `noteMainRestore`

Defined in msg_neu.t, line 817

note that we're restoring at startup via a saved-position launch


### `notRestarting`

Defined in msg_neu.t, line 758

"not restarting" confirmation


### `notTerminating`

Defined in msg_neu.t, line 745

"not terminating" confirmation - this is displayed when the player doesn't acknowledge a 'quit' command with an affirmative response to our confirmation question


### `objBurnedOut(obj)`

Defined in msg_neu.t, line 1702

daemon report for burning out a generic fueled light source


### `obscuredReadDesc(obj)`

Defined in msg_neu.t, line 226

obscured "read" description


### `obscuredThingDesc(obj, obs)`

Defined in msg_neu.t, line 185

generic long description of a Thing under obscured conditions


### `obscuredThingSmellDesc(obj, obs)`

Defined in msg_neu.t, line 207

generic obscured "smell" description


### `obscuredThingSoundDesc(obj, obs)`

Defined in msg_neu.t, line 196

generic obscured "listen" description


### `offMsg(obj)`

Defined in msg_neu.t, line 1683


### `okayQuitting`

Defined in msg_neu.t, line 738

QUIT message. We display this to acknowledge an explicit player command to quit the game. This is the last message the game displays on the way out; there is no need to offer any options at this point, because the player has decided to exit the game.


### `onMsg(obj)`

Defined in msg_neu.t, line 1682

on/off status - these are simply adjectives that can be used to describe the status of a switchable object


### `oopsNote`

Defined in msg_neu.t, line 583

Show a note about the OOPS command. This is, by default, added to the "I don't know that word" error the first time that error occurs.


### `openMsg(obj)`

Defined in msg_neu.t, line 1660

open/closed status - these are simply adjectives that can be used to describe the status of an openable object


### `openStatusMsg(obj)`

Defined in msg_neu.t, line 1668

stand-alone independent clause describing current open status


### `parserErrorString(actor, msg)`

Defined in msg_neu.t, line 442

Show a pre-resolved error message string. This simply displays the given string.


### `pauseEnded`

Defined in msg_neu.t, line 897

PAUSE ended


### `pausePrompt`

Defined in msg_neu.t, line 882

PAUSE prompt


### `pauseSaving`

Defined in msg_neu.t, line 891

saving from within a pause


### `pcDesc(actor)`

Defined in msg_neu.t, line 1299

default description of the player character


### `putDestBehind(obj)`

Defined in msg_neu.t, line 254


### `putDestContainer(obj)`

Defined in msg_neu.t, line 251

Prepositional phrases for putting objects into different types of objects.


### `putDestFloor(obj)`

Defined in msg_neu.t, line 255


### `putDestRoom(obj)`

Defined in msg_neu.t, line 256


### `putDestSurface(obj)`

Defined in msg_neu.t, line 252


### `putDestUnder(obj)`

Defined in msg_neu.t, line 253


### `recordingFailedException(exc)`

Defined in msg_neu.t, line 972

recording failed with exception


### `restoreCanceled`

Defined in msg_neu.t, line 823

restore canceled


### `restoreCorruptedFile`

Defined in msg_neu.t, line 840

restore failed because the file was corrupted


### `restoredDefaults`

Defined in msg_neu.t, line 1122

RESTORE DEFAULTS successful


### `restoreFailed(exc)`

Defined in msg_neu.t, line 858

restore failed for some reason other than those distinguished above


### `restoreFailedOnServer(exc)`

Defined in msg_neu.t, line 826

restore failed due to storage server request error


### `restoreInvalidFile`

Defined in msg_neu.t, line 833

restore failed because the file was not a valid saved game file


### `restoreInvalidMatch`

Defined in msg_neu.t, line 850

restore failed because the file was for the wrong game or version


### `restoreOkay`

Defined in msg_neu.t, line 820

successfully restored


### `roomActorHereDesc(actor)`

Defined in msg_neu.t, line 1331

mention that an actor is here, without mentioning the enclosing room, as part of a room description


### `roomActorPostureDesc(actor)`

Defined in msg_neu.t, line 1375

Describe an actor's posture, as part of an actor's "examine" description. If the actor is standing, don't bother mentioning anything, as standing is the trivial default condition.


### `roomActorStatus(actor)`

Defined in msg_neu.t, line 1310

Show a status line addendum for the actor posture, without mentioning the actor's location. We won't mention standing, since this is the default posture.


### `roomActorThereDesc(actor)`

Defined in msg_neu.t, line 1342

mention that an actor is visible at a distance or remotely, without mentioning the enclosing room, as part of a room description


### `saveCanceled`

Defined in msg_neu.t, line 787

save canceled


### `savedDefaults`

Defined in msg_neu.t, line 1108

SAVE DEFAULTS successful


### `saveFailed(exc)`

Defined in msg_neu.t, line 790

saved failed due to a file write or similar error


### `saveFailedOnServer(exc)`

Defined in msg_neu.t, line 798

save failed due to storage server request error


### `saveOkay`

Defined in msg_neu.t, line 784

successfully saved


### `sayArriving(traveler)`

Defined in msg_neu.t, line 1470

a traveler is arriving, but not from a compass direction


### `sayArrivingDir(traveler, dirName)`

Defined in msg_neu.t, line 1514

a traveler is arriving from a compass direction


### `sayArrivingDownStairs(traveler, stairs)`

Defined in msg_neu.t, line 1618

a traveler is arriving by coming down a stairway


### `sayArrivingLocally(traveler, dest)`

Defined in msg_neu.t, line 1487

a traveler is arriving locally (staying within view throughout the travel, and coming closer to the PC)


### `sayArrivingShipDir(traveler, dirName)`

Defined in msg_neu.t, line 1530

a traveler is arriving from a shipboard direction


### `sayArrivingThroughPassage(traveler, passage)`

Defined in msg_neu.t, line 1574

a traveler is arriving via a passage


### `sayArrivingUpStairs(traveler, stairs)`

Defined in msg_neu.t, line 1609

a traveler is arriving by coming up a stairway


### `sayArrivingViaPath(traveler, passage)`

Defined in msg_neu.t, line 1588

a traveler is arriving via a path


### `sayDeparting(traveler)`

Defined in msg_neu.t, line 1477

a traveler is departing, but not in a compass direction


### `sayDepartingAft(traveler)`

Defined in msg_neu.t, line 1546

a traveler is going aft


### `sayDepartingDir(traveler, dirName)`

Defined in msg_neu.t, line 1521

a traveler is leaving in a given compass direction


### `sayDepartingDownStairs(traveler, stairs)`

Defined in msg_neu.t, line 1602

a traveler is leaving down a stairway


### `sayDepartingFore(traveler)`

Defined in msg_neu.t, line 1555

a traveler is going fore


### `sayDepartingLocally(traveler, dest)`

Defined in msg_neu.t, line 1497

a traveler is departing locally (staying within view throughout the travel, and moving further away from the PC)


### `sayDepartingShipDir(traveler, dirName)`

Defined in msg_neu.t, line 1537

a traveler is leaving in a given shipboard direction


### `sayDepartingThroughPassage(traveler, passage)`

Defined in msg_neu.t, line 1567

a traveler is leaving via a passage


### `sayDepartingUpStairs(traveler, stairs)`

Defined in msg_neu.t, line 1595

a traveler is leaving up a stairway


### `sayDepartingViaPath(traveler, passage)`

Defined in msg_neu.t, line 1581

a traveler is leaving via a path


### `sayDepartingWith(traveler, lead)`

Defined in msg_neu.t, line 1627

acompanying another actor on travel


### `sayDepartingWithGuide(guide, lead)`

Defined in msg_neu.t, line 1642

Accompanying a tour guide. Note the seemingly reversed roles: the lead actor is the one initiating the travel, and the tour guide is the accompanying actor. So, the lead actor is effectively following the accompanying actor. It seems backwards, but really it's not: the tour guide merely shows the lead actor where to go, but it's up to the lead actor to actually initiate the travel.


### `sayOpenDoorRemotely(door, stat)`

Defined in msg_neu.t, line 1649

note that a door is being opened/closed remotely


### `sayTravelingRemotely(traveler, dest)`

Defined in msg_neu.t, line 1507

a traveler is traveling remotely (staying within view through the travel, and moving from one remote top-level location to another)


### `scoreChange(delta)`

Defined in msg_neu.t, line 322

score change - notification other than the first time


### `scriptingFailedException(exc)`

Defined in msg_neu.t, line 943

scripting failed with an exception


### `scriptingOkay`

Defined in msg_neu.t, line 923

acknowledge scripting on


### `scriptingOkayWebTemp`

Defined in msg_neu.t, line 930


### `shortFootnoteStatus(stat)`

Defined in msg_neu.t, line 419

show the footnote status, in short form


### `shortNotifyStatus(stat)`

Defined in msg_neu.t, line 617

show the current score notify status, in short form


### `shortVerboseStatus(stat)`

Defined in msg_neu.t, line 607

show the current VERBOSE setting, in short form


### `showCredit(name, byline)`

Defined in msg_neu.t, line 157

show a library credit (for a CREDITS listing)


### `showFinishMsg(msg)`

Defined in msg_neu.t, line 765

Show a game-finishing message - we use the conventional "*** You have won! ***" format that text games have been using since the dawn of time.


### `showFootnoteStatus(stat)`

Defined in msg_neu.t, line 373

show the current footnote status


### `showListState(state)`

Defined in msg_neu.t, line 171

Show a list state name - this is extra state information that we show for an object in a listing involving the object. For example, a light source might add a state like "(providing light)". We simply show the list state name in parentheses.


### `showNotifyStatus(stat)`

Defined in msg_neu.t, line 610

show the current score notify status


### `showScoreMessage(points, maxPoints, turns)`

Defined in msg_neu.t, line 280

show the basic score message


### `showScoreNoMaxMessage(points, turns)`

Defined in msg_neu.t, line 288

show the basic score message with no maximum


### `showScoreRankMessage(msg)`

Defined in msg_neu.t, line 295

show the full message for a given score rank string


### `showVersion(name, version)`

Defined in msg_neu.t, line 160

show a library version number (for a VERSION listing)


### `silentImplicitAction(action, ctx)`

Defined in msg_neu.t, line 141

Announce a silent implied action. This allows an implied action to work exactly as normal (including the suppression of a default response message), but without any announcement of the implied action.


### `smellDescSeparator`

Defined in msg_neu.t, line 547

separator for "smell" results - we ordinarily show each item's odor description as a separate paragraph


### `smellIsFromWithin(obj, loc)`

Defined in msg_neu.t, line 1287

odor is coming from inside/outside a container


### `smellIsFromWithout(obj, loc)`

Defined in msg_neu.t, line 1292


### `soundDescSeparator`

Defined in msg_neu.t, line 555

separator for "listen" results


### `soundIsFromWithin(obj, loc)`

Defined in msg_neu.t, line 1275

sound is coming from inside/outside a container


### `soundIsFromWithout(obj, loc)`

Defined in msg_neu.t, line 1280


### `systemActionToNPC`

Defined in msg_neu.t, line 714

system actions cannot be directed to non-player characters


### `textMenuMainPrompt(keylist)`

Defined in msg_neu.t, line 1184

main prompt text for text-mode menus - this is displayed each time we ask for a keystroke to navigate a menu in text-only mode


### `textMenuTopicPrompt`

Defined in msg_neu.t, line 1192

prompt text for topic lists in text-mode menus


### `thingFeelDesc(obj)`

Defined in msg_neu.t, line 222

generic "feel" description of a Thing


### `thingTasteDesc(obj)`

Defined in msg_neu.t, line 214

generic "taste" description of a Thing


### `tipStatusShort(stat)`

Defined in msg_neu.t, line 347

describe the tip mode setting


### `undoFailed`

Defined in msg_neu.t, line 1007

undo command failed


### `undoOkay(actor, cmd)`

Defined in msg_neu.t, line 994

undo command succeeded


### `unlitMatchDesc(obj)`

Defined in msg_neu.t, line 242


### `unlockedMsg(obj)`

Defined in msg_neu.t, line 1672


### `webNewUser(name)`

Defined in msg_neu.t, line 1732

web UI alert when a new user has joined a multi-user session


## Inherited Methods


*From [MessageHelper](messagehelper.md):* [`askDisambigList`](messagehelper.md#askDisambigList), [`shortTIMsg`](messagehelper.md#shortTIMsg), [`shortTMsg`](messagehelper.md#shortTMsg)
