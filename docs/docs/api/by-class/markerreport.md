# MarkerReport

*class* — defined in [report.t](../by-file/report.t.md) (line 163)


Report boundary marker. This is a pseudo-report that doesn't display anything; its purpose is to allow a caller to identify a block of reports (the reports between two markers) for later removal or reordering.


**Superclass chain:** [CommandReport](commandreport.md) > `object` > **MarkerReportSubclasses:** [EndOfDescReport](endofdescreport.md), [FailCommandMarker](failcommandmarker.md)


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


## Methods


### `showMessage`

Defined in report.t, line 164


## Inherited Methods


*From [CommandReport](commandreport.md):* [`construct`](commandreport.md#construct), [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)
