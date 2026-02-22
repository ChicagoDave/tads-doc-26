# GameID

*class* — defined in [modid.t](../by-file/modid.t.md) (line 553)


Base class for the game's module ID. This merely sets the listing order to 1 so that the game's credit is listed first. Normally, exactly one GameID object, called 'versionInfo', is defined in a game, to provide the game's identifying information.


**Superclass chain:** [GameInfoModuleID](gameinfomoduleid.md) > [MetadataModuleID](metadatamoduleid.md) > [ModuleID](moduleid.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **GameID**


## Properties


### `listingOrder` *(overridden)*

Defined in modid.t, line 555

always list the game's credits before any library credits


## Inherited Properties


*From [GameInfoModuleID](gameinfomoduleid.md):* [`authorEmail`](gameinfomoduleid.md#authorEmail), [`copyingRules`](gameinfomoduleid.md#copyingRules), [`desc`](gameinfomoduleid.md#desc), [`execAfterMe`](gameinfomoduleid.md#execAfterMe), [`firstPublished`](gameinfomoduleid.md#firstPublished), [`forgivenessLevel`](gameinfomoduleid.md#forgivenessLevel), [`gameInfoFilename`](gameinfomoduleid.md#gameInfoFilename), [`gameUrl`](gameinfomoduleid.md#gameUrl), [`genreName`](gameinfomoduleid.md#genreName), [`headline`](gameinfomoduleid.md#headline), [`htmlDesc`](gameinfomoduleid.md#htmlDesc), [`IFID`](gameinfomoduleid.md#IFID), [`languageCode`](gameinfomoduleid.md#languageCode), [`licenseType`](gameinfomoduleid.md#licenseType), [`metadataKeys`](gameinfomoduleid.md#metadataKeys), [`presentationProfile`](gameinfomoduleid.md#presentationProfile), [`releaseDate`](gameinfomoduleid.md#releaseDate), [`seriesName`](gameinfomoduleid.md#seriesName), [`seriesNumber`](gameinfomoduleid.md#seriesNumber)


*From [ModuleID](moduleid.md):* [`byline`](moduleid.md#byline), [`htmlByline`](moduleid.md#htmlByline), [`name`](moduleid.md#name), [`version`](moduleid.md#version)


*From [ModuleExecObject](moduleexecobject.md):* [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `showCredit` *(overridden)*

Defined in modid.t, line 570

Show the game's credits. By default, we'll just show our name and by-line.


### `showVersion` *(overridden)*

Defined in modid.t, line 580

show a blank line after the game's version information, to make it stand apart from the list of library and VM version numbers


## Inherited Methods


*From [GameInfoModuleID](gameinfomoduleid.md):* [`execute`](gameinfomoduleid.md#execute), [`getGameInfoToday`](gameinfomoduleid.md#getGameInfoToday), [`writeMetadataFile`](gameinfomoduleid.md#writeMetadataFile)


*From [ModuleID](moduleid.md):* [`getModuleList`](moduleid.md#getModuleList), [`showAbout`](moduleid.md#showAbout)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
