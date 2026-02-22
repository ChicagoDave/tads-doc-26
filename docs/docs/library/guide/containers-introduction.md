# Containers - Introduction

For the purposes of our guided tour of the TADS 3 library, "containers" include every type of physical object that can physically contain another in some way, not only in the obvious sense that the contained object is inside the container, but also where it is on, under or behind the container.

Another way of defining containers in the TADS 3 library is as descendants of the BulkLimiter class:

[BulkLimiter](bulklimiter.md)

```tads3
   BasicContainer
      Container
         Booth
         Dispenser
            Matchbook
      OpenableContainer
         KeyedContainer
         LockableContainer
      RestrictedContainer
      SingleContainer
      StretchyContainer
SpaceOverlay

RearContainer

      RearSurface

Underside

    Surface
      Bed
      Chair
      Platform
         NominalPlatform
Some of these will be left to later chapters, since they inherit from other classes we haven't dealt with yet (e.g. Bed, Chair and Platform are all types of NestedRoom, which we'll deal with later, and we'll need to delay discussion of KeyedContainer until we discuss locks and keys in the next chapter). In the present chapter we'll cover the simpler kind of containers. We'll also be covering the following functionally related classes:
   ComplexComponent
   ComplexContainer
```
