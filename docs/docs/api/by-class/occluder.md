# Occluder

*class* — defined in [sense.t](../by-file/sense.t.md) (line 693)


Occluder: this is a mix-in class that can be used with multiple inheritance to combine with other classes (such as SenseConnector, or Thing subclasses), to create an "occluded view." This lets you exclude certain objects from view, and you can make the exclusion vary according to the point of view.


**Superclass chain:** `object` > **Occluder**


## Methods


### `clearSenseInfo`

Defined in sense.t, line 712

When we initialize for the sense path calculation, register to receive notification after we've finished building the sense table. We'll use the notification to remove any occluded objects from the sense table.


### `finishSensePath(objs, sense)`

Defined in sense.t, line 735

Receive notification that the sense path calculation is now finished. 'objs' is a LookupTable containing all of the objects involved in the sense path calculation (the objects are the keys in the table). Each object in the table now has its tmpXxx_ properties set to the sense path data we've calculated for that object - tmpTrans_ is the transparency to the object, tmpAmbient_ is the ambient light level at the object, and so on.


### `occludeObj(obj, sense, pov)`

Defined in sense.t, line 700

Do we occlude the given object, in the given sense and from the given point of view? This returns true if the object is occluded, nil if not. By default, we simply ask the object whether it's occluded by this occluder from the given POV.
