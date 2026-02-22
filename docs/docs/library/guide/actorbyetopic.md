# ActorByeTopic

ActorByeTopic: [MiscTopic](misctopic.md)

ActorByeTopic is the third specialization of [ImpByeTopic](impbyetopic.md). It is used when the NPC terminates the conversation of its own accord via npc.endConversation(). In the absence of an active ActorByeTopic, the active ImpByeTopic will be used instead.

npc.endConversation() is used to make an NPC break off a current conversation. This is the complement to initiateConversation; it causes the NPC to effectively say BYE on its own, rather than waiting for the PC to decide to end the conversation. This call is mostly useful when the actor's current state is an [InConversationState](inconversationstate.md), since the main function of this routine is to switch to an out-of-conversation state.

For example, if our curator was particularly cantankerous, we might, for example, tweak one or more of his TopicEntries to call endConversation():

```tads3
+++ AltTopic
   "<q>Do I need another ticket if I want to come in again?</q>
    you ask.\b
    <q>No,</q> he assures you, <q>the ticket you showed me is
     good for multiple entry.</q> <<getActor().endConversation()>> "
   isActive = gRevealed('ticket-shown')
;
```

And then add the following in his ConversationReadyState:

+++ ActorByeTopic

   "<q>Now, if that's all, I have work to do,</q> he adds, turning back to the

    pile of papers on his desk. "

;
