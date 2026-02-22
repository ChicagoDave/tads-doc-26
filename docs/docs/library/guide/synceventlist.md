# SyncEventList

SyncEventList : [EventList](eventlist.md)

A synchronized event list is an event list that takes its actions from a separate event list object. It gets its current state from the other list, and advancing our state advances the other list's state in lock step. Set '**masterObject**' to refer to the master list whose state we synchronize with.

This can be useful, for example, when you have messages that reflect two different points of view on the same events: the messages for each point of view can be kept in a separate list, but the one list can be a slave of the other to ensure that the two lists are based on a common state.
