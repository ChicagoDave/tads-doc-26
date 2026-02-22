# ImpHelloTopic

ImpHelloTopic : [MiscTopic](misctopic.md)

An ImpHelloTopic (if defined) deals with the [greeting protocols](greetingprotocols.md) in the case where a conversation is started without an explicit greeting command (such as SARAH, HELLO or TALK TO SARAH). The normal place for an ImpHelloTopic is in a [ConversationReadyState](conversationreadystate.md).

For example, we might provide King Solomon with an ImpHelloTopic that looks like this:

```tads3
+++ ImpHelloTopic
  "Solomon turns and looks up at you as you start to speak.
  <<solomonHelloTopic.advanceState()>>"
;
```

This should be located in the solomonExamining ConversationReadyState. The one subtlety here is the call to solomonHelloTopic.advanceState(). The reason for calling this is that once this ImpHelloTopic has been triggered, we'd want to see the second response, not the first, in the list of responses on [solomonHelloTopic](hellotopic.md).
