# WeakRefLookupTable

*class* — defined in [lookup.h](../by-file/lookup.h.md) (line 135)


WeakRefLookupTable is a "weak reference" version of the basic lookup table. This is similar to the regular LookupTable, and has the same methods; the only difference is that this type of table references its values "weakly." A value that is reachable only through weak references is subject to deletion by the garbage collector. A weak-reference lookup table is useful when you don't want a value's presence in the table to force the value to stay active, such as when the lookup table is merely a fast index to a set of values that must be otherwise reachable to be useful. When the garbage collector deletes one of our values, the key/value pair for the value is automatically deleted from the table.


**Superclass chain:** [LookupTable](lookuptable.md) > [Collection](collection.md) > [Object](object.md) > **WeakRefLookupTable**


## Inherited Methods


*From [LookupTable](lookuptable.md):* [`applyAll`](lookuptable.md#applyAll), [`forEach`](lookuptable.md#forEach), [`forEachAssoc`](lookuptable.md#forEachAssoc), [`getBucketCount`](lookuptable.md#getBucketCount), [`getDefaultValue`](lookuptable.md#getDefaultValue), [`getEntryCount`](lookuptable.md#getEntryCount), [`isKeyPresent`](lookuptable.md#isKeyPresent), [`keysToList`](lookuptable.md#keysToList), [`nthKey`](lookuptable.md#nthKey), [`nthVal`](lookuptable.md#nthVal), [`removeElement`](lookuptable.md#removeElement), [`setDefaultValue`](lookuptable.md#setDefaultValue), [`valsToList`](lookuptable.md#valsToList)


*From [Collection](collection.md):* [`createIterator`](collection.md#createIterator), [`createLiveIterator`](collection.md#createLiveIterator)


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
