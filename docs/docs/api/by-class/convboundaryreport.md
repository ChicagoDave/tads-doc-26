# ConvBoundaryReport

*class* — defined in [report.t](../by-file/report.t.md) (line 275)


A conversation begin/end report. This is a special marker we insert into the transcript to flag the boundaries of an NPC's conversational message.


**Superclass chain:** [CommandReport](commandreport.md) > `object` > **ConvBoundaryReportSubclasses:** [ConvBeginReport](convbeginreport.md), [ConvEndReport](convendreport.md)


## Properties


### `actorID`

Defined in report.t, line 279

the actor's ID number, as assigned by the ConversationManager


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct(id)` *(overridden)*

Defined in report.t, line 276


## Inherited Methods


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
