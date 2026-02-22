# senseTmp

*object* — defined in [thing.t](../by-file/thing.t.md) (line 159)


Sense calculation scratch-pad globals. Many of the sense calculations involve recursive descents of portions of the containment tree. In the course of these calculations, it's sometimes useful to have information about the entire operation in one of the recursive calls. We could pass the information around as extra parameters, but that adds overhead, and performance is critical in the sense routines (because they tend to get invoked a *lot*). To reduce the overhead, particularly for information that's not needed very often, we stuff some information into this global object rather than passing it around through parameters.


**Superclass chain:** `object` > **senseTmp**


## Properties


### `notifyList`

Defined in thing.t, line 168

post-calculation notification list


### `pointOfView`

Defined in thing.t, line 165

The point of view of the sense calculation. This is the starting point of a sense traversal; it's the object that's viewing the other objects.
