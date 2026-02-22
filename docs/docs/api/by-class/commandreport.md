# CommandReport

*class* — defined in [report.t](../by-file/report.t.md) (line 55)


Command report objects. The library uses these to control how the text from a command is displayed. Game code can also use report objects to show and control command results, but this isn't usually necessary; game code can usually simply display messages directly.


**Superclass chain:** `object` > **CommandReport**


<details><summary>Subclasses (26)</summary>

- [CommandAnnouncement](commandannouncement.md)
- [AmbigObjectAnnouncement](ambigobjectannouncement.md)
- [CommandSepAnnouncement](commandsepannouncement.md)
- [DefaultObjectAnnouncement](defaultobjectannouncement.md)
- [ImplicitActionAnnouncement](implicitactionannouncement.md)
- [MultiObjectAnnouncement](multiobjectannouncement.md)
- [RemappedActionAnnouncement](remappedactionannouncement.md)
- [CommandReportMessage](commandreportmessage.md)
- [CosmeticSpacingCommandReport](cosmeticspacingcommandreport.md)
- [DefaultCommandReport](defaultcommandreport.md)
- [DefaultDescCommandReport](defaultdesccommandreport.md)
- [ExtraCommandReport](extracommandreport.md)
- [FullCommandReport](fullcommandreport.md)
- [AfterCommandReport](aftercommandreport.md)
- [BeforeCommandReport](beforecommandreport.md)
- [FailCommandReport](failcommandreport.md)
- [MainCommandReport](maincommandreport.md)
- [QuestionCommandReport](questioncommandreport.md)
- [ConvBoundaryReport](convboundaryreport.md)
- [ConvBeginReport](convbeginreport.md)
- [ConvEndReport](convendreport.md)
- [GroupSeparatorMessage](groupseparatormessage.md)
- [InternalSeparatorMessage](internalseparatormessage.md)
- [MarkerReport](markerreport.md)
- [EndOfDescReport](endofdescreport.md)
- [FailCommandMarker](failcommandmarker.md)

</details>


## Properties


### `action_`

Defined in report.t, line 97

the action I'm associated with


### `isFailure`

Defined in report.t, line 85

Flag: if this property is true, this report indicates a failure. By default, a report does not indicate failure.


### `isQuestion`

Defined in report.t, line 91

Flag: if this property is true, this report indicates an interruption for interactive input.


### `iter_`

Defined in report.t, line 94

iteration number current when we were added to the transcript


## Methods


### `construct`

Defined in report.t, line 56


### `getAction`

Defined in report.t, line 67

get/set my action


### `isActionImplicit`

Defined in report.t, line 71

check to see if my action is implicit


### `isActionNestedIn(other)`

Defined in report.t, line 74

check to see if my action is nested in the other report's action


### `isPartOf(report)`

Defined in report.t, line 104

Am I part of the same action as the given report? Returns true if this action is part of the same iteration and part of the same action as the other report.


### `setAction(action)`

Defined in report.t, line 68
