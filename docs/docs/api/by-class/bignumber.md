# BigNumber

*class* — defined in [bignum.h](../by-file/bignum.h.md) (line 39)


The BigNumber intrinsic class lets you perform floating-point and integer arithmetic with (almost) any desired precision. BigNumber uses a decimal representation, which means that decimal values can be represented exactly (i.e., with no rounding errors, as can happen with IEEE 'double' and 'float' values that languages like C typically support). BigNumber combines a varying-length mantissa with an exponent; the length of the mantissa determines how many digits of precision a given BigNumber can store, and the exponent lets you represent very large or very small values with minimal storage. You can specify the desired precision when you create a BigNumber explicitly; when BigNumber values are created implicitly by computations, the system chooses a precision based on the inputs to the calculations, typically equal to the largest of the precisions of the input values.


**Superclass chain:** [Object](object.md) > **BigNumber**


## Methods


### `valToSymbol` *(overridden)*

Defined in reflect.t, line 357


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType)
