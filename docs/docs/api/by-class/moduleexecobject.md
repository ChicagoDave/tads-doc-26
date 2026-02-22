# ModuleExecObject

*class* — defined in [_main.t](../by-file/_main.t.md) (line 314)


Module Execution Object. This is an abstract base class for various classes that provide modular execution hooks. This class and its subclasses are mix-in classes - they can be multiply inherited by any object (as long as it's not already some other kind of module execution object).


**Superclass chain:** `object` > **ModuleExecObject**


<details><summary>Subclasses (17)</summary>

- [InitObject](initobject.md)
- [PostRestoreObject](postrestoreobject.md)
- [PostUndoObject](postundoobject.md)
- [PreinitObject](preinitobject.md)
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
- [PreRestartObject](prerestartobject.md)
- [PreSaveObject](presaveobject.md)

</details>


## Properties


### `execAfterMe`

Defined in _main.t, line 327

List of objects that must be executed after me - this is analogous to execBeforeMe, but we make sure we run before these.


### `execBeforeMe`

Defined in _main.t, line 321

List of objects that must be executed before me - by default, the order doesn't matter, so we'll set this to an empty list. Instances can override this if it is necessary to execute other objects before this object can be executed.


### `hasInitialized_`

Defined in _main.t, line 422

flag to indicate that this is the first time running classExec


### `isDoingExec_`

Defined in _main.t, line 345

flag - true if we're in the process of executing


### `isExecuted_`

Defined in _main.t, line 342

flag - true if we've been executed on this round
