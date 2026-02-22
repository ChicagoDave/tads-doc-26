# DefaultObjectAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 397)


Default object announcement. We display this announcement whenever the player leaves out a required object from a command, but the parser is able to infer which object they must have meant. The parser infers that an object was intended when a verb requires an object that the player didn't specify, and there's only one logical choice for the missing object. We announce our assumption to put it out in the open, to ensure that the player is immediately alerted if they had something else in mind.


**Superclass chain:** [CommandAnnouncement](commandannouncement.md) > [CommandReport](commandreport.md) > `object` > **DefaultObjectAnnouncement**


## Properties


### `allResolved_`

Defined in report.t, line 426


### `obj_`

Defined in report.t, line 422

our defaulted object


### `whichObj_`

Defined in report.t, line 425

our message parameters


## Inherited Properties


*From [CommandAnnouncement](commandannouncement.md):* [`messageProp_`](commandannouncement.md#messageProp_), [`messageText_`](commandannouncement.md#messageText_)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct(obj, whichObj, action, allResolved)` *(overridden)*

Defined in report.t, line 398


### `getMessageText` *(overridden)*

Defined in report.t, line 415

get our message text


## Inherited Methods


*From [CommandAnnouncement](commandannouncement.md):* [`showMessage`](commandannouncement.md#showMessage)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
