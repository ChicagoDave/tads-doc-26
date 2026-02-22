# GroupSeparatorMessage

*class* — defined in [report.t](../by-file/report.t.md) (line 128)


Group separator. This simply displays separation between groups of messages - that is, between one set of messages associated with a single action and a set of messages associated with a different action.


**Superclass chain:** [CommandReport](commandreport.md) > `object` > **GroupSeparatorMessage**


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `construct(report)` *(overridden)*

Defined in report.t, line 129


### `showMessage`

Defined in report.t, line 137

show the normal command results separator


## Inherited Methods


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
