# MessageResult

*class* — defined in [exec.t](../by-file/exec.t.md) (line 1577)


Result message object. This is used for verification results and main command reports, which must keep track of messages to display.


**Superclass chain:** `object` > **MessageResult**


<details><summary>Subclasses (20)</summary>

- [CommandReportMessage](commandreportmessage.md)
- [CosmeticSpacingCommandReport](cosmeticspacingcommandreport.md)
- [DefaultCommandReport](defaultcommandreport.md)
- [DefaultDescCommandReport](defaultdesccommandreport.md)
- [ExtraCommandReport](extracommandreport.md)
- [FullCommandReport](fullcommandreport.md)
- [AfterCommandReport](aftercommandreport.md)
- [BeforeCommandReport](beforecommandreport.md)
- [FailCommandReport](failcommandreport.md)
- [MainCommandReport](maincommandreport.md)
- [QuestionCommandReport](questioncommandreport.md)
- [VerifyResult](verifyresult.md)
- [DangerousVerifyResult](dangerousverifyresult.md)
- [IllogicalNowVerifyResult](illogicalnowverifyresult.md)
- [IllogicalAlreadyVerifyResult](illogicalalreadyverifyresult.md)
- [IllogicalVerifyResult](illogicalverifyresult.md)
- [IllogicalSelfVerifyResult](illogicalselfverifyresult.md)
- [InaccessibleVerifyResult](inaccessibleverifyresult.md)
- [LogicalVerifyResult](logicalverifyresult.md)
- [NonObviousVerifyResult](nonobviousverifyresult.md)

</details>


## Properties


### `messageProp_`

Defined in exec.t, line 1850

the message property, if we have one


### `messageText_`

Defined in exec.t, line 1847

the text of our result message


## Methods


### `construct(msg, [params])`

Defined in exec.t, line 1585

Construct given literal message text, or alternatively a property of the current actor's verb messages object. In either case, we'll expand the message immediately to allow the message to be displayed later with any parameters fixed at the time the message is constructed.


### `resolveMessageText(sources, msg, params)`

Defined in exec.t, line 1620

Static method: resolve a message. If the message is given as a property, we'll look up the message in the given source objects and in the actor's "action messages" object. We'll return the resolved message string.


### `setMessage(msg, [params])`

Defined in exec.t, line 1831

set a new message, given the same type of information as we'd use to construct the object


### `showMessage`

Defined in exec.t, line 1840

Display a message describing why the command isn't allowed.
