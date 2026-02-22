# TranscriptTransform

*class* — defined in [report.t](../by-file/report.t.md) (line 1249)


Transcript Transform.


**Superclass chain:** `object` > **TranscriptTransformGlobal objects:** [complexMultiTransform](complexmultitransform.md), [defaultReportTransform](defaultreporttransform.md), [implicitGroupTransform](implicitgrouptransform.md), [reportOrderTransform](reportordertransform.md)


## Methods


### `applyTransform(trans, vec)`

Defined in report.t, line 1255

Apply our transform to the transcript vector. By default, we do nothing; each subclass must override this to manipulate the vector to make the change it wants to make.
