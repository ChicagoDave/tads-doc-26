# ModuleID

*class* — defined in [modid.t](../by-file/modid.t.md) (line 37)


Module ID. Each library add-in can define one of these, so that the "credits" command and the like can automatically show the version of each library module included in the finished game, without the game's author having to compile a list of the module versions manually.


**Superclass chain:** `object` > **ModuleIDSubclasses:** [MetadataModuleID](metadatamoduleid.md), [GameInfoModuleID](gameinfomoduleid.md), [GameID](gameid.md)


**Global objects:** [moduleAdv3](moduleadv3.md)


## Properties


### `byline`

Defined in modid.t, line 42

the "byline" for the module, in plain text and HTML versions


### `htmlByline`

Defined in modid.t, line 43


### `listingOrder`

Defined in modid.t, line 143

My listing order. When we compile a list of modules, we'll sort the modules first by ascending listing order; any modules with the same listing order will be sorted alphabetically by name with respect to the other modules with the same listing order.


### `name`

Defined in modid.t, line 39

my name


### `version`

Defined in modid.t, line 46

my version number string


## Methods


### `getModuleList`

Defined in modid.t, line 149

get a list of all of the modules that are part of the game, sorted in listing order


### `showAbout`

Defined in modid.t, line 127

Show the "about this game" information. By default, we show nothing here. Typically, only the game's module ID object will override this; in the game's module ID object, this method should display any desired background information about the game that the author wants the player to see on typing the ABOUT command.


### `showCredit`

Defined in modid.t, line 56

Show my library credit. By default won't show anything. Libraries should generally not override this, because we want to leave it up to the author to determine how the credits are displayed. If a library overrides this, then the author won't be able to control the formatting of the library credit, which is undesirable.


### `showVersion`

Defined in modid.t, line 65

Show version information. By default, we show our name and version number, then start a new line. The main game's module ID should generally override this to show an appropriate version message for the game, and any library add-ins that want to display their version information can override this to do so.
