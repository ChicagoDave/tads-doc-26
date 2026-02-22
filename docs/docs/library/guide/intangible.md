# Intangible

Intangible : [Thing](thing-introduction.md)

An Intangible object (as opposed to an object derived from some of Intangible's subclasses) is one that has no sensory presence whatsoever, which means that the player can never refer to it, even with a bare EXAMINE command. That means it is really only useful for abstract objects that the player will never interact with directly (as a mix-in class with a SenseConnector, perhaps, as in the [DistanceConnector](distanceconnector.md)). To represent intangible but sensible objects such a ray of light, you are better off using the [Vaporous](vaporous.md) class than trying to tweak Intangible.
