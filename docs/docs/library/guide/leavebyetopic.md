# LeaveByeTopic

LeaveByeTopic: [MiscTopic](misctopic.md)

A LeaveByeTopic is effectively a more specialised ImpByeTopic. We can use it in the case where we want to distinguish a conversation ending through the PC walking away from one ending because his interlocutor gives up waiting for him to speak. So, for example, we could add the following, which should also be located in his curatorWatching ConversationReadyState:

```tads3
+++ LeaveByeTopic
  "{The curator/he} watches you leave, and then resumes working. "
;
```

And then we'll see a different message depending on whether the conversation ends as a result of boredom or travel. Note that in this case the (more specific) LeaveByeTopic will be used when the PC departs, and the (less specific) ImpByeTopic will be used when the curator becomes bored, although we could achieve the same effect by using a [BoredByeTopic](boredbyetopic.md).
