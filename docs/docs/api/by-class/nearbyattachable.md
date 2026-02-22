# NearbyAttachable

*class* — defined in [extras.t](../by-file/extras.t.md) (line 3311)


A "nearby" attachable is a subclass of Attachable that adds a requirement that the attached objects be in a given location. By default, we simply require that they have a common immediate container, but this can be overridden so that each object's location is negotiated separately. This is a simple and effective pattern that avoids many of the potential anomalies with attachment (see the Attachable comments for examples).


**Superclass chain:** [Attachable](attachable.md) > `object` > **NearbyAttachable**


## Inherited Properties


*From [Attachable](attachable.md):* [`attachedObjects`](attachable.md#attachedObjects), [`attachmentLister`](attachable.md#attachmentLister), [`majorAttachmentLister`](attachable.md#majorAttachmentLister)


## Methods


### `dobjFor(AttachTo)` *(overridden)*

Defined in extras.t, line 3312


### `getNearbyAttachmentLocs(other)`

Defined in extras.t, line 3347

Get the target locations for attaching to the given other object. The "target locations" are the locations where the objects are required to be in order to carry out the ATTACH command to attach this object to the other object (or vice versa).


### `iobjFor(AttachTo)` *(overridden)*

Defined in extras.t, line 3317

require that the objects be in the negotiated locations


### `moveWhileAttached(movedObj, newCont)` *(overridden)*

Defined in extras.t, line 3373

when an attached object is being moved, detach the objects


### `nestedDetachFrom(obj)`

Defined in extras.t, line 3404

perform a nested DetachFrom action on the given object


## Inherited Methods


<details><summary>From [Attachable](attachable.md) (26)</summary>

[`attachTo`](attachable.md#attachTo), [`beforeTravel`](attachable.md#beforeTravel), [`canAttachTo`](attachable.md#canAttachTo), [`canDetachFrom`](attachable.md#canDetachFrom), [`cannotDetachMsgFor`](attachable.md#cannotDetachMsgFor), [`detachFrom`](attachable.md#detachFrom), [`dobjFor(Detach)`](attachable.md#dobjFor(Detach)), [`dobjFor(DetachFrom)`](attachable.md#dobjFor(DetachFrom)), [`dobjFor(TakeFrom)`](attachable.md#dobjFor(TakeFrom)), [`examineStatus`](attachable.md#examineStatus), [`explainCannotAttachTo`](attachable.md#explainCannotAttachTo), [`getNonPermanentAttachments`](attachable.md#getNonPermanentAttachments), [`handleAttach`](attachable.md#handleAttach), [`handleDetach`](attachable.md#handleDetach), [`initializeThing`](attachable.md#initializeThing), [`iobjFor(DetachFrom)`](attachable.md#iobjFor(DetachFrom)), [`iobjFor(TakeFrom)`](attachable.md#iobjFor(TakeFrom)), [`isAttachedTo`](attachable.md#isAttachedTo), [`isListedAsAttachedTo`](attachable.md#isListedAsAttachedTo), [`isListedAsMajorFor`](attachable.md#isListedAsMajorFor), [`isMajorItemFor`](attachable.md#isMajorItemFor), [`isPermanentlyAttachedTo`](attachable.md#isPermanentlyAttachedTo), [`mainMoveInto`](attachable.md#mainMoveInto), [`maybeHandleAttach`](attachable.md#maybeHandleAttach), [`maybeHandleDetach`](attachable.md#maybeHandleDetach), [`travelWhileAttached`](attachable.md#travelWhileAttached)

</details>
