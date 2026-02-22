# defaultReportTransform

*object* — defined in [report.t](../by-file/report.t.md) (line 1321)


Transcript Transform: remove unnecessary default reports. We'll scan the transcript for default reports for actions which also have implicit announcements or non-default reports, and remove those default reports. We'll also remove default descriptive reports which also have non-default reports in the same action.


**Superclass chain:** [TranscriptTransform](transcripttransform.md) > `object` > **defaultReportTransform**


## Methods


### `applyTransform(trans, vec)` *(overridden)*

Defined in report.t, line 1322
