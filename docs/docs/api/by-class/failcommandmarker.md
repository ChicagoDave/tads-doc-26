# FailCommandMarker

*class* — defined in [report.t](../by-file/report.t.md) (line 249)


failure marker - this is a silent report that marks an action as having failed without actually generating any message text


**Superclass chain:** [MarkerReport](markerreport.md) > [CommandReport](commandreport.md) > `object` > **FailCommandMarker**


## Properties


### `isFailure` *(overridden)*

Defined in report.t, line 250


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Inherited Methods


*From [MarkerReport](markerreport.md):* [`showMessage`](markerreport.md#showMessage)


*From [CommandReport](commandreport.md):* [`construct`](commandreport.md#construct), [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
