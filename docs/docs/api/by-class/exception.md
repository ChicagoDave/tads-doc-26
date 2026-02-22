# Exception

*class* — defined in [_main.t](../by-file/_main.t.md) (line 657)


Base class for all exception objects. We derive all exceptions from this base class so that we can write 'catch' blocks that catch all exceptions by catching 'Exception'.


**Superclass chain:** `object` > **Exception**


<details><summary>Subclasses (42)</summary>

- [AbortImplicitSignal](abortimplicitsignal.md)
- [ActionRemappingTooComplexError](actionremappingtoocomplexerror.md)
- [BreakLoopSignal](breakloopsignal.md)
- [CircularExecException](circularexecexception.md)
- [CompilerException](compilerexception.md)
- [DisambigException](disambigexception.md)
- [DisambigOrdinalOutOfRangeException](disambigordinaloutofrangeexception.md)
- [StillAmbiguousException](stillambiguousexception.md)
- [UnmatchedDisambigException](unmatcheddisambigexception.md)
- [EndOfFileException](endoffileexception.md)
- [ExitActionSignal](exitactionsignal.md)
- [ExitSignal](exitsignal.md)
- [FileException](fileexception.md)
- [FileClosedException](fileclosedexception.md)
- [FileCreationException](filecreationexception.md)
- [FileIOException](fileioexception.md)
- [FileModeException](filemodeexception.md)
- [FileNotFoundException](filenotfoundexception.md)
- [FileOpenException](fileopenexception.md)
- [FileSafetyException](filesafetyexception.md)
- [FileSyncException](filesyncexception.md)
- [NetException](netexception.md)
- [NetSafetyException](netsafetyexception.md)
- [SocketDisconnectException](socketdisconnectexception.md)
- [ParserException](parserexception.md)
- [ParseFailureException](parsefailureexception.md)
- [ReplacementCommandStringException](replacementcommandstringexception.md)
- [RetryCommandTokensException](retrycommandtokensexception.md)
- [TerminateCommandException](terminatecommandexception.md)
- [CancelCommandLineException](cancelcommandlineexception.md)
- [ProgramException](programexception.md)
- [QuittingException](quittingexception.md)
- [RemapActionSignal](remapactionsignal.md)
- [RestartSignal](restartsignal.md)
- [RuntimeError](runtimeerror.md)
- [StorageServerError](storageservererror.md)
- [SettingsNotSupportedException](settingsnotsupportedexception.md)
- [TokenizerError](tokenizererror.md)
- [TokErrorNoMatch](tokerrornomatch.md)
- [UnboundMultiMethod](unboundmultimethod.md)
- [UnboundInheritedMultiMethod](unboundinheritedmultimethod.md)
- [UnknownCharSetException](unknowncharsetexception.md)

</details>


## Properties


### `errmsg_`

Defined in _main.t, line 693

Private member: The error message passed to the constructor, if any. Note that this doesn't necessarily contain the actual displayed exception message, since displayException() can be overridden in subclasses to display additional parameters or other text entirely. The definitive message is the one that displayException() generates. If you want the displayed message as a string, use getExceptionMessage().


## Methods


### `construct(msg?, ...)`

Defined in _main.t, line 659

construct, with an optional message describing the error


### `displayException`

Defined in _main.t, line 667

display the exception - should always be overridden


### `getExceptionMessage`

Defined in _main.t, line 678

Get the exception message as a string. This captures the output of displayException() and returns it a string. Use this instead of accessing errmsg_, since that member is private and might not reflect the actual displayed message.


### `showStackTrace(stackList)`

Defined in _main.t, line 702

Display a stack trace, given a list of T3StackInfo objects. Note that, for efficiency, we do not by default cache a stack trace when an exception occurs; individual subclasses can obtain a stack trace if desired at construction and use the information to show a stack trace for the exception.
