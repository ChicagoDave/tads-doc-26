# AmbigObjectAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 447)


Ambiguous object announcement. We display this when the parser manages to resolve a noun phrase to an object (or objects) from an ambiguous set of possibilities, without having to ask the player for help but also without absolute certainty that the objects selected are the ones the player meant. This happens when more than enough objects are logical possibilities for selection, but some objects are more logical choices than others. The parser picks the most logical of the available options, but since other logical choices are present, the parser can't be certain that it chose the ones the player actually meant. Because of this uncertainty, we generate one of these announcements each time this happens. This report lets the player know exactly which object we chose, which will immediately alert the player when our selection is different from what they had in mind.


**Superclass chain:** [CommandAnnouncement](commandannouncement.md) > [CommandReport](commandreport.md) > `object` > **AmbigObjectAnnouncement**


## Properties


### `messageProp_` *(overridden)*

Defined in report.t, line 449

show the announceAmbigObject announcement


## Inherited Properties


*From [CommandAnnouncement](commandannouncement.md):* [`messageText_`](commandannouncement.md#messageText_)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Inherited Methods


*From [CommandAnnouncement](commandannouncement.md):* [`construct`](commandannouncement.md#construct), [`getMessageText`](commandannouncement.md#getMessageText), [`showMessage`](commandannouncement.md#showMessage)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
