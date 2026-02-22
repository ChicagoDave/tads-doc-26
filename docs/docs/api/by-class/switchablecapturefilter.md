# SwitchableCaptureFilter

*class* — defined in [output.t](../by-file/output.t.md) (line 708)


"Switchable" capture filter. This filter can have its blocking enabled or disabled. When blocking is enabled, we capture everything, leaving nothing to the underlying stream; when disabled, we pass everything through to the underyling stream unchanged.


**Superclass chain:** [CaptureFilter](capturefilter.md) > [OutputFilter](outputfilter.md) > `object` > **SwitchableCaptureFilterGlobal objects:** [senseContext](sensecontext.md)


## Properties


### `isBlocking`

Defined in output.t, line 724

Blocking enabled: if this is true, we'll capture all text passed through us, leaving nothing to the underyling stream. Blocking is enabled by default.


## Methods


### `filterText(ostr, txt)` *(overridden)*

Defined in output.t, line 710

filter the text
