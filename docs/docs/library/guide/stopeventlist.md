# StopEventList

StopEventList : [EventList](eventlist.md)

A StopEventList is just like an [EventList](eventlist.md), except that when the last item in the list is reached, it is then repeated indefinitely.

This is probably most useful in providing sequential responses in NPC conversations (which we'll be coming to in due course). For example, if you repeatedly ASK SARAH ABOUT HERSELF, you'd expect her not to give the same answer each time. Since, however, you cannot actually provide her with an infinite number of responses, you could use a StopEventList to provide, say, two or three different ones which progressively reveal more information, and a final one (to be then repeated indefinitely), which indicates that this particular topic has now been exhausted, while perhaps reminding the player of the essentials of what's been said.

We'll be meeting plenty of examples of this in connection with the conversation system, for example in conjunction with [GiveShowTopic](giveshowtopic.md), [AskTopic](asktopic.md), [TellTopic](telltopic.md), and [AskTellTopic](asktelltopic.md).
