# TadsObject

*class* — defined in [systype.h](../by-file/systype.h.md) (line 242)


The "TADS Object" intrinsic class. All objects that the program defines with the "class" or "object" statements descend from this class.


**Superclass chain:** [Object](object.md) > **TadsObject**


## Methods


### `createClone`

Defined in systype.h, line 260

Create a clone of this object. This creates an exact copy, with the same property values, as the original. This does not call any constructors; it merely instantiates an exact copy of the original.


### `createInstance(...)`

Defined in systype.h, line 250

Create an instance of this object: in other words, create a new object whose superclass is this object. The arguments provided are passed to the new object's constructor. This method returns a reference to the new object.


### `createTransientInstance(...)`

Defined in systype.h, line 267

Create a transient instance of this object. This works just like createInstance(), but creates a transient instance instead of an ordinary (persistent) instance.


### `getMethod(prop)`

Defined in systype.h, line 330

Get a method value. If the property is a method, this returns a function pointer to the method; this does NOT evaluate the method. If the property is not a method, this returns nil.


### `setMethod(prop, func)`

Defined in systype.h, line 341

Set a method value. Assigns the given function (which must be a function pointer value) to the given property of 'self'. This effectively adds a new method to the object.


### `setSuperclassList(scList)`

Defined in systype.h, line 317

Set the superclass list. scList is a list giving the new superclasses. The superclasses must all be TadsObject objects, with one exception: the list [TadsObject] may be passed to create an object based directly on TadsObject. No other intrinsic classes can be used in the list, and objects of other types cannot be used in the list.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
