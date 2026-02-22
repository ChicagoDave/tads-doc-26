# ImpByeTopic

ImpByeTopic : [MiscTopic](misctopic.md)

An ImpByeTopic is yet another kind of [TopicEntry](topicentry.md) used in [greeting protocols](greetingprotocols.md). Like [ByeTopic](byetopic.md), it is used at the end of a conversation, and would normally be placed in a [ConversationReadyState](conversationreadystate.md). Unlike ByeTopic, it handles only implicit conversation endings, which occur either when the player character simply leaves the area in mid-conversation, or else fails to address a conversational command to the NPC for enough turns to exhaust the NPC's attention span.

For example, we might define the following ImpByeTopic for the curator, which should be located in his curatorWatching  ConversationReadyState:

```tads3
+++ ImpByeTopic
  "{The curator/he} turns away and goes back to what
   passes for his work. "
;
```

Note that this doesn't distinguish between the cases where the conversation ends because the PC walks away from the curator and where it ends because the curator becomes bored waiting for us to speak. If we want to make that distinction, we can use [LeaveByeTopic](leavebyetopic.md) and [BoredByeTopic](boredbyetopic.md).
