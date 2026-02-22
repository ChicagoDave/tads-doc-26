# moduleAdv3

*object* — defined in [modid.t](../by-file/modid.t.md) (line 591)


The main TADS 3 library ID.


**Superclass chain:** [ModuleID](moduleid.md) > `object` > **moduleAdv3**


## Properties


### `byline` *(overridden)*

Defined in modid.t, line 593


### `htmlByline` *(overridden)*

Defined in modid.t, line 594


### `listingOrder` *(overridden)*

Defined in modid.t, line 606

We use a listing order of 50 so that, if all of the other credits use the defaults, we appear after the game's own credits (conventionally at listing order 1) and before any extension credits (which inherit the default order 100), but so that there's room for extensions that want to appear before us, or after us but before any default-ordered extensions.


### `listingOrder` *(overridden)*

Defined in modid.t, line 636

Use a very high listing order so that we're the last thing shown.


### `name` *(overridden)*

Defined in modid.t, line 592


### `version` *(overridden)*

Defined in modid.t, line 596


## Methods


### `showVersion` *(overridden)*

Defined in modid.t, line 618

An ID module not for the library but for the T3 VM itself. This doesn't display any credit information, but displays version number information for the VM so that the "version" command shows what version of the interpreter is in use.


## Inherited Methods


*From [ModuleID](moduleid.md):* [`getModuleList`](moduleid.md#getModuleList), [`showAbout`](moduleid.md#showAbout), [`showCredit`](moduleid.md#showCredit)
