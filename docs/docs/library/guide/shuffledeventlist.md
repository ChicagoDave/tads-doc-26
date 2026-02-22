# ShuffledEventList

ShuffledEventList : [RandomFiringScript](randomfiringscript.md), [EventList](eventlist.md)

The Shuffled event list is just like a random event list, except that it fires its events in a "shuffled" order rather than an independently random order. "Shuffled order" means that events are fired in random order; once an event is fired it is not fired again until all of the other events have been fired. The effect is similar to dealing from a pack (UK) / deck (USA) of cards.

For the first time through the main list, the strings are normally shuffled immediately at startup, but this is optional. If **shuffleFirst**is set to nil, the events will *not* be shuffled the first time through;  they'll be run through once in the order listed, then shuffled for the next time through, then shuffled again for the next, and so on. So, if you want a specific order for the first time through, just define the list in the desired order and set shuffleFirst to nil.

You can optionally specify a separate list of one-time-only sequential strings in the property **firstEvents**. This list of events will be run through once, much like a standard [EventList](eventlist.md). Once they've been exhausted, the ShuffledEventList will switch to the main eventList list, showing it one time through in its given order, then shuffling it and running through it again, and so on. The firstEvents list is never shuffled - it's always shown in exactly the order given. This combination of a list in a fixed order followed by a list which gets shuffled is particularly useful in connexion with [TopicEntries](topicentry.md), when you want an NPC to give a specific sequence of responses (probably conveying relatively important information), followed by a series of randomly-ordered responses (perhaps indicating that the NPC has nothing further to say on the subject).

We saw an example of a ShuffledEventList right at the start in the definition of our first [OutdoorRoom](outdoorroom.md), where we used one for the atmosphere list. We'll also be encountering examples in connection with [AskTopic](asktopic.md), [AskForAboutTopic](askaboutfortopic.md), [DefaultAskTopic](defaultasktopic.md), [DefaultTellTopic](defaulttelltopic.md), [DefaultAskTellTopic](defaultasktelltopic.md), and most of the other DefaultTopics.

The ShuffledEventList has its own [template](shuffledeventlisttemplate.md) to allow easy definition of its firstEvents and eventList properties.

Since ShuffledEventList inherits from [RandomFiringScript](randomfiringscript.md), it can also use the same eventPercent, eventReduceTo, and eventReduceAfter properties that were described on [RandomEventList](randomeventlist.md).
