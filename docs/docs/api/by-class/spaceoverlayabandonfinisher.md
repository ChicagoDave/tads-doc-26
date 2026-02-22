# SpaceOverlayAbandonFinisher

*class* — defined in [extras.t](../by-file/extras.t.md) (line 784)


Space Overlay Abandon Finisher - this is an internal object that we create in SpaceOverlay.abandonContents(). Its purpose is to receive an afterAction notification and clean up the report order if necessary.


**Superclass chain:** `object` > **SpaceOverlayAbandonFinisher**


## Properties


### `marker1`

Defined in extras.t, line 799

the transcript markers identifying the listing reports


### `marker2`

Defined in extras.t, line 800


### `origLocation`

Defined in extras.t, line 803

the actor's location at the time we generated the listing


## Methods


### `afterAction`

Defined in extras.t, line 806

receive our after-action notification


### `construct(m1, m2)`

Defined in extras.t, line 785
