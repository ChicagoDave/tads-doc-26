# ExternalEventList

ExternalEventList : [EventList](eventlist.md)

An "external" event list is one whose state is driven externally to the script. Specifically, the state is *not* advanced by invoking the script; the state is advanced exclusively by some external process (for example, by a daemon that invokes the event list's **advanceState()**method). In order words, each time you call the doScript() method of an ExternalEventList, the same event will fire (or the same string display), until you make an explicit call to advanceState().

A possible use for this would be for a list of strings/events where what happens/is displayed depends on some external event. Before that event occurs, you see the message/event relating to the earlier state of affairs; when the event occurs it can call the ExternalEventList's advanceState() method thereby causing the next event to be repeatedly fired, until another call to advanceState moves it on to the next, and so on.
