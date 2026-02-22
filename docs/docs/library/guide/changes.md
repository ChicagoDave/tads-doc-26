# Changes for v3.0.9

- Correction to the code for the vending machine slot in [PlugAttachable](plugattachable.md) to prevent the coin reappearing once the ticket is issued.

- Definition of the endGame function in[cannotGoThatWayInDark](cannotgothatwayindark.md) corrected, and the redundant redefinition in [Dynamite](dynamite.md) removed.

- Added a section on the [TravelConnector](travelconnector.md) class.

- Added a section on the [mainOutputStream](mainoutputstream.md) object.

- Changed definition of [longCaveWords](decoration.md) to reflect the fact that it's no longer necessary to override isListedInRoomPart().

- [remoteInitSpecialDesc()](distanceconnector.md) now takes actor instead of pov as its parameter.

- Use the new macro gTopicText in [DefaultAskTellTopic](defaultasktelltopic.md) in place of gTopic.getTopicText.

- Provided examples of dobjMsg and failCheck() which also correct previous bugs on the [glassJar](restrictedcontainer.md) object. The failCheck() method has also been used in one or two other places instead of the previous lengthier construct.

- Corrected an error on the [oilLamp](oillamp.md) object by using the new failCheck routine.

- Added a note of the new [Hint](hinttemplate.md), [SyncEventList](synceventlisttemplate.md)and [Unthing](unthingtemplate.md) templates. The use of the new [Unthing](unthing.md) template is also discussed in the Unthing section, and of the Hint template in the [Hint](hint.md) section.

- Added a discussion of some of the main properties and methods on [Lockable](lockable.md), including the new lockStatusReportable.

- Added a brief discussion of [BasicDoor](basicdoor.md) and noted that [Door](door.md) and [SecretDoor](secretdoor.md) now inherit from it.

- Added sections on [Openable](openable.md) and [BasicOpenable](basicopenable.md).

- Removed iobjFor(BurnWith) code on [RedCandle](candle.md)that's no longer necessary with TADS 3.0.9.

- Added a brief description of the new moveIntoAdd() and moveOutOf methods for [RoomParts](roomparts.md).

- Updated the explanation of verboseMode on [gameMain](startupcodegamemain.md).

- Added an example of [RoomPartItem](decoration.md).

- Added an explanation of the new SensoryEmanation property isEmanating in the [Odor](odor.md) section.

- Added a discussion of the revised occludeObj() method and the new isOccludedBy() method to the [Occluder](occluder.md) section.

- Added a brief section on [RandomFiringScript](randomfiringscript.md) and amended the superclass lists of [RandomEventList](randomeventlist.md) and [ShuffledEventList](shuffledeventlist.md) to show that they now inherit from it.

- Added an example of the new [AutoClosingDoor](autoclosingdoor.md) property reportAutoClose().

- Added a brief section on using the [past tense](pasttense.md) in TADS 3.0.9.

- Corrected sundry typos.
