# PermanentAttachment

*class* — defined in [extras.t](../by-file/extras.t.md) (line 3574)


Permanent attachments. This class is for things that are described in the story text as attached to one another, but which can never be separated. This is a mix-in class that can be combined with a Thing subclass.


**Superclass chain:** [Attachable](attachable.md) > `object` > **PermanentAttachmentSubclasses:** [PermanentAttachmentChild](permanentattachmentchild.md)


## Properties


### `baseCannotDetachMsg`

Defined in extras.t, line 3598

basic message to use when we try to detach something from self


## Inherited Properties


*From [Attachable](attachable.md):* [`attachedObjects`](attachable.md#attachedObjects), [`attachmentLister`](attachable.md#attachmentLister), [`majorAttachmentLister`](attachable.md#majorAttachmentLister)


## Methods


### `cannotDetachMsgFor(obj)` *(overridden)*

Defined in extras.t, line 3587

Get the message explaining why we can't detach from 'obj'.


## Inherited Methods


<details><summary>From [Attachable](attachable.md) (28)</summary>

[`attachTo`](attachable.md#attachTo), [`beforeTravel`](attachable.md#beforeTravel), [`canAttachTo`](attachable.md#canAttachTo), [`canDetachFrom`](attachable.md#canDetachFrom), [`detachFrom`](attachable.md#detachFrom), [`dobjFor(AttachTo)`](attachable.md#dobjFor(AttachTo)), [`dobjFor(Detach)`](attachable.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](attachable.md#dobjFor(DetachFrom)), [`dobjFor(TakeFrom)`](attachable.md#dobjFor(TakeFrom)), [`examineStatus`](attachable.md#examineStatus), [`explainCannotAttachTo`](attachable.md#explainCannotAttachTo), [`getNonPermanentAttachments`](attachable.md#getNonPermanentAttachments), [`handleAttach`](attachable.md#handleAttach), [`handleDetach`](attachable.md#handleDetach), [`initializeThing`](attachable.md#initializeThing), [`iobjFor(AttachTo)`](attachable.md#iobjFor(AttachTo)), [`iobjFor(DetachFrom)`](attachable.md#iobjFor(DetachFrom)), [`iobjFor(TakeFrom)`](attachable.md#iobjFor(TakeFrom)), [`isAttachedTo`](attachable.md#isAttachedTo), [`isListedAsAttachedTo`](attachable.md#isListedAsAttachedTo), [`isListedAsMajorFor`](attachable.md#isListedAsMajorFor), [`isMajorItemFor`](attachable.md#isMajorItemFor), [`isPermanentlyAttachedTo`](attachable.md#isPermanentlyAttachedTo), [`mainMoveInto`](attachable.md#mainMoveInto), [`maybeHandleAttach`](attachable.md#maybeHandleAttach), [`maybeHandleDetach`](attachable.md#maybeHandleDetach), [`moveWhileAttached`](attachable.md#moveWhileAttached), [`travelWhileAttached`](attachable.md#travelWhileAttached)

</details>
