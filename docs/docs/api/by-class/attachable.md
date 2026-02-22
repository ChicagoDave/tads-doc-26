# Attachable

*class* — defined in [extras.t](../by-file/extras.t.md) (line 2533)


An Attachable is an object that can be attached to another, using an ATTACH X TO Y command. This is a mix-in class that is meant to be combined with a Thing-derived class to create an attachable object.


**Superclass chain:** `object` > **AttachableSubclasses:** [NearbyAttachable](nearbyattachable.md), [PermanentAttachment](permanentattachment.md), [PermanentAttachmentChild](permanentattachmentchild.md)


## Properties


### `attachedObjects`

Defined in extras.t, line 2540

The list of objects I'm currently attached to. Note that each of the objects in this list must usually be an Attachable, and we must be included in the attachedObjects list in each of these objects.


### `attachmentLister`

Defined in extras.t, line 2849

the Lister we use to show our list of attached objects


### `majorAttachmentLister`

Defined in extras.t, line 2856

the Lister we use to list the items attached to us (i.e., the items for which we're the "major" item in the attachment relationship)


## Methods


### `attachTo(obj)`

Defined in extras.t, line 2548

Perform programmatic attachment, without any notifications. This simply updates my attachedObjects list and the other object's list to indicate that we're attached to the other object (and vice versa).


### `beforeTravel(traveler, connector)`

Defined in extras.t, line 2903

Receive notification of travel. If I'm involved in the travel, and I'm attached to anything, we'll notify ourself and our attachments.


### `canAttachTo(obj)`

Defined in extras.t, line 2660

Can I attach to the given object? This returns true if the other object is allowable as an attachment, nil if not.


### `canDetachFrom(obj)`

Defined in extras.t, line 2710

Is it possible for me to detach from the given object? This asks whether a given attachment relationship can be dissolved with DETACH FROM.


### `cannotDetachMsgFor(obj)`

Defined in extras.t, line 2748

A message explaining why we can't detach from the given object. Note that 'obj' can be nil, because we could be attempting a DETACH command with no indirect object.


### `detachFrom(obj)`

Defined in extras.t, line 2555

perform programmatic detachment, without any notifications


### `dobjFor(AttachTo)`

Defined in extras.t, line 2946

handle attachment on the direct object side


### `dobjFor(Detach)`

Defined in extras.t, line 3062

handle simple, unspecified detachment (DETACH OBJECT)


### `dobjFor(DetachFrom)`

Defined in extras.t, line 3108

handle detaching me from a specific other object


### `dobjFor(TakeFrom)`

Defined in extras.t, line 3200

TAKE X FROM Y is the same as DETACH X FROM Y for things we're attached to, but use the inherited handling otherwise


### `examineStatus`

Defined in extras.t, line 2859

add a list of our attachments to the desription


### `explainCannotAttachTo(obj)`

Defined in extras.t, line 2696

Explain why we can't attach to the given object. This should simply display an appropriate mesage. We use reportFailure to flag it as a failure report, but that's not actually required, since we call this from our 'check' routine, which will mark the action as having failed even if we don't here.


### `getNonPermanentAttachments`

Defined in extras.t, line 2562

get the subset of my attachments that are non-permanent


### `handleAttach(other)`

Defined in extras.t, line 2790

Process attachment to a new object. This routine is called on BOTH the direct and indirect object during the attachment process - that is, it's called on the direct object with the indirect object as the argument, and then it's called on the indirect object with the direct object as the argument.


### `handleDetach(other)`

Defined in extras.t, line 2843

Handle detachment. This works like handleAttach(), in that this routine is invoked symmetrically for both sides of a DETACH X FROM Y commands.


### `initializeThing`

Defined in extras.t, line 2925

during initialization, make sure the attachedObjects list is symmetrical for both sides of the attachment relationship


### `iobjFor(AttachTo)`

Defined in extras.t, line 2990

handle attachment on the indirect object side


### `iobjFor(DetachFrom)`

Defined in extras.t, line 3139

handle detachment on the indirect object side


### `iobjFor(TakeFrom)`

Defined in extras.t, line 3230

if we're attached, change this into a DETACH FROM action; otherwise, use the inherited TAKE FROM handling


### `isAttachedTo(obj)`

Defined in extras.t, line 2569

am I attached to the given object?


### `isListedAsAttachedTo(obj)`

Defined in extras.t, line 2611

Am I *listed* as attached to the given object? If this is true, then our examineStatus() will list 'obj' among the things I'm attached to: "Self is attached to obj." If this is nil, I'm not listed as attached.


### `isListedAsMajorFor(obj)`

Defined in extras.t, line 2638

Is 'obj' listed as attached to me when I'm described? If this is true, then our examineStatus() will list 'obj' among the things attached to me: "Attached to self is obj." If this is nil, then 'obj' is not listed among the things attached to me when I'm described.


### `isMajorItemFor(obj)`

Defined in extras.t, line 2591

Am I the "major" item in my attachment relationship to the given object? This affects how our relationship is described in our status message: in an asymmetrical relationship, where one object is the "major" item, we will always describe the minor item as being attached to the major item rather than vice versa. This allows you to ensure that the message is always "the sign is attached to the wall", and never "the wall is attached to the sign": the wall is the major item in this relationship, so it's always the sign that's attached to it.


### `isPermanentlyAttachedTo(obj)`

Defined in extras.t, line 2733

Am I permanently attached to the other object? This returns true if I'm a PermanentAttachment or the other object is.


### `mainMoveInto(newCont)`

Defined in extras.t, line 2882

Move into a new container. If I'm attached to anything, we'll notify ourself and our attachments.


### `maybeHandleAttach(other)`

Defined in extras.t, line 3047

Fire the handleAttach event - we'll notify both sides as soon as both sides are hooked up with each other. This ensures that both lists are updated before we notify either side, so the ordering doesn't depend on whether we handle the dobj or iobj first.


### `maybeHandleDetach(other)`

Defined in extras.t, line 3182

Fire the handleDetach event - we'll notify both sides as soon as both sides are un-hooked up. This ensures that both lists are updated before we notify either side, so the ordering doesn't depend on whether we handle the dobj or iobj first.


### `moveWhileAttached(movedObj, newCont)`

Defined in extras.t, line 2809

Receive notification that this object or one of its attachments is being moved to a new container. When an attached object is moved, we'll call this on the object being moved AND on every object attached to it. 'movedObj' is the object being moved, and 'newCont' is the new container it's being moved into.


### `travelWhileAttached(movedObj, traveler, connector)`

Defined in extras.t, line 2826

Receive notification that this object or one of its attachments is being moved in the course of an actor traveling to a new location. Whenever anyone travels while carrying an attachable object (directly or indirectly), we'll call this on the object being moved AND on every object attached to it. 'movedObj' is the object being carried by the traveling actor, 'traveler' is the Traveler performing the travel, and 'connector' is the TravelConnector that the traveler is traversing.
