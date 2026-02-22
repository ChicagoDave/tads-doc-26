# FollowInfo

*class* — defined in [actor.t](../by-file/actor.t.md) (line 80)


FollowInfo - this is an object that tracks an actor's knowledge of the objects that the actor can follow, which are objects that actor has witnessed leaving the current location. We keep track of each followable object and the direction we saw it depart.


**Superclass chain:** `object` > **FollowInfo**


## Properties


### `connector`

Defined in actor.t, line 85

the TravelConnector the object traversed to leave


### `obj`

Defined in actor.t, line 82

the object we can follow


### `sourceLocation`

Defined in actor.t, line 93

The source location - this is the location we saw the object depart. We keep track of this because an actor can follow an object only if the actor is starting from the same location where the actor saw the object depart.
