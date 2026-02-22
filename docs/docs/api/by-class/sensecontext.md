# senseContext

*object* — defined in [pov.t](../by-file/pov.t.md) (line 66)


Sense context output filter. When the sense context doesn't allow the player character to sense whatever's going on, we'll block all output; otherwise, we'll pass output through unchanged.


**Superclass chain:** [SwitchableCaptureFilter](switchablecapturefilter.md) > [CaptureFilter](capturefilter.md) > [OutputFilter](outputfilter.md) > `object` > **senseContext**


## Properties


### `cached_`

Defined in pov.t, line 109


### `isBlocking_`

Defined in pov.t, line 108

our current cached blocking status, and its validity


### `sense_`

Defined in pov.t, line 179

the source object and sense of the sensory context


### `source_`

Defined in pov.t, line 180


## Inherited Properties


*From [SwitchableCaptureFilter](switchablecapturefilter.md):* [`isBlocking`](switchablecapturefilter.md#isBlocking)


## Methods


### `isBlocking`

Defined in pov.t, line 91

Get our current blocking status. If we've already cached the status, we'll return the cached status; otherwise, we'll compute and cache the new blocking status, based on the current sensory environment.


### `recalcSenseContext`

Defined in pov.t, line 75

Recalculate the current sense context. We will check to see if the player character can sense the current sense context's source object in the current sense context's sense, and show or hide output from this point forward accordingly. This can be called any time conditions change in such a way that the sense context should be refigured.


### `setSenseContext(source, sense)`

Defined in pov.t, line 168

Set a sense context.


### `shouldBlock`

Defined in pov.t, line 115

Calculate whether or not I should be blocking output according to the current game state. Returns true if so, nil if not.


### `withSenseContext(source, sense, func)`

Defined in pov.t, line 141

invoke a callback with a given sense context


## Inherited Methods


*From [SwitchableCaptureFilter](switchablecapturefilter.md):* [`filterText`](switchablecapturefilter.md#filterText)
