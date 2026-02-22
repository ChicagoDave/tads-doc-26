# _multiMethodNonObjectBindings

*object* — defined in [multmeth.t](../by-file/multmeth.t.md) (line 464)


A placeholder object for bindings for non-object arguments. Whenever we have an actual argument value that's not an object, we'll look here for bindings for that parameter. When registering a function, we'll register a binding here for any parameter that doesn't have a type specification.


**Superclass chain:** [_MultiMethodPlaceholder](_multimethodplaceholder.md) > `object` > **_multiMethodNonObjectBindings**
