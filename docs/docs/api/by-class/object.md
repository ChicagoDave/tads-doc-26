# Object

*class* — defined in [systype.h](../by-file/systype.h.md) (line 38)


The root object class. All objects descend from this class.


<details><summary>Subclasses (20)</summary>

- [BigNumber](bignumber.md)
- [ByteArray](bytearray.md)
- [CharacterSet](characterset.md)
- [Collection](collection.md)
- [List](list.md)
- [LookupTable](lookuptable.md)
- [WeakRefLookupTable](weakreflookuptable.md)
- [Vector](vector.md)
- [AnonFuncPtr](anonfuncptr.md)
- [Dictionary](dictionary.md)
- [File](file.md)
- [GrammarProd](grammarprod.md)
- [IntrinsicClass](intrinsicclass.md)
- [Iterator](iterator.md)
- [IndexedIterator](indexediterator.md)
- [LookupTableIterator](lookuptableiterator.md)
- [RexPattern](rexpattern.md)
- [String](string.md)
- [StringComparator](stringcomparator.md)
- [TadsObject](tadsobject.md)

</details>


## Methods


### `getPropList`

Defined in systype.h, line 61

Get a list of my directly-defined properties. When called on intrinsic class objects, this returns a list of properties defined for instances of the class, as well as static properties of the class.


### `getPropParams(prop)`

Defined in systype.h, line 71

get parameter list information for the given method - returns a list: [minimumArgc, optionalArgc, varargs], where minimumArgc is the minimum number of arguments, optionalArgc is the number of additional optional arguments, and varargs is true if the function takes a varying number of arguments greater than or equal to the minimum, nil if not.


### `getSuperclassList`

Defined in systype.h, line 47

get the list of direct superclasses of this object


### `isClass`

Defined in systype.h, line 77

determine if I'm a "class" object - returns true if the object was defined with the "class" keyword, nil otherwise


### `isTransient`

Defined in systype.h, line 88

determine if this instance is transient


### `ofKind(cls)`

Defined in systype.h, line 44

Determine if I'm an instance or subclass of the given class 'cls'. Note that x.ofKind(x) returns true - an object is of its own kind.


### `propDefined(prop, flags, ?)`

Defined in systype.h, line 50

determine if a property is defined or inherited by this object


### `propInherited(prop, origTargetObj, definingObj, flags, ?)`

Defined in systype.h, line 85

Determine if a property is inherited further from the given object. definingObj is usually the value of the 'definingobj' pseudo-variable, and origTargetObj is usually the value of the 'targetobj' pseudo-variable.


### `propType(prop)`

Defined in systype.h, line 53

get the type of a property defined for this object


### `valToSymbol`

Defined in reflect.t, line 182
