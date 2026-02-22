# MultiObjectAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 354)


Multiple-object announcement. When the player applies a single command to a series of objects (as in "take the book and the folder" or "take all"), we'll show one of these announcements for each object, just before we execute the command for that object. This announcement usually just shows the object's name plus suitable punctuation (in English, a colon), and helps the player see which results go with which objects.


**Superclass chain:** [CommandAnnouncement](commandannouncement.md) > [CommandReport](commandreport.md) > `object` > **MultiObjectAnnouncement**


## Properties


### `messageProp_` *(overridden)*

Defined in report.t, line 370

show the announceMultiActionObject message


## Inherited Properties


*From [CommandAnnouncement](commandannouncement.md):* [`messageText_`](commandannouncement.md#messageText_)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct(preCalcMsg, obj, whichObj, action)` *(overridden)*

Defined in report.t, line 355


## Inherited Methods


*From [CommandAnnouncement](commandannouncement.md):* [`getMessageText`](commandannouncement.md#getMessageText), [`showMessage`](commandannouncement.md#showMessage)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
