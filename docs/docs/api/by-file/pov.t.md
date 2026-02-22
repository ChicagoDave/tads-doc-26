# pov.t


## Global Objects

- [senseContext](../by-class/sensecontext.md)
- callFromPOV
- callWithSenseContext
- clearPOV
- getPOV
- getPOVActor
- getPOVActorDefault
- getPOVDefault
- popPOV
- pushPOV
- setPOV
- setRootPOV


## Functions


### `callFromPOV(actor, pov, funcToCall, [args])`

Defined in pov.t, line 328

Call a function from a point of view. We'll set the new point of view, call the function with the given arguments, then restore the original point of view.


### `callWithSenseContext(source, sense, func)`

Defined in pov.t, line 56

Call a function with a given sensory context.


### `clearPOV`

Defined in pov.t, line 310

Clear the point of view and all stacked elements


### `getPOV`

Defined in pov.t, line 205

Get the current point of view. In *most* cases, this is the same as the point-of-view actor: the actor is looking around with its own eyes, so it's the point of view. However, this can differ from the actor when the actor is viewing the location being described through an intermediary of some kind. For example, if an actor is observing a remote room through a closed-circuit TV system, the point of view would be the camera in the remote room (not the TV - the point of view is intended to be the object that's physically absorbing the light rays or other sensory equivalents).


### `getPOVActor`

Defined in pov.t, line 189

Get the current point-of-view actor - this is the actor who's performing the action (LOOK AROUND, EXAMINE, SMELL, etc) that's generating the current description.


### `getPOVActorDefault(dflt)`

Defined in pov.t, line 211

get the POV actor, returning the given default if there isn't one set


### `getPOVDefault(dflt)`

Defined in pov.t, line 221

get the POV, returning the given default if there isn't one set


### `popPOV`

Defined in pov.t, line 283

Pop the most recent point of view pushed


### `pushPOV(actor, pov)`

Defined in pov.t, line 270

Push the current point of view


### `setPOV(actor, pov)`

Defined in pov.t, line 233

Change the point of view without altering the point-of-view stack


### `setRootPOV(actor, pov)`

Defined in pov.t, line 245

Set the root point of view. This doesn't affect the current point of view unless there is no current point of view; this merely sets the outermost default point of view.
