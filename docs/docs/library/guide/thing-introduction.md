# Thing - Introduction

The Thing class is important in the TADS3 library for two reasons: (1) because it is the class used for all sorts of portable objects the player may interact with and (2) because it is the ancestor class for anything that represents a physical object in game (included those that are [non-portable](nonportableintroduction.md) and some that are intangible). In the present chapter we shall concentrate principally on the first use of Thing - as a class in its own right - but because so many classes inherit (directly or indirectly) from Thing, much of what we say about the properties and methods of Thing will be equally applicable to classes that inherit from Thing.

The properties and methods of Thing we shall be going on to discuss (or at least, exemplify) include:

```tads3
brightness
bulk
canBeTouchedBy
```

```tads3
desc
described
disambigName
distantInitSpecialDesc
feelDesc
globalParamName
initSpecialDesc
initDesc
isEquivalent
isHeldBy
isKnown
location
material
moved
name
remoteInitSpecialDesc
seen
sightSize
soundSize
smellDesc
specialDesc
tasteDesc
throwTargetCatch
useSpecialDesc
vocabWords
weight
```

In the present chapter we shall discuss only the simplest and most common of these, since some of the others will only become relevant in the light of other classes and concepts we haven't covered yet.

There are also one or two subclasses of Thing that are both so straightforward and so miscellaneous they may as well be dealt with in this chapter, namely:

```tads3
Food
Readable
Wearable
```
