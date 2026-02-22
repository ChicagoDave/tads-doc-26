# PresentLater

*class* — defined in [extras.t](../by-file/extras.t.md) (line 3622)


A mix-in class for objects that don't come into play until some future event. This class lets us initialize these objects with their *eventual* location, using the standard '+' syntax, but they won't actually appear in the given location until later in the game. During pre-initialization, we'll remember the starting location, then set the actual location to nil; later, the object can be easily moved to its eventual location by calling makePresent().


**Superclass chain:** `object` > **PresentLater**


## Properties


### `eventualLocation`

Defined in extras.t, line 3787

our eventual location


### `initiallyPresent`

Defined in extras.t, line 3647

Flag: are we present initially? By default, we're only present later, as that's the whole point. In some cases, though, we have objects that come and go, but start out present. Setting this property to true makes the object present initially, but still allows it to come and go using the standard PresentLater mechanisms.


### `plKey`

Defined in extras.t, line 3637

My "key" - this is an optional property you can add to a PresentLater object to associate it with a group of objects. You can then use makePresentByKey() to move every object with a given key into the game world at once. This is useful when an event triggers a whole set of objects to come into the game world: rather than having to write a method that calls makePresent() on each of the related objects individually, you can simply give each related object the same key value, then call makePresentByKey() on that key.


## Methods


### `initializeLocation`

Defined in extras.t, line 3649


### `makePresent`

Defined in extras.t, line 3688

bring the object into the game world in its eventual location(s)


### `makePresentByKey(key)`

Defined in extras.t, line 3732

Bring every PresentLater object with the given key into the game. Note that this is a "class" method that you call on PresentLater itself:


### `makePresentByKeyIf(key, cond)`

Defined in extras.t, line 3760

Bring every PresentLater object with the given key into the game, or move every one out of the game, according to the condition 'cond'.


### `makePresentIf(cond)`

Defined in extras.t, line 3717

make myself present if the given condition is true; otherwise, remove me from the game world (i.e. move me into nil)
