# FullCommandReport

*class* — defined in [report.t](../by-file/report.t.md) (line 214)


base class for all "full" reports


**Superclass chain:** [CommandReportMessage](commandreportmessage.md) > [CommandReport](commandreport.md) > `object` > [MessageResult](messageresult.md) > **FullCommandReportSubclasses:** [AfterCommandReport](aftercommandreport.md), [BeforeCommandReport](beforecommandreport.md), [FailCommandReport](failcommandreport.md), [MainCommandReport](maincommandreport.md), [QuestionCommandReport](questioncommandreport.md)


## Properties


### `seqNum`

Defined in report.t, line 220

a full report has a sequence number that tells us where the report goes relative to the others - the higher this number, the later the report goes


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [CommandReportMessage](commandreportmessage.md):* [`construct`](commandreportmessage.md#construct)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)


*From [MessageResult](messageresult.md):* [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
