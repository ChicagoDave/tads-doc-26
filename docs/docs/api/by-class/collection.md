# Collection

*class* — defined in [systype.h](../by-file/systype.h.md) (line 142)


The native collection type - this is the base class for lists, vectors, and other objects that represent collections of values.


**Superclass chain:** [Object](object.md) > **CollectionSubclasses:** [List](list.md), [LookupTable](lookuptable.md), [WeakRefLookupTable](weakreflookuptable.md), [Vector](vector.md), [AnonFuncPtr](anonfuncptr.md)


## Methods


### `createIterator`

Defined in systype.h, line 151

Create an iterator for the collection. This returns a new Iterator object that can be used to iterate over the values in the collection. The Iterator will use a snapshot of the collection that will never change, even if the collection is changed after the iterator is created.


### `createLiveIterator`

Defined in systype.h, line 162

Create a "live iterator" for the collection. This returns a new Iterator object that refers directly to the original collection; if the original collection changes, the iterator will reflect the changes in its iteration. As a result, the iterator is not guaranteed to visit all of the elements in the collection if the collection changes during the course of the iteration. If consistent results are required, use createIterator() instead.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
