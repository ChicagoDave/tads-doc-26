# CommandAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 307)


Announcements. We use these to track announcements to be made as part of an action's results.


**Superclass chain:** [CommandReport](commandreport.md) > `object` > **CommandAnnouncementSubclasses:** [AmbigObjectAnnouncement](ambigobjectannouncement.md), [CommandSepAnnouncement](commandsepannouncement.md), [DefaultObjectAnnouncement](defaultobjectannouncement.md), [ImplicitActionAnnouncement](implicitactionannouncement.md), [MultiObjectAnnouncement](multiobjectannouncement.md), [RemappedActionAnnouncement](remappedactionannouncement.md)


## Properties


### `messageProp_`

Defined in report.t, line 339

our gLibMessages property


### `messageText_`

Defined in report.t, line 342

our message text


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct([params])` *(overridden)*

Defined in report.t, line 308


### `getMessageText([params])`

Defined in report.t, line 321

Get our message text. By default, we simply get the gLibMessages message given by the property.


### `showMessage`

Defined in report.t, line 332

Show our message. Our default implementation shows the library message given by our messageProp_ property, using the parameters we stored in our constructor.


## Inherited Methods


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
