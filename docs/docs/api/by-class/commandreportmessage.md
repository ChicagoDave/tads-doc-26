# CommandReportMessage

*class* — defined in [report.t](../by-file/report.t.md) (line 178)


Simple MessageResult-based command report


**Superclass chain:** [CommandReport](commandreport.md) > `object` > [MessageResult](messageresult.md) > **CommandReportMessageSubclasses:** [CosmeticSpacingCommandReport](cosmeticspacingcommandreport.md), [DefaultCommandReport](defaultcommandreport.md), [DefaultDescCommandReport](defaultdesccommandreport.md), [ExtraCommandReport](extracommandreport.md), [FullCommandReport](fullcommandreport.md), [AfterCommandReport](aftercommandreport.md), [BeforeCommandReport](beforecommandreport.md), [FailCommandReport](failcommandreport.md), [MainCommandReport](maincommandreport.md), [QuestionCommandReport](questioncommandreport.md)


## Inherited Properties


*From [CommandReport](commandreport.md):* [`action_`](commandreport.md#action_), [`isFailure`](commandreport.md#isFailure), [`isQuestion`](commandreport.md#isQuestion), [`iter_`](commandreport.md#iter_)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Methods


### `construct([params])` *(overridden)*

Defined in report.t, line 179


## Inherited Methods


*From [CommandReport](commandreport.md):* [`getAction`](commandreport.md#getAction), [`isActionImplicit`](commandreport.md#isActionImplicit), [`isActionNestedIn`](commandreport.md#isActionNestedIn), [`isPartOf`](commandreport.md#isPartOf), [`setAction`](commandreport.md#setAction)


*From [MessageResult](messageresult.md):* [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
