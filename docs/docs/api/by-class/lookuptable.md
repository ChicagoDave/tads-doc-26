# LookupTable

*class* — defined in [lookup.h](../by-file/lookup.h.md) (line 24)


The LookupTable intrinsic class provides a general-purpose hash table implementation. LookupTable can be used syntactically as though it were a list, but the index values are arbitrary hash key values rather than being limited to sequential integers.


**Superclass chain:** [Collection](collection.md) > [Object](object.md) > **LookupTableSubclasses:** [WeakRefLookupTable](weakreflookuptable.md)


## Methods


### `applyAll(func)`

Defined in lookup.h, line 46

Apply the given function to each entry, and replace the value of the entry with the return value of the function. The callback is invoked with the key and value as arguments for each entry: func(key, value). No return value.


### `forEach(func)`

Defined in lookup.h, line 54

Invoke the given function with each entry in the table. The function is invoked with value of an entry as its argument: func(value). Any return value of the function is ignored. No return value.


### `forEachAssoc(func)`

Defined in lookup.h, line 80

Invoke the given function with each entry in the table, passing the key and value to the callback. The function is invoked with key and value of an entry as its arguments: func(key, value). Any return value of the function is ignored. No return value.


### `getBucketCount`

Defined in lookup.h, line 63

Get the number of buckets (i.e., slots for unique hash values). The number of buckets doesn't vary over the life of the table, so this simply returns the number of buckets that was specified in the constructor when the table was created. This can be used to create a new table with the same parameters as an existing table.


### `getDefaultValue`

Defined in lookup.h, line 99

Get the default value. This returns the value previously set with setDefaultValue(), or nil if no explicit default has been set on this table.


### `getEntryCount`

Defined in lookup.h, line 72

Get the number of entries. This returns the number of key/value pairs stored in the table. Note that this is not the same as the initial capacity specified in the constructor when the table was created; this is the number of entries actually stored in the table.


### `isKeyPresent(key)`

Defined in lookup.h, line 30

Determine if a given key is present in the table. Returns true if the key is present, nil if not.


### `keysToList`

Defined in lookup.h, line 86

Make a list of all of my keys. The return value is a list, in arbitrary order, of all of the keys in the table.


### `nthKey(n)`

Defined in lookup.h, line 113

Get the nth key. This returns the key that would appear at the given index in the keysToList() result.


### `nthVal(n)`

Defined in lookup.h, line 119

Get the enth value. This returns the value that would appear at the given index in the valsToList() result.


### `removeElement(key)`

Defined in lookup.h, line 38

Remove an entry from the table. Removes the key/value pair associated with the given key, and returns the value that was associated with the key. If the key isn't present in the table, the return value is nil, and the method has no other effect.


### `setDefaultValue(val)`

Defined in lookup.h, line 107

Set the default value. This changes the value returned by the index operator (self[key]) for a key that doesn't exist in the table. The default value is initially nil, but you can change this to a different value of any type if desired.


### `valsToList`

Defined in lookup.h, line 92

Make a list of all of my values. The return value is a list, in arbitrary order, of all of the values in the table.


## Inherited Methods


*From [Collection](collection.md):* [`createIterator`](collection.md#createIterator), [`createLiveIterator`](collection.md#createLiveIterator)


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
