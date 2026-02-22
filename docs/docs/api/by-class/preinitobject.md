# PreinitObject

*class* — defined in [_main.t](../by-file/_main.t.md) (line 471)


Pre-Initialization object. During pre-initialization, we'll invoke the execute() method on each instance of this class.


**Superclass chain:** [ModuleExecObject](moduleexecobject.md) > `object` > **PreinitObject**


<details><summary>Subclasses (11)</summary>

- [GlobalRemapping](globalremapping.md)
- [MessageBuilder](messagebuilder.md)
- [MetadataModuleID](metadatamoduleid.md)
- [GameInfoModuleID](gameinfomoduleid.md)
- [GameID](gameid.md)
- [OutputStream](outputstream.md)
- [BannerOutputStream](banneroutputstream.md)
- [LogConsole](logconsole.md)
- [WebWinOutputStream](webwinoutputstream.md)
- [StringPreParser](stringpreparser.md)
- [TopHintMenu](tophintmenu.md)

</details>


**Global objects:** [adv3LibPreinit](adv3libpreinit.md), [Compiler](compiler.md), [conversationManager](conversationmanager.md), [exitLister](exitlister.md), [hintManager](hintmanager.md), [libScore](libscore.md), [objectRelations](objectrelations.md), [reflectionServices](reflectionservices.md), [scoreNotifier](scorenotifier.md), [styleTagFilter](styletagfilter.md)


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec), [`execute`](moduleexecobject.md#execute)
