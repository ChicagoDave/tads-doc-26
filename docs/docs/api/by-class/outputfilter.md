# OutputFilter

*class* — defined in [output.t](../by-file/output.t.md) (line 645)


Output Filter


**Superclass chain:** `object` > **OutputFilterSubclasses:** [CaptureFilter](capturefilter.md), [StringCaptureFilter](stringcapturefilter.md), [SwitchableCaptureFilter](switchablecapturefilter.md), [CommandTranscript](commandtranscript.md), [MessageBuilder](messagebuilder.md), [MonitorFilter](monitorfilter.md), [ParagraphManager](paragraphmanager.md)


**Global objects:** [commandSequencer](commandsequencer.md), [conversationManager](conversationmanager.md), [styleTagFilter](styletagfilter.md), [typographicalOutputFilter](typographicaloutputfilter.md)


## Methods


### `filterText(ostr, txt)`

Defined in output.t, line 653

Apply the filter - this should be overridden in each filter. The return value is the result of filtering the string.
