# QuestionCommandReport

*class* — defined in [report.t](../by-file/report.t.md) (line 266)


An interruption for interactive input. This is used to report a prompt for more information that's needed before the command can proceed, such as a prompt for a missing object, or a disambiguation prompt.


**Superclass chain:** [MainCommandReport](maincommandreport.md) > [FullCommandReport](fullcommandreport.md) > [CommandReportMessage](commandreportmessage.md) > [CommandReport](commandreport.md) > `object` > [MessageResult](messageresult.md) > **QuestionCommandReport**


## Properties


### `isQuestion` *(overridden)*

Defined in report.t, line 267


## Inherited Properties


*From [MainCommandReport](maincommandreport.md):* [`seqNum`](maincommandreport.md#seqNum)


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`iter_`](commandreport.md#iter_)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [CommandReportMessage](commandreportmessage.md):* [`construct`](commandreportmessage.md#construct)


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)


*From [MessageResult](messageresult.md):* [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
