# libGlobal

*object* — defined in [misc.t](../by-file/misc.t.md) (line 1587)


Library global variables


**Superclass chain:** `object` > **libGlobal**


## Properties


### `actorVisualAmbientCache`

Defined in misc.t, line 1643

Actor visual ambient cache - this keeps track of the ambient light level at the given actor.


### `allSenses`

Defined in misc.t, line 1697

List of all of the senses. The library pre-initializer will load this list with a reference to each instance of class Sense.


### `canTouchCache`

Defined in misc.t, line 1631

Can-Touch cache - we keep CanTouchInfo entries here, keyed by [from,to]. This cache is the touch-path equivalent of the sense cache, and is enabled and disabled


### `commandLineArgs`

Defined in misc.t, line 1812

Command line arguments. The library sets this to a list of strings containing the arguments passed to the program on the command line. This list contains the command line arguments parsed according to the local conventions for the operating system and C++ library. The standard parsing procedure used by most systems is to break the line into tokens delimited by space characters. Many systems also allow space characters to be embedded in tokens by quoting the tokens. The first argument is always the name of the .t3 file currently executing.


### `connectionCache`

Defined in misc.t, line 1637

Connection list cache - this is a cache of all of the objects connected by containment to a given object.


### `curAction`

Defined in misc.t, line 1784


### `curActor`

Defined in misc.t, line 1782

Current command information. We keep track of the current command's actor and action here, as well as the verification result list and the command report list.


### `curIssuingActor`

Defined in misc.t, line 1783


### `curVerifyResults`

Defined in misc.t, line 1785


### `exitListerObj`

Defined in misc.t, line 1788

the exitLister object, if included in the build


### `footnoteClass`

Defined in misc.t, line 1741

The global Footnote class object. We use a global for this, rather than referencing Footnote directly, to allow the footnote module to be left out entirely if the game doesn't make use of footnotes. The footnote class should set this during pre-initialization.


### `hintManagerObj`

Defined in misc.t, line 1791

the hint manager, if included in the build


### `IFID`

Defined in misc.t, line 1799

The game's IFID, as defined in the game's main module ID object. If the game has multiple IFIDs in the module list, this will store only the first IFID in the list. NOTE: the library initializes this automatically during preinit; don't set this manually.


### `lastActorForUndo`

Defined in misc.t, line 1775

Most recent target actor phrase; this goes with lastCommandForUndo. This is nil if the last command did not specify an actor (i.e., was implicitly for the player character), otherwise is the string the player typed specifying a target actor.


### `lastCommandForUndo`

Defined in misc.t, line 1766

Most recent command, for 'undo' purposes. This is the last command the player character performed, or the last initial command a player directed to an NPC.


### `libMessageObj`

Defined in misc.t, line 1608

The current library messages object. This is the source object for messages that don't logically relate to the actor carrying out the comamand. It's mostly used for meta-command replies, and for text fragments that are used to construct descriptions.


### `parserDebugMode`

Defined in misc.t, line 1750

flag: the parser is in 'debug' mode, in which it displays the parse tree for each command entered


### `playerChar`

Defined in misc.t, line 1702

The current player character


### `pointOfView`

Defined in misc.t, line 1717

The current perspective object. This is *usually* the actor performing the current command, but can be a different object when the actor is viewing the location being described via an intermediary, such as through a closed-circuit TV camera.


### `pointOfViewActor`

Defined in misc.t, line 1709

The current perspective actor. This is the actor who's performing the action (LOOK AROUND, EXAMINE, SMELL, etc) that's generating the current description.


### `povStack`

Defined in misc.t, line 1724

The stack of point of view objects. The last element of the vector is the most recent point of view after the current point of view.


### `scoreObj`

Defined in misc.t, line 1732

The global score object. We use a global for this, rather than referencing libScore directly, to allow the score module to be left out entirely if the game doesn't make use of scoring. The score module should set this during pre-initialization.


### `senseCache`

Defined in misc.t, line 1624

Sense cache - we keep SenseInfo lists here, keyed by [pov,sense]; we normally discard the cached information at the start of each turn, and disable caching entirely at the start of the "action" phase of each turn. We leave caching disabled during each turn's action phase because this is the phase where simulation state changes are typically made, and hence it would be difficult to keep the cache coherent during this phase.


### `totalTurns`

Defined in misc.t, line 1744

the total number of turns so far


## Methods


### `disableSenseCache`

Defined in misc.t, line 1662

disable the cache


### `enableSenseCache`

Defined in misc.t, line 1646

enable the cache, clearing any old cached information


### `getCommandSwitch(s)`

Defined in misc.t, line 1832

Retrieve a "switch" from the command line. Switches are options specifies with the conventional Unix "-xxx" notation. This searches for a command option that equals the given string or starts with the given substring. If we find it, we return the part of the option after the given substring - this is conventionally the value of the switch. For example, the command line might look like this:


### `invalSenseCache`

Defined in misc.t, line 1680

Invalidate the sense cache. This can be called if something happens during noun resolution or verification that causes any cached sense information to become out of date. For example, if you have to create a new game-world object during noun-phrase resolution, this should be called to ensure that the new object's visibility is properly calculated and incorporated into the cached information.
