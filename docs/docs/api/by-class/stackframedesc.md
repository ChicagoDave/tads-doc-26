# StackFrameDesc

*class* — defined in [systype.h](../by-file/systype.h.md) (line 1248)


StackFrameDesc intrinsic class. This class provides access to a stack frame. It lets us retrieve the values of local variables and method context variables (self, definingobj, targetobj, targetprop). It also allows us to assign new values to local variables.


## Methods


### `getDefiningObj`

Defined in systype.h, line 1293

Get the value of 'definingobj' in this frame.


### `getInvokee`

Defined in systype.h, line 1308

Get the value of 'invokee' in this frame.


### `getSelf`

Defined in systype.h, line 1288

Get the value of 'self' in this frame.


### `getTargetObj`

Defined in systype.h, line 1298

Get the value of 'targetobj' in this frame.


### `getTargetProp`

Defined in systype.h, line 1303

Get the value of 'targetprop' in this frame.


### `getVars`

Defined in systype.h, line 1283

Get a LookupTable consisting of all of the variables (local variables and parameters) in the frame. Each element in the table is keyed by the name of a variable, and contains the current value of the variable.


### `isActive`

Defined in systype.h, line 1264

Is the stack frame active? A stack frame is active until the function or method it represents returns to its caller. When the routine returns, the frame becomes inactive.
