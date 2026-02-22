# Iterator

*class* — defined in [systype.h](../by-file/systype.h.md) (line 174)


The native iterator type - this is the base class for all iterators. This class is abstract and is thus never directly instantiated.


**Superclass chain:** [Object](object.md) > **IteratorSubclasses:** [IndexedIterator](indexediterator.md), [LookupTableIterator](lookuptableiterator.md)


## Methods


### `getCurKey`

Defined in systype.h, line 204

Get the current key. This returns the value of the key for the current item in the collection. For an indexed collection, this returns the index value; for a keyed collection, this returns the current key value.


### `getCurVal`

Defined in systype.h, line 210

Get the current value. This returns the value of the current item in the collection.


### `getNext`

Defined in systype.h, line 183

Get the next item in the collection. This returns the next item's value, and advances the internal state in the iterator so that a subsequent call to getNext() returns the next item after this one. When the iterator is first created, or after calling resetIterator(), this returns the first item in the collection.


### `isNextAvailable`

Defined in systype.h, line 190

Determine if the collection is out of items. Returns true if getNext() will return a valid item, nil if no more items are available.


### `resetIterator`

Defined in systype.h, line 196

Reset to the first item. After calling this routine, the next call to getNext() will return the first item in the collection.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
