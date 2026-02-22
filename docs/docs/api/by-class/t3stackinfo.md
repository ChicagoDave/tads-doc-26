# T3StackInfo

*class* — defined in [_main.t](../by-file/_main.t.md) (line 1003)


The stack information object. The intrinsic function t3GetStackTrace() in the 't3vm' function set returns a list of these objects; each object represents a level in the stack trace.


**Superclass chain:** `object` > **T3StackInfo**


## Properties


### `argList_`

Defined in _main.t, line 1072

The list of positional arguments to the function or method. Each element is the value of an argument; the list is arranged in the same order as the arguments.


### `frameDesc_`

Defined in _main.t, line 1122

A StackFrameDesc object that can be used to get information from the frame and change local variables in the frame.


### `func_`

Defined in _main.t, line 1049

the function running at this stack level - this is nil if an object property is running instead of a function


### `locals_`

Defined in _main.t, line 1085

Local variables. This is a LookupTable containing the local variables currently in scope at this stack level. Each element in the table has a string key (index) giving the name of the local variable, and each corresponding value is the local's current value. The table is only included when the stack listing was produced by a call to t3GetStackTrace() with the T3GetStackLocals flag set; otherwise it's nil. If the locals were requested, and the stack level has no local variables, this will be an empty lookup table.


### `namedArgs_`

Defined in _main.t, line 1094

Named arguments. This is a LookupTable containing the named arguments passed in from this stack level. Each element in the table has a string key (index) giving the name of the argument, and each corresponding value is the value of that argument. If there are no named arguments, this value is nil.


### `obj_`

Defined in _main.t, line 1058

The object and property running at this stack level - these are nil if a function is running instead of an object method. The object is the object where the method is actually defined - this might not be the same as self, because the object might have inherited the method from a base class.


### `prop_`

Defined in _main.t, line 1059


### `self_`

Defined in _main.t, line 1065

the 'self' object at this level - this is nil if a function is running at this level instead of an object method


### `srcInfo_`

Defined in _main.t, line 1116

The source location of the next code to be executed in the function or method in this frame. If source-level debugging information is available for the current execution point in this frame, this will contain a list of two values:


## Methods


### `construct(func, obj, prop, selfObj, argList, srcInfo, locals, namedArgs, frameDesc)`

Defined in _main.t, line 1008

Construct a stack level object. The system invokes this constructor with information on the stack level.


### `isSystem`

Defined in _main.t, line 1027

Is this a system routine? This returns true if an intrinsic function or an intrinsic class method is running at this level.
