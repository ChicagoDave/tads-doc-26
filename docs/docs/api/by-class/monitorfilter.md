# MonitorFilter

*class* — defined in [output.t](../by-file/output.t.md) (line 663)


Output monitor filter. This is a filter that leaves the filtered text unchanged, but keeps track of whether any text was seen at all. Our 'outputFlag' is true if we've seen any output, nil if not.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **MonitorFilter**


## Properties


### `outputFlag`

Defined in output.t, line 676

flag: has any output occurred for this monitor yet?


## Methods


### `filterText(ostr, val)` *(overridden)*

Defined in output.t, line 665

filter text
