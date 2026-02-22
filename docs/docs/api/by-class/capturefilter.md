# CaptureFilter

*class* — defined in [output.t](../by-file/output.t.md) (line 690)


Capture Filter. This is an output filter that simply captures all of the text sent through the filter, sending nothing out to the underlying stream.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **CaptureFilterSubclasses:** [StringCaptureFilter](stringcapturefilter.md), [SwitchableCaptureFilter](switchablecapturefilter.md)


## Methods


### `filterText(ostr, txt)` *(overridden)*

Defined in output.t, line 695

Filter the text. We simply discard the text, passing nothing through to the underlying stream.
