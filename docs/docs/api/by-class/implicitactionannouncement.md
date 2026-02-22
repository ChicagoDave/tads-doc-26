# ImplicitActionAnnouncement

*class* — defined in [report.t](../by-file/report.t.md) (line 511)


Implicit action announcement. This is displayed when we perform a command implicitly, which we usually do to fulfill a precondition of an action.


**Superclass chain:** [CommandAnnouncement](commandannouncement.md) > [CommandReport](commandreport.md) > `object` > **ImplicitActionAnnouncement**


## Properties


### `justAsking`

Defined in report.t, line 582

flag: the action was interrupted with an interactive question


### `justTrying`

Defined in report.t, line 579

Flag: we're just attempting the action; this is set when we determine that the implicit action has failed, in which case we want an announcement indicating that we're merely attempting the action, not actually performing it. Presume that we're actually going to perform the action; the action can change this if necessary.


## Inherited Properties


*From [CommandAnnouncement](commandannouncement.md):* [`messageProp_`](commandannouncement.md#messageProp_), [`messageText_`](commandannouncement.md#messageText_)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct(action, msg)` *(overridden)*

Defined in report.t, line 512


### `makeSilent`

Defined in report.t, line 530

Make this announcement silent. This eliminates any announcement for this action, but makes it otherwise behave like a normal implied action.


### `noteJustTrying`

Defined in report.t, line 548

Note that the action we're attempting is merely an attempt that failed. This will change our report to indicate that we're only trying the action, rather than suggesting that we actually carried it out.


### `noteQuestion`

Defined in report.t, line 562

Note that the action we're attempting is incomplete, as it was interupted for interactive input (such as asking for a missing object).


## Inherited Methods


*From [CommandAnnouncement](commandannouncement.md):* [`getMessageText`](commandannouncement.md#getMessageText), [`showMessage`](commandannouncement.md#showMessage)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
