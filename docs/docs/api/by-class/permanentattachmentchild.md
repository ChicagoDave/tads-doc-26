# PermanentAttachmentChild

*class* — defined in [extras.t](../by-file/extras.t.md) (line 3607)


A permanent attachment "child" - this is an attachment that's explicitly attached to its container object. This is a convenient way of setting up an attachment relationship between container and contents when the contents object isn't a Component.


**Superclass chain:** [PermanentAttachment](permanentattachment.md) > [Attachable](attachable.md) > `object` > **PermanentAttachmentChild**


## Properties


### `attachedObjects` *(overridden)*

Defined in extras.t, line 3609

we're attached directly to our container


## Inherited Properties


*From [PermanentAttachment](permanentattachment.md):* [`baseCannotDetachMsg`](permanentattachment.md#baseCannotDetachMsg)


*From [Attachable](attachable.md):* [`attachmentLister`](attachable.md#attachmentLister), [`majorAttachmentLister`](attachable.md#majorAttachmentLister)


## Inherited Methods


*From [PermanentAttachment](permanentattachment.md):* [`cannotDetachMsgFor`](permanentattachment.md#cannotDetachMsgFor)


<details><summary>From [Attachable](attachable.md) (28)</summary>

[`attachTo`](attachable.md#attachTo), [`beforeTravel`](attachable.md#beforeTravel), [`canAttachTo`](attachable.md#canAttachTo), [`canDetachFrom`](attachable.md#canDetachFrom), [`detachFrom`](attachable.md#detachFrom), [`dobjFor(AttachTo)`](attachable.md#dobjFor(AttachTo)), [`dobjFor(Detach)`](attachable.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](attachable.md#dobjFor(DetachFrom)), [`dobjFor(TakeFrom)`](attachable.md#dobjFor(TakeFrom)), [`examineStatus`](attachable.md#examineStatus), [`explainCannotAttachTo`](attachable.md#explainCannotAttachTo), [`getNonPermanentAttachments`](attachable.md#getNonPermanentAttachments), [`handleAttach`](attachable.md#handleAttach), [`handleDetach`](attachable.md#handleDetach), [`initializeThing`](attachable.md#initializeThing), [`iobjFor(AttachTo)`](attachable.md#iobjFor(AttachTo)), [`iobjFor(DetachFrom)`](attachable.md#iobjFor(DetachFrom)), [`iobjFor(TakeFrom)`](attachable.md#iobjFor(TakeFrom)), [`isAttachedTo`](attachable.md#isAttachedTo), [`isListedAsAttachedTo`](attachable.md#isListedAsAttachedTo), [`isListedAsMajorFor`](attachable.md#isListedAsMajorFor), [`isMajorItemFor`](attachable.md#isMajorItemFor), [`isPermanentlyAttachedTo`](attachable.md#isPermanentlyAttachedTo), [`mainMoveInto`](attachable.md#mainMoveInto), [`maybeHandleAttach`](attachable.md#maybeHandleAttach), [`maybeHandleDetach`](attachable.md#maybeHandleDetach), [`moveWhileAttached`](attachable.md#moveWhileAttached), [`travelWhileAttached`](attachable.md#travelWhileAttached)

</details>
