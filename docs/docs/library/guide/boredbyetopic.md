# BoredByeTopic

BoredByeTopic: [MiscTopic](misctopic.md)

The BoredByeTopic is the second special case of [ImpByeTopic](impbyetopic.md), and complements [LeaveByeTopic](leavebyetopic.md). It is triggered whenever a conversation is terminated because an NPC gives up waiting for the PC to speak.

We could, for example, change the curator's ImpByeTopic to a BoredByeTopic:

```tads3
+++ BoredByeTopic
  "{The curator/he} turns away and goes back to what
   passes for his work. "
;
```

In this case the change won't make any practical difference, since either way (given that we've defined a separate LeaveByTopic) this will be the topic that's invoked when the curator tires of waiting for the PC to talk, although using BoredByeTopic in this case probably makes our source code a little clearer.
