# GameInfoModuleID

*class* — defined in [modid.t](../by-file/modid.t.md) (line 218)


A module ID with GameInfo metadata. The GameInfo metadata format is the standard TADS format for descriptive data about the game. The usual way to use GameInfo metadata is to create a file called "gameinfo.txt" for a game, then embed this file directly in the game's .t3 file using the TADS 3 resource bundler (t3res). Once the gameinfo.txt is embedded in the .t3 file, tools will be able to read the game's descriptive data directly from the .t3 file. For example, HTML TADS on Windows can read the information into its Game Chest, which allows the interpreter to show the full name of the game, the author, and a blurb describing the game, among other things.


**Superclass chain:** [MetadataModuleID](metadatamoduleid.md) > [ModuleID](moduleid.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **GameInfoModuleIDSubclasses:** [GameID](gameid.md)


## Properties


### `authorEmail`

Defined in modid.t, line 313

The names and email addresses of the authors, in GameInfo format. This list must use the following format:


### `copyingRules`

Defined in modid.t, line 412

The copying rules for this game. Most text games these days are released as freeware with minimal restrictions on copying, so we use a default of "nominal cost only." Other values defined in the GameInfo format include Prohibited, No Restrictions, No-Cost Only, At-Cost Only, and Other. A modifier indicates whether or not the game may be included in compilations (such as those "10,001 great games" CD-R's that people like to sell on auction sites); we indicate that inclusion in compilations is allowed by default. You can change this to "Compilations Prohibited" if you prefer not to allow your game to be distributed in that fashion.


### `desc`

Defined in modid.t, line 327

Descriptive text for the game, in plain text format. This is a short description that can be used, for example, in a catalog of games. This should be a couple of sentences or so.


### `execAfterMe` *(overridden)*

Defined in en_us.t, line 111

Make sure we run BEFORE the main library preinitializer, so that we install the comparator in the dictionary before we add the vocabulary words to the dictionary. This doesn't make any difference in terms of the correctness of the dictionary, since the dictionary will automatically rebuild itself whenever we install a new comparator, but it makes the preinitialization run a tiny bit faster by avoiding that rebuild step.


### `firstPublished`

Defined in modid.t, line 357

The date of first publication. This can be just a year in YYYY format, or a full YYYY-MM-DD date. This is the original release date of the original version of the game, which is often of interest to archivists. This should *not* be updated when a new release is made - it's always the date of *original* publication.


### `forgivenessLevel`

Defined in modid.t, line 296

The forgiveness level, according to the Zarfian scale propounded by Andrew Plotkin on rec.arts.int-fiction. This must be one of these terms, using the exact capitalization shown: Merciful, Polite, Tough, Nasty, Cruel.


### `gameInfoFilename`

Defined in modid.t, line 466

the GameInfo filename - by default, we write the standard gameinfo.txt file


### `gameUrl`

Defined in modid.t, line 320

The game's web site, if any. If specified, this must be an absolute URL with http protocol - that is, it must be of the form "http://mydomain.com/...".


### `genreName`

Defined in modid.t, line 288

The genre of the game. Some games don't fit any particular genre, and some authors just don't like the idea of having to pigeonhole their games, so feel free to leave it out. If there's a good fit to a well-established genre, though, you can specify it here. We recommend you keep this short - one word, maybe two - and use a genre name that's generally recognized as such. You might want to use Baf's Guide as a reference (http://www.wurb.com/if/genre).


### `headline`

Defined in modid.t, line 264

The game's headline. It's become an IF tradition to use a quasi-subtitle of the sort that Infocom used, of the form "An Interactive Mystery." This can be used to define that subtitle.


### `htmlDesc`

Defined in modid.t, line 339

Descriptive text for the game, as an HTML fragment. This should have the same information as the 'desc', but this version can use HTML markups (including tags and character entities) to embellish the display of the text. Any HTML markups should be "in-line" body elements only, not "block" or head elements, so that this text can be inserted into a larger HTML document. For example, markups like <i> and <b> are fine, but <p> and <table> should not be used.


### `IFID`

Defined in modid.t, line 257

The IFID - this is a UUID uniquely identifying the game, using the standard UUID format (xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, where each 'x' is a hexadecimal digit). You should pick an IFID when you start each game project, and then keep the same IFID throughout the game's entire existence, *including* version updates. Each new version release of the same game - even major new versions - should use the same IFID, so that the versions can all be related to one another as the same game.


### `languageCode`

Defined in modid.t, line 367

The language in which this game's text is written. This is the RFC3066 language code for the main language of the work. For example, games written in US English would use 'en-US', while games written in British English would use 'en-GB'. Note that each language-specific library module should use 'modify' to set this to the default for the library.


### `licenseType`

Defined in modid.t, line 384

The license type for this game. Most text IF games these days are released as freeware, so we use this as the default. The GameInfo metadata format defines several other standard license types, including Public Domain, Shareware, Commercial Demo, Commercial, and Other. Authors should change this if they plan to release under a licensing model other than freeware.


### `metadataKeys`

Defined in modid.t, line 474

The metadata key mappings. This is a list of key/property pairs. The key in each pair is a string giving a standard GameInfo key name, and the property gives the property (of self) that we evaluate to get the string value for that key.


### `presentationProfile`

Defined in modid.t, line 420

The recommended "presentation profile" for the game. 'Default' means that the interpreter's default profile should be used. (Some interpreters let the user select which profile to use as the default, in which case 'Default' means we'll use that profile.)


### `releaseDate`

Defined in modid.t, line 348

The release date. By default, we compute this statically to be today's date. This means this will be set to the date of compilation. If the game wishes to override this, note that the GameInfo format requires this to be of the form YYYY-MM-DD. For example, December 9, 2001 would be '2001-12-09'.


### `seriesName`

Defined in modid.t, line 276

If this game is part of a series, such as a trilogy, these can be used to identify the name of the series and the position in the series. The series name should be something like "The Enchanter Trilogy"; the series number, if provided, should be a simple integer string ('1', '2', etc) giving the position in the series. Note that the series number isn't required even if a series name is specified, since some series are just groups of works without any particular ordering.


### `seriesNumber`

Defined in modid.t, line 277


## Inherited Properties


*From [ModuleID](moduleid.md):* [`byline`](moduleid.md#byline), [`htmlByline`](moduleid.md#htmlByline), [`listingOrder`](moduleid.md#listingOrder), [`name`](moduleid.md#name), [`version`](moduleid.md#version)


*From [ModuleExecObject](moduleexecobject.md):* [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in en_us.t, line 95

During start-up, install a case-insensitive truncating comparator in the main dictionary.


### `getGameInfoToday`

Defined in modid.t, line 502

get today's date, using the GameInfo standard date format (YYYY-MM-DD)


### `writeMetadataFile` *(overridden)*

Defined in modid.t, line 423

write our metadata file


## Inherited Methods


*From [ModuleID](moduleid.md):* [`getModuleList`](moduleid.md#getModuleList), [`showAbout`](moduleid.md#showAbout), [`showCredit`](moduleid.md#showCredit), [`showVersion`](moduleid.md#showVersion)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
