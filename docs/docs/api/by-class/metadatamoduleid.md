# MetadataModuleID

*class* — defined in [modid.t](../by-file/modid.t.md) (line 189)


A module ID with metadata. During pre-initialization, we'll automatically write out a file with the metadata for each of these objects. This is an abstract base class; a subclass must be created for each specific metadata format.


**Superclass chain:** [ModuleID](moduleid.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **MetadataModuleIDSubclasses:** [GameInfoModuleID](gameinfomoduleid.md), [GameID](gameid.md)


## Inherited Properties


*From [ModuleID](moduleid.md):* [`byline`](moduleid.md#byline), [`htmlByline`](moduleid.md#htmlByline), [`listingOrder`](moduleid.md#listingOrder), [`name`](moduleid.md#name), [`version`](moduleid.md#version)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in modid.t, line 191

execute pre-initialization


### `writeMetadataFile`

Defined in modid.t, line 203

write our metadata file - this must be overridden by each subclass to carry out the specific steps needed to create and write the metadata file in the appropriate format for the subclass


## Inherited Methods


*From [ModuleID](moduleid.md):* [`getModuleList`](moduleid.md#getModuleList), [`showAbout`](moduleid.md#showAbout), [`showCredit`](moduleid.md#showCredit), [`showVersion`](moduleid.md#showVersion)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
