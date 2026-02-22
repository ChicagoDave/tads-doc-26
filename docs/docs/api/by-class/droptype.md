# DropType

*class* — defined in [thing.t](../by-file/thing.t.md) (line 270)


Drop Descriptor. This is passed to the receiveDrop() method of a "drop destination" when an object is discarded via commands such as DROP or THROW. The purpose of the descriptor is to identify the type of command being performed, so that the receiveDrop() method can generate an appropriate report message.


**Superclass chain:** `object` > **DropTypeSubclasses:** [DropTypeThrow](droptypethrow.md), [DropTypeShortThrow](droptypeshortthrow.md)


**Global objects:** [dropTypeDrop](droptypedrop.md)


## Methods


### `// getReportPrefix (obj, dest)`

Defined in thing.t, line 299

Get a short report describing the action without saying where the object ended up. This is roughly the same as the standard report, but omits any information on where the object lands, so that the caller can show a separate message explaining that part.


### `// standardReport (obj, dest)`

Defined in thing.t, line 279

Generate the standard report message for the action. The drop destination's receiveDrop() method can call this if the standard message is adequate to describe the result of the action.
