# implicitAnnouncementGrouper

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 5465)


Implied action announcement grouper. This takes a list of ImplicitActionAnnouncement reports and returns a single message string describing the entire list of actions.


**Superclass chain:** `object` > **implicitAnnouncementGrouper**


## Properties


### `keepAllFailures`

Defined in msg_neu.t, line 5487

Configuration option: keep all failures in a list of implied announcements. If this is true, then we'll write things like "trying to unlock the door and then open it"; if nil, we'll instead write simply "trying to unlock the door".


## Methods


### `compositeMessage(lst)`

Defined in msg_neu.t, line 5490

build the composite message
