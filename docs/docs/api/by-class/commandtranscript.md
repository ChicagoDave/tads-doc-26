# CommandTranscript

*class* — defined in [report.t](../by-file/report.t.md) (line 606)


Command Transcript. This is a "semantic transcript" of the results of a command. This provides a list of CommandReport objects describing the results of the command.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **CommandTranscript**


## Properties


### `isActive`

Defined in report.t, line 648

flag: I'm active; when this is nil, we'll pass text through our filter routine unchanged


### `isFailure`

Defined in report.t, line 617

flag: the command has failed (i.e., at least one failure report has been generated)


### `iter_`

Defined in report.t, line 1235

iteration number - for an iterated top-level command, this helps us keep the results for a particular iteration grouped together


### `reports_`

Defined in report.t, line 1238

our vector of reports


### `transforms_`

Defined in report.t, line 1241

our list of transformations


## Methods


### `actionFailed(action)`

Defined in report.t, line 634

Did the given action fail? This scans the transcript to determine if there are any failure messages associated with the given action.


### `activate`

Defined in report.t, line 842

activate - set up to capture output


### `addCommandSep`

Defined in report.t, line 1148

Add a command separator.


### `addMarker`

Defined in report.t, line 1005

Add a marker report. This adds a marker to the report stream, and returns the marker object. The marker doesn't show any message in the final display, but callers can use a pair of markers to identify a range of reports for later reordering or removal.


### `addReport(report)`

Defined in report.t, line 934

Add a report.


### `announceAmbigActionObject(obj, whichObj)`

Defined in report.t, line 1129

Announce an object that was resolved with slight ambiguity.


### `announceDefaultObject(obj, whichObj, action, allResolved)`

Defined in report.t, line 1138

Announce a default object.


### `announceImplicit(action, msgProp)`

Defined in report.t, line 1080

Announce that the action is implicit


### `announceMultiActionObject(preCalcMsg, obj, whichObj)`

Defined in report.t, line 1119

Announce one of a set of objects to a multi-object action. We'll record this announcement for display with our report list.


### `announceRemappedAction`

Defined in report.t, line 1109

Announce a remapped action


### `applyTransforms`

Defined in report.t, line 1203

apply transformations


### `canShowReport(report)`

Defined in report.t, line 1169

Can we show a given report? By default, we always return true, but subclasses might want to override this to suppress certain types of reports.


### `clearReports`

Defined in report.t, line 1157

clear our reports


### `construct`

Defined in report.t, line 607


### `currentActionHasReport(func)`

Defined in report.t, line 1214

check to see if the current action has a report matching the given criteria


### `deactivate`

Defined in report.t, line 849

deactivate - stop capturing output


### `deleteLastReport`

Defined in report.t, line 991

delete the last report added


### `deleteRange(marker1, marker2)`

Defined in report.t, line 1018

delete the reports between two markers


### `endDescription`

Defined in report.t, line 1071

End the description section of the report. This adds a marker report that indicates that anything following (and part of the same action) is no longer part of the description; this can be important when we apply the default description suppression transformation, because it tells us not to consider the non-descriptive messages following this marker when, for example, suppressing default descriptive messages.


### `filterText(ostr, txt)` *(overridden)*

Defined in report.t, line 1177

Filter text. If we're active, we'll turn the text into a command report and add it to our report list, blocking the text from reaching the underlying stream; otherwise, we'll pass it through unchanged.


### `findCurrentActionReport(func)`

Defined in report.t, line 1221

find a report in the current action that matches the given criteria


### `flushForInput`

Defined in report.t, line 871

Flush the transcript in preparation for reading input. This shows all pending reports, clears the backlog of reports (so that we don't show them again in the future), and deactivates the transcript's capture feature so that subsequent output goes directly to the output stream.


### `forEachReport(func)`

Defined in report.t, line 1060

Perform a callback on all of the reports in the transcript. We'll invoke the given callback function func(rpt) once for each report, with the report object as the parameter.


### `getLastReport`

Defined in report.t, line 984

get the last report added


### `moveRangeAppend(marker1, marker2)`

Defined in report.t, line 1035

Pull out the reports between two markers, and reinsert them at the end of the transcript.


### `newIter`

Defined in report.t, line 859

Count an iteration. An Action should call this once per iteration if it's a top-level (non-nested) command.


### `noteFailure`

Defined in report.t, line 623

Note that the current action has failed. This is equivalent to adding a reportFailure() message to the transcript.


### `showReports(deact)`

Defined in report.t, line 887

Show our reports. Returns true if the transcript was previously active, nil if not.


### `summarizeAction(cond, report)`

Defined in report.t, line 693

Summarize the current action's reports. This allows a caller to turn a series of iterated reports into a single report for the entire action. For example, we could change something like this:
