# RemappedActionAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 466)


Remapped action announcement. This is used when we need to mention a defaulted or disambiguated object, but the player's original input was remapped to a different action that rearranges the object roles. In these cases, rather than just announcing the defaulted object name, we announce the entire remapped action; we show the full action description because rearrangement of the object roles usually makes the standard object-only announcement confusing to read, since it doesn't naturally fit in as a continuation of what the user typed.


**Superclass chain:** [CommandAnnouncement](commandannouncement.md) > [CommandReport](commandreport.md) > `object` > **RemappedActionAnnouncement**


## Properties


### `messageProp_` *(overridden)*

Defined in report.t, line 473

use the action as the message parameter


## Inherited Properties


*From [CommandAnnouncement](commandannouncement.md):* [`messageText_`](commandannouncement.md#messageText_)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct` *(overridden)*

Defined in report.t, line 467


## Inherited Methods


*From [CommandAnnouncement](commandannouncement.md):* [`getMessageText`](commandannouncement.md#getMessageText), [`showMessage`](commandannouncement.md#showMessage)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
